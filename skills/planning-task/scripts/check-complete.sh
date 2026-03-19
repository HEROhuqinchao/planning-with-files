#!/bin/bash
# 检查 task_plan.md 中所有阶段是否已完成
# 始终以退出码 0 退出 — 通过 stdout 输出状态报告
# 由 Stop hook 调用，用于报告任务完成状态

PLAN_FILE="${1:-task_plan.md}"

if [ ! -f "$PLAN_FILE" ]; then
    echo "[planning-with-files] No task_plan.md found — no active planning session."
    exit 0
fi

# 统计总阶段数
TOTAL=$(grep -c "### Phase" "$PLAN_FILE" || true)

# 优先检查 **Status:** 格式
COMPLETE=$(grep -cF "**Status:** complete" "$PLAN_FILE" || true)
IN_PROGRESS=$(grep -cF "**Status:** in_progress" "$PLAN_FILE" || true)
PENDING=$(grep -cF "**Status:** pending" "$PLAN_FILE" || true)

# 兜底方案：若未找到 **Status:** 格式，则检查 [complete] 内联格式
if [ "$COMPLETE" -eq 0 ] && [ "$IN_PROGRESS" -eq 0 ] && [ "$PENDING" -eq 0 ]; then
    COMPLETE=$(grep -c "\[complete\]" "$PLAN_FILE" || true)
    IN_PROGRESS=$(grep -c "\[in_progress\]" "$PLAN_FILE" || true)
    PENDING=$(grep -c "\[pending\]" "$PLAN_FILE" || true)
fi

# 若变量为空则默认置 0
: "${TOTAL:=0}"
: "${COMPLETE:=0}"
: "${IN_PROGRESS:=0}"
: "${PENDING:=0}"

# 输出状态报告（始终以退出码 0 退出 — 任务未完成是正常状态）
if [ "$COMPLETE" -eq "$TOTAL" ] && [ "$TOTAL" -gt 0 ]; then
    echo "[planning-with-files] ALL PHASES COMPLETE ($COMPLETE/$TOTAL). If the user has additional work, add new phases to task_plan.md before starting."
else
    echo "[planning-with-files] Task in progress ($COMPLETE/$TOTAL phases complete). Update progress.md before stopping."
    if [ "$IN_PROGRESS" -gt 0 ]; then
        echo "[planning-with-files] $IN_PROGRESS phase(s) still in progress."
    fi
    if [ "$PENDING" -gt 0 ]; then
        echo "[planning-with-files] $PENDING phase(s) pending."
    fi
fi
exit 0
