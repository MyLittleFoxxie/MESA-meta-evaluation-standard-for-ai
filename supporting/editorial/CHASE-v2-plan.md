# Plan for paper_chase_v2.tex

> Historical record. Manuscript targets and commands below describe earlier work. See the [3 November 2026 consolidation record](../../provenance/manuscript-consolidation-2026-11-03.md) for Git retrieval and the current entry point.

Status: proposed implementation plan, 28 October 2026. This plan does not create the manuscript or launch experiments. New study results do not yet exist. The existing participant survey is Study 3; no second survey is required.

## 1. Output and boundaries

Create `paper_chase_v2.tex` beside `paper_chase.tex` when implementing this plan. Copy the existing IEEE structure: `\documentclass[10pt,conference]{IEEEtran}`, packages, author block, title treatment, abstract structure, keywords, table conventions, hyperlinks, and IEEE bibliography style. Retain the confirmed title, “MESA: Adapting the EFPA Test Review Model for AI Benchmark Review.” Change content, not typesetting. The filename identifies the revision; do not print “v2” in the title.

Preserve `paper_chase.tex`, `paper_refsq.tex`, `paper.tex`, `paper_old.tex`, the participant survey and all frozen research records. Reuse `references.bib`, adding only verified entries needed for the new discussion. Do not compile LaTeX or open a PDF preview. Report page length and layout as unchecked.

The first manuscript draft will contain explicit placeholders for experiments not yet conducted. It is a draft, not a submission ready report. Do not reuse old numerical results as if they came from the new conditions.

## 2. Main argument

Purpose: make it possible for readers without measurement training to understand what benchmark information supports and what remains unknown. Do not define approachability only as reduced reading or time. Do not claim that all existing methods are difficult or that 25 questions is an optimal number.

Candidate gap: the literature provides review criteria, but this review does not settle how explanations and prepared benchmark descriptions affect people's ability to apply them. EFPA's intended expertise and OECD's reported difficulties with some facets motivate the question; they do not establish that all competing methods are difficult to approach.

Contribution: a documented EFPA adaptation, an account of what it keeps and omits in relation to other research, and model studies testing the application of its questions and the influence of its summaries. Human approachability remains an objective until appropriate human findings support specific claims.

Keep the 25 questions, six domains and five categorical choices. No overall quality score. Questions 1–5 assess whether descriptive information is documented. A check having occurred is different from a favourable outcome. Missing information is different from an explicit finding that a condition was not met.

Use plain terms throughout: “answer,” “information supplied,” “source passage,” “answer supported by the information,” and “readers without measurement training.” Explain necessary technical terms where they first appear. Avoid relying on phrases such as “guided judgments” to describe the method.

## 3. Literature and conceptual basis

| Source | Use in the paper |
| --- | --- |
| EFPA 2025 | Historical adaptation source and review procedure, including description, evaluation and explanations |
| AERA/APA/NCME Standards | Why interpretations and uses of scores require support; meaning of validity, reliability and fairness |
| OECD Chapter 6 | Terminology and comparison of conceptual coverage; distinguish classification facets from quality criteria |
| Measuring what Matters | Problems connecting intended abilities, selected tasks, scoring and claims |
| BetterBench | Implementation, documentation, reproduction and maintenance |
| The Leaderboard Illusion | Comparison conditions, selective reporting and limits of rankings |
| A Definition of AGI | Scope of claims about general intelligence; not a universal quality scale |
| ECBD and relevant accessibility comparators | Prior worksheets, explanations and reader support; prevent unsupported novelty claims |

Retain EFPA as the basis. Explain OECD correspondences without claiming that OECD informed the original development. Keep the six domains in the studied questionnaire. Do not convert all 18 OECD facets into Yes/No questions or imply full preservation. Use the existing proposal's map to identify partial and absent coverage, then have the author review it.

Review source interpretations and candidate gaps before treating them as manuscript conclusions. Describe the literature work as a bounded review with systematic procedures, including search limits and unresolved texts. Do not label it exhaustive or independently screened. Existing bibliography keys for six starting references were found; verify and add OECD and ECBD entries as needed.

## 4. Research questions

**RQ1: Which review concerns does MESA keep, change or leave out?** Answer through the source correspondence analysis, with reasons and examples. This is a design analysis, not an experiment proving equivalent coverage.

**RQ2: Do MESA's explanations help AI reviewers answer its questions using the information supplied?** Answer through Study 1, with fictional cases and real benchmark descriptions assessed separately.

**RQ3: How do AI reviewers' answers change when original passages are replaced with the survey summaries?** Answer through Study 2. Changes may reflect missing information, clearer wording, direct answer cues or unsupported conclusions; disagreement alone does not establish an error.

The later extension adds: **How do participants describe their experience using MESA, and what difficulties do they report?** That question is answered by the existing survey, Study 3. Human findings are outside CHASE. A second survey or human comparison group is not required.

## 5. Prepare reference answers before new model responses

Create a new versioned study folder, separate from current and archived runs, for example `surveys/colleague-review/mesa-study/chase-v2/`. Record source versions and hashes. Prepare reference records for all 25 questions for ARC-AGI-2 and DesignQA: 50 question–benchmark pairs. HLE remains the common teaching example, not a test case.

For each pair record:

- Question ID and exact wording.
- Benchmark version and the intended use under review.
- Original source passage, page/section or code locator.
- Corresponding survey summary passage.
- Reference answer supported by the original passages, with reasons.
- Reference answer supported by the summary, with reasons.
- Any alternative defensible answer and the reason for allowing it.
- Status: assessable under the rule, contested, or unresolved.
- Missing facts, omitted qualifications and wording that supplies an answer directly.
- Preparer, checking person, date and decisions.

Do not equate knowing benchmark results with knowing every review answer. Factual and explicit-rule questions can have definite answers; adequacy and broad claim questions may remain contested. Assess main label matches only for items with a settled reference, and publish the full denominator and contested items. Show sensitivity to admissible alternatives. Never remove items after seeing which method benefits.

Where the full sources report repeated testing but the summary omits it, Yes may be supported by the source passages and Not sure by the summary. Do not penalise a reviewer for information they were not given. Record explicit nonperformance separately from absence of a report, and follow each question's wording for documentation questions.

The author checks the references before execution; an additional person with relevant expertise is preferable if available. Record what actually occurred. Author checking is not independent validation. Reference answers are not supplied to reviewer models. If human responses already exist when the reference is made, disclose that timing and any analyst access; do not claim a prospectively frozen human scoring key.

## 6. Study 1: questions with and without explanations

Purpose: test the contribution of explanations, not superiority over entire EFPA or OECD instruments.

Compare:

- **A: Questions alone.** Exact questions, five choices and common definitions of those choices.
- **B: Questions with explanations.** The same material plus the existing question explanations and associated term definitions.

Give both conditions the same completed HLE example and general answer rules. Thus the contrast tests the additional explanations when a teaching example is already available. Do not give only one condition an example. Preserve a file-level account of every difference.

Two tasks:

1. **Fictional descriptions.** Use 24 question–description cases covering six distinctions, with four cases each: missing information versus explicit absence; checking versus outcome; repeated versus changed conditions; scoring description versus marking checks; some available materials versus reproducibility; tested tasks versus broader claims. Use Yes, Partly, No, Not sure and Not applicable only where the actual question supports them. Do not force equal category counts. Keep these cases separate from development examples and have the answers checked before use. Each case targets a selected current question; this does not test all 25 questions equally.
2. **Real benchmark descriptions.** Both conditions answer all 25 questions for ARC-AGI-2 and DesignQA using the existing survey summaries and versioned reference records. Report results separately from fictional cases.

Each response contains choice, short reason and supporting passage ID or quotation. Missing information does not require an invented quotation; a reviewer can state which needed fact is absent. Avoid measuring only formatting compliance. Preserve invalid and incomplete outputs and follow a frozen failure/retry rule.

Outputs: label-match counts and denominators by condition and session; unsupported conclusions; confusion table; performance by distinction; contested examples. Report categorical answers without converting them into a benchmark quality score. Matching a reference is not proof of reviewer correctness on contested questions.

## 7. Study 2: original passages and survey summaries

Compare condition B from the real benchmark task with:

- **C: Questions with explanations and original passages.** Same questions, definitions, teaching example, system instructions and response format as B; replace only the benchmark reading material.

Share condition B between the two studies to avoid duplicate runs, but disclose that the studies reuse this condition and are not independent replications.

Build the original passage packet through a stated selection procedure across the same dated source set, including relevant qualifications and contrary findings. Source excerpts are also selected by researchers and are not automatically unbiased. If software supplies an important fact, use a labelled code excerpt and avoid adding an evaluative conclusion that answers the question. Record differences in information amount and readability instead of claiming these are controlled away.

Audit propositions in both packets before running the model. Preserve the existing survey summary even if an omission is discovered; record the issue. A corrected packet would be a new version with its own results, not a silent repair.

Outputs: answer transitions by question, reasons for transitions, omitted information, unsupported certainty and whether each response fits its own packet's reference. Present a few original-passage → summary → answer examples. Do not treat identical answers as proof of no bias or original-passage answers as automatic ground truth.

## 8. Execution size and analysis

Use the lower cost models available through this Codex session: `gpt-6-luna` as the first reviewer and `gpt-6.1-terra` as the second. Both are exposed by the session's agent model selector. Among the current models with verified prices, Luna costs less than Terra, and both cost less than Sol and Astra. This selection follows the user's preference for cheaper models available here, not observed answer quality. Report each model separately; two models from OpenAI do not establish agreement across providers.

Use fresh reviewer agents coordinated from this chat, with no inherited conversation history (`fork_turns="none"`), explicit model selection and low reasoning effort for both models. Supply only the frozen experimental material. Do not answer experimental questions in this planning conversation, which already contains reference answers and research discussion. Verify available isolation controls before execution: no inherited chat history does not by itself remove workspace access, tools or repository instructions. Record the actual environment and tool access; if the available runner cannot enforce the frozen isolation requirements, resolve that before collecting responses rather than claiming isolation that was not achieved.

Cost reference checked on 28 October 2026: [official OpenAI API pricing](https://developers.openai.com/api/docs/pricing) lists standard input/output rates per million tokens of $0.10/$0.50 for Luna and $1.00/$5.00 for Terra. These establish an API price comparison, not the billing or quota consumption of this Codex session. Do not claim the runs are free or calculate the user's Codex charges from API prices. Use the existing session access; do not set up separately billed API execution for this plan. Recheck availability before execution and record any substitution before collecting results.

| Task | Conditions | Sessions per condition | Total |
| --- | --- | --- | --- |
| Fictional cases | A and B | 3 | 6 |
| ARC-AGI-2 and DesignQA | A, B and C | 3 | 9 |
| Total per actual model | | | 15 |
| Total across Luna and Terra | | | 30 |

Each real benchmark session answers 50 questions; each fictional session answers 24 cases. This is a feasibility limit for an exploratory study, not a power calculation. Fifteen sessions are not fifteen people. Keep session-level summaries, recognise repeated questions within sessions, and do not treat every answer as an independent observation. The two benchmarks are separate tasks within each real session; record and vary order under a frozen schedule, use the same schedule across conditions, and acknowledge possible carryover.

Interleave condition execution under a recorded schedule. Freeze exact prompts, case ordering, settings, model identifier, permitted tools, output schema, failures/retries, reference keys, denominators and analysis before execution. Use fresh sessions without project files, other answers or reference keys. Do not reuse this drafting conversation as a reviewer session. Retain raw responses and failures, and record assistant involvement.

No model experiment is launched by this planning step. Preparing a manuscript draft does not require execution. New execution follows only when the study materials and checking are complete and execution is requested.

## 9. Study 3: the existing human survey

Use the survey already prepared or being collected. No new survey, compulsory transfer task or additional human condition. Preserve its packet version, questions, flow and feedback items. Verify actual collection status from records rather than assuming no responses exist.

Report perceived question clarity, distinction between choices, manageable workload, understanding of what to look for and confidence separately. Keep Cannot judge distinct from missing answers. Analyse comments with an account of actual analysts and decisions. Account for optional DesignQA participation and repeated judgments from the same session.

Reference answers can provide a supplementary descriptive comparison on assessable items using the material participants actually saw. Because reasons are optional, a matching choice does not demonstrate understanding and disagreement alone does not establish misunderstanding. If the scoring analysis was added after collection began, label the amendment and analysis timing. AI answers are not the human answer key.

Do not claim measured duration, improvement, independent understanding, or equivalence with experts. Human versus AI answer patterns do not replace a human comparison condition. CHASE describes this as future work; the later REFSQ extension adds observed findings when available. The absence of human results does not make CHASE incomplete.

## 10. Section plan for paper_chase_v2.tex

| Section | Content |
| --- | --- |
| Abstract | Problem, approachability objective, EFPA adaptation, two model studies, only actual results, scope of conclusions. Use explicit placeholders before execution. |
| Introduction | Why people need to scrutinise benchmark claims; specific gap; approachability definition; contributions; RQ1–RQ3. Avoid speed as the sole objective. |
| Background and Related Work | Source roles, prior review methods and reader support, limits of current evidence. Explain why another checklist alone is insufficient. |
| MESA and Its Basis | Existing questions and choices; EFPA adaptation; OECD correspondences; retained and omitted functions; explanation of descriptions versus assessments. |
| Reference Answers and Study Materials | Source versions, fictional cases, real benchmarks, two references per real question, checking, contested items and summary audit. |
| Study 1: Questions and Explanations | A versus B; separate fictional and real tasks; measures and results. |
| Study 2: Passages and Summaries | B versus C; shared condition disclosure; transitions, omissions and results. |
| Discussion and Limitations | What the studies establish about the materials; what remains unknown about people; source selection, reference bias, teaching cues, model limits and coverage omissions. |
| Human Evaluation as Future Work | Existing survey as Study 3 and its actual measures, without invented findings or a second survey requirement. |
| Study Artifacts and Use of AI | Inputs, versions, reference records, scripts and responses; disclose assistant preparation and analysis. Retain repository link. |
| Conclusion | Answer the research questions only to the extent supported by completed work. |

Use tables for source roles, selected adaptations, reference examples, experiment conditions and results. Prefer one answer-transition table over several charts. Place the full 25-item crosswalk, 50 reference records and all model outputs in supporting artifacts. No figure should suggest that a single score captures benchmark quality.

## 11. Relationship to the existing model study

Preserve the current reporting selection and all results. If discussed in v2, label them as an earlier study with different materials and comparisons: 30 completed conversations, 28 usable responses and 32 attempts. Do not call them observations from conditions A–C or pool them with new data.

The older cases were used during development. Do not describe them as unseen tests. New reference records created now do not retroactively make earlier analyses prospective. Any analysis of saved outputs using the new reference records is retrospective and reported separately.

## 12. Implementation order and completion checks

1. Create the v2 file from the current formatting template and replace the argument and section structure. Preserve the original file's hash.
2. Verify literature interpretations and citation metadata. Complete the adaptation/omission table and author review of candidate gap claims.
3. Draft and check the reference records and fictional cases. Record unresolved judgments. Prepare packet audit and condition files.
4. Write methods and results placeholders from the frozen design. Do not fill numbers from expectations or prior experiments.
5. When execution is requested, run the frozen model study, preserve failures, compute counts, inspect reasons and record analyst decisions.
6. Populate results and rewrite abstract/discussion/conclusion around observed findings, including null or adverse findings. Keep Study 3 future work in CHASE.
7. Check question counts, choices, condition differences, reference-answer traceability, totals, exclusions, citations, labels, LaTeX braces/environments and asset paths. Check Markdown links. Do not compile or open an automatic PDF preview.

Definition of done for the first writing phase: a separate `paper_chase_v2.tex` in the same IEEE format, with the full revised argument and methods, honest result placeholders, verified citations, and links to study preparation records. Definition of done for an empirical submission: actual Studies 1 and 2 results, recorded reference checks, reproducible analysis, and claims restricted to those findings. Study 3 remains the existing human survey for the later extension.

## Related records

- [Current manuscript](https://github.com/MyLittleFoxxie/MESA-meta-evaluation-standard-for-ai/blob/0a24e62dc9fb337dc05e61309b528972dd5b4d86/paper_chase.tex)
- [Current study and provenance](../../CHASE-study.md)
- [Literature review](../../literature/slr-2026-10-28/README.md)
- [Concept and experiment proposal](../../literature/slr-2026-10-28/mesa-direction-proposal.md)
- [Current adaptation map](../adaptation/adaptation-map.md)
- [Human evaluation plan](../../surveys/colleague-review/future-steps.md)

Planning source manuscript SHA-256: `6ab65de73c1451120ff85c931451926f1736dd9fc54538788ffd97a3c778f4b3`.
