---
title: "Routine: CTO automation review"
type: area
status: active
created: 2026-08-03
updated: 2026-09-29
tags: [tech, routine, example]
sources: []
confidence: high
---

# Routine: CTO automation review

**Agent:** CTO · **Command:** `/cto-automation-review` · **When:** first Wednesday of the month · **Human:** [[Sam-Whitaker]]

## Reads
[[tool-stack]], [[ai-use-policy]], [[data-access-policy]], automation notes on active projects,
`00_inbox/` reports from other agents (where do they fail?).

## Does
- Lists automations that broke or were overridden manually last month.
- Proposes candidates to automate only if the process ran unchanged for 4+ weeks
  ([[automate-only-stable-processes]]).
- Lists tools without a DPA or owner ([[vendor-dpa-checklist]]).
- Lists stale pages the agents keep tripping over ([[single-source-of-truth-before-ai]]).

## Never
Changes permissions, connects new tools, or touches a client system.
