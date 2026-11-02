# MESA Repository Context for Claude

Read [`AGENTS.md`](AGENTS.md) for repository rules and source boundaries, [`v4/README.md`](v4/README.md) for the v4 comparative standard and rubric study, and [`README.md`](README.md) and [`CHASE-study.md`](CHASE-study.md) for the earlier 25-question questionnaire study.

## Current Contribution and Manuscripts

The repository tracks both the **v4 MESA comparative standard and derived evidence rubric** ([`v4/`](v4/)) and the preserved earlier iterations of MESA:

- **Current CHASE v4 submission (`paper_chase_v4.tex`) and full v4 manuscript (`paper_mesa_v4.tex`):** *A Common Standard for Comparing Reviews of Artificial Intelligence Benchmarks.* Maps 280 items across seven benchmark review frameworks (BetterBench, ECBD worksheet, Scorecard of AI Benchmark Quality, How2Bench, Agentic Benchmark Checklist, Benchmark Caliper, OECD facets) onto 30 shared concerns, recodes outcomes into *favorable*, *unfavorable*, and *unresolved* with *partial* and *unresolved by rule* markers, and evaluates a derived 8-facet, 29-question evidence rubric across HumanEval, TruthfulQA, Humanity's Last Exam, and $\tau$-bench using Claude Sonnet 5.5 (`v4/study/`). See [`v4/README.md`](v4/README.md) and [`v4/study/README.md`](v4/study/README.md) for file, snapshot, export, and packaging details.
- **Preserved v3 audit rubric manuscript:** [`paper_mesa_v3.tex`](paper_mesa_v3.tex) ([`v3/`](v3/)).
- **Preserved 25-question EFPA questionnaire manuscripts:** [`paper_chase.tex`](paper_chase.tex) and [`paper_refsq.tex`](paper_refsq.tex) (*MESA: Adapting the EFPA Test Review Model for AI Benchmark Review*), covering the 25-question questionnaire adapted from the EFPA Test Review Model 2025 (`surveys/colleague-review/mesa-study/chase-report/`, Claude Sonnet 5.5, 30 conversations).
- **Preserved RETRAI submission manuscript:** [`paper.tex`](paper.tex), preserved unless the user explicitly requests changes.
- **Preserved older manuscript:** [`paper_old.tex`](paper_old.tex), preserved unless the user explicitly requests changes.

## Repository Structure and Working Rules

- [`literature/README.md`](literature/README.md): Source index and thematic reading guide covering `literature/pdfs/`, `literature/transcriptions/`, and `literature/notes/`.
- [`supporting/adaptation/`](supporting/adaptation/): [`adaptation-map.md`](supporting/adaptation/adaptation-map.md) and [`standards-assessment.md`](supporting/adaptation/standards-assessment.md).
- [`supporting/retrai-paper/`](supporting/retrai-paper/): Detailed adaptation documents (`MESA EFPA template official.md`, generated `MESA scorecard.md`), pilot `reviews/`, `thesis/` records, and `provenance/` files supporting `paper.tex`. Do not describe them as a separate “full MESA” instrument in the current papers.
- [`supporting/editorial/`](supporting/editorial/): [`CHASE-review-response.md`](supporting/editorial/CHASE-review-response.md).
- [`provenance/`](provenance/): [`archive-index.md`](provenance/archive-index.md) and [`relocation-map.json`](provenance/relocation-map.json) documenting relocated files and retrieval of archived historical studies from the `pre-reorganization-2026-10-22` Git snapshot.

Use simple academic prose and verified sources in [`references.bib`](references.bib). Preserve frozen inputs, raw outputs, failures, benchmark reviews, the live survey, and unrelated edits.

For survey tasks, read [`surveys/colleague-review/agent-guide.md`](surveys/colleague-review/agent-guide.md), [`surveys/colleague-review/packet.json`](surveys/colleague-review/packet.json), and [`surveys/colleague-review/future-steps.md`](surveys/colleague-review/future-steps.md). Keep the 25 questions, five choices, three familiarity self-reports, completed HLE teaching example, blank ARC-AGI-2 and DesignQA participant answers, and five required closing feedback ratings (each with `Cannot judge` and no composite score). Never fabricate human observations or send real survey submissions/emails without authorization.

## Verification

- v4 mapping & study harness: `python3 v4/mapping/check.py` and `python3 v4/study/test_harness.py`
- Earlier CHASE questionnaire study & manuscript: `python3 surveys/colleague-review/mesa-study/chase-report/analyze.py` and `python3 surveys/colleague-review/mesa-study/chase-report/verify.py`
- Guided survey: `python3 surveys/colleague-review/verify.py`
- Supporting RETRAI bundle: `python3 tools/check-thesis.py`
- **Do not compile LaTeX or open an automatic PDF preview.** Use static checks and report layout and page length as unchecked.
