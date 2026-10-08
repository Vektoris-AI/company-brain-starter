---
description: COO delivery check: health per project, stale pages, slipping sprints, scope creep, capacity
---

# /coo-delivery-check

Run as agent `coo`. Routine page: `20_areas/operations/coo-delivery-check-routine.md`.

1. For each active page in `10_projects/`: last `updated`, next step, owner, due date.
2. Flag: no update in 7 days · next step without owner or date · sprint past its planned week ·
   new small asks from the client (scope creep).
3. Compare with `20_areas/operations/capacity-board.md`: more sprints than slots? Retainer hours
   over budget?
4. Propose a health rating (red/amber/green, with the reason) per client and a diff for
   `client-health-scorecard.md`.
5. Write `00_inbox/<YYYY-MM-DD>-coo-delivery-check.md`.

**Always:** follow the brain's schema contract (`CLAUDE.md`). Output is a draft
(`type: inbox`, `status: draft`, honest `confidence`, `sources` linking the pages you used).
Sources you could not reach go under `## Not checked`. Never send, never move money, never sign,
never commit. Reply in chat with a summary that fits on one screen and the path of the draft.
