---
title: "Routine: legal contract check"
type: area
status: active
created: 2026-08-03
updated: 2026-10-07
tags: [legal, routine, example]
sources: []
confidence: high
---

# Routine: legal contract check

**Agent:** Legal & Compliance · **Command:** `/legal-contract-check <file>` · **When:** every incoming
contract, MSA, DPA or RFP · **Human:** [[Dana-Kettlewell]]

## Reads
The document, [[contract-playbook]], [[internal-privacy-policy]], [[ai-use-policy]], the client page.

## Writes
`00_inbox/<date>-legal-contract-check.md`: a clause table (standard / deviates / missing), each
deviation with the playbook fallback, and a list "questions for counsel" for [[Pembury-Lane-Legal]].

## Watches especially
Liability caps, IP ownership, payment terms vs. [[ADR-017-net-15-payment-terms]], subprocessors and
AI use ([[ADR-013-vendor-dpa-before-any-ai-tool]]), approval SLAs ([[sales-to-delivery-handoff]]).

## Never
Signs, accepts, negotiates with the other side, or calls its output legal advice.
