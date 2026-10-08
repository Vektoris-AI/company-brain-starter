---
title: "ADR-003: Sell the pipeline setup as a fixed-price six-week sprint"
type: adr
status: active
created: 2026-02-20
updated: 2026-09-02
tags: [decision, sales, ops, example]
sources: ["[[2026-02-06-pipeline-sprint-pilot-retro]]", "[[2026-02-19-pricing-workshop-notes]]"]
confidence: high
---

# ADR-003: Sell the pipeline setup as a fixed-price six-week sprint

## Context
We kept doing pipeline setups hourly ([[pricing-model-2025]]). The pilot showed the work is
repeatable ([[2026-02-06-pipeline-sprint-pilot-retro]]); the pricing workshop modeled cost and margin
([[2026-02-19-pricing-workshop-notes]]).

## Options

| Option | Pros | Cons |
|---|---|---|
| A: Fixed price $18,500, 6 weeks, fixed scope | Easy to buy, clear margin | We carry the overrun risk |
| B: Hourly | No overrun risk | Clients hate open bills |
| C: Fixed price, 8 weeks | Realistic | Weaker offer, lower margin per week |

## Decision
A, scope as in [[pipeline-sprint-six-week-scope]]. Decided by [[Dana-Kettlewell]] with
[[Jordan-Pike]] and [[Marcus-Finch]] on 2026-02-20.

## Consequences
In the [[service-catalog]]. Needs a written handoff ([[sales-to-delivery-handoff]]) and slot
planning ([[ADR-008-cap-concurrent-sprints-at-three]]).

## Revisit when
Two sprints in a row run longer than 7 weeks. **Triggered** in August:
[[pipeline-sprints-run-eight-weeks-in-practice]]; review pending.
