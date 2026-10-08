---
name: query
description: Answer a question from the company brain with citations to its pages (query loop). Use for questions about the company's own customers, decisions, offers, processes, history or strategy, e.g. "what did we decide about X?", "what do we know about customer Y?", "how do we do Z?". Answers only from the vault and says clearly when the vault does not know.
---

# Query: answer from the brain, with citations

## Steps

1. **Retrieve.** Combine both:
   - Semantic: `python3 tools/search.py -k 8 "<question>"` (use the `.venv`
     Python if numpy lives there). If it says the index is outdated, run
     `tools/embed.py` first or add `--allow-stale` and say so in the answer.
     If there is no index or Ollama is not running, skip this step and say so.
   - Exact: grep for names, product terms, dates.
2. **Read whole pages,** not snippets. Follow their `[[links]]` one hop, and
   check what links back to them. Decisions live in `_meta/ADR-*.md`.
3. **Answer.**
   - Lead with the answer in one or two sentences.
   - Cite every claim with the page it comes from: `[[page-name]]`. Cite the
     `_raw/` source when the exact wording matters.
   - Report `confidence:` and `updated:` of the pages you rely on when they are
     low or old.
   - Surface contradictions (`contradicts:`, `needs-review`) instead of
     picking a side.
   - If the vault does not contain the answer, say "The brain has nothing on
     this" and stop. Do not fill gaps from general knowledge without labeling
     it as such.
4. **Compound.** If the answer took real synthesis across several pages and
   will be asked again, offer to save it as a new page in `30_knowledge/`
   (with sources and links). Write it only if the user agrees; never commit.
