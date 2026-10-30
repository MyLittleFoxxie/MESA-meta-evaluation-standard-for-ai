# Gemini Repository Guide

Read [`AGENTS.md`](AGENTS.md) first; it is the authoritative repository guide for research scope, manuscript targets, source boundaries, and verification rules. Then read [`README.md`](README.md), [`CHASE-study.md`](CHASE-study.md), and the relevant source files before editing.

## Project Scope and Manuscripts

MESA is the **25-question questionnaire** for reviewing AI benchmarks, adapted from the EFPA Test Review Model 2025. It covers six domains and uses five categorical choices (`Yes`, `Partly`, `No`, `Not sure`, `Not applicable`) with no aggregate quality score. Keep descriptive benchmark facts (Questions 1–5) separate from evaluative judgments, and keep missing documentation (`Not sure`) separate from explicit negative findings (`No`). Distinguish whether a check occurred from whether its findings were favorable.

- **`paper_chase.tex` (CHASE submission, IEEE format):** Reports the questionnaire adaptation and the 30-conversation Claude Sonnet 5.5 study (`surveys/colleague-review/mesa-study/chase-report/`). Human evaluation belongs in future work only.
- **`paper_refsq.tex` (REFSQ submission):** Planned extension of the CHASE paper adding human evaluation. Retain the shared adaptation and model-study contribution and use explicit placeholders until real human records are collected.
- **`paper.tex`:** Preserved RETRAI submission manuscript; do not replace its content without an explicit request.
- **`paper_old.tex`:** Preserved older manuscript; do not replace its content.
- **`references.bib`:** Shared bibliography for all four manuscripts; keep existing citation keys intact.

## Repository Layout and Source Boundaries

- [`literature/README.md`](literature/README.md): Source index and thematic reading guide pairing original PDFs (`literature/pdfs/`), extracted transcriptions (`literature/transcriptions/`), and benchmark documentation notes (`literature/notes/`). Original PDFs remain authoritative where extraction loses detail.
- [`supporting/adaptation/`](supporting/adaptation/): Active EFPA correspondence map ([`adaptation-map.md`](supporting/adaptation/adaptation-map.md)) and ACM SIGSOFT empirical standards assessment ([`standards-assessment.md`](supporting/adaptation/standards-assessment.md)).
- [`supporting/retrai-paper/`](supporting/retrai-paper/): Supporting records for the preserved RETRAI manuscript (`MESA EFPA template official.md`, generated `MESA scorecard.md`, `reviews/`, `thesis/`, and `provenance/`). Do not describe these as a second current MESA instrument in the CHASE or REFSQ papers, and do not hand-edit `MESA scorecard.md`.
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

## Verification

- Run `python3 surveys/colleague-review/mesa-study/chase-report/analyze.py` and `python3 surveys/colleague-review/mesa-study/chase-report/verify.py` for CHASE study and manuscript checks.
- Run `python3 surveys/colleague-review/verify.py` for guided survey checks.
- Run `python3 tools/check-thesis.py` for supporting RETRAI manuscript and scorecard checks.
- **Do not compile LaTeX or open an automatic PDF preview.** Report visual layout and page length as unchecked.
