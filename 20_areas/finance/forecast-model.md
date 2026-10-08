---
title: "Forecast model (13 weeks)"
type: area
status: active
created: 2026-06-01
updated: 2026-09-17
tags: [finance, example]
sources: []
confidence: medium
---

# Forecast model (13 weeks)

Owner: [[Priya-Raman]]. Updated by the [[cfo-cash-check-routine]] as a draft every Monday.

## Inputs
- Signed retainers from [[service-catalog]] contracts.
- Sprint milestones (50% upfront, 50% at launch) from [[capacity-board]].
- Weighted deals from [[pipeline]] only in the trend scenario, never in the conservative one.
- Payroll as one line; planned hires from [[hiring-plan-q4]].

## Output
Two lines, conservative and trend ([[forecasts-show-two-scenarios]]), plus runway in weeks
([[cash-runway-in-weeks]]).

## Known weakness
Sprint launches slip (see [[pipeline-sprints-run-eight-weeks-in-practice]]), so the second
50% arrives later than planned. The conservative scenario assumes 8 weeks.
