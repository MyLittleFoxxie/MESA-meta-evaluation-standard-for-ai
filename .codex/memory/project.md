# Project Memory

## Current decisions — 15 October 2026

`AGENTS.md` is authoritative for current scope. MESA is the 25-question questionnaire with five categorical choices and no total quality score.

- `paper_chase.tex` is the **CHASE** submission: questionnaire adaptation and model experiments, with human evaluation only as future work.
- `paper_refsq.tex` is the **REFSQ** submission: planned as the CHASE paper extended with human evaluation, retaining the shared contribution and model study. Existing contents may still need alignment; do not assume that extension has already been implemented.
- Preserve `paper.tex` as the original manuscript. Do not fabricate human methods or results.
- Use `CHASE-study.md` and saved study records for reported model findings. Sol is the main series; Astra is incomplete and separate. Model roles/repetitions do not represent human participants.
- Use simple terms. Do not present a separate full MESA instrument or previous AI-assisted development as validation in the current papers.
- Human-study claims require actual collected evidence. Do not compile LaTeX or open automatic PDF previews.
- The repository link and `CHASE-study.md` provide supporting files; no separate anonymized-link placeholder is requested. The SWARM subproject was removed.

## Historical context — 25 September 2026

The notes below preserve earlier navigation and design context. Statements about a current manuscript, active instrument, or review pipeline describe that earlier state and are superseded by the decisions above and `AGENTS.md`.

Last checked against the local repository: 2026-09-25. This is a navigation summary; the active template and source materials remain authoritative.

## Thesis revision

The manuscript is now titled **MESA: Adapting and Testing an EFPA-Based Framework for AI Benchmark Review**. Its main contribution is explaining the EFPA adaptation and examining its use. Read `thesis/README.md` for the new scope, question map, pilot analysis, and limited AI-assisted checks. Full new applications, human timing observations, and independent reviewer validation remain unfinished. The original nine reviews were preserved. Use plain language and keep future revisions brief.

## Purpose and Foundations

MESA (Meta-Evaluation Standard for AI Benchmarks) audits AI benchmarks as measurement instruments. The repository contains the manuscript, review framework, source literature, and development records.

Benchmark scores are not self-interpreting: their meaning depends on the claimed capability, task construction, scoring, reliability, validity, documentation, and maintenance. MESA adapts the EFPA Test Review Model 2025, uses CHC theory for capability-domain grounding, BetterBench for lifecycle and engineering quality, and *Measuring what Matters* for the phenomenon-task-metric-claim chain.

## Review Model

- **Part A — description:** General Description, Source Inventory, and Sections 1–5 record identity, provenance, classification, intended systems, tasks, scoring, outputs, access, reproducibility materials, contamination documentation, and maintenance. It answers “What is this benchmark?” without ratings.
- **Part B — evaluation:** Sections 6–12 assess rationale/development/documentation, materials, baselines, reliability, validity, fair use/comparability, and reporting/public claims. The Final Evaluation includes conclusions, recommendations, a Summary of Ratings, and a Gap Register.
- **Ratings:** `n/a` means the attribute does not apply; `0` means insufficient usable evidence about an applicable attribute; `1`–`4` run from inadequate to excellent. Ratings require evidence, missing evidence, reviewer rationale, and interpretation caution. Overall judgments are not mechanical averages.
- **Full template and scorecard:** the current full template has 87 rated items; the generated scorecard retains 40, supporting Part A fields, and the Final Evaluation. Both preserve the same item IDs. The scorecard needs the full template when an omitted question matters, including scorer checks. Neither form is validated for certification.

## Repository Map

| Path | Role |
| --- | --- |
| `README.md`, `CLAUDE.md`, `AGENTS.md` | Project overview, context, and operating instructions; read these before making changes. |
| `paper.tex`, `references.bib` | Current IEEEtran manuscript and bibliography. `paper_old.tex` is also present; do not confuse it with the current manuscript. |
| `MESA EFPA template official.md` | Active unified Part A + Part B source template. |
| `MESA scorecard.md` | Generated short form; do not hand-edit. |
| `tools/build-scorecard.py`, `tools/scorecard-manifest.md` | Scorecard generator and documented selection of retained items. |
| `Papers/` | Original PDF source library. |
| `literature/` | 13 Markdown source transcriptions, including EFPA, BetterBench, construct-validity/AGI literature, benchmark critiques, HLE, and DesignQA. |
| `benchmark_official_documentation_inventory.md` | Candidate benchmarks and their primary documentation for evidence sourcing. |
| `reviews/` | Nine pilot review documents: three benchmarks across two independent reviewers and a supervising editor. |
| `index.html`, `assets/` | Static review website, interactive forms, case-study browser, and fillable PDF support. |
| `feedback/` | Paper/template critique, synthesis, and revision planning; `95-mesa-core-plan.md` records scorecard selection and template migration. |
| `presentation/` | MESA RETRAI 2026 presentation outline. |
| `.codex/agents/` | Research-assistant and benchmark-reviewer profiles, plus reviewer configuration. |
| `.codex/memory/` | Project context, research method, workflow, template structure, and source extraction checklist. |

`dist/hf_mesa_dataset/` and `reports/` are described in repository guides but are absent from this checkout. If generated later, treat them as derived exports/reports, not source evidence.

## Pilot Reviews and Version Boundaries

The case studies cover **Humanity's Last Exam, ARC-AGI-2, and DesignQA**. Each has a draft under `reviews/chatgpt_reviewer1/` and `reviews/claude_reviewer2/`, plus a reconciled review under `reviews/gemini_supervising_editor/`. `GEMINI.md` defines the supervising-editor role. Older guides mention only HLE and ARC-AGI-2; the current files include all three.

The pilot reviews are frozen evidence from the earlier 89-item template. The current v2 template has 87 rated items. Retired IDs are preserved rather than renumbering surviving items: `2.6 → 2.9`, `4.10 → 2.4`, `10.6.2 → 10.6.1`, and `11.3.2 → 11.3.1`. Consult `feedback/95-mesa-core-plan.md` Part 3 before comparing versions.

## Website and Generation Workflow

- `assets/mesa-site.js` routes the static site and loads README/case-study Markdown using relative paths.
- `assets/mesa-form.js` builds the full-template and scorecard forms. Answers persist in browser `localStorage` and share item keys across both views.
- `assets/mesa-pdf.js` exports fillable PDFs and imports their answers. Markdown rendering, Mermaid diagrams, and PDF support use vendored libraries under `assets/vendor/`.
- Regenerate the scorecard from the repository root with `python3 tools/build-scorecard.py` after authorized template or manifest changes. The script reads the full template and writes the scorecard; inspect the resulting diff.
- Keep `.codex/memory/template-structure.md` synchronized when template headings change. Use it together with `source-checklist.md` when researching or drafting reviews.

## Working Constraints

Keep descriptive facts separate from evaluation. Prefer primary benchmark evidence, attribute claims, and record missing documentation as an evidence gap rather than proof of poor quality. Assign Part B ratings only when requested, after collecting the factual evidence. Broad intelligence claims need evidence across relevant capabilities.

Preserve original papers, templates, pilot reviews, and existing notes unless the user authorizes their modification. Treat exports and generated scorecards as derived artifacts. Follow `CLAUDE.md`'s instruction not to compile LaTeX.
