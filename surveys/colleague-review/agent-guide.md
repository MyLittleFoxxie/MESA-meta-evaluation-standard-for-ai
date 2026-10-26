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

Completed examples use the label **Example**, a selected answer and a brief reason in simple language. The current HLE selections are in `packet.json`, with source and comparison notes in `hle-example-notes.md`. Do not present them as correct answers for ARC-AGI-2 or DesignQA. The HLE example stage has a reading passage before all 25 completed answers; each participant question has a collapsed matching HLE example. Preserve the earlier DesignQA example in `supporting/retrai-paper/provenance/mesa-25/` (relocated from `proposals/mesa-25/`). New examples need their own source-grounded review and explicit scope.

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

The guided survey collects no name or respondent email. It sends three self-reported familiarity ratings, both benchmark evaluations (50 selections), five separate feedback ratings, optional comments, version, device-derived UTC completion time and a random submission identifier in one FormSubmit request. Avoid identifying comments; the external service may process technical request information. Do not promise technical anonymity. Require all three familiarity ratings, both completed benchmarks, and all five feedback ratings before submission. Acceptance by the service is not proof of inbox delivery. Preserve answers on failures, duplicate protection and retry IDs; do not claim guaranteed idempotency or independently verified timestamps.

Do not send test or real responses without explicit authorization. Automated checks must mock delivery. Never commit collected participant responses, browser drafts or private email contents to the public repository.

When publishing is requested, inspect the current Git state and Pages configuration, stage only authorized files, preserve unrelated changes, and use the authorized GitHub account. Confirm the built live page before reporting publication. Do not assume the checkout's current branch is the Pages publishing branch.

## Guided draft compatibility

Version 2.2 uses `mesa-guided-arc-designqa-v2-2` and its own fingerprint. Archive 2.0 is in `archive/v2.0/`, including packet, generated HTML/Markdown, manifest and example notes. Version 2.2 cannot load 2.1 or earlier drafts. Do not load named ARC/HLE drafts into the new anonymous ARC/DesignQA form. Keep the previous circulated packet in `archive/v1.11-packet.json` and earlier HTML in Git history. Familiarity uses three separately labelled 1–5 scales with explanations for every value; do not average them into a knowledge or benchmark-quality score.

## Feedback and future human evaluation

Read [future-steps.md](future-steps.md) for recruitment and analysis decisions and the REFSQ extension. Current model-study reporting uses `mesa-study/chase-report/`, not a historical batch analysis. Human findings are not part of CHASE.

Version 2.2 aligns all explanations, instructions and HLE answers with the reported study materials, copied without edits to `study-alignment.txt`; its origin and SHA256 are in `source-manifest.json`. Preserve question texts, passages and source-inspection dates. The preparation date is 22 October 2026.

On the final review page require five separate ratings: understanding the questions, distinguishing choices, manageable workload, understanding what to look for in a benchmark review, and confidence using MESA, in that order. No answer is preselected; Cannot judge is a selected category distinct from null. Written feedback is optional. Include feedback in draft saving/restoration, validation, retry signatures and the single payload, with packet ID and fingerprint. A changed rating or comment must get a new submission identifier; unchanged retries retain theirs. Do not add names, respondent emails, tracking or elapsed-time measurements.

Report each rating separately, with explicit denominators for Cannot judge and optional comments. They are not a validated usability measure and must not be combined into a score. Account for repeated judgments within participants; document actual human coding of comments. Do not use model answers as ground truth or disagreement as proof of misunderstanding.

The final two feedback items ask about understanding what to look for when reviewing a benchmark, then confidence using MESA. Report both separately as perceptions, not demonstrated ability or correctness. The opening confidence item concerns interpreting AI test scores, while the final item concerns using MESA; do not subtract them or claim a measured improvement. No overall feedback score is calculated.

Packet 2.1 and its generated survey are preserved in `archive/v2.1/`. Version 2.2 drafts have a new identifier and fingerprint; do not migrate or silently reinterpret older drafts. The author confirmed on 22 October 2026 that the survey has not been shared. Source-inspection dates remain unchanged.


## Version 2.3 — 26 October 2026

The current participant survey uses `mesa-guided-arc-designqa-v2-3`. Version 2.2 is preserved in `archive/v2.2/`. Earlier drafts cannot load into 2.3. HLE explanations now name supporting facts from the existing passages; the 25 answer selections, question texts, passages and source inspection dates are unchanged. Nine definitions were added for published, claims, evidence, comparisons, protections, test materials, methods, situations and repeatedly submitting results. Frozen study materials and `study-alignment.txt` retain the original wording; the participant explanations no longer match them word for word.

Back remains visible, and each question links to its passage with a return control. Contents includes questions under domains and marks the current reading position. Images open the viewer when clicked. Selected answers use category colors without producing scores. After service acceptance, readers can revisit their responses but cannot edit or submit again. These presentation changes do not establish easier use.

Run `verify.py`, `check-browser.cjs` and `check-navigation.cjs` after changes. Browser checks intercept requests; they do not send responses or establish inbox delivery.


## Version 2.4 — 26 October 2026

The current survey uses `mesa-guided-arc-designqa-v2-4` and a new packet fingerprint. Version 2.3 is preserved in `archive/v2.3/`; its drafts cannot load into 2.4. HLE Q18 explains that precautions do not reveal whether public questions or answers were used in an AI’s training. Participant text now uses ability and abilities, matching `paper_chase.tex`, including the Ability definition. The passage edits only replace interchangeable terminology; sources, inspection dates, question texts and answer selections are unchanged. Frozen study instructions and manuscript text remain unchanged.


## Version 2.5 — 26 October 2026

The current survey uses `mesa-guided-arc-designqa-v2-5`, with a new fingerprint. Version 2.4 is archived and its drafts cannot load into 2.5. Nine definitions explain familiarity ratings, answers, feedback, optional comments, survey identifier, fingerprint, completion time, organizer and FormSubmit. The survey answers and feedback definitions apply only inside submission explanations, so benchmark answers and feedback keep their meaning. Other participant content and submission fields are unchanged.


## Version 2.6 — 26 October 2026

The current survey uses `mesa-guided-arc-designqa-v2-6`; version 2.5 is archived and earlier drafts are rejected. Current flow: introduction, familiarity, HLE example, ARC-AGI-2, ARC feedback/review, ARC confirmation, optional DesignQA, DesignQA feedback/review, DesignQA confirmation. A reader can finish after ARC. This supersedes earlier instructions requiring both benchmarks and one combined payload.

Each submission contains one benchmark’s 25 answers, comments, five separately stored feedback ratings, feedback comment, shared familiarity ratings, packet metadata, random session ID, submission ID and device timestamp. Feedback concerns that benchmark review. Accepted responses and familiarity are locked; other work remains editable. Drafts retain separate submission states, signatures and retry IDs; unchanged retries retain their ID and time. Neither saving nor loading sends responses. A session ID links the two reviews without claiming a verified person identity.

Definitions and introductions describe the task and benchmark versions; new definition provenance is in `definition-sources.json`. Original passage inspection dates are unchanged. Popup colors differ from the page in both themes. Questionnaire texts, HLE judgments and frozen study materials remain unchanged. These changes do not establish easier use.

Run `verify.py`, `check-browser.cjs` and `check-navigation.cjs`. Automated deliveries must be mocked. The author authorized two live TEST submissions for this release; label their subjects and payloads TEST — exclude from research and keep fabricated responses out of research analysis. That authorization is not permission for future live tests.


## Version 2.7 — 26 October 2026

Version 2.6 is archived; its drafts do not load into 2.7. Guide choices use the answer colors. Definitions appear on the first and every third subsequent occurrence of each concept on a page, with counts reset when the review is rebuilt. Checking and limit definitions are added; score definitions are enabled again. Contents follows the center of the reading area between the fixed controls. Passage buttons say Return to Passage. Validation, storage and delivery errors use a dialog; closing it focuses the relevant control. Question texts, HLE judgments and submission payloads are unchanged. No further live test submissions are authorized by this revision.


## Version 2.8 — 26 October 2026

Current survey text uses data contamination in place of exposure, matching the CHASE manuscript. The definition explains that test questions, answers or related material can enter training or development before evaluation. Risk is not treated as proof of contamination. Version 2.7 is archived and its drafts cannot load into 2.8. Question texts, choices, HLE judgments and source records remain unchanged. Historical notes and frozen study materials retain their wording.


## Version 2.9 — 26 October 2026

Current survey uses `mesa-guided-arc-designqa-v2-9` and a new packet fingerprint. Version 2.8 is archived in `archive/v2.8/`; older drafts cannot load into 2.9. Reading passages for HLE, ARC-AGI-2, and DesignQA are re-read and refined for natural, easy-to-understand reading, strict impartiality, and complete adherence to official primary sources with sufficient facts for all 25 questions. Each benchmark incorporates official primary-source data tables. Awkward hyphenated compound terms are replaced with common everyday terminology. Questions 11, 12, and 14 are refined for natural clarity and synchronized with `paper_chase.tex` Table II. The interface removes the standalone Sources and links button while keeping in-text citations functional to open references. Save draft and Load saved draft controls are kept grouped together side by side, and the theme toggle is displayed as an accessible sun/moon icon toggle button positioned on the opposite side of the toolbar controls. Categorical choices, blank participant reviews, and separate feedback remain preserved.


