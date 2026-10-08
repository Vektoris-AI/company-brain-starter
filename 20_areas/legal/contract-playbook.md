---
title: "Contract playbook"
type: area
status: active
created: 2026-02-10
updated: 2026-09-16
tags: [legal, example]
sources: ["[[2026-02-06-pipeline-sprint-pilot-retro]]"]
confidence: high
---

# Contract playbook

| Clause | Our standard | Fallback | Never |
|---|---|---|---|
| Payment | Net-15 ([[ADR-017-net-15-payment-terms]]); sprints 50% upfront | Net-30 for existing clients | Net-60+ |
| Liability cap | Fees of the last 12 months | 1.5x fees | Unlimited |
| IP | Client owns deliverables on payment | License for templates we reuse | Assigning our tools |
| Client approvals | 3 business days ([[2026-02-06-pipeline-sprint-pilot-retro]]) | 5 days | No SLA at all |
| Data | Client's systems, named accounts ([[ADR-007-client-data-stays-in-client-crm]]) | | Exporting client data to our tools |
| AI use | Disclosed, approved tools only ([[ai-use-policy]]) | | Client data in unapproved tools |

Reviewed by [[Pembury-Lane-Legal]] in February. Used by [[legal-contract-check-routine]] and [[proposal-sop]].
