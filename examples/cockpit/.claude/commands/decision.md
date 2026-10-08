---
description: Record a decision as an ADR in the company brain (proposal, no commit)
argument-hint: "<decision topic>"
---

# /decision

Record the decision on `$ARGUMENTS` as a decision record (ADR) in
`<path-to-brain>/_meta/`.

1. **Clarify the context.** If the conversation does not make it clear, ask:
   What is the problem? Which options were on the table? What was decided, and
   why? An ADR without a reason is worthless.
2. **Pick the number.** List the existing `_meta/ADR-*.md` and use the next free
   number. File name: `ADR-<NNN>-<kebab-slug>.md`.
3. **Write it** from the template `<path-to-brain>/40_resources/templates/adr.md`: frontmatter per the
   brain's schema contract (`type: adr`, `status: draft` until a human merges it,
   honest `confidence`),
   then **Context, Options (pros and cons), Decision, Consequences, Revisit
   when** (the signal that tells us to reconsider).
4. **Link it.** Reference affected notes as `[[note-name]]`. If the decision
   contradicts an existing note, add `contradicts: [[...]]` and the tag
   `needs-review` there.
5. **Do not commit.** The diff stays for human review.
