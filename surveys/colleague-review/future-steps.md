# Human evaluation for the REFSQ extension

This is a preparation plan, not a report of human results. The CHASE paper reports the adaptation and model study; human evaluation is future work. The planned REFSQ paper extends that contribution. The author reports that the survey has not yet been circulated.

## Research questions

1. How do participants distribute their categorical judgments for each MESA question on ARC-AGI-2 and DesignQA, and where do judgments agree or differ?
2. Which questions, explanations, answer choices or examples do participants report as difficult to interpret or use, and what reasons do they give?
3. How do participants rate the clarity of questions, the ease of distinguishing answer choices, and the manageability of reading and answering?

The object of study is the questionnaire together with the supplied passages, definitions, HLE teaching example and fixed sequence. These questions do not isolate the questionnaire wording from those materials.

## Settle before recruitment

Record the target population, sampling approach, eligibility criteria, recruitment channels and text, consent process, applicable ethics review or exemption procedures, data access and retention arrangements, and a sample-size rationale tied to the intended descriptive estimates. Settle exclusions, duplicate handling, incomplete responses, withdrawals where feasible without identifiers, and the analysis plan before collecting responses. Freeze the exact packet, generated page, fingerprint and analysis plan. Do not invent recruitment dates or approvals.

Decide in advance whether the available sample can support agreement estimates or uncertainty intervals and how sparse categories will be reported. The 50 judgments from one participant do not provide 50 independent participants. Do not select sample size from the number of question responses alone. Keep collected responses out of this public repository.

## Collection and analysis

Packet 2.1 (`mesa-guided-arc-designqa-v2-1`) collects three separate familiarity self-reports, 50 categorical judgments, optional question comments, three required feedback ratings and one optional feedback comment. Each feedback rating includes Cannot judge. Store labels separately; unanswered is null and is never recoded as Cannot judge. No name, respondent email, elapsed-time measure or additional tracking is collected. Device-derived completion timestamps and random submission identifiers support delivery records and duplicate review, not duration measurement or participant identification.

Report the participant flow and explicit denominators: received deliveries, distinct eligible responses, exclusions, participants with each response, Cannot judge selections, and participants who supplied comments. Distinguish repeat deliveries of one submission from changed responses with different identifiers; do not infer that different identifiers necessarily mean different people. Freeze the adjudication rule before recruitment.

For each question and benchmark, report the five-category distribution and an appropriate, prespecified categorical agreement summary with its denominator and assumptions. Do not average Yes/Partly/No/Not sure/Not applicable into a quality score. If uncertainty estimation is justified by the design and sample, resample whole participants with all their judgments together; never bootstrap individual answers as independent observations. Convenience sampling still limits generalization.

Report each familiarity item separately as self-report. Report each feedback item separately, retaining Cannot judge as its own category and disclosing whether any percentage denominator excludes it. Do not combine the feedback ratings into a score or call them a validated usability measure. Ratings describe perceived clarity and workload, not demonstrated comprehension, objective effort or measured duration. Optional comment summaries must identify both the number of commenters and the eligible participant denominator; silence is not evidence of ease or agreement.

## Human interpretation of comments

Document who reads and codes the comments, the coding approach, code definitions, changes to codes, and any independent coding or discussion that actually occurs. Retain an auditable record of decisions and anonymized excerpts where consent permits. Any assistant support must be disclosed and distinguished from human analysis. Do not claim multiple coders, reliability checks or reconciliation unless performed.

Use comments to explain participants' stated reasons and difficulties. Model answers and the worked example are not ground truth. Disagreement does not by itself prove misunderstanding; it can reflect reasonable differences in interpretation or uncertainty. Evaluate claims about understanding against suitable additional evidence if that becomes a research objective.

## Extending CHASE into REFSQ

Retain the adaptation rationale, questionnaire and verified model study, using the current reporting selection in `mesa-study/chase-report/`. Add the human method, actual recruitment and participant characteristics supported by the data, observed results, and discussion after records exist. Use explicit placeholders until then. Keep human findings out of the CHASE study.

Discuss shared passage cues, the teaching example, fixed benchmark order, convenience sampling, optional comments, only two participant benchmarks, and repeated judgments within participants. Differences from model outputs are descriptive comparisons, not a test of human correctness. Claims of comparative efficiency require a suitable comparison and effort measurements; claims of team benefits require evidence from team discussions or decisions. Neither follows from the three feedback ratings.

See [maintenance instructions](agent-guide.md), [organizer notes](organizer-notes.md), and [packet source](packet.json).
