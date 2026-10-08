# Company Brain Starter

**Karpathy's LLM-wiki idea, applied to a whole company.**

A plain-Markdown knowledge base for a small team that both people (in
Obsidian) and AI agents (in Claude Code) can read, keep in order and trust.
It comes with a schema contract that tells agents how to write, three agent
loops (ingest, query, lint), a link and frontmatter checker, and an optional
local semantic search.

Extracted from the brain we run our own 2-person AI studio on. Our content is
removed; the structure, rules and tools are the ones we use.

## The problem it solves

AI tools are only as good as what they read. In most small companies the
truth is scattered across chat threads, a shared drive and one or two
people's heads. Point an assistant at that and it answers confidently from
an outdated document.

So before more AI, you need one place where the current, reviewed version of
things lives:

- **Plain files in git.** Every change an agent makes is a diff a human reviews.
  No vendor lock-in, no database to run.
- **Raw sources are kept, never edited** (`_raw/`). Knowledge pages cite them,
  so every statement can be traced back.
- **One idea per page, linked.** Small pages with `[[links]]` are easy for
  agents to retrieve and easy for humans to correct.
- **Contradictions are flagged, not overwritten.** Conflicting information
  gets a `needs-review` tag and waits for a human.

The idea comes from Andrej Karpathy's
[LLM wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):
raw material is "compiled" by an LLM into a linked wiki that keeps getting
better, guided by a schema file. This kit applies that to a company:
customers, decisions, processes, offers.

## What's inside

```
CLAUDE.md                    Schema contract for agents: where things go, required frontmatter, principles, autonomy levels
00_inbox/ … 90_archive/      Folders for humans (PARA): inbox, projects, areas, resources, archive
30_knowledge/ 50_people/     Folders for agents: the wiki and its entities
_raw/                        Immutable sources (transcripts, exports, PDFs)
_meta/                       Decision records (ADRs), ingest log, conventions
_index/                      Local search index (generated, git-ignored)
.claude/skills/              /ingest, /query, /lint
tools/lint.py                Frontmatter, dead links, orphans, edits to _raw/ (standard library only)
tools/embed.py, search.py    Optional: page-level embeddings via Ollama, cosine search
.githooks/post-commit        Rebuilds the search index after commits that touch notes
.obsidian/                   Minimal vault settings (new notes go to the inbox, links update on rename)
tests/                       unittest suite for lint, embed and search
examples/cockpit/            Optional: four agents and three commands that work on top of the brain
```

Four fictional example pages (a customer, a knowledge page, a decision, a
raw call note) are included so the graph is not empty and you can see links,
sources and lint in action. They are marked as examples. Delete them once
you have your own.

## Set it up (about 15 minutes)

You need git, Python 3.9+, Claude Code and, if you want it, Obsidian.

1. **Copy the kit** to where your company brain should live and make it a
   private git repo:
   ```bash
   cp -R company-brain-starter ~/company-brain && cd ~/company-brain
   git init && git add -A && git commit -m "Start company brain"
   ```
2. **Open it in Obsidian** ("Open folder as vault"). Look at the graph: four
   example pages, linked.
3. **Run the checks:**
   ```bash
   python3 tools/lint.py                       # 0 errors, 0 warnings
   python3 -m unittest discover -s tests       # search tests skip without numpy
   ```
4. **Read `CLAUDE.md` and adjust it.** Folder names, allowed types and tags
   are yours to change. Keep `tools/lint.py` in sync (`NOTE_DIRS`, `ALLOWED`).
5. **Ingest your first real source.** Start Claude Code in the vault folder
   and run `/ingest` with a meeting transcript, a proposal or an email thread.
   Review the diff, then commit it yourself.
6. **Optional: semantic search.**
   ```bash
   ollama pull bge-m3
   python3 -m venv .venv && .venv/bin/pip install -r tools/requirements.txt
   .venv/bin/python tools/embed.py
   .venv/bin/python tools/search.py "what did we decide about onboarding?"
   git config core.hooksPath .githooks          # rebuild the index after each commit
   ```
   Everything runs locally. The only network call goes to your Ollama server.

## How agents work with it

| Loop | You say | The agent |
|---|---|---|
| Ingest | "/ingest these call notes" | Saves the source to `_raw/`, updates or creates atomic pages, links them both ways, flags contradictions, logs the ingest, runs lint, leaves the diff for you |
| Query | "/query what do we know about this customer?" | Searches (semantic + grep), reads the full pages and their links, answers with `[[citations]]`, says so when the brain doesn't know |
| Lint | "/lint" | Runs `tools/lint.py`, fixes mechanical issues, lists stale, unsourced, duplicate and contradictory pages in a report for you |

By default agents write files and you commit (level 1 of the autonomy slider
in `CLAUDE.md`). Raise autonomy per loop, and only once its checks have been
green for a while.

## Limits

- **It is a structure, not content.** The value comes from what you put in
  and from reviewing what agents write. Unreviewed agent output is not
  knowledge.
- **Lint checks structure, not truth.** It finds broken links and missing
  fields. Whether a page is still correct is the content review in `/lint`,
  and a human's call.
- **The search index is page-level and linear.** That keeps it simple and
  fast for a small team's vault. For a very large vault you would want
  chunking and a vector store.
- **The `_raw/` check needs git** and only catches uncommitted edits.
- **Private by default.** A company brain collects customer and personal
  data. Keep the repo private and don't sync it into tools you haven't vetted.

## License

MIT. See `LICENSE`.

---

Built by Moritz · [@VektorisAI](https://x.com/VektorisAI)
