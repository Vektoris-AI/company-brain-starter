---
title: "ADR-007: Client data stays in the client's own systems"
type: adr
status: active
created: 2026-04-15
updated: 2026-04-15
tags: [decision, tech, legal, example]
sources: ["[[2026-04-09-granitefold-crm-audit-export]]"]
confidence: high
---

# ADR-007: Client data stays in the client's own systems

## Context
During the [[granitefold-crm-cleanup]] someone proposed exporting the client's CRM into our tools
for analysis ([[2026-04-09-granitefold-crm-audit-export]]).

## Options

| Option | Pros | Cons |
|---|---|---|
| A: Work inside client systems with named accounts | Less liability, clean offboarding | Slower analysis |
| B: Copy data to our tools | Faster | We become a data holder |
| C: Case by case | Flexible | Inconsistent |

## Decision
A. Aggregated exports only, deleted after the project. Decided by [[Dana-Kettlewell]] and
[[Sam-Whitaker]] on 2026-04-15.

## Consequences
[[data-access-policy]], [[client-data-least-privilege]], [[contract-playbook]].

## Revisit when
A client asks us in writing to host their data.
