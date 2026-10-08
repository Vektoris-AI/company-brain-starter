---
title: "Granitefold Insurance Brokers: CRM cleanup"
type: project
status: active
created: 2026-04-09
updated: 2026-09-20
tags: [customer, project, example]
sources: ["[[2026-04-09-granitefold-crm-audit-export]]"]
confidence: medium
---

# Granitefold Insurance Brokers: CRM cleanup

| | |
|---|---|
| Client | [[Granitefold-Insurance-Brokers]] |
| Offer | CRM cleanup ([[service-catalog]]), $9,800 fixed |
| Team | [[Andre-Wallace]], AM [[Chris-Delgado]] |
| Status | Final week; handover call planned 2026-10-12 |

## Starting point
23,410 records, 3,120 duplicates, 5,870 without owner, 6 conflicting workflows
([[2026-04-09-granitefold-crm-audit-export]]).

## Approach
Dedupe, archive dead records, then one owner per record. No new automation until the data
holds for 30 days ([[crm-hygiene-before-automation]], [[automate-only-stable-processes]]).

## Next step
Handover with [[client-offboarding-sop]], then offer a light ops retainer. Upsell only if the
client asks; see [[one-owner-per-client-relationship]].
