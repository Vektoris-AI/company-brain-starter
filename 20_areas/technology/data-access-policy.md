---
title: "Data access policy"
type: area
status: active
created: 2026-04-15
updated: 2026-08-12
tags: [tech, legal, example]
sources: []
confidence: high
---

# Data access policy

1. Client data stays in the client's systems; we get named, revocable accounts
   ([[ADR-007-client-data-stays-in-client-crm]]).
2. Least privilege per project; access ends at offboarding ([[client-data-least-privilege]],
   [[client-offboarding-sop]]).
3. Requests and removals via [[access-request-sop]].
4. Agents read the brain and read-only connectors; no agent gets client CRM write access.
5. Suspected exposure: [[data-incident-sop]].

Owner [[Sam-Whitaker]]; legal side [[internal-privacy-policy]].
