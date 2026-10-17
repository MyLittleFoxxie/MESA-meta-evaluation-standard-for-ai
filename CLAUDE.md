# MESA repository context

Read `AGENTS.md` for current research instructions and source boundaries. `README.md` explains the questionnaire; `CHASE-study.md` links the model-study methods, records, findings, and analysis commands.

## Current contribution and manuscripts

MESA is the 25-question AI benchmark review questionnaire adapted from the EFPA Test Review Model 2025. It uses six domains and five categorical choices, without an aggregate quality score. Keep descriptive benchmark facts separate from review judgments and missing information separate from explicit negative findings.

- **CHASE submission:** `paper_chase.tex`, covering adaptation and model experiments. Human evaluation belongs in future work.
- **REFSQ submission:** `paper_refsq.tex`, planned as the CHASE paper with human evaluation added. Preserve the shared conceptual and model-study contribution, then add the human method and real findings when available.
- **Original manuscript:** `paper.tex`, preserved unless the user explicitly requests changes.

The current papers share the title “MESA: Adapting the EFPA Test Review Model for AI Benchmark Review.” IEEE is confirmed for CHASE. Empirical method standards are separate from submission formatting. Do not assume REFSQ uses the CHASE format.

The current study (`surveys/colleague-review/mesa-study/claude-sonnet-5-5/`, Claude Sonnet 5.5, 30 conversations) compares the questionnaire with the original complete EFPA model and ordinary review. MESA is framed as a more accessible approach to AI benchmark review; easier human use is a design goal, not a measured result. Repeated model runs are not people, and role instructions are not validated human simulations. The assistant's current study involvement must be disclosed; earlier development, reconciliation, and agreement are not validation evidence for the questionnaire.

## Working rules

Use simple academic prose and verified sources. Preserve frozen inputs, raw outputs, failures, benchmark reviews, the live survey, and unrelated edits. Detailed adaptation documents and scorecards remain supporting records, not a separate “full MESA” instrument in the papers. Historical agent and memory files do not override `AGENTS.md`.

For survey tasks, read `surveys/colleague-review/agent-guide.md` and `packet.json`. Keep the 25 questions, five choices, completed HLE teaching example, and blank ARC-AGI-2/DesignQA participant answers. Human evaluation is future work for the CHASE paper and an intended addition for the REFSQ paper; never fabricate its observations.

Do not compile LaTeX or open an automatic PDF preview. Use static checks and report layout/page length as unchecked.
