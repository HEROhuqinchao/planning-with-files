# Findings & Decisions（发现与决策）
<!--
  是什么：任务的知识库，存储你发现和决定的一切。
  为什么：上下文窗口有限，此文件是你的「外部记忆」——持久且无限。
  何时：任何发现后立即更新，尤其是每 2 次查看/浏览/搜索操作后（两步操作规则）。
-->

## Requirements（需求）
<!--
  是什么：用户请求的内容，拆解为具体需求条目。
  为什么：让需求保持可见，避免忘记自己在构建什么。
  何时：在 Phase 1（需求与调研）期间填写。
  示例：
    - Command-line interface
    - Add tasks
    - List all tasks
    - Delete tasks
    - Python implementation
-->
<!-- 从用户请求中提取 -->
-

## Research Findings（研究发现）
<!--
  是什么：来自网络搜索、文档阅读或探索的关键发现。
  为什么：多模态内容（图片、浏览器结果）不会持久化，必须立即写下来。
  何时：每 2 次查看/浏览/搜索操作后更新此节（两步操作规则）。
  示例：
    - Python's argparse module supports subcommands for clean CLI design
    - JSON module handles file persistence easily
    - Standard pattern: python script.py <command> [args]
-->
<!-- 探索过程中的关键发现 -->
-

## Technical Decisions（技术决策）
<!--
  是什么：已做出的架构和实现选择，及其依据。
  为什么：你会忘记选择某项技术或方案的原因，此表保留这些知识。
  何时：每当做出重要技术选择时更新。
  示例：
    | Use JSON for storage | Simple, human-readable, built-in Python support |
    | argparse with subcommands | Clean CLI: python todo.py add "task" |
-->
<!-- 已做决策及依据 -->
| Decision（决策） | Rationale（依据） |
|-----------------|------------------|
|                 |                  |

## Issues Encountered（遇到的问题）
<!--
  是什么：遇到的问题及解决方式。
  为什么：类似于 task_plan.md 中的错误记录，但聚焦于更宏观的问题（不仅限于代码错误）。
  何时：遇到阻碍或意外挑战时记录。
  示例：
    | Empty file causes JSONDecodeError | Added explicit empty file check before json.load() |
-->
<!-- 错误及解决方式 -->
| Issue（问题） | Resolution（解决方式） |
|--------------|----------------------|
|              |                      |

## Resources（资源）
<!--
  是什么：发现的有用 URL、文件路径、API 参考、文档链接。
  为什么：便于后续查阅，不要让重要链接淹没在上下文中。
  何时：发现有用资源时随时添加。
  示例：
    - Python argparse docs: https://docs.python.org/3/library/argparse.html
    - Project structure: src/main.py, src/utils.py
-->
<!-- URL、文件路径、API 参考 -->
-

## Visual/Browser Findings（视觉/浏览器发现）
<!--
  是什么：查看图片、PDF 或浏览器结果时获得的信息。
  为什么：关键！视觉/多模态内容不会在上下文中持久化，必须立即以文字形式记录。
  何时：查看图片或浏览器结果后立即更新，不要等待！
  示例：
    - Screenshot shows login form has email and password fields
    - Browser shows API returns JSON with "status" and "data" keys
-->
<!-- 关键：每 2 次查看/浏览操作后更新 -->
<!-- 多模态内容必须立即以文字形式记录 -->
-

---
<!--
  提醒：两步操作规则
  每进行 2 次查看/浏览/搜索操作，必须更新此文件。
  这能防止视觉信息在上下文重置时丢失。
-->
*每 2 次查看/浏览/搜索操作后更新此文件*
*防止视觉信息丢失*
