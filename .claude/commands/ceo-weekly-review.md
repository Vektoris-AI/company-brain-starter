---
description: CEO weekly review: OKR movement, decisions for next week, fired revisit triggers, open contradictions
---

# /ceo-weekly-review

Run as agent `ceo`. Routine page: `20_areas/strategy/ceo-weekly-review-routine.md`.

1. Read `20_areas/strategy/okrs-*.md` and `strategy-kpis.md`.
2. Read this week's reports in `00_inbox/` from all other roles. Note what each one flagged.
3. For each objective: what moved, with the page that shows it. No page, no claim.
4. List `_meta/ADR-*.md` whose "Revisit when" condition is now met, with the evidence.
5. List pages tagged `needs-review` and the decision each one needs.
6. Propose the three decisions for next week: decision · owner · due · pages.
7. Write `00_inbox/<YYYY-MM-DD>-ceo-weekly-review.md`.

**Always:** follow the brain's schema contract (`CLAUDE.md`). Output is a draft
(`type: inbox`, `status: draft`, honest `confidence`, `sources` linking the pages you used).
Sources you could not reach go under `## Not checked`. Never send, never move money, never sign,
never commit. Reply in chat with a summary that fits on one screen and the path of the draft.
