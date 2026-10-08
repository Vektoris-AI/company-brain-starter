---
title: "Cobaltline Software: CRM migration (estimate)"
type: project
status: draft
created: 2026-09-12
updated: 2026-09-29
tags: [customer, project, example]
sources: ["[[2026-09-10-cobaltline-renewal-call]]"]
confidence: low
---

# Cobaltline Software: CRM migration (estimate)

- **Client:** [[Cobaltline-Software]]. **Status:** estimate in progress, not sold.
- **Owner:** [[Andre-Wallace]] (estimate), [[Jordan-Pike]] (proposal).
- **Context:** raised on the renewal call ([[2026-09-10-cobaltline-renewal-call]]); could be bundled
  with [[cobaltline-ops-retainer]].

## Rough scope
- Freeze and export the cleaned data (we cleaned it in spring, so this is cheaper than usual).
- Rebuild 9 workflows; drop 4 that no one uses ([[automate-only-stable-processes]]).
- Client keeps ownership of the CRM and the data ([[ADR-007-client-data-stays-in-client-crm]]).

## Open questions
- Does their in-house hire start before or after the migration?
- Who signs the data processing terms for the new instance ([[legal-contract-check-routine]])?
