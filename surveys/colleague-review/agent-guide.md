# MESA survey guidance for agents

## Choose the requested output

MESA is the 25-question questionnaire. Detailed adaptation templates and scorecards are supporting research records, not a separate full MESA instrument. For survey work use this guide and `packet.json`.

Distinguish two survey tasks:

- **Colleague survey:** prepare clear reading material and leave participant selections and comments blank. The current guided packet concerns ARC-AGI-2 and DesignQA, with a completed original-HLE example.
- **Agent-completed survey:** when explicitly requested, select responses and give brief reasons in a separate, labelled reviewer output. Specify whether judgments use only the supplied passage or independently inspected benchmark sources. Do not insert agent answers into the participant form.

A request to prepare a survey does not authorize filling it in, sending responses, or replacing a supporting detailed review. The three existing benchmarks are examples, not restrictions on future review targets.

## Question and response structure

Use the exact 25 questions, IDs, domain order and choices from `packet.json`. Questions 1–5 judge whether descriptive information is documented; benchmark passages supply the facts. The six domains are Description, Purpose and development, Scoring and comparisons, Consistency of results, Meaning and fairness, and Use and reporting.

The choices are **Yes**, **Partly**, **No**, **Not sure**, and **Not applicable**:

- Yes: the information supports the whole condition.
- Partly: it supports some parts but not all.
- No: the information shows that the condition is not met.
- Not sure: information is missing, unclear or insufficient to decide.
- Not applicable: the issue does not apply to this benchmark or intended use.

For checking/testing questions, Yes means every named check occurred, regardless of unfavorable findings; Partly means only some checks or parts are supported. Record limits in optional comments without lowering an answer solely because checking found errors or disagreement. Do not convert absent documentation into No. Unanswered remains `null`, distinct from every selected response. Comments are optional; participants are not required to provide evidence, citations or reasons.

Do not convert these choices to EFPA `0`–`4` ratings, calculate a total quality score, or claim that the survey is a validated scale. When comparing a completed survey with a supporting detailed review, compare the underlying conclusions, evidence gaps and interpretation limits. Report differences; agreement alone does not validate the survey or establish a correct answer key.

## Prepare reading passages and examples

Read the benchmark's primary sources and relevant existing reviews before writing. Keep factual statements, author claims and reviewer inferences distinguishable. Identify the benchmark edition, test materials, scoring method, intended interpretation and source inspection date. Preserve uncertainty and bound missing information to the sources inspected.

Use plain, connected sentences. Explain unfamiliar terms before using them. Put benchmark facts in a continuous reading passage before the questions, with meaningful headings, selective bold emphasis and source links in the bibliography. The passage must supply the information needed for the judgments without requiring readers to open sources. Keep question help declarative and labelled **Meaning**; it must not be another question or an instruction to search for evidence.

Use the same overview structure for DesignQA and other benchmarks:

1. A short explanation of what the AI receives and must do, followed by reassurance that participants do not need to solve the benchmark problems.
2. **Which test this survey covers** — edition, materials, scoring implementation and inspection date.
3. **How to interpret its scores** — the intended comparison or claim being considered.

Completed examples use the label **Example**, a selected answer and a brief reason in simple language. The current HLE selections are in `packet.json`, with source and comparison notes in `hle-example-notes.md`. Do not present them as correct answers for ARC-AGI-2 or DesignQA. The HLE example stage has a reading passage before all 25 completed answers; each participant question has a collapsed matching HLE example. Preserve the earlier DesignQA example in `proposals/mesa-25/`. New examples need their own source-grounded review and explicit scope.

Use official figures and logos only with attribution and accurate labels. Do not invent a benchmark logo or substitute institutional logos. Avoid redundant diagrams when a figure already explains the task. Keep commit hashes in organizer provenance records rather than visible prose.

## Content, interface and maintenance

- `packet.json` is the participant content source: questions, choices, passages, examples, source references and submission configuration.
- `template.html` is the interface source.
- `survey.html` and `survey.md` are generated by `build.py`; do not hand-edit them.
- `source-manifest.json` records packet and source fingerprints. Recompute its `packet_sha256` after changing packet content; do not rewrite source fingerprints to hide a mismatch.
- `organizer-notes.md` documents scope, limitations and delivery behavior.

Keep the full paper title and MESA introduction. The flow is intro → three familiarity questions → HLE example → ARC-AGI-2 → DesignQA → review/submit → confirmation. Use Back/Continue, not benchmark tabs; validate the familiarity ratings and all 25 choices per benchmark before advancing. Contents links only to the current stage. On wide screens (at least 80rem), Contents appears as a sticky sidebar. On smaller screens, it belongs beside the title, opens a hidden overlay without shifting the centered survey, and remains accessible through the compact scroll toolbar. Preserve the light/dark preference, responsive layout, visible keyboard focus, dialog close/Escape behavior and focus restoration. Keep progress and Save draft near the questions and in the scroll toolbar; one combined email submission occurs on the final review page. Definitions belong beside relevant terms and work on hover, focus and click/tap, with Escape/outside-click dismissal; do not restore an opening glossary. Do not restore file importing or response download controls.

After edits, run `python3 surveys/colleague-review/build.py` and `python3 surveys/colleague-review/verify.py`. For interface or submission changes, run `check-browser.cjs` with Playwright and Chrome paths configured as needed. Inspect desktop/mobile layouts in both themes and verify keyboard behavior and enlarged text. Structural and browser checks cannot establish factual accuracy, scientific validity or actual email delivery.

For material changes to circulated facts, questions or instructions, version the packet and retain the circulated snapshot. Drafts are checked against the packet ID and fingerprint; account for compatibility rather than silently loading responses from a different packet. Keep provenance dates truthful; a layout edit does not imply sources were re-inspected.

## Submission and publishing

The guided survey collects no name or respondent email. It sends three self-reported familiarity ratings, both benchmark evaluations (50 selections), optional comments, version, device-derived UTC completion time and a random submission identifier in one FormSubmit request. Avoid identifying comments; the external service may process technical request information. Do not promise technical anonymity. Require all three familiarity ratings and both completed benchmarks before submission. Acceptance by the service is not proof of inbox delivery. Preserve answers on failures, duplicate protection and retry IDs; do not claim guaranteed idempotency or independently verified timestamps.

Do not send test or real responses without explicit authorization. Automated checks must mock delivery. Never commit collected participant responses, browser drafts or private email contents to the public repository.

When publishing is requested, inspect the current Git state and Pages configuration, stage only authorized files, preserve unrelated changes, and use the authorized GitHub account. Confirm the built live page before reporting publication. Do not assume the checkout's current branch is the Pages publishing branch.

## Guided draft compatibility

Version 2.1 uses `mesa-guided-arc-designqa-v2-1` and its own fingerprint. Archive 2.0 is in `archive/v2.0/`, including packet, generated HTML/Markdown, manifest and example notes. It is not compatible with 2.1 drafts. Do not load named ARC/HLE drafts into the new anonymous ARC/DesignQA form. Keep the previous circulated packet in `archive/v1.11-packet.json` and earlier HTML in Git history. Familiarity uses three separately labelled 1–5 scales with explanations for every value; do not average them into a knowledge or benchmark-quality score.

## Feedback and future human evaluation

Read [future-steps.md](future-steps.md) for recruitment and analysis decisions and the REFSQ extension. Current model-study reporting uses `mesa-study/chase-report/`, not a historical batch analysis. Human findings are not part of CHASE.

Version 2.1 aligns all explanations, instructions and HLE answers with the reported study materials, copied without edits to `study-alignment.txt`; its origin and SHA256 are in `source-manifest.json`. Preserve question texts, passages and source-inspection dates. The preparation date is 18 October 2026.

On the final review page require three separate ratings of understanding the questions, distinguishing choices, and manageable workload. No answer is preselected; Cannot judge is a selected category distinct from null. Written feedback is optional. Include feedback in draft saving/restoration, validation, retry signatures and the single payload, with packet ID and fingerprint. A changed rating or comment must get a new submission identifier; unchanged retries retain theirs. Do not add names, respondent emails, tracking or elapsed-time measurements.

Report each rating separately, with explicit denominators for Cannot judge and optional comments. They are not a validated usability measure and must not be combined into a score. Account for repeated judgments within participants; document actual human coding of comments. Do not use model answers as ground truth or disagreement as proof of misunderstanding.
