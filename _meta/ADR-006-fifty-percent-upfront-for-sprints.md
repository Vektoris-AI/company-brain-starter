---
title: "ADR-006: Sprints are invoiced 50% upfront"
type: adr
status: active
created: 2026-04-02
updated: 2026-04-02
tags: [decision, finance, example]
sources: ["[[2026-04-01-ar-aging-export]]"]
confidence: high
---

# ADR-006: Sprints are invoiced 50% upfront

## Context
Average receivable days were 49 ([[2026-04-01-ar-aging-export]]). Fixed-price sprints put the whole
fee at risk until launch.

## Options

| Option | Pros | Cons |
|---|---|---|
| A: 50% upfront, 50% at launch | Cash before work, less risk | Some clients push back |
| B: 100% at the end | Easy sale | Cash gap of 8+ weeks |
| C: Monthly | Smooth | Doesn't fit a 6-week product |

## Decision
A. Decided by [[Priya-Raman]] and [[Dana-Kettlewell]] on 2026-04-02.

## Consequences
In [[service-catalog]] and [[contract-playbook]]. Effect tracked in [[receivables]],
[[upfront-payment-reduces-receivable-days]].

## Revisit when
Two qualified deals in a quarter are lost because of upfront payment.
