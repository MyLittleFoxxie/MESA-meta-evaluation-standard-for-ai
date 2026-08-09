---
name: review-benchmark
description: This skill should be used when the user asks to "review this benchmark", "MESA-review <paper/link>", "produce a MESA review from this paper", "audit this benchmark from its GitHub repo", "write a benchmark review", or supplies a paper (path or URL) and/or documentation links (GitHub repository, dataset card, leaderboard, official site) and wants a MESA review produced from them.
---

# Review Benchmark

Turn a paper and/or a set of documentation links into a full MESA review by gathering the starting
source material and delegating the actual review-writing to the `benchmark-reviewer` agent. This
skill is a source-gathering and delegation wrapper, not a second review pipeline — all review-quality
rules (Part A/Part B standards, EFPA rating discipline, broad-claim handling, output conventions)
live in `.claude/agents/benchmark-reviewer.md` (mirrored at `.codex/agents/benchmark-reviewer.md`)
and must not be duplicated here.

## Workflow

1. **Identify and normalize the benchmark entity.** Derive a clear name from what the user supplied
   (a paper title, a repo name, an explicit benchmark name), preserving meaningful capitalization and
   hyphenation, matching the existing `reviews/{normalized-benchmark-name}.md` convention (e.g.
   `ARC-AGI-2`, `DesignQA`).

2. **Check for an existing review.** Use `Glob` for `reviews/**/{name}.md` (the repo currently nests
   reviews under `reviews/{reviewer}/`, e.g. `reviews/chatgpt_reviewer1/{name}.md` — check the
   relevant reviewer folder(s) for this invocation, or `reviews/{name}.md` for a flat single review).
   If a matching review already exists, stop and ask the user for explicit approval before
   overwriting it — never overwrite silently.

3. **Assemble the starting source set** from whatever the user supplied. Use
   `.codex/memory/source-checklist.md` for what to pull out of each source type while
   reading/fetching it (a paper, a repo, a dataset card, a leaderboard, etc. each have a different
   extraction checklist there):
   - A local paper path → read it directly.
   - An arXiv/paper URL → fetch it; also check whether a local copy already exists under `Papers/`
     or a transcription under `literature/` and prefer that if present.
   - A GitHub repository URL → fetch the README/landing page; note the dataset location, evaluation
     harness, license, and any docs worth flagging.
   - Other links (dataset host, leaderboard, official website, docs) → fetch each.
   - If nothing usable was supplied beyond a bare benchmark name, pass the name through as-is and let
     the agent's own Source Discovery Standards find sources from scratch.
   - If a supplied link fails to resolve or clearly does not match the stated benchmark, note that
     explicitly rather than silently dropping it or guessing a replacement.

4. **Determine review scope** from the user's phrasing:
   - "review" / "MESA-review" / "audit" / "full review" with no qualifier → full Part A + Part B.
   - "just the description" / "Part A" / "descriptive only" → Part A-only, no ratings.
   - "prepare Part B" / "evidence table" → Part B evidence preparation, ratings only if the user asks.
   - If scope is ambiguous and consequential (e.g. unclear whether ratings are wanted), ask before
     proceeding rather than guessing.

5. **Delegate to the agent.** Invoke the `Agent` tool with `subagent_type: "benchmark-reviewer"`.
   Pass in the prompt: the normalized benchmark name and target output path, the source material
   gathered in step 3 (fetched content, or the raw links with a note if fetching failed), which
   sources were user-supplied versus still need independent discovery, and the requested scope from
   step 4. Do not pre-draft any part of the review here — the agent produces the review.

6. **Report back.** Once the agent finishes, state the resulting review file's path and surface
   anything the agent itself flagged as missing, unresolved, or needing user approval (e.g. an
   existing-review overwrite it declined to make).

## Notes

- The delegated agent already reads `.codex/memory/template-structure.md` (a condensed map of every
  MESA template heading/subheading with a one-line description) as part of its own operating
  instructions — there is no need to re-supply template structure here.
- If the user names multiple candidate benchmarks, or the request is ambiguous about which entity to
  review, ask which one before invoking the agent.
- This skill never writes to `reviews/` directly; only the delegated `benchmark-reviewer` agent
  writes review files, so every review produced this way still goes through the agent's own
  overwrite-approval and quality rules.
