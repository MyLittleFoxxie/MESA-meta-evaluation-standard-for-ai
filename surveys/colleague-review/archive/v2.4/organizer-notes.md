# Organizer notes — guided MESA survey, version 2.2

## What respondents see

The survey is a sequential form with seven stages: introduction, familiarity questions, a completed HLE example, ARC-AGI-2, DesignQA, review/submission, and confirmation. Each benchmark has a reading passage followed by its 25 questions on the same page. Back and Continue preserve responses; respondents cannot jump to future stages through tabs or the contents menu.

The three familiarity questions are self-reports, not a knowledge test: familiarity with AI, familiarity with AI benchmarks before reading the survey, and current confidence interpreting AI test scores. Each has five explicitly described choices. These ratings provide context; they do not produce a total or alter the questions received.

The same 25 questionnaire items and five response choices are used for both benchmarks. Participant selections begin blank. Comments are optional, and no evidence notes or citations are required. HLE is a worked example with all 25 selected reviewer judgments and short reasons; the corresponding HLE example under each participant question is collapsed by default. These judgments are teaching aids, not a validated answer key.

Definitions appear beside relevant terms as bold, dotted-underlined text with a small circled question mark. Hover, keyboard focus or click/tap opens the explanation; Escape or an outside click closes it. There is no opening glossary. The printable copy includes the same definitions at the end because it cannot provide interactive help.

On wide screens, the contents sidebar lists only headings from the current stage. On smaller screens, a title-adjacent Contents button opens those same links. A compact scrolling toolbar provides the current stage, answer count where relevant and Save draft. Both light and dark themes remain available.

## Source boundaries and provenance

The ARC-AGI-2 and HLE source materials were inspected on 7 October 2026. The DesignQA source review was checked on 6 October 2026. The guided form was prepared on 22 October 2026; no new source inspection is implied by that date.

`packet.json` is the content source, `template.html` is the interface source, and `build.py` generates the standalone `survey.html` and printable `survey.md`. The generated HTML embeds the official ARC and HLE figures and logos. DesignQA has no substituted institutional logo. The original DesignQA completed example remains in `proposals/mesa-25/designqa-example.json` and its companion notes. Earlier circulated survey versions remain in Git history; the version 1.11 packet is also retained under `archive/` for explicit content provenance.

The new HLE example is grounded in the existing supplied passages and source records, with reviewer judgments kept distinct from facts. Expert disagreement is not called a confirmed answer-error rate. A confidence range calculated by code is distinguished from headline leaderboard reporting and from repeated-run variation. Source-based concerns in full reviews are not automatically converted into questionnaire answers; see `hle-example-notes.md` for the example's scope and comparison cautions.

The ARC-AGI-2 passage distinguishes full-task success from the inspected runner's input-averaged score. HLE remains the original 2,500-question benchmark, not HLE-Rolling or HLE-Diamond. DesignQA remains the original 2024 benchmark and inspected public software, rather than all engineering work. Unavailable research is bounded to the inspected sources, not proof that no study exists.

## No identifying questions and one combined submission

The form asks for no name, respondent email, demographic fields or identifying profile information. Respondents are asked to avoid identifying details in optional comments. Do not describe it as guaranteeing technical anonymity: FormSubmit and hosting services may process request information.

At the end, Submit survey sends all three familiarity ratings, all 50 answers and comments, five separate feedback ratings and optional feedback text, the packet identifier and fingerprint, the survey version, a device-derived UTC completion time and a random submission identifier to the configured organizer at vitorraposo2@gmail.com. It sends one combined response, not separate benchmark emails. The identifier supports duplicate recognition; it is not an identifying respondent field. Provider acceptance does not prove delivery to the organizer's inbox.

All familiarity questions and all 25 choices per benchmark are required before advancing. All five feedback ratings are required before submission; Cannot judge is available and distinct from an unanswered field. A failed delivery preserves the answers and supports saving and retrying. Changing any response, including a feedback rating or its optional text, creates a new identifier on the next submission. Retry of the same completed response retains its submission identifier and completion time. The provider does not guarantee idempotency; an unconfirmed delivery may already have reached the service. The user is told to check with the organizer before retrying. A confirmed response reaches a confirmation page with no second submission action.

No new live email is sent during implementation testing. Browser tests intercept FormSubmit requests and inspect the payload. The prior activation remains attached to the hosted survey URL, but service acceptance and actual inbox receipt are separate observations.

## Draft compatibility and checks

Version 2.2 uses `mesa-guided-arc-designqa-v2-2` and a packet fingerprint. Older named ARC/HLE drafts are not loaded or silently reinterpreted. Drafts preserve feedback ratings/text, familiarity responses, benchmark choices/comments, the current stage and submission state. Draft saving uses local browser storage, is not encrypted and can be unavailable. Earlier browser keys are not read or copied into the new format.

After editing, run `python3 surveys/colleague-review/build.py`, `python3 surveys/colleague-review/verify.py`, and the configured Playwright `check-browser.cjs` for interface changes. Check both themes, current-page contents, keyboard focus, definitions, Back/Continue, small screens, enlarged text, draft compatibility and mocked submission failures/retries. These checks establish implementation behavior, not factual completeness or scientific validity.

This remains a packet-based pilot. Teaching examples, wording, emphasis, page order and information compression may influence judgments. Agreement with an existing MESA review does not validate the questionnaire, and simulated readers do not constitute a human study. Do not commit real respondent answers, browser drafts or private email messages to this repository.

## Packet 2.2 and planned human analysis

The author reports that the survey has not yet been circulated. The prior packet and generated survey are preserved in [archive/v2.0/](archive/v2.0/). Question texts, passages, choices, source-inspection dates and blank participant responses are unchanged. All 25 explanations, answer instructions and the HLE example match `study-alignment.txt`, copied from the reported MESA study input. Its origin and fingerprint are recorded in the source manifest. HLE Q8 is Yes: checks occurred; remaining expert disagreement does not undo them.

The final page asks about question understanding, distinguishing answer choices, manageable reading/answering workload, understanding what to look for in a review, and confidence using MESA. Each required rating has six labelled options including Cannot judge, with no default. The optional written prompt asks which question, explanation or example was difficult and why. These are separate self-reports, not a composite score or a validated usability measure. No elapsed-time measurement or new tracking is introduced.

Follow [future-steps.md](future-steps.md) before recruitment and analysis. Report participant-level distributions and agreement with repeated judgments accounted for, familiarity separately, and denominators for Cannot judge and optional comments. Document the actual human analysis of comments. Model outputs are not ground truth. REFSQ extends CHASE with actual human methods/results/discussion while retaining the adaptation and current model study, whose reporting selection is `mesa-study/chase-report/`. Comparative efficiency and team benefits require additional evidence.

The final two feedback items ask about understanding what to look for when reviewing a benchmark, then confidence using MESA. Report both separately as perceptions, not demonstrated ability or correctness. The opening confidence item concerns interpreting AI test scores, while the final item concerns using MESA; do not subtract them or claim a measured improvement. No overall feedback score is calculated.

Packet 2.1 and its generated survey are preserved in `archive/v2.1/`. Version 2.2 drafts have a new identifier and fingerprint; do not migrate or silently reinterpret older drafts. The author confirmed on 22 October 2026 that the survey has not been shared. Source-inspection dates remain unchanged.


## Version 2.3 — 26 October 2026

The current participant survey uses `mesa-guided-arc-designqa-v2-3`. Version 2.2 is preserved in `archive/v2.2/`. Earlier drafts cannot load into 2.3. HLE explanations now name supporting facts from the existing passages; the 25 answer selections, question texts, passages and source inspection dates are unchanged. Nine definitions were added for published, claims, evidence, comparisons, protections, test materials, methods, situations and repeatedly submitting results. Frozen study materials and `study-alignment.txt` retain the original wording; the participant explanations no longer match them word for word.

Back remains visible, and each question links to its passage with a return control. Contents includes questions under domains and marks the current reading position. Images open the viewer when clicked. Selected answers use category colors without producing scores. After service acceptance, readers can revisit their responses but cannot edit or submit again. These presentation changes do not establish easier use.

Run `verify.py`, `check-browser.cjs` and `check-navigation.cjs` after changes. Browser checks intercept requests; they do not send responses or establish inbox delivery.


## Version 2.4 — 26 October 2026

The current survey uses `mesa-guided-arc-designqa-v2-4` and a new packet fingerprint. Version 2.3 is preserved in `archive/v2.3/`; its drafts cannot load into 2.4. HLE Q18 explains that precautions do not reveal whether public questions or answers were used in an AI’s training. Participant text now uses ability and abilities, matching `paper_chase.tex`, including the Ability definition. The passage edits only replace interchangeable terminology; sources, inspection dates, question texts and answer selections are unchanged. Frozen study instructions and manuscript text remain unchanged.
