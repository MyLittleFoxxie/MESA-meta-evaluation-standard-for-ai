# Protocol draft

Status: preparation, 29 October 2026. **Not registered, frozen or executed.** The [revamp plan](../../../../supporting/editorial/CHASE-v2-plan.md) states the intended comparisons. This document makes the execution requirements inspectable; it must not be used to imply that preparation or author checking has finished.

## Questions and comparisons

- Study 1: do the added question explanations and definitions change reference matches and unsupported answers? Compare A with B separately on fictional cases and real benchmark summaries.
- Study 2: do original passages and the survey summary lead to different answers or reasons? Compare B with C on real benchmarks. Assess each response against its own reading material, not against facts withheld from that condition.
- Study 3: the existing human survey remains separate and will report perceptions and difficulties in the later paper. No second survey is planned.

The common HLE example and answer rules stay the same. Do not describe A as entirely without guidance. The explanation contrast concerns the added explanations in the presence of the common example.

## Units and allocation

Two named models: `gpt-6-luna` and `gpt-6.1-terra`, low reasoning effort, using the access available through this session. This is the chosen plan, not evidence that either model has been invoked. Recheck before freezing; document substitutions before responses. No separately billed API setup is proposed.

Three repeats per model and eligible condition. Fictional sessions answer 24 cases; real sessions answer all 50 question–benchmark pairs. The total is 30 sessions. Account for answers nested within a session, repeated question content and related fictional cases. Report models and task types separately. Do not pool all answers into an apparently large independent sample.

Before execution, generate and save a schedule that interleaves conditions and records benchmark and case order. Hold order fixed across matched conditions for a repeat, vary it between repeats, and disclose imbalance with three repeats. A draft schedule is saved in `preparation/schedule.json`. There is no randomisation claim in this draft.

## Sources and reference records

The packet snapshot is 2.9. Reference construction must use the sources and versions tied to the reading material, not current web pages silently substituted for older sources. Record passages, page/section/code locators and checking dates. A snapshot of the participant packet is not verification of all statements it contains.

Fictional references are proposed choices with reasons and pending author review. All 50 summary references have proposed answers; 30 are flagged as contested. Original-passage references remain unset. No proposed answer has author approval. Before freeze, assign each item assessable, contested or unresolved. Document admissible alternatives before outputs. Main label-match counts include only assessable items with complete references; show the number omitted from that count and all disputed cases separately. An item is not discarded merely because answers differ from the key.

Reference checks require an actual named checker and record of decisions. Do not describe assistant preparation followed by assistant rereading as independent validation. The author may approve the source interpretation or retain a disagreement. Retain each version and do not silently edit frozen keys.

## Reviewer isolation and input assembly

The drafting conversation includes research interpretations and proposed answers. Reviewer sessions must start without that history and must not receive keys, analyst files, other responses or organiser instructions. `fork_turns="none"` prevents inherited chat history but is not proof that shared workspace access is removed. Establish and record actual environment restrictions before execution. Do not rely solely on a prompt asking a tool-enabled reviewer not to look at the keys.

Assemble each input from an explicit allowlist of reviewer materials. The packet includes HLE answers as teaching material; those are intentional. Real and fictional reference files are analyst-only and must never be included. The analysis metadata and status labels in draft files are not automatically participant prompts. Output material hashes and an inspection report before freezing.

Preserve text, tables and relevant visual context. If the model input omits survey images or changes the reading presentation, document the change and assess its relevance before freeze. Do not claim equality with the human condition merely because paragraph wording matches.

## Responses and failures

Responses use the [schema](preparation/response-schema.json). In addition to schema checks, require exactly the requested unique IDs and no others. Validate 24 fictional or 50 real answers according to the session's task. Passage identifiers must resolve in that session's input. A quotation can be null when the reason identifies missing information. A located quotation does not by itself demonstrate a supported interpretation.

Proposed failure rule for author review: permit one retry only for a documented infrastructure failure before any model output. Retain both physical attempts. Preserve completed invalid or partial output without repair, replacement or a request to improve it; report it outside the main complete-response analysis. Any partial-response sensitivity analysis must be specified before execution. Record timeouts, authentication failures and unexpected tool access separately from review errors.

## Analysis

Report attempted, completed, usable and excluded sessions by model/condition/task, with failure reasons. Keep the planned-session count distinct from physical attempts.

For Study 1, report matches to the checked reference choices among assessable items, a five-choice confusion table and the range across sessions. Separate fictional cases from real benchmarks and provide breakdowns for the six fictional distinctions. Report examples where the choice matches but the reason goes beyond the passage. Human/assistant reading of reasons is a separate coding activity, with analyst identity and decisions recorded.

For Study 2, compare distributions of choices for each benchmark question across B and C. Distinguish references that change because the information changed from model answers that exceed either packet. An illustrative transition table may match repeats by schedule; it must not imply that a single human reviewer changed their mind. Compare reasons and trace changes to specific source and summary passages.

Do not calculate a total benchmark quality score, use agreement as correctness, or interpret repeated model outputs as human approachability evidence. This exploratory design does not specify population significance tests. Any additional analysis must be marked as an amendment or as exploratory after execution.

## Freeze requirements

Reference checking, original excerpts, visual/text projection, selection rules, coding rules, schedule, exact prompts, settings, tool controls, schema, failure policy and planned denominators must be settled and hashed. Record actual author review before freezing. Preparation hashes alone are not a freeze. The current state fails these requirements by design and must not be launched as a completed protocol.
