# Agent Instructions

Use this file as the default repository guide for AI coding and research agents. Read `README.md` and `CHASE-study.md` for the current project and study, then the relevant source files before editing.

## Current project

MESA is the **25-question questionnaire** for reviewing AI benchmarks, adapted from the EFPA Test Review Model 2025. It has six domains and five categorical choices: Yes, Partly, No, Not sure, and Not applicable. Do not convert these choices to EFPA ratings or a total quality score.

Questions 1–5 judge whether descriptive information is documented. Benchmark passages supply the facts; questionnaire answers are judgments about that information. Keep missing information separate from explicit negative findings and distinguish checking that occurred from favorable outcomes.

Detailed adaptation documents and scorecards remain supporting research records. Do not describe them as a separate “full MESA” instrument in the current papers. The comparison instrument is the original complete EFPA Test Review Model, not the older adaptation template.

## Manuscripts and submission targets

Both current manuscripts use the title **MESA: Adapting the EFPA Test Review Model for AI Benchmark Review.**

- **`paper_chase.tex` → CHASE:** reports the questionnaire adaptation and model experiments. Human evaluation is outside this paper's study and belongs only in future work. Do not describe a human study as unfinished work required to complete the CHASE paper.
- **`paper_refsq.tex` → REFSQ:** is planned as the CHASE paper extended with human evaluation. Retain the shared questionnaire, conceptual basis, and model-study contribution, then add the human-study method, observed results, and discussion. Do not treat it as an unrelated human-only paper or assume the existing file already contains the complete extension.
- **`paper.tex`:** preserved original manuscript; do not replace it with either submission manuscript without an explicit request.

When asked to update manuscript content, keep shared definitions and verified model-study facts consistent across the relevant versions while preserving their different evaluation scope. Do not copy human findings into the CHASE paper. Do not invent participants, recruitment details, dates, responses, agreement, comments, or findings for REFSQ; use explicit placeholders until real records are available.

IEEE is the confirmed CHASE manuscript format. Research methods follow relevant ACM SIGSOFT Empirical Standards independently of the typesetting format; see `surveys/colleague-review/simulation-study/analyst/standards-assessment.md`. Do not assume that the CHASE format also determines REFSQ's format.

## Research and writing

- Use simple conference-paper prose. Avoid marketing language and unexplained terms such as “evidence-use” and “task-score-claim alignment.”
- Explain retained, changed, combined, omitted, and added EFPA functions transparently. Proposed correspondences are not evidence of a historical derivation or EFPA endorsement.
- Cite the verified original 90-page EFPA document, including its forms and guidance. Reduced review effort is a design objective, not an observed human benefit.
- Use BetterBench for implementation, documentation, maintenance, and reproducibility concerns; use measurement literature for whether tasks and scores support the intended claims. Consult CHC/AGI literature when broad intelligence interpretations require it.
- Prefer primary sources and verified existing bibliography keys. Add sources only when necessary and verified.
- Do not use previous AI-assisted development, reviewer agreement, reconciliation, or assistant-generated examples as validation evidence for the current questionnaire.
- Disclose the assistant's role in preparing, conducting, and analyzing the current experiments. Separate mechanically checked results from the same assistant's interpretations.
- Repeated model sessions are not independent people or distinct models. Role prompts do not establish human behavior. Reserve claims about human understanding, effort, usefulness, and decision quality for suitable human evidence.
- Do not equate missing documentation with poor underlying quality, agreement with correctness, or a completed form with complete coverage.

## Model-study records

Start with `CHASE-study.md` and `surveys/colleague-review/mesa-study/chase-report/selection.json`. Current reporting and traceability are in `surveys/colleague-review/mesa-study/chase-report/`; consult the frozen batch protocols for execution details.

- `surveys/colleague-review/mesa-study/chase-report/`: current reporting selection, combining ten MESA sessions from `claude-sonnet-5-5-guidance-v2` with twenty EFPA-TRM/general-instruction sessions from `claude-sonnet-5-5`. It contains 30 conversations, 28 usable responses and 32 physical attempts, including two authentication failures. Historical batch analyses and all frozen materials remain preserved; use this selection for current manuscript findings.
- Archived GPT-6.1 Sol series, never pooled with the current study: `mesa-study/main/` (same 30-run design, stopped at a Codex usage limit), `mesa-study/2026-10-17/` (stopped 180-run design), `accessibility-study/v1/`, and `simulation-study/` (first 120-run series and an incomplete Astra series). The paper names only the current study's model; these series are described in the repository records.
- The reviewer model (Claude Sonnet 5.5) and an assistant running Claude Code with Claude Opus 5.5 are from the same model family; disclose this when the assistant analyzes the outputs.
- Original prompts, expected fictional answers, raw responses, and failure logs are research records. Do not rewrite them after observing results. Changed materials require a new version and manifest.
- Preserve incomplete and invalid outputs. A completed invalid response cannot be silently repaired or replaced. Keep retries separately and follow the protocol's handling rules.
- Keep independently generated responses without reconciliation into an answer key. Reviewer sessions must not receive expected answers, other responses, organizer notes, or project history.
- Do not launch more experiments merely to edit or summarize the paper. Use saved records for offline analysis unless new testing is requested.

## Human survey

For survey work, read `surveys/colleague-review/agent-guide.md` and `surveys/colleague-review/packet.json`. The packet is the source for the 25 questions, five choices, definitions, passages, and completed example.

The guided flow is Introduction → three 1–5 familiarity self-reports → completed HLE example → ARC-AGI-2 → DesignQA → combined review/submission → confirmation. Leave both participant benchmarks blank. Use Back and Continue with contents restricted to the current page and inline definitions. Collect no names or respondent emails. Familiarity is self-report, not a knowledge test; comments are optional. One final payload contains familiarity, all 50 answers, three separately stored required feedback ratings, optional written feedback, and packet identifier/fingerprint metadata. The final review page asks about question clarity, distinguishing choices and manageable workload, each with Cannot judge and no preselection. Preserve feedback in drafts, validation and retry signatures; unanswered and Cannot judge remain distinct.

Read [the human-evaluation plan](surveys/colleague-review/future-steps.md) before recruitment or human analysis. Freeze population, recruitment, consent/ethics, sample-size rationale, exclusions and analysis decisions before collection. Report feedback separately, with explicit Cannot judge and optional-comment denominators; do not compute a composite score or call it a validated usability measure. Human comment analysis must document actual analysts and decisions; model answers are not ground truth and disagreement does not establish misunderstanding.

Human research for REFSQ examines the questionnaire together with supplied passages, definitions, and the teaching example. Do not claim measured duration, comprehension, usability, expert correctness, or improvement over other methods unless the collected data support those claims. Account for repeated judgments within participants. Discuss shared passage cues, the worked example, fixed order, convenience sampling, optional comments, and limited benchmark coverage.

Prepare agent-completed examples only when requested and label them separately. Experimental presentation changes belong in a separate static HTML document with no response fields, submission service, saving, email integration, or tracking. Preserve the live participant survey. Never send real submissions or test emails without explicit authorization.

## Source boundaries and preservation

- `Papers/`: original PDF source library.
- `literature/`: source transcriptions; `EFPA_Test_Review_Model_2025_Markdown.md` records EFPA's source structure. The original PDF remains authoritative where extraction loses detail.
- `MESA EFPA template official.md` and `MESA scorecard.md`: supporting adaptation records. The scorecard is generated; do not hand-edit it.
- `reviews/`: supporting benchmark reviews, including HLE, ARC-AGI-2, and DesignQA. Preserve their version boundaries; they are not current questionnaire ground truth.
- `tools/`: utilities; `reports/` and `dist/hf_mesa_dataset/`, if present, are derived outputs rather than source evidence.
- `.codex/agents/`: task profiles; `.codex/memory/`: durable context. Historical instructions must not override the manuscript scope recorded here.

Inspect Git status and preserve unrelated changes. Do not overwrite source papers, templates, reviews, participant records, or notes without authorization. Assign numerical EFPA-style ratings only when explicitly requested for that instrument or a supporting detailed review, with evidence, missing evidence, reasons, and cautions. Do not mechanically average them.

The SWARM subproject was removed at the user's request; do not restore it as part of MESA work.

## Verification

Check question counts and study descriptions against the packet, reported findings against saved outputs, and references against source records. Verify citation keys, LaTeX references, balanced braces/environments, and asset paths. Check Markdown links and any static HTML's reading behavior.

**Do not compile LaTeX or open an automatic PDF preview.** Report layout and page length as unchecked. The paper uses the existing GitHub repository link and `CHASE-study.md` for supporting files; do not reintroduce an anonymized-link requirement unless the user requests it.
