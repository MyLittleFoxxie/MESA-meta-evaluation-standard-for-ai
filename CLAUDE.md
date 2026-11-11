# MESA Repository Context for Claude

Read [`AGENTS.md`](AGENTS.md) for repository rules and source boundaries, [`v4/README.md`](v4/README.md) for the v4 comparative standard and rubric study, and [`README.md`](README.md) and [`CHASE-study.md`](CHASE-study.md) for the earlier 25-question questionnaire study.

## Current Contribution and Manuscripts

The current MESA manuscript is [`mesa_paper.tex`](mesa_paper.tex), **Unifying Benchmark Evaluation Protocols: A Meta-Evaluation Standard for Artificial Intelligence in Requirements Engineering**, intended for REFSQ in Springer LNCS format. It reports the framework comparison and rubric study and proposes a requirements traceability application. Human validation and effects on requirements decisions remain unestablished.

The frozen v4 mapping allocates 280 framework items to 30 comparison concerns. Its derived rubric has eight description fields and 29 evaluation questions. Rubric v5 ([`v5/rubric/rubric.md`](v5/rubric/rubric.md)) keeps that mapping, adopts the paper's level names, adds outcome, scope, check kind, detection limits and task defects to each rating, and splits B14 and B28, giving 31 evaluation questions; see [`v5/README.md`](v5/README.md). The current rubric text is [`v5/rubric/rubric-v5.1.md`](v5/rubric/rubric-v5.1.md), which settles feedback item 15 without changing any question; `rubric.md` stays frozen for Study 3. `mesa_paper.tex` presents v5 as its only rubric, with no version names, and reports the v5 sessions (`v5/study/`) as its Study 2; the v4 rubric sessions are not in the paper. These are distinct from the earlier 25 question questionnaire with six domains, five choices, and no total quality score. See [`v4/README.md`](v4/README.md) and [`v4/study/README.md`](v4/study/README.md).

Preserve [`paper.tex`](paper.tex), [`paper_old.tex`](paper_old.tex), [`paper_mesa_v3.tex`](paper_mesa_v3.tex), and [`paper2_preview.tex`](paper2_preview.tex). The removed CHASE manuscripts and MESA v4 manuscript remain retrievable through the [consolidation record](provenance/manuscript-consolidation-2026-11-03.md). Do not restore them as active submission targets.

Paper 2 ([`paper2.tex`](paper2.tex)) and its protocol 5 evaluation: read [`paper2_runbook.md`](paper2_runbook.md) first, and update it in the same change whenever the procedure, code, records, or state change.

Feedback for the MESA paper from implementing it in Paper 2 is in [`mesa_paper_feedback_from_paper_2.md`](mesa_paper_feedback_from_paper_2.md); read it before revising `mesa_paper.tex`.

## Repository Structure and Working Rules

- [`literature/README.md`](literature/README.md): Source index and thematic reading guide covering `literature/pdfs/`, `literature/transcriptions/`, and `literature/notes/`.
- [`supporting/adaptation/`](supporting/adaptation/): [`adaptation-map.md`](supporting/adaptation/adaptation-map.md) and [`standards-assessment.md`](supporting/adaptation/standards-assessment.md).
- [`supporting/retrai-paper/`](supporting/retrai-paper/): Detailed adaptation documents (`MESA EFPA template official.md`, generated `MESA scorecard.md`), pilot `reviews/`, `thesis/` records, and `provenance/` files supporting `paper.tex`. Do not describe them as a separate “full MESA” instrument in the current papers.
- [`supporting/editorial/`](supporting/editorial/): [`CHASE-review-response.md`](supporting/editorial/CHASE-review-response.md).
- [`provenance/`](provenance/): [`archive-index.md`](provenance/archive-index.md) and [`relocation-map.json`](provenance/relocation-map.json) documenting relocated files and retrieval of archived historical studies from the `pre-reorganization-2026-10-22` Git snapshot.

Use simple academic prose and verified sources in [`references.bib`](references.bib). Preserve frozen inputs, raw outputs, failures, benchmark reviews, the live survey, and unrelated edits.

For survey tasks, read [`surveys/colleague-review/agent-guide.md`](surveys/colleague-review/agent-guide.md), [`surveys/colleague-review/packet.json`](surveys/colleague-review/packet.json), and [`surveys/colleague-review/future-steps.md`](surveys/colleague-review/future-steps.md). Keep the 25 questions, five choices, three familiarity self-reports, completed HLE teaching example, blank ARC-AGI-2 and DesignQA participant answers, and five required closing feedback ratings (each with `Cannot judge` and no composite score). Never fabricate human observations or send real survey submissions/emails without authorization.

## Rules

- Avoid hyphenated terms unless necessary.
- Avoid adjectives unless necessary.
- Avoid marketing-style terms, such as those common in titles.
- Make written text be easy to understand, and flow naturally.
- Do not make mistakes.

## Verification

- Current manuscripts: `python3 verify_manuscripts.py` (MESA and paper two preview).

- v4 mapping & study harness: `python3 v4/mapping/check.py` and `python3 v4/study/test_harness.py`
- Historical questionnaire checks: run the analysis and verification commands in `CHASE-study.md` only in the earlier checkout described by the [consolidation record](provenance/manuscript-consolidation-2026-11-03.md); its verifier requires the removed CHASE manuscript.
- Guided survey: `python3 surveys/colleague-review/verify.py`
- Supporting RETRAI bundle: `python3 tools/check-thesis.py`
- **LaTeX compilation is supported locally.** Use Tectonic (`/Applications/ChatGPT.app/Contents/Resources/tectonic/tectonic <file>.tex` or system `tectonic`) or BasicTeX (`/Library/TeX/texbin/pdflatex`) with `llncs.cls` and `splncs04.bst` in the root. Verify that both manuscripts remain $\le 15$ pages including references (`mdls -name kMDItemNumberOfPages <file>.pdf` or `pypdf`). Do not open automatic GUI PDF previews.
