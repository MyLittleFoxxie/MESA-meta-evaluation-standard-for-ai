# Literature context for MESA

Research record dated 28 October 2026. This is a bounded review with systematic procedures, not a claim of exhaustive coverage. Inclusion decisions, extractions and gap claims were prepared by one assistant and await author review. See [counts and limits](limitations-and-counts.md), [screening decisions](screening-decisions.md) and [source notes](README.md#source-notes).

## What the seven starting sources contribute

| Source | Contribution to this review | What it does not establish |
|---|---|---|
| [Measuring what Matters](summaries/S01.md) | Connects the phenomenon of interest, task, metric and claim; audits validity evidence in benchmark papers. | That a short review form improves understanding for readers without measurement expertise. |
| [The Leaderboard Illusion](summaries/S02.md) | Shows why ranking interpretation requires scrutiny of participation, selection, sampling and disclosure. | That all leaderboards share the observed problems, or that scores alone identify their causes. |
| [EFPA 2025](summaries/S03.md) | Provides a review process, separates description from evaluation, and supplies item guidance and rating anchors. | That transfer from psychological tests to AI benchmarks is validated, or that the original model is intended for novices. |
| [AERA/APA/NCME 2014](summaries/S04.md) | Grounds validity in evidence for interpretations and uses; distinguishes reliability/precision and fairness. | A ready made AI benchmark review instrument or empirical evidence for MESA. This source is a foundation exception. |
| [OECD Chapter 6](summaries/S05.md) | Defines 18 facets for characterising evaluation instruments and applies them to 36 instruments. | A universal quality score. The classification study does not establish comparative accessibility for general readers. |
| [A Definition of AGI](summaries/S06.md) | Makes the breadth and structure of an intelligence claim explicit through a proposed cognitive framework. | A consensus definition or a reason to treat every task benchmark as a measure of general intelligence. |
| [BetterBench](summaries/S07.md) | Provides criteria for benchmark development, documentation, implementation and maintenance, with an audit and stakeholder input. | That benchmark usability and reviewer understanding are the same outcome. Version counts also need care. |

These works answer different questions. Standards define expectations; frameworks organise judgments; audits observe problems under particular conditions. Their conclusions should not be pooled as though they were repeated trials of one intervention.

## RQ1: Concerns and review procedures

The literature supports reviewing the relation between a claim and its evidence, rather than treating a score as a sufficient description of capability. Relevant activities include defining the intended phenomenon; examining task and item coverage; checking scoring and reference answers; identifying alternative explanations; and limiting conclusions to the tested setting. The Standards, Measuring what Matters and ECBD provide distinct accounts of this reasoning. OECD offers a classification of the instrument, while the AGI sources address the breadth of capability claims. [S01](summaries/S01.md), [S04](summaries/S04.md), [S05](summaries/S05.md), [S06](summaries/S06.md), [B03](summaries/B03.md), [B08](summaries/B08.md).

Empirical work supplies reasons to ask these questions. Studies examine benchmark correlations, task demands, annotation errors, prompt sensitivity, contamination and changes in rankings. The findings support scrutiny of these mechanisms, but their rates are specific to the models, tasks and interventions studied. An attack or perturbation experiment establishes a possible failure under stated conditions; it does not estimate its prevalence in ordinary use. [R291](summaries/R291.md), [R042](summaries/R042.md), [B09](summaries/B09.md), [B10](summaries/B10.md), [B11](summaries/B11.md), [B12](summaries/B12.md), [B19](summaries/B19.md), [B20](summaries/B20.md).

Another group concerns execution and accountability: documenting prompts, model versions, data sources, scoring, uncertainty, exclusions and maintenance. BetterBench and the evaluation harness practice report explain how implementation choices affect comparison. Evaluation Cards and Croissant Tasks organise reporting and reproduction. The Leaderboard Illusion adds scrutiny of the process through which scores become public. These procedures complement measurement reasoning; reproducible execution cannot, by itself, establish that a task measures the claimed construct. [S02](summaries/S02.md), [S07](summaries/S07.md), [B02](summaries/B02.md), [R362](summaries/R362.md), [R383](summaries/R383.md).

Fairness has several objects. It can concern equal conditions for competing systems, coverage of languages and cultures, differences in model outputs across groups, or the rights of human test takers. These require different evidence. Studies of multilingual evaluation, social bias probes and automated judges show why one unspecified fairness question would be difficult to interpret. [S04](summaries/S04.md), [S05](summaries/S05.md), [B17](summaries/B17.md), [R055](summaries/R055.md), [R294](summaries/R294.md), [R299](summaries/R299.md).

The retrieved literature already provides checklists, worksheets, scorecards, taxonomies, search tools and reporting schemas. ECBD has a 20 question worksheet; OECD has 18 facets; BetterBench has criterion specific rubrics; the Scorecard of AI Benchmark Quality requires judgments and reasons. Therefore, “there is no structured way to review AI benchmarks” is not supported. [B03](summaries/B03.md), [S05](summaries/S05.md), [S07](summaries/S07.md), [R097](summaries/R097.md).

## RQ2: Explanations, judgments and missing information

Existing guidance does more than name criteria. ECBD distinguishes describing a decision, justifying it and supplying evidence. EFPA provides anchors and explanatory material. OECD defines each facet and its possible values. The Scorecard requires reasons for judgments, and Evaluation Cards provides different presentations for different readers. A MESA contribution cannot rest on definitions or guidance being absent from prior work. [B03](summaries/B03.md), [S03](summaries/S03.md), [S05](summaries/S05.md), [R097](summaries/R097.md), [R362](summaries/R362.md).

Missing information is handled differently across tools. EFPA section 6.4 separates no information from inadequate evidence and inapplicability. OECD permits N/A for reliability when the methodology is unclear, so N/A does not always mean the criterion is irrelevant. BetterBench can assign zero when required documentation is absent. The Scorecard can treat inadequate documentation as nonfulfilment, while SIGHT combines No and Not reported for scoring. Evaluation Cards instead surfaces reporting gaps. These are differences in decision rules, not a ranking of which instrument is best. [S03](summaries/S03.md), [S05](summaries/S05.md), [S07](summaries/S07.md), [R097](summaries/R097.md), [R063](summaries/R063.md), [R362](summaries/R362.md).

For MESA, three distinctions warrant investigation: information absent versus an explicitly reported problem; a check performed versus a favourable outcome; and an answer about documentation versus a claim about underlying benchmark quality. Keeping distinct choices is a design provision. Whether readers use them as intended remains an empirical question. The mere presence of a Not sure option does not demonstrate calibrated uncertainty.

## RQ3: Evidence about use by reviewers

| Evidence | Observed activity | Limit for an accessibility claim |
|---|---|---|
| [OECD](summaries/S05.md) | AI related undergraduate and graduate students classified instruments; discussion changed some ratings. Time taken was requested. | This is not a novice versus expert comparison or a demonstrated reduction in effort. Agreement following discussion is different from initial agreement. |
| [BetterBench](summaries/S07.md) | Stakeholder interviews, author assessment and calibration informed the framework. | Design consultation and benchmark auditing do not establish comparative reader comprehension or review duration. |
| [BenchScout](summaries/R004.md) | Twenty two participants used a benchmark search tool and provided ratings. | Most reported familiarity with the field. Ratings concern perceived usability and effectiveness, not a controlled test of correct review decisions or time savings. |
| [Scorecard](summaries/R097.md) | Two assessors applied the penultimate form to Vending-Bench 2 and differed on six items. | One case identifies interpretation problems but does not quantify general reviewer accessibility. |
| [Evaluation Cards](summaries/R362.md) | Interviews and feedback informed summary and research presentations. | Perceived time savings are not timed results. Systematic usability evaluation is planned, and reported interview counts conflict within the PDF. |
| [QUADAS-2 comparison](summaries/R357.md) | Five experienced human reviewers and repeated runs of one model assessed twenty AI imaging papers. | Adjacent appraisal evidence; no novice comparison. Agreement was sensitive to study design and category prevalence, and does not establish correctness. |
| [PRAISE](summaries/R377.md) | Three chemistry students and a tutor implemented and assessed a published model through a guided workflow. | Adjacent evidence that guidance can support people without programming expertise. It is a teaching case, not a comparison of benchmark review methods. |

These sources rule out “no one has studied reviewers” and “no tool supports readers without technical expertise.” They leave a narrower question: how well can an intended population of readers apply a benchmark review procedure, and what judgments are lost or preserved when the procedure is shortened? The retrieved evidence does not settle that question across populations, tools and benchmark types.

Model experiments can examine response completeness, interpretation of supplied evidence, unsupported inferences and stability under stated conditions. They cannot establish how people understand the form, how long people take, or whether people make better decisions. Research on evaluator bias and prompt sensitivity makes this distinction more necessary, not less. [R053](summaries/R053.md), [R055](summaries/R055.md), [B11](summaries/B11.md), [B24](summaries/B24.md), [B25](summaries/B25.md).

## RQ4: What remains open

There is evidence of recurring problems in how benchmark claims are supported, how evaluation procedures are reported and how reviewers interpret criteria. There is also substantial work addressing each concern. The review supports studying the application of guidance, not claiming that MESA invents benchmark review or resolves validity through a questionnaire.

The strongest candidate direction is **a concise, evidence guided review procedure whose accessibility is evaluated for a defined group of readers**. “Accessible” should mean an outcome that can be observed: finding relevant information, understanding a criterion, distinguishing uncertainty from a negative finding, or producing a warranted conclusion. Length and completion rate are insufficient substitutes. Reduced effort is an objective until measured.

The [gap ledger](gap-ledger.md) records supporting evidence, counterexamples and uncertainties for each candidate. These are proposals for author consideration, not approved manuscript conclusions.

## Candidate implications for MESA

MESA could use OECD terms where the meanings fit, while explaining differences rather than renaming every domain mechanically. The [terminology comparison](terminology.md) identifies the 18 facets and several terms whose meanings differ across sources. OECD is a conceptual comparator; EFPA remains the stated adaptation method unless the author changes that account on documentary grounds.

Possible research questions are:

1. **Evidence judgments:** When reviewing supplied benchmark material, how well does MESA help a reviewer distinguish documented information, reported checks, reported outcomes and unresolved information?
2. **Coverage and concision:** Which concerns from existing review approaches can MESA express, and which require further analysis outside its 25 questions?
3. **Use by intended readers:** How do readers with different levels of AI and measurement familiarity interpret the questions and response choices, and what effort does the task require?

These are candidates, not changes to the current study. Saved model experiments may answer parts of the first two only where the recorded design supplies suitable evidence. Human responses can add evidence for the third, but feedback alone measures perceptions. Demonstrated understanding needs suitable tasks and a justified assessment procedure; duration needs timing; comparative improvement needs a comparison. This review does not require a human study to complete CHASE or imply that the current survey already measures these outcomes.

Before manuscript use, the author should review the exclusions, source interpretations, version conflicts and proposed gaps. No questionnaire, manuscript, experiment or survey was changed in this phase.
