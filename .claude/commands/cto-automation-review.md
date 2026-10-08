---
description: CTO automation review: broken automations, candidates to automate, tools without DPA, pages that trip the agents
---

# /cto-automation-review

Run as agent `cto`. Routine page: `20_areas/technology/cto-automation-review-routine.md`.

1. Run `python3 tools/lint.py` and list errors and warnings.
2. Scan this month's `00_inbox/` reports for places where agents relied on stale or contradictory
   pages.
3. List automations that broke or were overridden by hand (from project pages).
4. Candidates to automate: only processes that ran unchanged for about four weeks, with evidence.
5. Compare `tool-stack.md` with `ai-use-policy.md`: tools without owner or DPA.
6. Write `00_inbox/<YYYY-MM-DD>-cto-automation-review.md`.

**Always:** follow the brain's schema contract (`CLAUDE.md`). Output is a draft
(`type: inbox`, `status: draft`, honest `confidence`, `sources` linking the pages you used).
Sources you could not reach go under `## Not checked`. Never send, never move money, never sign,
never commit. Reply in chat with a summary that fits on one screen and the path of the draft.
