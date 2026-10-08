---
title: "ADR-009: Regulated-industry content gets an internal legal check"
type: adr
status: active
created: 2026-05-20
updated: 2026-05-20
tags: [decision, legal, example]
sources: ["[[2026-04-22-oakvane-compliance-email]]"]
confidence: high
---

# ADR-009: Regulated-industry content gets an internal legal check

## Context
[[Oakvane-Wealth-Advisors]] requires compliance review of every piece
([[2026-04-22-oakvane-compliance-email]]); [[Wrenfield-Dental-Partners]] reviews clinical claims.

## Options

| Option | Pros | Cons |
|---|---|---|
| A: Internal checklist + client review buffer | Fewer rejected drafts | More lead time |
| B: Rely on client review only | Less work for us | Many rejections, slips |
| C: Avoid regulated clients | Simple | Loses good clients |

## Decision
A. Decided by [[Dana-Kettlewell]] with [[Aisha-Morgan]] on 2026-05-20.

## Consequences
[[content-qa-sop]] has a regulated section; calendars include [[regulated-clients-need-review-buffers]].

## Revisit when
Two quarters without a client rejection on compliance grounds; then simplify.
