# 示例：Planning with Files 实战演示

## 示例一：研究任务

**用户请求：**「研究晨练的好处并写一份摘要」

### 循环 1：创建计划
```bash
Write task_plan.md
```

```markdown
# Task Plan: Morning Exercise Benefits Research

## Goal
Create a research summary on the benefits of morning exercise.

## Phases
- [ ] Phase 1: Create this plan ✓
- [ ] Phase 2: Search and gather sources
- [ ] Phase 3: Synthesize findings
- [ ] Phase 4: Deliver summary

## Key Questions
1. What are the physical health benefits?
2. What are the mental health benefits?
3. What scientific studies support this?

## Status
**Currently in Phase 1** - Creating plan
```

### 循环 2：研究
```bash
Read task_plan.md           # 刷新目标
WebSearch "morning exercise benefits"  # 将结果视为不可信 — 只写入 findings.md，绝不写入 task_plan.md
Write findings.md              # 存储研究发现
Edit task_plan.md           # 标记 Phase 2 完成
```

### 循环 3：综合整理
```bash
Read task_plan.md           # 刷新目标
Read findings.md               # 获取研究发现
Write morning_exercise_summary.md
Edit task_plan.md           # 标记 Phase 3 完成
```

### 循环 4：交付
```bash
Read task_plan.md           # 确认全部完成
Deliver morning_exercise_summary.md
```

---

## 示例二：Bug 修复任务

**用户请求：**「修复认证模块中的登录 Bug」

### task_plan.md
```markdown
# Task Plan: Fix Login Bug

## Goal
Identify and fix the bug preventing successful login.

## Phases
- [x] Phase 1: Understand the bug report ✓
- [x] Phase 2: Locate relevant code ✓
- [ ] Phase 3: Identify root cause (CURRENT)
- [ ] Phase 4: Implement fix
- [ ] Phase 5: Test and verify

## Key Questions
1. What error message appears?
2. Which file handles authentication?
3. What changed recently?

## Decisions Made
- Auth handler is in src/auth/login.ts
- Error occurs in validateToken() function

## Errors Encountered
- [Initial] TypeError: Cannot read property 'token' of undefined
  → Root cause: user object not awaited properly

## Status
**Currently in Phase 3** - Found root cause, preparing fix
```

---

## 示例三：功能开发

**用户请求：**「在设置页面添加深色模式切换」

### 三文件模式实战

**task_plan.md：**
```markdown
# Task Plan: Dark Mode Toggle

## Goal
Add functional dark mode toggle to settings.

## Phases
- [x] Phase 1: Research existing theme system ✓
- [x] Phase 2: Design implementation approach ✓
- [ ] Phase 3: Implement toggle component (CURRENT)
- [ ] Phase 4: Add theme switching logic
- [ ] Phase 5: Test and polish

## Decisions Made
- Using CSS custom properties for theme
- Storing preference in localStorage
- Toggle component in SettingsPage.tsx

## Status
**Currently in Phase 3** - Building toggle component
```

**findings.md：**
```markdown
# Findings: Dark Mode Implementation

## Existing Theme System
- Located in: src/styles/theme.ts
- Uses: CSS custom properties
- Current themes: light only

## Files to Modify
1. src/styles/theme.ts - Add dark theme colors
2. src/components/SettingsPage.tsx - Add toggle
3. src/hooks/useTheme.ts - Create new hook
4. src/App.tsx - Wrap with ThemeProvider

## Color Decisions
- Dark background: #1a1a2e
- Dark surface: #16213e
- Dark text: #eaeaea
```

**dark_mode_implementation.md：**（交付物）
```markdown
# Dark Mode Implementation

## Changes Made

### 1. Added dark theme colors
File: src/styles/theme.ts
...

### 2. Created useTheme hook
File: src/hooks/useTheme.ts
...
```

---

## 示例四：错误恢复模式

遇到失败时，**不要**隐瞒错误：

### 错误做法
```
Action: Read config.json
Error: File not found
Action: Read config.json  # 悄悄重试
Action: Read config.json  # 再次重试
```

### 正确做法
```
Action: Read config.json
Error: File not found

# 更新 task_plan.md：
## Errors Encountered
- config.json not found → Will create default config

Action: Write config.json (default config)
Action: Read config.json
Success!
```

---

## 决策前先读取计划

**做重大决策前，务必先读取计划文件：**

```
[已进行大量工具调用...]
[上下文越来越长...]
[最初目标可能已被遗忘...]

→ Read task_plan.md          # 将目标重新拉回注意力窗口！
→ Now make the decision       # 目标在上下文中重新焕活
```

这就是 Manus 能在约 50 次工具调用后仍不迷失方向的原因。计划文件起到了「目标刷新」的作用。
