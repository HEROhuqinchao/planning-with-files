# Progress Log（进度日志）
<!--
  是什么：会话日志——按时间顺序记录你做了什么、何时做的、发生了什么。
  为什么：回答五问重启测试中「我做了什么？」这一问题，帮助你在中断后恢复工作。
  何时：完成每个阶段或遇到错误后更新，比 task_plan.md 更详细。
-->

## Session（会话）：[DATE]
<!--
  是什么：本次工作会话的日期。
  为什么：帮助追踪工作时间，便于在时间间隔后恢复。
  示例：2026-01-15
-->

### Phase 1: [Title]（标题）
<!--
  是什么：此阶段所采取行动的详细日志。
  为什么：提供操作上下文，便于恢复工作或调试。
  何时：在阶段进行过程中更新，或至少在完成时更新。
-->
- **Status:** in_progress
- **Started:** [timestamp]（时间戳）
<!--
  状态：与 task_plan.md 相同（pending, in_progress, complete）
  时间戳：开始此阶段的时间（如"2026-01-15 10:00"）
-->
- Actions taken（已采取的行动）：
  <!--
    是什么：列出你执行的具体操作。
    示例：
      - Created todo.py with basic structure
      - Implemented add functionality
      - Fixed FileNotFoundError
  -->
  -
- Files created/modified（创建/修改的文件）：
  <!--
    是什么：创建或修改了哪些文件。
    为什么：快速参考被改动的内容，便于调试和审查。
    示例：
      - todo.py (created)
      - todos.json (created by app)
      - task_plan.md (updated)
  -->
  -

### Phase 2: [Title]（标题）
<!--
  是什么：与 Phase 1 相同的结构，用于下一个阶段。
  为什么：为每个阶段保留独立的日志条目，清晰追踪进度。
-->
- **Status:** pending
- Actions taken（已采取的行动）：
  -
- Files created/modified（创建/修改的文件）：
  -

## Test Results（测试结果）
<!--
  是什么：运行的测试表格，包含期望结果和实际结果。
  为什么：记录功能验证情况，帮助发现回归问题。
  何时：测试功能时更新，尤其在 Phase 4（测试与验证）期间。
  示例：
    | Add task | python todo.py add "Buy milk" | Task added | Task added successfully | ✓ |
    | List tasks | python todo.py list | Shows all tasks | Shows all tasks | ✓ |
-->
| Test（测试） | Input（输入） | Expected（期望） | Actual（实际） | Status（状态） |
|-------------|--------------|-----------------|---------------|--------------|
|             |              |                 |               |              |

## Error Log（错误日志）
<!--
  是什么：遇到的每个错误的详细日志，包含时间戳和解决尝试记录。
  为什么：比 task_plan.md 的错误表更详细，帮助从错误中学习。
  何时：错误发生时立即添加，即使很快解决也要记录。
  示例：
    | 2026-01-15 10:35 | FileNotFoundError | 1 | Added file existence check |
    | 2026-01-15 10:37 | JSONDecodeError | 2 | Added empty file handling |
-->
<!-- 保留所有错误记录 — 有助于避免重复 -->
| Timestamp（时间戳） | Error（错误） | Attempt（次数） | Resolution（解决方式） |
|--------------------|--------------|----------------|----------------------|
|                    |              | 1              |                      |

## 五问重启检查
<!--
  是什么：验证上下文是否稳固的五个问题，能全部回答说明状态良好。
  为什么：这是「重启测试」——如果能回答所有 5 个问题，就能有效恢复工作。
  何时：定期更新，尤其是在中断或上下文重置后恢复时。

  五个问题：
  1. 我在哪里？→ task_plan.md 中的当前阶段
  2. 我要去哪里？→ 剩余阶段
  3. 目标是什么？→ task_plan.md 中的目标声明
  4. 我学到了什么？→ 参见 findings.md
  5. 我做了什么？→ 参见 progress.md（本文件）
-->
<!-- 能回答这些问题说明上下文稳固 -->
| 问题 | 答案 |
|------|------|
| 我在哪里？ | Phase X |
| 我要去哪里？ | 剩余阶段 |
| 目标是什么？ | [目标声明] |
| 我学到了什么？ | 参见 findings.md |
| 我做了什么？ | 参见上方 |

---
<!--
  提醒：
  - 完成每个阶段或遇到错误后更新
  - 记录详细 — 这是你的「发生了什么」日志
  - 为错误添加时间戳，便于追踪问题发生时间
-->
*完成每个阶段或遇到错误后更新*
