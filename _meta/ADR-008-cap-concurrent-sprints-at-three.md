---
title: "ADR-008: Run at most three sprints at the same time"
type: adr
status: active
created: 2026-05-06
updated: 2026-10-01
tags: [decision, ops, example]
sources: ["[[2026-05-05-capacity-planning-meeting]]"]
confidence: high
---

# ADR-008: Run at most three sprints at the same time

## Context
Four parallel sprints in April pushed the ops group to 86% utilization
([[2026-05-05-capacity-planning-meeting]]).

## Options

| Option | Pros | Cons |
|---|---|---|
| A: Max 3 sprints, planned in slots | Sustainable, honest start dates | Some deals start later |
| B: Hire ahead of demand | More throughput | Cash risk |
| C: Keep going | Revenue now | Burnout |

## Decision
A ([[capacity-is-planned-in-sprint-slots]]). Decided by [[Marcus-Finch]] on 2026-05-06.

## Consequences
Slots on the [[capacity-board]]; sales quotes start dates from there. Utilization 78% by
October ([[2026-10-01-q3-all-hands-notes]]).

## Revisit when
Ops utilization below 65% for a quarter, or a fourth sprint team is hired.
