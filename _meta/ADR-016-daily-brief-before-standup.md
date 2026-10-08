---
title: "ADR-016: The daily brief is ready before standup"
type: adr
status: active
created: 2026-09-09
updated: 2026-10-01
tags: [decision, ops, example]
sources: ["[[2026-08-05-ai-leadership-pilot-notes]]"]
confidence: high
---

# ADR-016: The daily brief is ready before standup

## Context
In the pilot, people checked pipeline, cash and delivery in four places each morning
([[2026-08-05-ai-leadership-pilot-notes]]).

## Options

| Option | Pros | Cons |
|---|---|---|
| A: One daily brief at 8:30, before the 9:00 standup | One page, same for all | Depends on fresh pages |
| B: Each role reports separately | Detailed | Nobody reads four reports |

## Decision
A. The `/daily-brief` command orchestrates the COO, Sales and CFO agents. Decided by
[[Marcus-Finch]] on 2026-09-09. Example: [[2026-10-07-daily-brief]].

## Consequences
Standup starts from the brief's "decisions needed" list. Stale pages show up fast.

## Revisit when
Fewer than half the team reads it for a month ([[2026-10-01-q3-all-hands-notes]]: 15 of 23 do).
