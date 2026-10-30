# MESA Repository Context for Claude

Read [`AGENTS.md`](AGENTS.md) for current research instructions and source boundaries. [`README.md`](README.md) explains the questionnaire and repository layout; [`CHASE-study.md`](CHASE-study.md) links the model-study methods, records, findings, and offline analysis commands.

## Current Contribution and Manuscripts

MESA is the **25-question AI benchmark review questionnaire** adapted from the EFPA Test Review Model 2025. It uses six domains and five categorical choices (`Yes`, `Partly`, `No`, `Not sure`, `Not applicable`), without an aggregate quality score. Keep descriptive benchmark facts (Questions 1–5) separate from review judgments, missing information separate from explicit negative findings, and evidence that a check occurred separate from whether its findings were favorable.

- **CHASE submission:** [`paper_chase.tex`](paper_chase.tex), covering the questionnaire adaptation and model experiments. Human evaluation belongs in future work.
- **REFSQ submission:** [`paper_refsq.tex`](paper_refsq.tex), planned as the CHASE paper with human evaluation added. Preserve the shared conceptual and model-study contribution, then add the human method and real findings when available (using explicit placeholders until then).
- **RETRAI submission manuscript:** [`paper.tex`](paper.tex), preserved unless the user explicitly requests changes.
- **Older manuscript:** [`paper_old.tex`](paper_old.tex), preserved unless the user explicitly requests changes.

The current CHASE and REFSQ papers share the title “MESA: Adapting the EFPA Test Review Model for AI Benchmark Review.” IEEE is confirmed for CHASE; empirical method standards ([`supporting/adaptation/standards-assessment.md`](supporting/adaptation/standards-assessment.md)) are separate from submission formatting. Do not assume REFSQ uses the CHASE format.

The current reporting selection ([`surveys/colleague-review/mesa-study/chase-report/`](surveys/colleague-review/mesa-study/chase-report/), Claude Sonnet 5.5, 30 conversations: 10 MESA from `claude-sonnet-5-5-guidance-v2` and 20 EFPA-TRM/general-instruction from `claude-sonnet-5-5`, with 28 usable responses and 32 physical attempts) compares the questionnaire package with the original complete 90-page EFPA model and general review instructions. Easier human use is a design goal, not a measured result. Repeated model runs are not people, and role prompts are not validated human simulations. Disclose that Claude Opus 5.5 (same model family as reviewer Claude Sonnet 5.5) and OpenAI Codex assisted with the batches and analysis. Earlier development, reconciliation, and agreement are not validation evidence for the questionnaire.

## Repository Structure and Working Rules

- [`literature/README.md`](literature/README.md): Source index and thematic reading guide covering `literature/pdfs/`, `literature/transcriptions/`, and `literature/notes/`.
- [`supporting/adaptation/`](supporting/adaptation/): [`adaptation-map.md`](supporting/adaptation/adaptation-map.md) and [`standards-assessment.md`](supporting/adaptation/standards-assessment.md).
- [`supporting/retrai-paper/`](supporting/retrai-paper/): Detailed adaptation documents (`MESA EFPA template official.md`, generated `MESA scorecard.md`), pilot `reviews/`, `thesis/` records, and `provenance/` files supporting `paper.tex`. Do not describe them as a separate “full MESA” instrument in the current papers.
- [`supporting/editorial/`](supporting/editorial/): [`CHASE-review-response.md`](supporting/editorial/CHASE-review-response.md).
- [`provenance/`](provenance/): [`archive-index.md`](provenance/archive-index.md) and [`relocation-map.json`](provenance/relocation-map.json) documenting relocated files and retrieval of archived historical studies from the `pre-reorganization-2026-10-22` Git snapshot.

Use simple academic prose and verified sources in [`references.bib`](references.bib). Preserve frozen inputs, raw outputs, failures, benchmark reviews, the live survey, and unrelated edits.

For survey tasks, read [`surveys/colleague-review/agent-guide.md`](surveys/colleague-review/agent-guide.md), [`surveys/colleague-review/packet.json`](surveys/colleague-review/packet.json), and [`surveys/colleague-review/future-steps.md`](surveys/colleague-review/future-steps.md). Keep the 25 questions, five choices, three familiarity self-reports, completed HLE teaching example, blank ARC-AGI-2 and DesignQA participant answers, and five required closing feedback ratings (each with `Cannot judge` and no composite score). Never fabricate human observations or send real survey submissions/emails without authorization.

## Verification

- CHASE study & manuscript: `python3 surveys/colleague-review/mesa-study/chase-report/analyze.py` and `python3 surveys/colleague-review/mesa-study/chase-report/verify.py`
- Guided survey: `python3 surveys/colleague-review/verify.py`
- Supporting RETRAI bundle: `python3 tools/check-thesis.py`
- **Do not compile LaTeX or open an automatic PDF preview.** Use static checks and report layout and page length as unchecked.
