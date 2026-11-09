# MESA rubric, version 5.1

Version 5.1 (identifier `mesa-rubric-v5.1`, 9 November 2026) corrects version 5 (`rubric.md`, `mesa-rubric-v5`), which stays frozen as the rubric of Study 3. It changes no question, level or field. It settles feedback item 15 from Paper 2 and three outcome calls, with the author's answers of 9 November 2026:

| Change | Where |
|---|---|
| The outcome describes the check on the tasks in scope after the listed task defects are left out; failed means a defect beyond the listed tasks | outcome field, task defects |
| B14a: a source that shows models reproduce the benchmark's test material makes the outcome failed, whatever models it names | rules for single questions |
| B14b: when every task predates the model's stated cutoff and no contamination check for that model exists, the outcome is not performed | rules for single questions |
| B28b: later history in a shipped environment that a search for the answer did not find answers in is recorded in the evidence; the outcome is passed with that limit | rules for single questions |

No Study 3 rating listed a task defect, cited a source showing exposure of models under B14a, or searched environment history under B28b, so the Study 3 records read the same under version 5.1.

The text below is version 5 with these changes.

Status of version 5: written 9 November 2026; the author confirmed the default answers at the end on 9 November 2026, before the Study 3 pilot. Derived from the frozen v4 rubric (`../../v4/rubric/rubric-draft.md`, identifier `mesa-rubric-v4`, frozen 31 October 2026) and from the gaps that implementing the traceability matrix in Paper 2 exposed (`../../mesa_paper_feedback_from_paper_2.md`, items 1 to 14). The v4 rubric, its study materials and its outputs are unchanged. Identifier when frozen: `mesa-rubric-v5`. The default answers at the end were confirmed by the author before `v5/study/freeze.py` ran.

## What changed from v4

| Change | Feedback item |
|---|---|
| Level names follow the paper: Claimed, Documented, Verified, Contradicted, Undocumented, Not applicable | 1 |
| Every Part B rating also records the check outcome, the scope, the kind of check, its detection limits and any task defects | 2, 3, 4, 5, 7 |
| Contradicted cites a location; Not applicable gives a reason and is refused where a question applies always | 12 |
| B05 covers tests that reject a correct solution; B07 covers tests and scoring code that accept a wrong one | 6 |
| B07 may reach Verified through an exploit check the reviewer runs | 9, 14 |
| B12 says what a sample size without an uncertainty measure earns | 10, 14 |
| B14 is split into B14a, the benchmark's safeguards, and B14b, exposure of one named model | 8 |
| B28 is split into B28a, the grading environment, and B28b, the agent environment | 11 |

Part B now has 31 questions; with the eight Part A facets the rubric has 39 criteria. Concern C14 gives B14a and B14b, concern C28 gives B28a and B28b, and every other concern C*nn* gives criterion B*nn*. C30 is the Part A description and has no B identifier. The 30 concerns and the item mapping of v4 are unchanged.

## Part A: description

Unchanged from v4: eight OECD facets, one value each, each with a source location and a short quote.

| Facet | Values | Decides |
|---|---|---|
| Purpose | research, conformity, other (say which) | |
| Judgeability | manual, automated, mixed | B07 applies only when automated or mixed |
| Reference | absolute, relative (say to what) | B09 applies in full only when relative |
| Containedness | fully contained, partial interference (say what), not contained (say what) | informs B28a and B28b; does not decide them |
| Objectivity | loose, customised, fully independent | |
| Autonomy | autonomous, coupled (say with what), component | |
| Progression | static, developmental | |
| Variation | fixed, altered, procedural | B20 applies in full only when altered or procedural, or when the sources record more than one release |

## Part B: evidence

### Levels

| Level | Meaning | v4 name |
|---|---|---|
| Claimed | the sources claim the concern is met but show nothing that can be inspected | Stated |
| Documented | the sources show an inspectable artefact or description that bears on the concern | Shown |
| Verified | a check was done, and its coverage, findings and limits are reported by the sources or recorded by the reviewer | Checked |
| Contradicted | the sources show a defect or a statement that contradicts the claim, at a cited location | Contradicted |
| Undocumented | the sources do not let the reviewer choose a level; not a defect | Insufficient evidence |
| Not applicable | the concern does not arise for this benchmark, for a reason taken from Part A or from the stated use | Not applicable |

Contradicted is the only negative level. A rating at Contradicted without a cited location is invalid. Not applicable is refused for every question whose "Applies when" column says "always"; elsewhere it needs a reason that cites the Part A value or the stated use.

No total score. A higher level is not a better benchmark: a benchmark whose authors report a thorough check that found many errors reaches Verified while disclosing more defects than a benchmark that reports no check.

### The rating record

Every Part B rating records:

| Field | Values | Meaning |
|---|---|---|
| level | one of the six levels | as above |
| reason | one or two sentences | why this level |
| evidence | source locations with short quotes | what the level rests on |
| missing | text | what the sources lack |
| checks performed | text | what the reviewer read or ran |
| outcome | passed, failed, not performed, not recorded | whether the check found a defect that bears on the criterion, on the tasks in scope after the listed task defects are left out; independent of the level, so a rating at Verified may have outcome failed |
| check kind | reported by the sources, run by the reviewer, both, none | who did the check behind the outcome |
| scope | release, configuration, task or subset, with identifiers | the part of the benchmark the rating covers (below) |
| detection limits | one sentence, "The check could not detect X" | what the check could miss; empty only when no check was performed |
| task defects | task identifier, direction, cited location and quote | single tasks whose tests are shown to be wrong (below) |
| rated by, signed by | name and kind of each rater (person, or model with its identifier and prompt) | recorded by the harness or the signer, not by the rater's own claim |

Scope levels. *Release*: the published benchmark at a named version. *Configuration*: the benchmark run with one model setup, harness and environment. *Task*: one named task. *Subset*: a named list of tasks. B14b is rated at configuration scope; B05 is often rated at task or subset scope; B07, B18, B20 and B28a are usually rated at release scope.

Task defects. A rating may list tasks whose tests are shown to be wrong, each with a cited location. Under B05 the direction is *rejects a correct solution* (or the reference answer is wrong); under B07 it is *accepts a wrong solution*. When the defect is shown by a patch that passes the tests while breaking behavior the task statement asks for, the patch must have been executed. A defect of the whole benchmark, such as a scorer that accepts every answer, is not listed per task; it makes the criterion Contradicted. The outcome describes the check on the tasks in scope after the listed task defects are left out. Failed means a defect that bears on the criterion beyond the listed tasks. When every defect found is listed per task, the outcome is passed for the remaining tasks.

### Questions

| Id | Question | What counts as Documented | What counts as Verified | Applies when | Source items that shaped the wording |
|---|---|---|---|---|---|
| B01 | Is the ability under test stated and made concrete? | a definition with scope and an operational form | the authors compare their definition with others or test its boundaries | always | BB-01, ECBD-Q3, SC-02, SC-03, H2B-04, ABC-R.5 |
| B02 | Are the intended use, users and real world relevance stated? | intended users and uses named | use cases or user input described | always | BB-03, BB-06, ECBD-Q1, ECBD-Q2, H2B-03 |
| B03 | Is the selection of tasks justified for the claimed ability? | a reason why these tasks are evidence; differences from related benchmarks | expert or empirical support for the selection | always | BB-07, BB-13, ECBD-Q4, ECBD-Q7, SC-24, SC-25, H2B-01 |
| B04 | Does the task set cover the ability, and is it representative? | the task space and its range described; sampling described | coverage verified against the documented task space | always | SC-06, SC-07, ECBD-Q12, ECBD-Q13, H2B-11, H2B-12, OECD-Coverage |
| B05 | Were tasks, reference answers and tests checked for errors that reject a correct solution? | the checking procedure described | coverage, findings and limits of the check reported | always | SC-58, SC-60, H2B-13, H2B-18, ABC-T.7, ABC-T.8, ABC-O.d.1 |
| B06 | Is the scoring rule described? | the metric and output validation method stated, including answer formats | edge cases stated: timeouts, partial answers, unexpected formats, refusals | always | BB-36, H2B-20, H2B-21, SC-65, ABC-O.h.1 |
| B07 | Was the scoring implementation checked, and can it accept a wrong solution? | the implementation can be read and compared with the rule | parser or judge validated, or exploit attempts reported or run by the reviewer, with every attempt and its limits recorded | Judgeability automated or mixed | BB-12, SC-64, SC-66, SC-67, SC-68, ABC-O.c.1, ABC-O.i.1, H2B-22 |
| B08 | Are aggregation and subscores justified? | how scores are combined is stated | a reason for the combination, or facets reported separately | more than one score or subscore exists | SC-04, SC-18, SC-19, ECBD-Q18, ECBD-Q19 |
| B09 | Are the comparison points justified? | human, random or trivial baselines reported | the baseline procedure described well enough to judge the comparison | always; in full when Reference is relative | BB-10, BB-11, SC-55, SC-56, ABC-R.12, ABC-R.13 |
| B10 | Is variation on repeated testing reported? | repeated runs or an estimate of variation reported | the design of the repetition and its result stated | always | SC-48, H2B-33, H2B-38, OECD-Reliability |
| B11 | Are prompting and setup described, and is their effect tested? | prompts and adaptation method given | sensitivity to prompt wording or setup measured | always | ECBD-Q9, BB-14, SC-31, H2B-26, H2B-28, H2B-29 |
| B12 | Are uncertainty and statistical support reported for the benchmark's own scores? | sample size and an uncertainty measure (interval, standard error or spread over runs) for primary scores | power or significance reasoning given | always | BB-22, SC-14, SC-15, ABC-R.10 |
| B13 | Were shortcuts, confounds and chance investigated? | the possibility named and discussed | an analysis of confounds, guessing or error modes reported | always | SC-21, SC-28, SC-29, SC-38, ABC-O.b.3, ABC-O.h.2, OECD-Specificity |
| B14a | Does the benchmark guard against exposure of its test material in training data? | the risk acknowledged; a safeguard described, such as hidden tests, dated tasks or a private split | a contamination check or held out procedure reported | always | BB-19, BB-20, SC-35, H2B-08, ABC-R.3 |
| B14b | Could the test material be in the training data of the named model configuration? | the model's stated training cutoff and the task creation dates recorded with their sources | a contamination check for that model reported, or tasks created after its stated cutoff used as a held out set | a model configuration is named for the review | BB-19, BB-20, SC-35, H2B-08, ABC-R.3 |
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
| B28a | Is the grading environment controlled, so that the system under test cannot reach answers or alter the scoring? | the grading environment and its isolation described | isolation of the system's output from the tests and the scorer verified or enforced in code | scoring runs the system's output as code or in an environment | ABC-T.4, ABC-T.5, SC-37, SC-34, OECD-Containedness |
| B28b | Is the agent environment controlled and isolated from answers? | the environment, its tools and its isolation described | state clearing and isolation from answers, history and network verified or enforced in code | the benchmark runs systems in an environment with tools or state | ABC-T.4, ABC-T.5, SC-37, SC-34, OECD-Containedness |
| B29 | Did domain experts or users take part in design or review? | involvement stated | the form of involvement and its effect described | always | BB-05, SC-40, SC-41 |

### Rules for single questions

- **B05 and B07.** A test that rejects a correct solution, or a wrong reference answer, belongs to B05. A test or scoring code that accepts a wrong solution belongs to B07. A test that is too narrow is a B05 matter; a test that is too wide is a B07 matter.
- **B07 exploit check.** An exploit check run by the reviewer counts as a check for Verified when it records: the attempts (patches or answers meant to pass the scoring while breaking behavior the task statement asks for), an independent test that shows each attempt is wrong and that accepts the reference solution, every attempt with its result, and its limits. An exploit counts only when it breaks behavior the task statement asks for, not behavior inferred from the reference fix alone. Failing to find an exploit does not show that none exists.
- **B12.** B12 concerns the scores the benchmark itself reports. A sample size without an uncertainty measure does not reach Documented; the rating is Undocumented and `missing` names the uncertainty measure. When a team computes its own interval for a decision, the number of observations used in that decision limits the decision, whatever B12 says.
- **B14a.** A source that shows models reproduce the benchmark's test material, such as reference answers or fixes, makes the outcome failed, whatever models it names, and the record cites it.
- **B14b.** Tasks created after a model's stated training cutoff count as a held out check for that model, with the source of the cutoff recorded. A stated cutoff is a claim by the provider, not a verified fact, and the detection limits say so. When every task was created before the stated cutoff and no contamination check for that model exists, no check is possible: the outcome is not performed, and exposure is possible but not shown. The outcome is failed when a source shows that this model reproduces the test material.
- **B28a and B28b.** Containedness informs both but decides neither. The environment a team uses for its own sessions is not part of the benchmark; it belongs to the requirement record.
- **B28b history.** When a shipped environment holds history beyond the task's starting state, such as later commits, and a search of it does not find the answer, the history is recorded in the evidence and the outcome is passed; the detection limits say what the search could not find, such as a reworded fix or hints short of the answer. The outcome is failed when the answer, or content that reveals it, is found at a cited location.

## Default answers to the open questions (confirmed by the author, 9 November 2026)

| Item | Question in the feedback file | Default |
|---|---|---|
| 1 | Name of the qualifier | *unreported* ($-r$) (decided 9 November 2026) |
| 1 | Change the frozen rubric or freeze a new one | freeze this file as `mesa-rubric-v5`; v4 stays as frozen (decided) |
| 1 | C30 as the only concern without a B identifier | yes |
| 2 | Does outcome failed imply Contradicted | no; a failed outcome makes a criterion inadmissible only with a cited location of the defect, otherwise it requires inquiry |
| 2 | Who decides pass or fail when sources report findings without a verdict | the rater, with a reason; if the rater cannot tell, outcome not recorded |
| 3 | May a narrower scope support a larger task set | no; the requirement narrows its task set instead |
| 3 | Scope as a field or derived | a field |
| 4 | Bias from removing tasks | the score is reported with and without the removed tasks; the removal is fixed before any model score is seen |
| 4 | Smallest remaining task set | the minimum number of observations stated in the requirement; below it the evidence requires inquiry |
| 4 | Who may list a task | any rating, with a cited location and, when shown by a patch, an executed patch |
| 5 | Does a later audit lower an earlier rating | no; it is added to the detection limits and the rating is marked |
| 5 | Who judges whether limits are acceptable | the requirements engineer, in the requirement |
| 6 | B15 in the scoring inference | no; B15 moves to the extrapolation inference beside B14a and B14b |
| 6 | Too narrow and too wide tests | too narrow under B05, too wide under B07 |
| 7 | May a model sign | a model may draft; the record names who signed, and the requirement states whether a person must sign |
| 7 | Second person for safety relevant criteria | the requirement may demand it; the standard does not |
| 8 | B14b in Part B | yes, at configuration scope (decided: split into new identifiers) |
| 8 | Storing a rating that exists once per model | one rating per named configuration, with that configuration as its scope |
| 9 | Model written exploit attempts | allowed when every attempt is recorded; a person may review them, and the record says whether one did |
| 9 | Minimum number of attempts | none in the standard; the requirement may set one |
| 10 | B12 in the mandatory profile when the team computes its own interval | the requirement decides |
| 10 | Minimum number of observations | a property of the requirement |
| 11 | Split for the rubric or only for traceability | in the rubric (decided) |
| 11 | Which "applies when" wording | the rubric's wording, as in the table above |
| 12 | Is a Part A gate enough reason for Not applicable | yes, when the rating cites the Part A value |
| 12 | What the companion work promises | the step from source tasks to the target requirement, argued in a transfer justification; "semantic task matching" is dropped |
| 13 | Paper 2's verdict names | MESA uses evidence status (Inadmissible, Inquiry Required, Admissible) and decision (Accept, Reject, Inconclusive); Paper 2 maps its names to these |
| 13 | Rename Conditional Query | yes, to Inquiry Required |
| 14 | Must a person check a model's ratings | the standard does not require it; the record names the rater, the model and the prompt, and who signed |

## Lineage

| Element | Source |
|---|---|
| Describe, then evaluate | EFPA Test Review Model, separation of description from evaluation |
| Part A vocabulary | OECD facets with consistent rater agreement (chapter 6) |
| Part B questions | the shared concerns in `../../v4/mapping/concerns.md`; C14 and C28 each give two questions |
| Levels Claimed, Documented, Verified | the distinction between a claim, an inspectable artefact and a documented check (v4 Stated, Shown, Checked) |
| Undocumented and Not applicable as null states | EFPA section 6.4 and the OECD allowance of N/A under uncertainty |
| Outcome, scope, check kind, detection limits, task defects, rater | gaps found when Paper 2 implemented the traceability matrix |
| Evidence record per judgment | the standard; the Scorecard's requirement of a justification per item |

## What this rubric does not claim

It covers every shared concern by construction, so coverage says nothing about it. It is not validated against a person, and nobody has used it by hand. Study 3 measures whether its ratings repeat across two sessions, whether the new fields repeat, and whether its ratings hold up when the cited sources are checked. Its sessions read files and cannot execute code, so a check "run by the reviewer" in Study 3 is an inspection, and B07 exploit attempts are not part of it.

## Answers to feedback item 15 (confirmed by the author, 9 November 2026)

| Question | Answer |
|---|---|
| Does a check that finds broken tests on listed tasks record outcome failed | no; the outcome describes the remaining tasks, and failed means a defect beyond the listed tasks |
| B14b when every task predates the model's stated cutoff | outcome not performed; failed only when a source shows this model reproduces the test material |
| B14a when a source shows other models reproduce the test material | outcome failed |
| B28b when a shipped image holds later commits and a search found no fix in them | outcome passed, with the commits in the evidence and the limits of the search stated |
| New version or correction note | this file, `mesa-rubric-v5.1`; `rubric.md` stays frozen as `mesa-rubric-v5` for Study 3 |
