---
name: mesa-core-plan
description: This skill should be used after the MESA self-review feedback is complete, when the user asks to "plan the new template", "design MESA Core", "trim the template", "plan the template rewrite", or wants a migration plan turning the feedback in `feedback/` into a shorter MESA template plus the repo-wide changes that must follow it. Produces a plan, not the template itself.
---

# MESA Core Plan

Turn the completed section-by-section feedback in `feedback/` into a single plan for a
**shorter, usable MESA template** and the repo-wide migration that must accompany it.

This skill produces `feedback/95-mesa-core-plan.md` — a **plan**, not the new template and not
new feedback. It consumes the output of `/mesa-self-review`; it never generates findings of its
own beyond what the feedback supports.

The design problem it solves: the template is 2,479 lines with 89 rated items, plus free-text
prompts, fill-in tables, and checkbox matrices across 194 headings — more than most reviewers
will finish. But MESA's authority comes from being a faithful
adaptation of the EFPA Test Review Model 2025. Shortening it without a traceability record
would trade the standard's credibility for its usability. The EFPA traceability table exists to
make every cut provably non-silent.

## Gate

Read `feedback/00-progress.md` first. If any ledger unit is not `done`, **stop**: report which
units are still pending and how many, and do not produce a partial plan. A trim designed from
half the evidence is worse than no trim.

If `feedback/` does not exist at all, tell the user to run `/mesa-self-review` first.

## Inputs

- Every file in `feedback/` — read them all. The **Verdict** blocks (`Keep as-is / Trim /
  Rewrite / Merge into §X`, with item counts before → after) are the primary signal.
- `feedback/80-xcut-terminology` — the Substitute / Keep+define / Split decisions.
- `feedback/80-xcut-length-budget` — where reviewer burden concentrates.
- `feedback/90-synthesis` — the ranked findings.
- `literature/EFPA_Test_Review_Model_2025_Markdown.md` (2,804 lines) — required in full for the
  traceability table, since every EFPA item must appear in it.
- `MESA EFPA template official.md` — for current item counts and section numbering.

## Output: `feedback/95-mesa-core-plan.md`

### Part 1 — MESA Core

The minimum item set a reviewer must complete for a MESA review to be **valid**. Give a target
item count and an estimated completion time.

Core must be defensible as *sufficient*, not merely short. For each section, state what the
Core subset preserves about the intended score meaning and what a Core-only review can and
cannot conclude. If a section contributes nothing to Core, say so explicitly and justify it.

### Part 2 — MESA Extended

Items retained but made **conditional on benchmark type**, so a reviewer answers them only when
they apply. Define the trigger for each conditional block. Expected triggers:

- benchmarks making broad capability, general-intelligence, or AGI claims;
- benchmarks scored by another model (LLM-as-judge);
- hosted leaderboards and public results portals;
- private, held-out, or rolling/refreshed forms;
- benchmarks used in procurement, policy, or other high-stakes comparison.

### Part 3 — EFPA traceability table

One row per EFPA item. **Every EFPA item appears.** An item missing from this table is a silent
drop — the single failure mode this deliverable exists to prevent.

| EFPA § | EFPA line ref | MESA § (new) | Disposition | Note |
|---|---|---|---|---|
| … | `EFPA_Test_Review_Model_2025_Markdown.md:NNNN` | … | Core / Extended / Merged into §X / Dropped | reason required for Merged and Dropped |

Rules:

- `Dropped` rows **must** carry a reason, and that reason must be why the item does not apply to
  AI benchmarks — not that it was inconvenient or long.
- `Merged into §X` rows must name where the function survives.
- Include MESA-original items (those with no EFPA ancestor) in a second, clearly separate table,
  so the adaptation boundary stays visible.
- Close with a count: EFPA items in / Core / Extended / merged / dropped.

### Part 4 — Terminology migration

Turn `80-xcut-terminology` into an executable find-and-replace list applied across the **whole
repo**, not just the template. Columns: term, verdict (Substitute / Keep+define / Split),
replacement wording, files affected.

A term renamed in the template but left standing in the reviews, the agent files, and the
website is worse than not renaming it at all. Note that the Keep+define rows are the only
glossary entries — the glossary should be short by design.

### Part 5 — Sequenced repo migration plan

The template is not standalone. Seven surfaces encode its structure and drift silently when it
changes. The plan must carry an ordered step for each, naming files and the specific coupling.
Verify each path against the repo before writing the step — do not copy this table blind.

| # | Surface | Files | Coupling |
|---|---|---|---|
| 1 | **Template** | `MESA EFPA template official.md` | Source of truth. Section numbering is load-bearing — items are cited as e.g. "6.1.9" across the repo, so any renumbering cascades to everything below. State up front whether numbering is preserved or changed; preserving it makes steps 2-7 dramatically cheaper. |
| 2 | **Agent / skill assets** | `.claude/agents/benchmark-reviewer.md`, `.claude/skills/review-benchmark/SKILL.md`, `.codex/agents/benchmark-reviewer.md`, `.codex/agents/benchmark-reviewer.toml` | These carry the Part A / Part B standards and output conventions. Stale section names here silently produce new reviews against the old template. |
| 3 | **Agent memory** | `.codex/memory/template-structure.md` (281 lines; self-declared mirror, numbering "exact and load-bearing"), `.codex/memory/source-checklist.md`, `.codex/memory/research-method.md` | `template-structure.md` must be **regenerated** from the new template, not hand-patched. `source-checklist.md` maps source types to template destinations and breaks the same way. |
| 4 | **Website** | `assets/mesa-form.js`, `assets/mesa-pdf.js`, `index.html` | Already data-driven: `assets/mesa-form.js:19` fetches the template markdown at load time and builds the fillable form by parsing it, so a new template is picked up with **no code change** — provided the authoring conventions at `assets/mesa-form.js:6-14` survive. Two real risks: (a) convention drift silently drops items from the live form; (b) item IDs derive from numeric heading prefixes while answers persist under `STORAGE_KEY = "mesa-form-answers-v1"` (`assets/mesa-form.js:20`), so renumbering orphans every in-progress saved review. **Decide explicitly whether to bump that key.** |
| 5 | **Case studies** | 9 files under `reviews/` — `chatgpt_reviewer1/`, `claude_reviewer2/`, `gemini_supervising_editor/`, ~12,000 lines | Completed reviews against the old numbering, cited by the paper. **Choose and justify one:** migrate all nine; migrate only the three reconciled `gemini_supervising_editor/` finals; or freeze all nine with a version stamp ("reviewed against MESA v1"). Freezing is likely cheapest and most honest — the reviews are dated evidence, not living documents — but it must be an explicit decision recorded in the plan, not neglect. |
| 6 | **Paper and docs** | `paper.tex:140-189` (§The MESA Test Review Model), the Figure 1 structure diagram in both `paper.tex` and the template front matter, `README.md` phase lists, `MESA___Thesis___Vitor_Brandao_Raposo.pdf` | The paper *describes* the template; if it describes a version that no longer exists, the paper's artifact claim is false. The PDF needs recompiling **by the user** — do not compile LaTeX (`CLAUDE.md`). |
| 7 | **Generated export** | `dist/hf_mesa_dataset/` (gitignored, untracked) | Derived output whose `schema/*.schema.json` is keyed to template fields. No build script exists in the repo, so flag regeneration as manual and name who does it. |

For each step state: files touched, whether it is **mechanical** or **judgment-dependent**, and
**what breaks if skipped**.

### Part 6 — Consistency check

Name the concrete check to run after migration: grep the repo for old section numbers and for
the old spellings of every substituted or split term, and confirm zero hits outside `feedback/`
and any intentionally frozen reviews. Give the actual grep patterns.

## Standing constraints

- **Plan, don't build.** Do not write the new template, do not edit the existing one, and do not
  touch any of the seven surfaces. Write only `feedback/95-mesa-core-plan.md`.
- **Every cut is traceable.** No item leaves the template without a row in the EFPA table.
- **Ground every recommendation in a finding.** Cite the feedback file and finding ID
  (`F-<unit>-<n>`) that motivates each Core/Extended/drop decision. A recommendation with no
  finding behind it does not belong in the plan.
- **Preserve the parser contract.** Any structural proposal must keep the authoring conventions
  at `assets/mesa-form.js:6-14` intact, or explicitly schedule the parser change alongside it.
- **Be honest about cost.** Give a realistic effort estimate per migration step. If migrating
  all nine reviews is a week of work, say so — that is the information the user needs to choose
  freezing instead.
- **Repo style applies** (`CLAUDE.md`): concise academic prose, explicit assumptions, cautious
  language, uncertainty flagged rather than filled in.
- **Do not compile LaTeX.**

## Notes

- If the feedback contains contradictory verdicts for related sections, surface the conflict and
  recommend a resolution rather than silently picking one.
- If the feedback does not support a defensible Core for some section, say the evidence is
  insufficient and name what additional review would settle it. Do not invent a cut.
- The plan's success condition is that a reader can see, in one table, that MESA got shorter
  **without** getting less faithful to EFPA. If the table cannot show that, the trim is too
  aggressive and the plan should say so.
