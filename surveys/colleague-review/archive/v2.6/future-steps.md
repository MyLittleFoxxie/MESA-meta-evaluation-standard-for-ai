# Human evaluation for the REFSQ extension

This is a preparation plan, not a report of human results. The CHASE paper reports the adaptation and model study; human evaluation is future work. The planned REFSQ paper extends that contribution. The author reports that the survey has not yet been circulated.

## Research questions

The main focus is accessibility: whether participants feel able to use MESA for benchmark review, what they find difficult, and how confident they feel.

1. How do participants rate question clarity, the ease of distinguishing choices, and manageable reading and answering?
2. How well do participants feel MESA helped them understand what to look for, and how confident did they feel using it?
3. Which questions, explanations, choices or examples do participants report as difficult, and why?

As supporting analyses, describe answer distributions and agreement for each question and benchmark. Disagreement alone does not establish misunderstanding.

The object of study is the questionnaire together with the supplied passages, definitions, HLE teaching example and ARC-first sequence with an optional second benchmark. These questions do not isolate the questionnaire wording from those materials.

## Settle before recruitment

Record the target population, sampling approach, eligibility criteria, recruitment channels and text, consent process, applicable ethics review or exemption procedures, data access and retention arrangements, and a sample-size rationale tied to the intended descriptive estimates. Settle exclusions, duplicate handling, incomplete responses, withdrawals where feasible without identifiers, and the analysis plan before collecting responses. Freeze the exact packet, generated page, fingerprint and analysis plan. Do not invent recruitment dates or approvals.

Decide in advance whether the available sample can support agreement estimates or uncertainty intervals and how sparse categories will be reported. The 25 or 50 judgments from one session do not provide 25 or 50 independent participants. Do not select sample size from the number of question responses alone. Keep collected responses out of this public repository.

## Collection and analysis

Packet 2.6 (`mesa-guided-arc-designqa-v2-6`) collects three familiarity ratings and separate benchmark submissions. ARC-AGI-2 comes first; DesignQA is optional. Each submission has 25 choices, optional question comments, five required feedback ratings with Cannot judge, and one optional feedback comment. Feedback refers to that benchmark review, so two submissions from one session contain two feedback sets. No composite score is calculated.

A random session identifier links reviews from the same saved browser session; it is not verified participant identity. Each benchmark has its own submission identifier and device timestamp. These records support duplicate review, not duration measurement. Repeated delivery of an unchanged response retains its identifier; editing before acceptance creates a new identifier. Test deliveries marked TEST — exclude from research must be excluded before analysis.

Report the participant flow and explicit denominators: received deliveries, distinct eligible responses, exclusions, participants with each response, Cannot judge selections, and participants who supplied comments. Distinguish repeat deliveries of one submission from changed responses with different identifiers; do not infer that different identifiers necessarily mean different people. Freeze the adjudication rule before recruitment.

For each question and benchmark, report the five-category distribution and an appropriate, prespecified categorical agreement summary with its denominator and assumptions. Do not average Yes/Partly/No/Not sure/Not applicable into a quality score. If uncertainty estimation is justified by the design and sample, resample whole participants with all their judgments together; never bootstrap individual answers as independent observations. Convenience sampling still limits generalization.

Report each familiarity item separately as self-report. Report each feedback item separately, retaining Cannot judge as its own category and disclosing whether any percentage denominator excludes it. Do not combine the feedback ratings into a score or call them a validated usability measure. Ratings describe perceived clarity, workload, understanding of what to look for, and confidence, not demonstrated comprehension, objective effort or measured duration. Optional comment summaries must identify both the number of commenters and the eligible participant denominator; silence is not evidence of ease or agreement.

## Human interpretation of comments

Document who reads and codes the comments, the coding approach, code definitions, changes to codes, and any independent coding or discussion that actually occurs. Retain an auditable record of decisions and anonymized excerpts where consent permits. Any assistant support must be disclosed and distinguished from human analysis. Do not claim multiple coders, reliability checks or reconciliation unless performed.

Use comments to explain participants' stated reasons and difficulties. Model answers and the worked example are not ground truth. Disagreement does not by itself prove misunderstanding; it can reflect reasonable differences in interpretation or uncertainty. Evaluate claims about understanding against suitable additional evidence if that becomes a research objective.

## Extending CHASE into REFSQ

Retain the adaptation rationale, questionnaire and verified model study, using the current reporting selection in `mesa-study/chase-report/`. Add the human method, actual recruitment and participant characteristics supported by the data, observed results, and discussion after records exist. Use explicit placeholders until then. Keep human findings out of the CHASE study.

Discuss shared passage cues, the teaching example, fixed benchmark order, convenience sampling, optional comments, only two participant benchmarks, and repeated judgments within participants. Differences from model outputs are descriptive comparisons, not a test of human correctness. Claims of comparative efficiency require a suitable comparison and effort measurements; claims of team benefits require evidence from team discussions or decisions. Neither follows from the five feedback ratings.

See [maintenance instructions](agent-guide.md), [organizer notes](organizer-notes.md), and [packet source](packet.json).

The final two feedback items ask about understanding what to look for when reviewing a benchmark, then confidence using MESA. Report both separately as perceptions, not demonstrated ability or correctness. The opening confidence item concerns interpreting AI test scores, while the final item concerns using MESA; do not subtract them or claim a measured improvement. No overall feedback score is calculated.


## Version 2.6 analysis amendment

Report received deliveries, distinct submission IDs and linked session IDs separately; do not count the two benchmark submissions as two independent participants. Report ARC completion, optional DesignQA uptake, unfinished second reviews where known, and exclusions with benchmark-specific denominators. Do not infer an unfinished review from an absent delivery. Repeated judgments and feedback within linked sessions must be accounted for.

Describe optional participation in DesignQA as a source of selection differences and retain the fixed ARC-first order as a limitation. Report feedback for each benchmark separately, with Cannot judge and optional-comment denominators. The confidence item concerns using MESA for this benchmark, not both benchmarks. Do not compare opening score-interpretation confidence with this item as a measured improvement. Freeze these amendments with population, recruitment and analysis decisions before collecting research responses. The authorized synthetic TEST deliveries are implementation checks, not human study data.
