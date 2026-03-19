# Task Plan: [简要描述]
<!--
  是什么：这是整个任务的路线图，是你「磁盘上的工作记忆」。
  为什么：50+ 次工具调用后，最初目标容易被遗忘。此文件让目标始终保持新鲜。
  何时：在开始任何工作之前**先**创建它。每个阶段完成后更新。
-->

## Goal（目标）
<!--
  是什么：一句话清晰描述你要达成的结果。
  为什么：这是你的北极星，重读它能让你专注于最终状态。
  示例："Create a Python CLI todo app with add, list, and delete functionality."
-->
[一句话描述最终状态]

## Current Phase（当前阶段）
<!--
  是什么：当前正在处理的阶段（如"Phase 1"、"Phase 3"）。
  为什么：快速定位任务进度，随进展及时更新。
-->
Phase 1

## Phases（阶段）
<!--
  是什么：将任务拆分为 3-7 个逻辑阶段，每个阶段应可独立完成。
  为什么：分阶段推进能避免失控，并使进度可视化。
  何时：每完成一个阶段后更新状态：pending → in_progress → complete
-->

### Phase 1: Requirements & Discovery（需求与调研）
<!--
  是什么：理解待完成的工作并收集初始信息。
  为什么：在不理解需求的情况下开始会造成大量无效工作，此阶段可预防这一问题。
-->
- [ ] Understand user intent（理解用户意图）
- [ ] Identify constraints and requirements（识别约束与需求）
- [ ] Document findings in findings.md（将发现记录到 findings.md）
- **Status:** in_progress
<!--
  状态值：
  - pending：尚未开始
  - in_progress：当前正在处理
  - complete：此阶段已完成
-->

### Phase 2: Planning & Structure（规划与结构）
<!--
  是什么：决定解决问题的方式和采用的结构。
  为什么：良好的规划可以避免返工，记录决策便于日后回忆选择的原因。
-->
- [ ] Define technical approach（确定技术方案）
- [ ] Create project structure if needed（按需创建项目结构）
- [ ] Document decisions with rationale（记录决策及其依据）
- **Status:** pending

### Phase 3: Implementation（实施）
<!--
  是什么：实际构建/创建/编写解决方案。
  为什么：这是工作的核心，如有需要可进一步拆分为更小的子任务。
-->
- [ ] Execute the plan step by step（逐步执行计划）
- [ ] Write code to files before executing（执行前先将代码写入文件）
- [ ] Test incrementally（增量测试）
- **Status:** pending

### Phase 4: Testing & Verification（测试与验证）
<!--
  是什么：验证一切是否正常运行并满足需求。
  为什么：尽早发现问题节省时间，将测试结果记录到 progress.md。
-->
- [ ] Verify all requirements met（验证所有需求均已满足）
- [ ] Document test results in progress.md（将测试结果记录到 progress.md）
- [ ] Fix any issues found（修复发现的问题）
- **Status:** pending

### Phase 5: Delivery（交付）
<!--
  是什么：最终审查并移交给用户。
  为什么：确保不遗漏任何内容，交付物完整。
-->
- [ ] Review all output files（审查所有输出文件）
- [ ] Ensure deliverables are complete（确保交付物完整）
- [ ] Deliver to user（交付给用户）
- **Status:** pending

## Key Questions（关键问题）
<!--
  是什么：任务过程中需要回答的重要问题。
  为什么：这些问题指导你的研究和决策，随进展逐步作答。
  示例：
    1. Should tasks persist between sessions? (Yes - need file storage)
    2. What format for storing tasks? (JSON file)
-->
1. [待回答的问题]
2. [待回答的问题]

## Decisions Made（已做决策）
<!--
  是什么：已做出的技术与设计决策，及其背后的原因。
  为什么：你会忘记做选择的原因，此表帮助你记住并为决策辩护。
  何时：每当做出重要选择（技术、方案、结构）时更新。
  示例：
    | Use JSON for storage | Simple, human-readable, built-in Python support |
-->
| Decision（决策） | Rationale（依据） |
|-----------------|------------------|
|                 |                  |

## Errors Encountered（遇到的错误）
<!--
  是什么：每个遇到的错误、尝试次数和解决方式。
  为什么：记录错误可防止重复犯错，对学习至关重要。
  何时：错误发生时立即添加，即使很快解决也要记录。
  示例：
    | FileNotFoundError | 1 | Check if file exists, create empty list if not |
    | JSONDecodeError | 2 | Handle empty file case explicitly |
-->
| Error（错误） | Attempt（次数） | Resolution（解决方式） |
|--------------|----------------|----------------------|
|              | 1              |                      |

## Notes（备注）
<!--
  提醒：
  - 随进展更新阶段状态：pending → in_progress → complete
  - 做重大决策前重读此计划（注意力操控）
  - 记录所有错误 — 有助于避免重复
  - 绝不重复失败的操作 — 改变策略
-->
- 随进展更新阶段状态：pending → in_progress → complete
- 做重大决策前重读此计划（注意力操控）
- 记录所有错误 — 有助于避免重复
