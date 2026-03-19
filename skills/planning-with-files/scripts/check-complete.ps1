# 检查 task_plan.md 中所有阶段是否已完成
# 始终以退出码 0 退出 -- 通过 stdout 输出状态报告
# 由 Stop hook 调用，用于报告任务完成状态

param(
    [string]$PlanFile = "task_plan.md"
)

if (-not (Test-Path $PlanFile)) {
    Write-Host '[planning-with-files] No task_plan.md found -- no active planning session.'
    exit 0
}

# 读取文件内容
$content = Get-Content $PlanFile -Raw

# 统计总阶段数
$TOTAL = ([regex]::Matches($content, "### Phase")).Count

# 优先检查 **Status:** 格式
$COMPLETE = ([regex]::Matches($content, "\*\*Status:\*\* complete")).Count
$IN_PROGRESS = ([regex]::Matches($content, "\*\*Status:\*\* in_progress")).Count
$PENDING = ([regex]::Matches($content, "\*\*Status:\*\* pending")).Count

# 兜底方案：若未找到 **Status:** 格式，则检查 [complete] 内联格式
if ($COMPLETE -eq 0 -and $IN_PROGRESS -eq 0 -and $PENDING -eq 0) {
    $COMPLETE = ([regex]::Matches($content, "\[complete\]")).Count
    $IN_PROGRESS = ([regex]::Matches($content, "\[in_progress\]")).Count
    $PENDING = ([regex]::Matches($content, "\[pending\]")).Count
}

# 输出状态报告 -- 始终以退出码 0 退出，任务未完成是正常状态
if ($COMPLETE -eq $TOTAL -and $TOTAL -gt 0) {
    Write-Host ('[planning-with-files] ALL PHASES COMPLETE (' + $COMPLETE + '/' + $TOTAL + '). If the user has additional work, add new phases to task_plan.md before starting.')
} else {
    Write-Host ('[planning-with-files] Task in progress (' + $COMPLETE + '/' + $TOTAL + ' phases complete). Update progress.md before stopping.')
    if ($IN_PROGRESS -gt 0) {
        Write-Host ('[planning-with-files] ' + $IN_PROGRESS + ' phase(s) still in progress.')
    }
    if ($PENDING -gt 0) {
        Write-Host ('[planning-with-files] ' + $PENDING + ' phase(s) pending.')
    }
}
exit 0
