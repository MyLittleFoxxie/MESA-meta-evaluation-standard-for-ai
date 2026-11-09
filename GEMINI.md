# Gemini Repository Guide

Read [`AGENTS.md`](AGENTS.md) first; it is the authoritative repository guide for research scope, manuscript targets, source boundaries, and verification rules. Then read [`README.md`](README.md), [`v4/README.md`](v4/README.md), and the relevant source files before editing.

## Project Scope and Manuscripts

The current MESA manuscript is [`mesa_paper.tex`](mesa_paper.tex), **Unifying Benchmark Evaluation Protocols: A Meta-Evaluation Standard for Artificial Intelligence in Requirements Engineering**, intended for REFSQ in Springer LNCS format. It reports the framework comparison and rubric study and proposes a requirements traceability application. Human validation and effects on requirements decisions remain unestablished.

The frozen v4 mapping allocates 280 framework items to 30 comparison concerns. Its derived rubric has eight description fields and 29 evaluation questions. Rubric v5 ([`v5/rubric/rubric.md`](v5/rubric/rubric.md)) keeps that mapping, adopts the paper's level names, adds outcome, scope, check kind, detection limits and task defects to each rating, and splits B14 and B28, giving 31 evaluation questions; see [`v5/README.md`](v5/README.md). The current rubric text is [`v5/rubric/rubric-v5.1.md`](v5/rubric/rubric-v5.1.md), which settles feedback item 15 without changing any question; `rubric.md` stays frozen for Study 3. `mesa_paper.tex` presents v5 as its only rubric, with no version names, and reports the v5 sessions (`v5/study/`) as its Study 2; the v4 rubric sessions are not in the paper. These are distinct from the earlier 25 question questionnaire with six domains, five choices, and no total quality score. See [`v4/README.md`](v4/README.md) and [`v4/study/README.md`](v4/study/README.md).

Preserve [`paper.tex`](paper.tex), [`paper_old.tex`](paper_old.tex), [`paper_mesa_v3.tex`](paper_mesa_v3.tex), and [`paper2_preview.tex`](paper2_preview.tex). The removed CHASE manuscripts and MESA v4 manuscript remain retrievable through the [consolidation record](provenance/manuscript-consolidation-2026-11-03.md). Do not restore them as active submission targets.

## Repository Layout and Source Boundaries

- [`literature/README.md`](literature/README.md): Source index and thematic reading guide pairing original PDFs (`literature/pdfs/`), extracted transcriptions (`literature/transcriptions/`), and benchmark documentation notes (`literature/notes/`). Original PDFs remain authoritative where extraction loses detail.
- [`supporting/adaptation/`](supporting/adaptation/): Active EFPA correspondence map ([`adaptation-map.md`](supporting/adaptation/adaptation-map.md)) and ACM SIGSOFT empirical standards assessment ([`standards-assessment.md`](supporting/adaptation/standards-assessment.md)).
- [`supporting/retrai-paper/`](supporting/retrai-paper/): Supporting records for the preserved RETRAI manuscript (`MESA EFPA template official.md`, generated `MESA scorecard.md`, `reviews/`, `thesis/`, and `provenance/`). Do not describe these as a second current MESA instrument in the current paper, and do not hand-edit `MESA scorecard.md`.
- [`supporting/editorial/`](supporting/editorial/): [`CHASE-review-response.md`](supporting/editorial/CHASE-review-response.md).
- [`surveys/colleague-review/`](surveys/colleague-review/): Live participant survey bundle (`packet.json`, `template.html`, `survey.html`, `survey.md`, `build.py`, `verify.py`) and the CHASE model-study records (`mesa-study/chase-report/`, `mesa-study/claude-sonnet-5-5/`, `mesa-study/claude-sonnet-5-5-guidance-v2/`).
- [`provenance/`](provenance/): [`archive-index.md`](provenance/archive-index.md), [`relocation-map.json`](provenance/relocation-map.json), and [`reorganization-plan.md`](provenance/reorganization-plan.md) documenting relocated paths and retrieval of archived historical studies from the `pre-reorganization-2026-10-22` Git snapshot.

## Guided Survey Workflow

For survey tasks, read [`surveys/colleague-review/agent-guide.md`](surveys/colleague-review/agent-guide.md), [`surveys/colleague-review/packet.json`](surveys/colleague-review/packet.json), and [`surveys/colleague-review/future-steps.md`](surveys/colleague-review/future-steps.md).

- The guided sequence is: Introduction → three 1–5 familiarity self-reports → completed Humanity's Last Exam (HLE) teaching example → ARC-AGI-2 → DesignQA → combined review and submission → confirmation.
- Leave both participant benchmarks (`ARC-AGI-2` and `DesignQA`) blank. Use Back and Continue navigation with contents restricted to the current stage and inline hover/focus/click definitions. Collect no names or respondent emails.
- One final payload contains the three familiarity ratings, all 50 benchmark answers, **five separately stored required feedback ratings** (question clarity, distinguishing choices, manageable workload, understanding what to look for when reviewing a benchmark, and confidence using MESA, each with `Cannot judge` and no preselection), optional written feedback, and packet identifier/fingerprint metadata.
- Report the five feedback items separately as perceptions, with explicit `Cannot judge` and optional-comment denominators; do not compute a composite usability score or subtract the opening score-interpretation confidence item from the closing MESA-confidence item.
- Never send real survey submissions or test emails without explicit authorization; mock delivery during automated checks.

## Optional Review Reconciliation Role

When explicitly asked to reconcile candidate benchmark reviews or agent-completed survey examples:
- Confirm that candidates share the same benchmark edition, intended interpretation, and source boundary.
- For passage-based survey responses, judge support strictly against the supplied passage without silently adding external facts.
- For supporting full-template RETRAI reviews in `supporting/retrai-paper/`, keep Part A descriptive and Part B evaluative and source-grounded; do not average Part B ratings mechanically or convert EFPA `0`–`4` ratings into 25-question MESA choices.
- Do not reconcile independent model-study responses in `surveys/colleague-review/mesa-study/` into an answer key or call reviewer agreement validation.

## Rules

- Avoid hyphenated terms unless necessary.
- Avoid adjectives unless necessary.
- Avoid marketing-style terms, such as those common in titles.
- Make written text be easy to understand, and flow naturally.
- Do not make mistakes.

## Verification

- Current manuscripts: `python3 verify_manuscripts.py` (MESA and paper two preview).

- Historical questionnaire checks: run the analysis and verification commands in `CHASE-study.md` only in the earlier checkout described by the [consolidation record](provenance/manuscript-consolidation-2026-11-03.md); its verifier requires the removed CHASE manuscript.
- Run `python3 surveys/colleague-review/verify.py` for guided survey checks.
- Run `python3 tools/check-thesis.py` for supporting RETRAI manuscript and scorecard checks.
- **Do not compile LaTeX or open an automatic PDF preview.** Report visual layout and page length as unchecked.
