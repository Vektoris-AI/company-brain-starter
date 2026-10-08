---
title: "Clean the CRM before automating on top of it"
type: knowledge
status: active
created: 2026-02-02
updated: 2026-09-12
tags: [tech, customer, example]
sources: ["[[2026-01-14-cobaltline-discovery-call]]", "[[2026-04-09-granitefold-crm-audit-export]]"]
confidence: high
---

# Clean the CRM before automating on top of it

Automation multiplies whatever the data says. On dirty data it multiplies mistakes.

**Evidence:** "It got faster at being wrong" ([[2026-01-14-cobaltline-discovery-call]]);
6 conflicting workflows at [[Granitefold-Insurance-Brokers]] ([[2026-04-09-granitefold-crm-audit-export]]).

**Practice:** audit, dedupe, one owner per record, then automate
([[granitefold-crm-cleanup]], [[cobaltline-ops-retainer]]). Same logic for our own company:
[[single-source-of-truth-before-ai]], [[automate-only-stable-processes]].
