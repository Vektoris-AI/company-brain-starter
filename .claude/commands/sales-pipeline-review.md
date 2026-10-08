---
description: Head of Sales pipeline review: due and stale deals, follow-up drafts, price and term checks
---

# /sales-pipeline-review

Run as agent `head-of-sales`. Routine page: `20_areas/sales/sales-pipeline-review-routine.md`.

1. Read `20_areas/sales/pipeline.md`. List deals with a next step due or overdue, by owner.
2. Flag deals without contact for 7+ days (`follow-up-rules.md`).
3. Check every quoted price and term against `service-catalog.md` and the ADRs. List conflicts;
   don't resolve them.
4. Draft follow-ups for due deals (owner, recipient, subject, body). Never send.
5. Propose a diff for `pipeline.md` (stages, next steps).
6. Write `00_inbox/<YYYY-MM-DD>-sales-pipeline-review.md`.

**Always:** follow the brain's schema contract (`CLAUDE.md`). Output is a draft
(`type: inbox`, `status: draft`, honest `confidence`, `sources` linking the pages you used).
Sources you could not reach go under `## Not checked`. Never send, never move money, never sign,
never commit. Reply in chat with a summary that fits on one screen and the path of the draft.
