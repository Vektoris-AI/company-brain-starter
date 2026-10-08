---
title: "ADR-017: New clients get net-15 payment terms"
type: adr
status: active
created: 2026-09-17
updated: 2026-09-17
tags: [decision, finance, example]
sources: ["[[2026-09-17-cash-review-meeting]]"]
confidence: high
---

# ADR-017: New clients get net-15 payment terms

## Context
Runway was 7.6 weeks without new inflows; 38% of receivables older than 30 days
([[2026-09-17-cash-review-meeting]]).

## Options

| Option | Pros | Cons |
|---|---|---|
| A: Net-15 for new clients, existing stay net-30 | Faster cash, no surprises for current clients | Some pushback |
| B: Net-15 for all | Fastest | Damages relationships |
| C: Keep net-30 | Easy | Cash stays tight |

## Decision
A, from 2026-10-01. Decided by [[Priya-Raman]] and [[Dana-Kettlewell]].

## Consequences
[[contract-playbook]] updated; checked in [[legal-contract-check-routine]]; tracked in [[receivables]].

## Revisit when
Receivable days under 30 for two quarters, or a lost deal over terms.
