# MESA rubric, draft 1

Status: specified before any session, 31 October 2026, from the finalized question mapping and the frameworks' item specifications, and reviewed by the author on 31 October 2026. Frozen together with the Study 1 materials before the main sessions, so the Study 1 results do not shape it; the anchors borrow wording from the framework items that mapped best to each concern. Identifier when frozen: `mesa-rubric-v4`.

The rubric follows the shape of the EFPA Test Review Model: describe the instrument first, then evaluate the evidence. It has two parts.

## Part A: description

Eight facets from the OECD framework, read off the benchmark's paper, README and repository text and recorded as one value each. They are a description, not a score. The 2023 raters agreed on these facets consistently, which is why they are here and not in Part B. Three of them decide which Part B questions apply.

| Facet | Values | Decides |
|---|---|---|
| Purpose | research, conformity, other (say which) | |
| Judgeability | manual, automated, mixed | B07 applies only when automated or mixed |
| Reference | absolute, relative (say to what) | B09 applies in full only when relative |
| Containedness | fully contained, partial interference (say what), not contained (say what) | |
| Objectivity | loose, customised, fully independent | |
| Autonomy | autonomous, coupled (say with what), component | |
| Progression | static, developmental | |
| Variation | fixed, altered, procedural | B20 applies in full only when altered or procedural, or when the sources record more than one release |

Each value is recorded with a source location and a short quote, like every judgment in Part B.

## Part B: evidence

One question per shared concern. Each question has three positive anchors, one negative anchor and two null states.

- **Stated**: the sources claim the concern is met but show nothing that can be inspected.
- **Shown**: the sources show an inspectable artefact or description that bears on the concern.
- **Checked**: the sources show that a check was done and report its coverage, findings and limits.
- **Contradicted**: the sources show a defect or a statement that contradicts the claim. This is the only negative anchor, and it needs a cited location.
- **Insufficient evidence**: the sources do not let the reviewer choose an anchor. Not a defect.
- **Not applicable**: the concern does not arise for this benchmark, with the reason taken from Part A or from the benchmark's stated use.

No total score. A higher anchor is not a better benchmark: a benchmark whose authors report a thorough check that found many errors reaches Checked while disclosing more defects than a benchmark that reports no check.

Every judgment records: the anchor or null state; the reason in one or two sentences; one or more source locations with short quotes; what was missing; and which checks the reviewer performed.

| Id | Question | What counts as Shown | What counts as Checked | Applies when | Source items that shaped the wording |
|---|---|---|---|---|---|
| B01 | Is the ability under test stated and made concrete? | a definition with scope and an operational form | the authors compare their definition with others or test its boundaries | always | BB-01, ECBD-Q3, SC-02, SC-03, H2B-04, ABC-R.5 |
| B02 | Are the intended use, users and real world relevance stated? | intended users and uses named | use cases or user input described | always | BB-03, BB-06, ECBD-Q1, ECBD-Q2, H2B-03 |
| B03 | Is the selection of tasks justified for the claimed ability? | a reason why these tasks are evidence; differences from related benchmarks | expert or empirical support for the selection | always | BB-07, BB-13, ECBD-Q4, ECBD-Q7, SC-24, SC-25, H2B-01 |
| B04 | Does the task set cover the ability, and is it representative? | the task space and its range described; sampling described | coverage verified against the documented task space | always | SC-06, SC-07, ECBD-Q12, ECBD-Q13, H2B-11, H2B-12, OECD-Coverage |
| B05 | Were tasks and reference answers checked? | the checking procedure described | coverage, findings and limits of the check reported | always | SC-58, SC-60, H2B-13, H2B-18, ABC-T.7, ABC-T.8, ABC-O.d.1 |
| B06 | Is the scoring rule described? | the metric and output validation method stated, including answer formats | edge cases stated: timeouts, partial answers, unexpected formats, refusals | always | BB-36, H2B-20, H2B-21, SC-65, ABC-O.h.1 |
| B07 | Was the scoring implementation checked, and can it be gamed? | the implementation can be read and compared with the rule | parser or judge validated; exploit tests reported | Judgeability automated or mixed | BB-12, SC-64, SC-66, SC-67, SC-68, ABC-O.c.1, ABC-O.i.1, H2B-22 |
| B08 | Are aggregation and subscores justified? | how scores are combined is stated | a reason for the combination, or facets reported separately | more than one score or subscore exists | SC-04, SC-18, SC-19, ECBD-Q18, ECBD-Q19 |
| B09 | Are the comparison points justified? | human, random or trivial baselines reported | the baseline procedure described well enough to judge the comparison | always; in full when Reference is relative | BB-10, BB-11, SC-55, SC-56, ABC-R.12, ABC-R.13 |
| B10 | Is variation on repeated testing reported? | repeated runs or an estimate of variation reported | the design of the repetition and its result stated | always | SC-48, H2B-33, H2B-38, OECD-Reliability |
| B11 | Are prompting and setup described, and is their effect tested? | prompts and adaptation method given | sensitivity to prompt wording or setup measured | always | ECBD-Q9, BB-14, SC-31, H2B-26, H2B-28, H2B-29 |
| B12 | Are uncertainty and statistical support reported? | sample size and uncertainty for primary scores | power or significance reasoning given | always | BB-22, SC-14, SC-15, ABC-R.10 |
| B13 | Were shortcuts, confounds and chance investigated? | the possibility named and discussed | an analysis of confounds, guessing or error modes reported | always | SC-21, SC-28, SC-29, SC-38, ABC-O.b.3, ABC-O.h.2, OECD-Specificity |
| B14 | Was exposure of test material in training data assessed? | the risk acknowledged; a safeguard described | a contamination check or held out procedure reported | always | BB-19, BB-20, SC-35, H2B-08, ABC-R.3 |
| B15 | Are the rules for training on the test and for repeated submission stated? | a policy stated | the policy enforced or its effect discussed | a leaderboard or submission process exists | BB-25, ABC-R.4 |
| B16 | Are claims about performance beyond the test supported? | the intended scope of interpretation stated | evidence for transfer or deployment conditions reported | always | BB-04, SC-26, SC-41 to SC-47, H2B-40, OECD-Capability |
| B17 | Is fairness across systems and conditions addressed? | conditions for competing systems stated | checks that no system or condition is favoured | always | SC-45, OECD-Partiality, OECD-Objectivity |
| B18 | Are materials and instructions for repeating the evaluation provided? | code, data, environment and steps present | a replication by the authors or a third party reported | always | BB-15, BB-16, BB-21, BB-26, BB-27, H2B-49 to H2B-55, ABC-R.1, ABC-R.2 |
| B19 | Are the terms of access and license stated? | a license for data and code | terms for reuse and protections for responsible use | always | BB-37, H2B-46 |
| B20 | Are versions and changes recorded? | an identifier or release name | a change record with the effect on comparisons | always; in full when more than one release exists | BB-38, BB-39, SC-36, ABC-T.6 |
| B21 | Are limitations and flaws stated, and do claims stay within the evidence? | limitations listed | flaw impact discussed qualitatively or quantified, with guidance for interpretation | always | BB-34, SC-51 to SC-53, ABC-R.7 to ABC-R.9, ABC-R.11 |
| B22 | Do maintenance and a contact exist? | a contact named | a feedback channel or recent upkeep visible in the sources | always | BB-45, BB-46, BB-47 |
| B23 | Is transfer to another cultural or deployment context assessed? | the context of origin stated | an assessment of transfer to a named other context | a target context is declared for the review | CAL-IO-2, CAL-IC-1, CAL-OC-1, OECD-Partiality |
| B24 | Is harmful or sensitive content handled? | the need for warnings or redaction considered | a review of released material for secrets or toxic content reported | always | BB-23, H2B-17, H2B-47, H2B-48 |
| B25 | Are the systems evaluated and the benchmark's difficulty examined? | the set of systems and the score range reported | discrimination between systems or ceiling effects analysed | the paper reports an evaluation of systems | H2B-24, H2B-25, H2B-36, H2B-37 |
| B26 | Are results presented and explained? | results in tables or figures | the findings explained and connected to the ability | the paper reports an evaluation of systems | H2B-41, H2B-42, H2B-43 |
| B27 | Are data provenance and collection documented? | sources, collection and preprocessing described | the annotation process and its quality reported | always | BB-31, BB-40, BB-41, BB-42, H2B-05, ECBD-Q6 |
| B28 | Is the evaluation environment controlled and isolated from answers? | the environment and its isolation described | state clearing and isolation verified or enforced in code | the benchmark runs systems in an environment with tools or state | ABC-T.4, ABC-T.5, SC-37, SC-34, OECD-Containedness |
| B29 | Did domain experts or users take part in design or review? | involvement stated | the form of involvement and its effect described | always | BB-05, SC-40, SC-41 |

Twenty nine questions is more than the plan's estimate of about 22, because the mapping added concerns the first draft lacked (C24 to C29). B25 and B26 concern the evaluation the benchmark authors report in their paper rather than the instrument itself; the author decided on 31 October 2026 to keep them in Part B as written. They apply only when the paper reports an evaluation of systems, and B26 is answered from extracted text, so figure quality is out of reach.

## Lineage

| Element | Source |
|---|---|
| Describe, then evaluate | EFPA Test Review Model, separation of description from evaluation |
| Part A vocabulary | OECD facets with consistent rater agreement (chapter 6) |
| Part B questions | the shared concerns in `../mapping/concerns.md`, one each |
| Anchors Stated, Shown, Checked | the distinction between a claim, an inspectable artefact and a documented check; wording informed by the items in the last column of the table |
| Insufficient evidence and Not applicable as null states | EFPA section 6.4 and the OECD allowance of N/A under uncertainty |
| Evidence record per judgment | the standard; the Scorecard's requirement of a justification per item |

## What this rubric does not claim

It covers every shared concern by construction, so coverage says nothing about it. It is not validated, and nobody has used it by hand. What the study measures is whether its ratings hold up when a person checks the cited sources, how often two repetitions agree, and whether items a benchmark does not report are recorded as insufficient evidence rather than as defects.
