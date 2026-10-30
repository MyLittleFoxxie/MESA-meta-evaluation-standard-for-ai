# MESA: accessibility, source integration and study proposal

28 October 2026. Proposal for author consideration. This note extends the review discussion; it does not change the frozen protocol, inclusion decisions, questionnaire, manuscripts, study inputs or participant survey. No experiment was launched. The correspondences below were prepared by the assistant and are not independent validation or a claim about MESA's historical derivation.

## Recommended purpose

MESA aims to make scrutiny of AI benchmark evidence accessible to readers without training in measurement. Accessibility means being able to understand the review criteria, find relevant evidence, distinguish evidence from uncertainty, and explain what a result supports. Reading length and time can be secondary outcomes; they are not the definition of accessibility. Specify the intended readers before making population claims, for example software researchers and practitioners without measurement training. This does not establish accessibility for every member of the public or for people with disabilities.

The candidate contribution is a documented translation of established review functions into guided questions, with evidence about what this translation preserves and where interpretations fail. The broader research question concerns access to benchmark scrutiny; the EFPA adaptation is the method used to investigate it. A profile of supported findings and unresolved matters is more defensible than an overall benchmark quality score.

The literature supplies reasons to investigate this question, not proof that all existing approaches are inaccessible. EFPA explicitly addresses expert reviewers. Its 90 pages include forms and guidance, so page count alone does not measure difficulty. OECD Chapter 6 reports that Coverage and Specificity sometimes required related literature and that facets differed in rater agreement (printed pp. 104–105). Some facets were classified consistently. Do not generalise the difficulty of some facets to all 18.

## Roles for the sources

| Source | Role in the argument and design | Boundary |
| --- | --- | --- |
| [EFPA](summaries/S03.md) | Review process, separation of description and evaluation, guidance, reasons and omissions | Remains the documented adaptation source; expert review cannot be reproduced by removing vocabulary alone |
| [AERA/APA/NCME Standards](summaries/S04.md) | Evidence supports interpretations and uses of scores; reliability and fairness require context | Foundation, not an AI questionnaire or evidence of MESA's accessibility |
| [OECD Chapter 6](summaries/S05.md) | Vocabulary and comparison of what an instrument measures, how it operates and whom it compares | Facets mix classification and evaluation; do not convert all values into Yes/No judgments |
| [Measuring what Matters](summaries/S01.md) | Motivation and checks connecting intended capability, tasks, metrics and claims | Its benchmark audit does not measure novice use of MESA |
| [BetterBench](summaries/S07.md) | Documentation, implementation, reproducibility and maintenance checks | Benchmark usability differs from accessibility of the review procedure |
| [The Leaderboard Illusion](summaries/S02.md) | Concrete reasons to examine comparison rules, selection and reporting | Findings about one platform do not establish that all rankings are defective |
| [A Definition of AGI](summaries/S06.md) | Scope of broad intelligence claims and cognitive coverage | Conditional reference when broad claims arise; its proposed categories and score are not a universal benchmark quality model |
| [ECBD](summaries/B03.md) | Comparator for describing decisions, justifying them and supporting them with evidence | Already offers a worksheet; MESA cannot claim to invent guidance or concise review |

Use the review's [gap ledger](gap-ledger.md): G1 motivates interpretation support, G2 motivates accessibility research, G3 motivates explicit uncertainty rules, and G4 motivates checking what simplification loses. G5 and G6 identify content that the review must distinguish. These gaps overlap; do not present six separate problems that one questionnaire solves.

## EFPA basis with OECD correspondences

Recommendation: keep EFPA as the procedural basis and the existing six domains for the studied questionnaire. Use OECD concepts in the explanation and an explicit correspondence table. Replacing the six domains with OECD's three groups would combine different review activities and leave some MESA functions without a clear home. OECD is not shown to be a better basis for this intended use.

The following map identifies related content, not equivalence or complete coverage. Consult the [terminology comparison](terminology.md) and the [EFPA adaptation map](../../supporting/adaptation/adaptation-map.md). The latter link is relative to this review folder's location under literature.

| OECD facet | Related current MESA questions | What remains different or absent |
| --- | --- | --- |
| Capability | Q2, Q6, Q20, Q25 | Stating an ability differs from establishing that scores measure it |
| Coverage | Q7, Q9 | MESA asks for evidence; it does not reproduce OECD's classification |
| Purpose | Q2, Q13, Q19 | Purpose supplies context for judgments, not a preferred universal use |
| Realism | Q3, Q20 | No dedicated classification of toy, simulated or real settings |
| Reference | Q5, Q13 | Identifying a reference and justifying a comparison are separate activities |
| Specificity | Q10, Q17 | Confounding differs from training data exposure in Q18 |
| Adjustability | Q7, Q15, weak correspondence | Changing a setup is not the same as controlled item characteristics or adaptive testing |
| Containedness | Q4, Q21 | Described resources do not fully classify dependence on external conditions |
| Judgeability | Q5, Q12 | Scoring mode is descriptive; checking scoring errors is evaluative |
| Reliability | Q14, Q16 | Repetition and uncertainty are addressed without all technical reliability analyses |
| Reproducibility | Q1, Q4, Q22 | Access to materials does not establish identical interactions or reproduced results |
| Variation | Q3, Q15, weak correspondence | No explicit fixed/altered/procedural classification; Q24 concerns release changes instead |
| Ambition | Q2, Q25, weak correspondence | Intended horizon is not explicitly recorded and is not a quality ranking |
| Antecedents | Q7, weak correspondence | Problem provenance does not fully assess transfer from a human test to AI |
| Autonomy | Q2, Q4, Q21 | System boundaries can be described but no mandatory component/coupled classification exists |
| Objectivity | Q4, Q21 | Conditions and comparability are related; independence of specifications is not separately classified |
| Partiality | Q21 | Current breadth may conceal distinct cultural, resource and technology advantages |
| Progression | No explicit item; Q2 could provide context | Learning during the test differs from training rules Q19 or release maintenance Q24 |

This map already rules out a claim that everything in OECD is preserved. Some omissions can be justified by scope; others may warrant a future questionnaire version. Do not add items merely to reach 18/18 coverage. Similarly, matching EFPA headings does not preserve all technical checks within them.

A future explanatory structure could describe the benchmark first, then organise evidence concerning validity, consistency and fairness, followed by access and reporting. That is a candidate presentation, not an adopted instrument. Any changes to wording, order, guidance or categories require a new version; existing results continue to refer to their original materials. Replacing EFPA with OECD retrospectively would misstate the derivation.

## What can count as an expected answer

| Task | Basis for assessment | Reporting rule |
| --- | --- | --- |
| Identify a fact in a fixed source version | Located passage, table or code and stated scope | Assess factual fidelity |
| Apply an explicit review rule to a description | Rule specified before responses; case supplies sufficient premises | Assess rule application, including appropriate uncertainty |
| Judge adequacy, coverage or support for a broad claim | Reasons, intended use and sometimes additional literature | Allow defensible alternatives or mark the item as contested; do not silently force one label |

Knowing HLE or ARC-AGI-2 results does not establish the answer to every review question. A low model score does not demonstrate benchmark quality. HLE is already a completed teaching example and cannot also be described as an unseen evaluation case. ARC-AGI-2 and DesignQA permit sourced case analyses but do not automatically supply an authoritative answer key. The current P6B disagreement demonstrates why expected labels need sensitivity analysis.

For any new key, record source version, claim, applicable rule, supporting passage, expected label or admissible alternatives, and uncertainty. Have a human with relevant expertise check it before new responses are collected. Record the actual reviewer and decisions; do not claim independence unless it occurred. A consensus key is a reference judgment, not infallible truth. Do not edit the saved key or responses from the existing study.

## Recommended evidence package for CHASE

### Study 1: preservation and omissions

Extend the conceptual correspondence analysis using the sources above. Define the unit as a review function, not a document heading. For each selected function record: source locator, intended judgment, MESA wording, retained distinction, lost detail, and an example of a conclusion the question cannot support. Mark retained, partly retained, omitted or added, with reasons. Have the author review these decisions. Do not report a preservation percentage unless the denominator and coding rules are justified; a technical function may be more consequential than several descriptive ones.

Presentation: one concern-by-question matrix with explicit partial and omitted cells, plus two worked examples. This is a design analysis, not an experiment demonstrating equivalent coverage.

### Study 2: existing model interpretation study

Use the saved 24 descriptions and 49 claims, together with the two benchmark applications. Report the original labels, denominators and exclusions, including the P6B alternative. Group interpretation problems by missing information versus negative evidence, occurrence versus outcome, and task performance versus broader claims only after documenting the coding rules. Any new coding of saved outputs is retrospective analysis.

Presentation: a confusion table for Supported/Contradicted/Not established, a table of disputed items, and a small set of source passage → rule → response examples. Keep these claim labels separate from MESA's five questionnaire choices. A confusion table assesses agreement with the reference key, not unquestionable correctness.

This study can expose interpretation failures. It does not establish human accessibility or a causal advantage over other methods: guidance was developed after earlier testing, batches were sequential, only MESA received a teaching example, and one reviewer model was used. Preserve those limits even if differences appear large.

### Optional future experiment if another controlled test is needed

Do not launch it merely to reframe the paper. A manageable prospective test would isolate the presentation of guidance: current plain explanations versus a reference wording condition covering the same concerns. Give both the same evidence, response task and equally informative teaching examples. Keep concept coverage matched so the difference is not simply extra information. This would be a comparison of guidance presentations, not a comparison with complete EFPA or OECD.

Illustrative ceiling: two guidance conditions × two actual models × three separate sessions = 12 sessions. Each session answers 24 short cases: six review distinctions, each with four evidence states. Construct these after selecting the distinctions, separate them from development examples, have the key checked, and freeze prompts and analysis before execution. Distribute paired cases within each session, vary order with a recorded rule, withhold answers and project history, and report any order or within-session dependence. Repeated sessions are not independent people; cases within a session are not independent runs. Model selection and paid use are separate execution decisions, not made here.

Compare reference-label matches, unsupported conclusions and handling of missing evidence separately by distinction, model and session. Report all failures and denominators. Use a matrix of condition by distinction and individual example transitions. This is exploratory model evidence; 12 sessions is a feasibility proposal, not a sample-size or power justification. It would not measure accessibility for people.

## Summary bias and the existing survey

The current packet includes interpretations as well as factual descriptions. For example, statements distinguishing varied retrieval passages from identical repeated conditions can teach the Q14/Q15 distinction directly. This is legitimate as instructional support, but a correct response may reflect a cue rather than independent reasoning. Likewise, remarks that evidence does not establish a composite ability can supply part of a Q11 judgment. These observations identify a risk, not a finding that the survey is invalid.

Audit the packet separately from questionnaire coverage: identify factual extraction, interpretation, omission and direct answer cues; link each to the original source; check qualifications and conflicts; record author and assistant involvement. Have someone other than its preparer check the packet if feasible. An audit now is retrospective for the saved model study. Do not rewrite frozen passages to repair observed outcomes.

If changing evidence presentation later, test it separately from guidance wording. A summary-versus-source-excerpts study changes the information presentation and possibly the amount of information; it does not isolate questionnaire effects. Freeze selection rules and assess omissions as well as factual accuracy. Neither summary nor excerpts are automatically ground truth.

## Human contribution after CHASE

Keep the current survey as an evaluation of the packet as a whole: questions, explanations, passages and HLE example. Report the five feedback ratings separately as perceptions and analyse optional comments with actual analyst decisions. Familiarity ratings are self reports. Do not infer correctness from agreement, or duration from submission timestamps. Account for the optional DesignQA review and repeated responses within participants.

Those responses can identify perceived clarity, difficulty distinguishing choices, perceived workload, understanding of what to look for and confidence using MESA. They can motivate changes, but cannot establish independent comprehension or improvement over another method.

If demonstrated understanding is later required, use a separately specified transfer task with new short passages, evidence identification and reasons, assessed against a reviewed rubric. This requires its own frozen materials, collection plan and applicable consent procedures. Do not insert it into an active survey or pool versions without an explicit plan. HLE remains teaching material.

## Proposed research questions

1. Which review functions and distinctions can MESA express through guided questions, and which require further analysis?
2. What interpretation failures occur when the procedure is applied to supplied benchmark evidence?
3. How do intended readers understand and use the procedure, and which forms of support do they need?

CHASE can address the first and model evidence for the second. The current human survey contributes perceptions and reported difficulties relevant to the third; a transfer task would add evidence of demonstrated understanding. Accessibility remains the research purpose throughout, without defining it solely as speed or claiming it has already been achieved.

## Sources and checks

Read against the current packet, CHASE-study.md, EFPA adaptation map, OECD Chapter 6 printed pp. 101–105, and the review's source summaries. Primary institutional records: [OECD volume](https://www.oecd.org/en/publications/ai-and-the-future-of-skills-volume-2_a9fe53cb-en.html), [EFPA 2025](https://www.efpa.eu/resource/efpa-test-review-model-version-2025/); framework comparators: [ECBD](https://arxiv.org/abs/2406.08723), [BetterBench](https://arxiv.org/abs/2411.12990). Research interpretations and proposed experiments need author review. No new empirical finding is claimed in this note.
