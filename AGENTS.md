# Agent Instructions

Use this file as the default repository guide for AI coding and research agents. Read `README.md` and `v4/README.md` for the current project and study, then the relevant source files before editing.

## Current project

The current MESA manuscript is [`mesa_paper.tex`](mesa_paper.tex), **Unifying Benchmark Evaluation Protocols: A Meta-Evaluation Standard for Artificial Intelligence in Requirements Engineering**, intended for REFSQ in Springer LNCS format. It reports the framework comparison and rubric study and proposes a requirements traceability application. Human validation and effects on requirements decisions remain unestablished.

The frozen v4 mapping allocates 280 framework items to 30 comparison concerns. Its derived rubric has eight description fields and 29 evaluation questions. Rubric v5 ([`v5/rubric/rubric.md`](v5/rubric/rubric.md)) keeps that mapping, adopts the paper's level names, adds outcome, scope, check kind, detection limits and task defects to each rating, and splits B14 and B28, giving 31 evaluation questions; see [`v5/README.md`](v5/README.md). The current rubric text is [`v5/rubric/rubric-v5.1.md`](v5/rubric/rubric-v5.1.md), which settles feedback item 15 without changing any question; `rubric.md` stays frozen for Study 3. `mesa_paper.tex` presents v5 as its only rubric, with no version names, and reports the v5 sessions (`v5/study/`) as its Study 2; the v4 rubric sessions are not in the paper. These are distinct from the earlier 25 question questionnaire with six domains, five choices, and no total quality score. See [`v4/README.md`](v4/README.md) and [`v4/study/README.md`](v4/study/README.md).

Preserve [`paper.tex`](paper.tex), [`paper_old.tex`](paper_old.tex), [`paper_mesa_v3.tex`](paper_mesa_v3.tex), and [`paper2_preview.tex`](paper2_preview.tex). The removed CHASE manuscripts and MESA v4 manuscript remain retrievable through the [consolidation record](provenance/manuscript-consolidation-2026-11-03.md). Do not restore them as active submission targets.

Paper 2 ([`paper2.tex`](paper2.tex)) and its protocol 5 evaluation: read [`paper2_runbook.md`](paper2_runbook.md) first, and update it in the same change whenever the procedure, code, records, or state change.

Feedback for the MESA paper from implementing it in Paper 2 is in [`mesa_paper_feedback_from_paper_2.md`](mesa_paper_feedback_from_paper_2.md); read it before revising `mesa_paper.tex`.

For the earlier questionnaire, Questions 1–5 judge whether descriptive information is documented. Keep missing information separate from negative findings, and distinguish a check from its outcome. The five choices are Yes, Partly, No, Not sure, and Not applicable. Do not convert questionnaire choices into EFPA ratings. Supporting adaptation records are not a separate current instrument. The earlier questionnaire comparison used the complete EFPA Test Review Model, not the adaptation template.

## Manuscripts and submission targets

Use `mesa_paper.tex` for the MESA REFSQ manuscript and `verify_manuscripts.py` for manuscript checks. Preserve the manuscript content during path refactors. Do not invent participants, recruitment, responses, agreement, or findings. Research methods follow relevant ACM SIGSOFT Empirical Standards independently of typesetting format.

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

Start with `v4/README.md`, `v4/study/README.md`, and the frozen v4 protocol for the current paper. Study 1 has 18 framework sessions. The v4 study also has eight rubric sessions, which the paper does not report; the paper's Study 2 is the eight v5 sessions in `v5/study/`. Two amendment sessions and seven pilots are recorded separately. Preserve all v4 paths and records. The source checker and disagreement coder are assistants, not independent human validators.

The following records belong to the earlier questionnaire study described in `CHASE-study.md`, not the v4 comparison:

- `surveys/colleague-review/mesa-study/chase-report/`: historical questionnaire reporting selection, combining ten MESA sessions from `claude-sonnet-5-5-guidance-v2` with twenty EFPA-TRM/general-instruction sessions from `claude-sonnet-5-5`. It contains 30 conversations, 28 usable responses and 32 physical attempts, including two authentication failures. Historical batch analyses and all frozen materials remain preserved; use this selection only for findings about that questionnaire study.
- Archived GPT-6.1 Sol series, never pooled with the current study: `mesa-study/main/` (same 30-run design, stopped at a Codex usage limit), `mesa-study/2026-10-17/` (stopped 180-run design), `accessibility-study/v1/`, and `simulation-study/` (first 120-run series and an incomplete Astra series). The paper names only the current study's model; these historical series are preserved in the `pre-reorganization-2026-10-22` Git snapshot and indexed in [provenance/archive-index.md](provenance/archive-index.md).
- The reviewer model (Claude Sonnet 5.5) and an assistant running Claude Code with Claude Opus 5.5 are from the same model family; disclose this when the assistant analyzes the outputs.
- Original prompts, expected fictional answers, raw responses, and failure logs are research records. Do not rewrite them after observing results. Changed materials require a new version and manifest.
- Preserve incomplete and invalid outputs. A completed invalid response cannot be silently repaired or replaced. Keep retries separately and follow the protocol's handling rules.
- Keep independently generated responses without reconciliation into an answer key. Reviewer sessions must not receive expected answers, other responses, organizer notes, or project history.
- Do not launch more experiments merely to edit or summarize the paper. Use saved records for offline analysis unless new testing is requested.

## Human survey

For survey work, read `surveys/colleague-review/agent-guide.md` and `surveys/colleague-review/packet.json`. The packet is the source for the 25 questions, five choices, definitions, passages, and completed example.

The guided flow is Introduction → three 1–5 familiarity self-reports → completed HLE example → ARC-AGI-2 → DesignQA → combined review/submission → confirmation. Leave both participant benchmarks blank. Use Back and Continue with contents restricted to the current page and inline definitions. Collect no names or respondent emails. Familiarity is self-report, not a knowledge test; comments are optional. One final payload contains familiarity, all 50 answers, five separately stored required feedback ratings, optional written feedback, and packet identifier/fingerprint metadata. The final review page asks about question clarity, distinguishing choices, manageable workload, understanding what to look for, and confidence using MESA, each with Cannot judge and no preselection. Preserve feedback in drafts, validation and retry signatures; unanswered and Cannot judge remain distinct.

Read [the human-evaluation plan](surveys/colleague-review/future-steps.md) before recruitment or human analysis. Freeze population, recruitment, consent/ethics, sample-size rationale, exclusions and analysis decisions before collection. Report feedback separately, with explicit Cannot judge and optional-comment denominators; do not compute a composite score or call it a validated usability measure. Human comment analysis must document actual analysts and decisions; model answers are not ground truth and disagreement does not establish misunderstanding.

The earlier questionnaire human research plan examines the questionnaire together with supplied passages, definitions, and the teaching example. Do not claim measured duration, comprehension, usability, expert correctness, or improvement over other methods unless the collected data support those claims. Account for repeated judgments within participants. Discuss shared passage cues, the worked example, fixed order, convenience sampling, optional comments, and limited benchmark coverage.

Prepare agent-completed examples only when requested and label them separately. Experimental presentation changes belong in a separate static HTML document with no response fields, submission service, saving, email integration, or tracking. Preserve the live participant survey. Never send real submissions or test emails without explicit authorization.

The final two feedback items ask about understanding what to look for when reviewing a benchmark, then confidence using MESA. Report both separately as perceptions, not demonstrated ability or correctness. The opening confidence item concerns interpreting AI test scores, while the final item concerns using MESA; do not subtract them or claim a measured improvement. No overall feedback score is calculated.

## Source boundaries and preservation

- `literature/`: [source index and thematic reading guide](literature/README.md), original PDFs (`literature/pdfs/`), extracted transcriptions (`literature/transcriptions/`, including `EFPA_Test_Review_Model_2025_Markdown.md`), and source inventories (`literature/notes/`). The original PDF remains authoritative where extraction loses detail.
- `supporting/adaptation/`: current EFPA correspondence map (`adaptation-map.md`) and ACM SIGSOFT empirical standards assessment (`standards-assessment.md`).
- `supporting/retrai-paper/`: supporting adaptation records substantiating `paper.tex` (`MESA EFPA template official.md`, generated `MESA scorecard.md`, `reviews/`, `thesis/`, and `provenance/`). The scorecard is generated; do not hand-edit it. Supporting reviews preserve their version boundaries and are not current questionnaire ground truth.
- `supporting/editorial/`: `CHASE-review-response.md`.
- `tools/`: scorecard and thesis verification utilities (`build-scorecard.py`, `check-thesis.py`, `scorecard-manifest.md`).
- `provenance/`: [archive-index.md](provenance/archive-index.md), [relocation-map.json](provenance/relocation-map.json), and [reorganization-plan.md](provenance/reorganization-plan.md) mapping relocated paths and documenting retrieval from the `pre-reorganization-2026-10-22` Git snapshot. Historical instructions in the archive must not override the manuscript scope recorded here.

Inspect Git status and preserve unrelated changes. Do not overwrite source papers, templates, reviews, participant records, or notes without authorization. Assign numerical EFPA-style ratings only when explicitly requested for that instrument or a supporting detailed review, with evidence, missing evidence, reasons, and cautions. Do not mechanically average them.

The SWARM subproject was removed at the user's request; do not restore it as part of MESA work.

## Rules

- Avoid hyphenated terms unless necessary.
- Avoid adjectives unless necessary.
- Avoid marketing-style terms, such as those common in titles.
- Make written text be easy to understand, and flow naturally.
- Do not make mistakes.

## Verification

Check question counts and study descriptions against the packet, reported findings against saved outputs, and references against source records. Verify citation keys, LaTeX references, balanced braces/environments, and asset paths. Check Markdown links and any static HTML's reading behavior.

**LaTeX compilation is supported locally.** The repository includes `llncs.cls` (v2.25) and `splncs04.bst` in the workspace root. Compile manuscripts using Tectonic (`/Applications/ChatGPT.app/Contents/Resources/tectonic/tectonic <file>.tex` or system `tectonic`) or BasicTeX (`/Library/TeX/texbin/pdflatex`). Verify page counts via `mdls -name kMDItemNumberOfPages <file>.pdf` or `pypdf` (both `mesa_paper.pdf` and `paper2.pdf` are verified to fit strictly within $\le 15$ pages including references for REFSQ). Do not launch automatic GUI PDF previews. The paper uses the existing GitHub repository link; `v4/README.md` indexes its study, while `CHASE-study.md` describes the earlier questionnaire study; do not reintroduce an anonymized-link requirement unless the user requests it.
