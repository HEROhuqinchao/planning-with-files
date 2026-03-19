#!/usr/bin/env python3
"""
planning-with-files 会话追赶脚本

分析上一个会话，找出最后一次规划文件更新之后尚未同步的上下文。
设计为在 SessionStart 时运行。

用法：python3 session-catchup.py [project-path]
"""

import json
import sys
import os
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from datetime import datetime

PLANNING_FILES = ['task_plan.md', 'progress.md', 'findings.md']


def get_project_dir(project_path: str) -> Path:
    """将项目路径转换为 Claude 的存储路径格式。"""
    sanitized = project_path.replace('/', '-')
    if not sanitized.startswith('-'):
        sanitized = '-' + sanitized
    sanitized = sanitized.replace('_', '-')
    return Path.home() / '.claude' / 'projects' / sanitized


def get_sessions_sorted(project_dir: Path) -> List[Path]:
    """获取所有会话文件，按修改时间排序（最新在前）。"""
    sessions = list(project_dir.glob('*.jsonl'))
    main_sessions = [s for s in sessions if not s.name.startswith('agent-')]
    return sorted(main_sessions, key=lambda p: p.stat().st_mtime, reverse=True)


def parse_session_messages(session_file: Path) -> List[Dict]:
    """解析会话文件中的所有消息，保留原始顺序。"""
    messages = []
    with open(session_file, 'r') as f:
        for line_num, line in enumerate(f):
            try:
                data = json.loads(line)
                data['_line_num'] = line_num
                messages.append(data)
            except json.JSONDecodeError:
                pass
    return messages


def find_last_planning_update(messages: List[Dict]) -> Tuple[int, Optional[str]]:
    """
    查找规划文件最后一次被写入/编辑的时间。
    返回 (行号, 文件名)，若未找到则返回 (-1, None)。
    """
    last_update_line = -1
    last_update_file = None

    for msg in messages:
        msg_type = msg.get('type')

        if msg_type == 'assistant':
            content = msg.get('message', {}).get('content', [])
            if isinstance(content, list):
                for item in content:
                    if item.get('type') == 'tool_use':
                        tool_name = item.get('name', '')
                        tool_input = item.get('input', {})

                        if tool_name in ('Write', 'Edit'):
                            file_path = tool_input.get('file_path', '')
                            for pf in PLANNING_FILES:
                                if file_path.endswith(pf):
                                    last_update_line = msg['_line_num']
                                    last_update_file = pf

    return last_update_line, last_update_file


def extract_messages_after(messages: List[Dict], after_line: int) -> List[Dict]:
    """提取指定行号之后的对话消息。"""
    result = []
    for msg in messages:
        if msg['_line_num'] <= after_line:
            continue

        msg_type = msg.get('type')
        is_meta = msg.get('isMeta', False)

        if msg_type == 'user' and not is_meta:
            content = msg.get('message', {}).get('content', '')
            if isinstance(content, list):
                for item in content:
                    if isinstance(item, dict) and item.get('type') == 'text':
                        content = item.get('text', '')
                        break
                else:
                    content = ''

            if content and isinstance(content, str):
                if content.startswith(('<local-command', '<command-', '<task-notification')):
                    continue
                if len(content) > 20:
                    result.append({'role': 'user', 'content': content, 'line': msg['_line_num']})

        elif msg_type == 'assistant':
            msg_content = msg.get('message', {}).get('content', '')
            text_content = ''
            tool_uses = []

            if isinstance(msg_content, str):
                text_content = msg_content
            elif isinstance(msg_content, list):
                for item in msg_content:
                    if item.get('type') == 'text':
                        text_content = item.get('text', '')
                    elif item.get('type') == 'tool_use':
                        tool_name = item.get('name', '')
                        tool_input = item.get('input', {})
                        if tool_name == 'Edit':
                            tool_uses.append(f"Edit: {tool_input.get('file_path', 'unknown')}")
                        elif tool_name == 'Write':
                            tool_uses.append(f"Write: {tool_input.get('file_path', 'unknown')}")
                        elif tool_name == 'Bash':
                            cmd = tool_input.get('command', '')[:80]
                            tool_uses.append(f"Bash: {cmd}")
                        else:
                            tool_uses.append(f"{tool_name}")

            if text_content or tool_uses:
                result.append({
                    'role': 'assistant',
                    'content': text_content[:600] if text_content else '',
                    'tools': tool_uses,
                    'line': msg['_line_num']
                })

    return result


def main():
    project_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    project_dir = get_project_dir(project_path)

    # 检查规划文件是否存在（表示有活跃任务）
    has_planning_files = any(
        Path(project_path, f).exists() for f in PLANNING_FILES
    )
    if not has_planning_files:
        # 该项目无规划文件，跳过追赶以避免无效输出
        return

    if not project_dir.exists():
        # 没有历史会话，无需追赶
        return

    sessions = get_sessions_sorted(project_dir)
    if len(sessions) < 1:
        return

    # 找到一个内容充实的历史会话（文件大小 > 5000 字节）
    target_session = None
    for session in sessions:
        if session.stat().st_size > 5000:
            target_session = session
            break

    if not target_session:
        return

    messages = parse_session_messages(target_session)
    last_update_line, last_update_file = find_last_planning_update(messages)

    # 目标会话中无规划文件更新记录，跳过追赶输出
    if last_update_line < 0:
        return

    # 仅当存在未同步内容时才输出
    messages_after = extract_messages_after(messages, last_update_line)

    if not messages_after:
        return

    # 输出追赶报告
    print("\n[planning-with-files] SESSION CATCHUP DETECTED")
    print(f"Previous session: {target_session.stem}")

    print(f"Last planning update: {last_update_file} at message #{last_update_line}")
    print(f"Unsynced messages: {len(messages_after)}")

    print("\n--- UNSYNCED CONTEXT ---")
    for msg in messages_after[-15:]:  # 最近 15 条消息
        if msg['role'] == 'user':
            print(f"USER: {msg['content'][:300]}")
        else:
            if msg.get('content'):
                print(f"CLAUDE: {msg['content'][:300]}")
            if msg.get('tools'):
                print(f"  Tools: {', '.join(msg['tools'][:4])}")

    print("\n--- RECOMMENDED ---")
    print("1. Run: git diff --stat")
    print("2. Read: task_plan.md, progress.md, findings.md")
    print("3. Update planning files based on above context")
    print("4. Continue with task")


if __name__ == '__main__':
    main()
