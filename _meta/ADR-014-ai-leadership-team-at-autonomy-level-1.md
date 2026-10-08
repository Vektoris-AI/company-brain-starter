---
title: "ADR-014: The AI leadership team starts at autonomy level 1"
type: adr
status: active
created: 2026-08-12
updated: 2026-10-01
tags: [decision, strategy, tech, example]
sources: ["[[2026-08-05-ai-leadership-pilot-notes]]"]
confidence: high
---

# ADR-014: The AI leadership team starts at autonomy level 1

## Context
Eight role agents went live in August ([[ai-leadership-team-rollout]]). The brain's schema contract
defines autonomy levels 0 to 3.

## Options

| Option | Pros | Cons |
|---|---|---|
| A: Level 1 for all (write files, never commit) | Every change is a reviewed diff | Review load on Marcus |
| B: Level 2 for low-risk agents | Less review | No track record yet |
| C: Level 0 (chat only) | Safest | Little value |

## Decision
A. Decided by [[Dana-Kettlewell]] on 2026-08-12.

## Consequences
All agents write to `00_inbox/`; Marcus merges. Roster and boundaries in [[ai-leadership-team]].

## Revisit when
December review: a loop with 8 green weeks may move to level 2 ([[decisions-need-revisit-triggers]]).
