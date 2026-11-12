# REFSQ 2027 research track: review of submission "What a Benchmark Audit Lets a Team Conclude: MESA Applied to a Coding Agent Requirement on SymPy"

Category claimed: scientific evaluation paper (15 pages). Length: 13 pages with references.

## 1. Summary of the paper

The paper asks what a team may conclude about a coding agent from a benchmark score. The requirement is stated for one tooling lead: the agent fixes SymPy bug reports, without network access and without editing the test runner, within 900 seconds. The team accepts the agent if the one sided 95% exact lower bound of the resolve rate is at least 0.70. The authors run one agent (GPT-6.1 Sol) once on 44 SWE-bench Verified SymPy tasks ("source") and on 44 SymPy issues fixed after the model's training cutoff ("target"). Before the sessions they check whether the tests accept incomplete patches, whether the model may have seen the tasks, and whether edits to the test runner alone pass the grading. They rate the benchmark with the MESA rubric from a companion paper under review. They then compare seven decision methods on the source sessions: score alone, defect removal alone, the Agentic Benchmark Checklist with and without a gate, and three MESA policies (strict, lenient, controlled). The MESA method has three ordered levels: records intact, evidence admissible, then the statistical rule. The agent resolves 35 of 44 source tasks. Score alone gives Inconclusive. The tests accept a wrong fix on 32 of 44 source tasks, and 11 runner only patches all pass the grading. The strict and lenient policies give no decision. The controlled policy checks each patch, keeps 12 tasks, and gives Inconclusive at 10 of 12. No method reaches Accept. On the target tasks the agent resolves 21 of 44, and the direct test gives Reject. Four sessions broke a rule; none changes a decision.

## 2. Strengths

1. The topic fits the REFSQ 2027 special theme. It treats a benchmark score as evidence for a requirement and asks what a requirements engineer may conclude from it.
2. The requirement and the decision rule are stated in full before the data. The paper gives the cut points and the chance of Accept at 44 and 12 tasks. This lets a reader see in advance that 12 kept tasks can only give Accept at 12 of 12.
3. Every number I could recompute is correct (Section 5 below). Counts add up across Table 1, Table 3, Table 4 and the text.
4. The direct test on issues fixed after the training cutoff is a sound design idea. It gives the team a second line of evidence that does not depend on the benchmark.
5. The grading control check (11 runner only patches, all graded as resolved) is a concrete and easy to repeat finding with direct value for practice.
6. The RQ3 analysis is honest. It reports a session where the rule against runner edits caught a real fix, and it draws a requirements lesson from it (Section 6, last paragraph).
7. The prose is mostly short and plain. The Limitations section names the main threats.
8. The Data Availability Statement lists the content of the package, the licenses and what is left out and why.

## 3. Weaknesses

**W1. The central count rests on language model judgments that no human checked.**
Where: Section 4.3 (weak test check, scope judgment), Table 1, abstract, Section 8.
Why it matters: "The tests accepted a wrong fix on 32 of 44 source tasks" (73%) drives the whole paper. It sets the kept set to 12 tasks, it sets the "weak tests" rating, and it is the basis of the claim that removal "leaves too few tasks to accept". The incomplete patches come from the model under test. The check scripts come from a second model. The decision whether the issue states the missed behavior comes from a third model. No step was checked by a person. The rate of 73% is far above what the cited audits report for SWE-bench Verified (the paper does not give their rates or discuss the gap). Agreement between two runs of the same model (kappa 0.88) does not show that the judgments are right. My recomputation also shows that a kappa of 0.88 at 81 of 82 agreements requires that only about 5 of 82 tasks got a "does not state" label from either run; the judge almost always says "states it", so the scope step filters very little (2 of 58 tasks).
How to fix: With no new data: report the rates of the cited audits next to 32 of 44 and explain the gap; state in the abstract and the conclusion that the count comes from model judgments; give one worked example of an accepted wrong fix. With new work: have a person check a sample of the 58 findings.
Decides recommendation: yes.

**W2. The study cannot show that the method changes a team's decision.**
Where: Section 5.1, Section 5.2, Section 6, abstract (Contribution).
Why it matters: Score alone already gives Inconclusive. So the audit moves the result from "Inconclusive" to "no decision" or keeps it at Inconclusive. The study has no case where a method without the audit reaches a wrong Accept that the MESA method stops. RQ2 ends with "the source and target decisions cannot be compared as agreeing or disagreeing", so RQ2 has no answer. The controlled policy gives the same 10 of 12 and the same decision as "defect removal alone", so the added value of the MESA levels over simple removal is not shown by the data. The grading control finding comes from the authors' own check, which any method could use.
How to fix: With no new data: state plainly what a team does differently after "no decision" versus "Inconclusive" (Section 6 starts this). Rephrase the contribution as a demonstration on one case. Add a short analysis on the existing records, for example at what source score each method would have accepted (score alone accepts at 37 of 44; the controlled policy can never accept below 12 of 12), to show where the methods would diverge. Say explicitly that controlled policy and defect removal alone agree here.
Decides recommendation: yes.

**W3. A requirements engineer who has not read the MESA paper cannot follow Sections 3 and 4.4.**
Where: Sections 1, 3, 4.4, Table 2.
Why it matters: MESA is never expanded. The seven review frameworks are not named (Section 2 names five). The "five concerns behind the seven criteria" are never given. "Record of origin", "inquiry", "admissible", "policy", "digital fingerprint" are not explained in plain terms. The word "level" means two things: the evidence level of a rating (Verified, Documented, ...) and the three steps of the method (level 1 to 3). The word "Verified" also means two things: SWE-bench Verified and the MESA level. The criteria have short names in the text (task correctness, weak tests, grading control, isolation) and long names in Table 2, and the paper never maps one to the other. The only definition of MESA is in a paper under review that a reader cannot access.
How to fix: Expand MESA once. Rename the method's three levels as "steps" or "gates". Add a short name column to Table 2. Give the five concerns. Add two sentences on each of "record of origin" and "inquiry". Name the seven frameworks or drop the number.
Decides recommendation: partly. It lowers clarity a lot, but it can be fixed with edits.

**W4. Table 2 rates "weak tests" as Verified / passed although half of the kept source tasks were never checked.**
Where: Section 4.4, Table 2 row 2, and Section 4.3 ("6 had no valid check").
Why it matters: The text says that 6 of the 12 kept source tasks had no valid check script. A rating of "passed" for the kept tasks claims more than was found. Under the paper's own outcomes, "not performed" is the honest outcome for those 6 tasks, and since this criterion is required by all three policies, the controlled policy might then give no decision. The same pattern holds for "task correctness": a failed check turns into "passed" once the one defective task is listed. A reader needs to know if this is a MESA rule or a choice of the authors.
How to fix: State the rule that turns a failed check into a passed one after defective tasks are listed. Report the outcome for the 6 unchecked kept tasks and say how the controlled policy would decide if they count as "not performed".
Decides recommendation: yes, together with W1.

**W5. Table 2 criteria mix positive and negative wording, so "passed" is hard to read.**
Where: Table 2 rows 2 and 5.
Why it matters: "The tests can accept a wrong fix: Verified / passed" and "The test material could be in the training data of this model: Verified / passed" read as if the risk was confirmed. Row 6 is worded the other way ("The agent cannot alter the grading"). Row 5 also seems to be rated on the target tasks (text after Table 2), while the table describes the benchmark that holds the source tasks.
How to fix: Word every criterion as a property that passes, for example "The tests reject a wrong fix". Say which task set row 5 is rated on.
Decides recommendation: no.

**W6. Table 3 prints a score for the strict and lenient policies, against the method's own rule.**
Where: Table 3 rows "Strict policy" and "Lenient policy"; Section 3 says tasks are removed and the score computed only if the evidence is admissible.
Why it matters: A reader sees 10/12 and bounds for methods that, by definition, never compute a score.
How to fix: Replace these cells with a dash and a footnote.
Decides recommendation: no.

**W7. The "direct test" on the target tasks uses the same weak grading.**
Where: Sections 4.3, 5.2, 6.
Why it matters: The tests accepted a wrong fix on 26 of 44 target tasks, and the runner gap applies to them too (one target session edited the runner). The paper calls the target result "a direct test of the requirement" without this caveat. The Reject is still robust, because weak tests can only raise the resolve rate, but the paper should say so. The 31.8 point drop also has more than one cause (exposure, difficulty, time of creation), which Section 7 notes only briefly; the exact file set probe (30 of 44 versus 13 of 44; difference 38.6 points, Newcombe 95% interval 17.8 to 55.1, my computation) is stronger evidence than the "at least one file" probe and is not given an interval.
How to fix: Add one or two sentences on why weak tests do not threaten a Reject. Report the interval for the exact file set difference.
Decides recommendation: no.

**W8. Design details for an empirical study with language models are missing.**
Where: Section 4.1, 4.3, 4.4.
Why it matters: The call points to the ACM SIGSOFT Empirical Standards and the LLM guidelines. The paper gives no prompts, no sampling settings, no model dates or versions for the checker models, one run per task without a note on variation, and no reason why 44 of the 75 SymPy tasks were used (with 75 tasks the "too few tasks" claim could be tested). The research method is not named (case study, experiment). Check results are reported in the design section (Section 4.3 and 4.4) instead of the results section.
How to fix: Name the method. Add a short table of model settings or point to the exact package files. Give the reason for 44 of 75. Move check results to Section 5 or label them clearly.
Decides recommendation: partly (soundness).

**W9. The requirement and its stakeholder are assumed, not elicited.**
Where: Section 3.
Why it matters: For an RE venue, the threshold 0.70, the 900 seconds and the tooling lead are choices without a source. Also, the requirement is worded as "passing the maintainers' tests for the behavior that the report states". Read literally, a wrong fix that passes weak tests meets this wording. The paper should explain how it reads the requirement so that weak tests count against it.
How to fix: Two or three sentences on where the threshold comes from and how the requirement is meant to be read.
Decides recommendation: no.

**W10. Figure 1 does not show the direct test path.**
Where: Figure 1, page 4.
Why it matters: The figure sends all tasks through the checks into the decision method. It does not show that the target tasks get the statistical rule directly (Section 4.5). It also does not show that level 1 can reject the input. A reader cannot see from the figure how RQ2 is answered.
How to fix: Add a branch "target tasks: statistical rule only" and label the arrow from level 1 "rejected".
Decides recommendation: no.

## 4. Questions to the authors

1. What does a team do differently after "no decision" than after "Inconclusive"? Who runs the "inquiry", and what ends it?
2. Is turning a failed check into "passed" after listing defective tasks a rule of MESA or a choice in this study? How would the controlled policy decide if the 6 unchecked kept source tasks counted as "not performed"?
3. Why 44 of the 75 SymPy tasks? How many kept tasks would you expect from all 75 at the same removal rate, and could they reach Accept at 0.70?
4. How does your 73% rate of accepted wrong fixes compare with UTBoost [34] and Wang et al. [32] on the same tasks? Did any of your 32 tasks appear in their lists?
5. In the scope judgment, how is "unclear" mapped to the yes or no "deciding question" used for kappa?
6. Of the 82 tasks, how many got "does not state" from each Claude run? My computation suggests about 5.
7. The requirement already forbids runner edits in the team's own sessions, and RQ3 enforces it. Why should a benchmark level failure on grading control block the decision when the team checks each session anyway? Is the controlled policy not the only sensible policy here?
8. Which task set is the criterion "The test material could be in the training data of this model" rated on?
9. In the replay (Section 4.6 and 5.1), what is a "case"? The decision is made on the set of 44 tasks, so why does the replay report 44 decisions?
10. When level 1 "rejects the input", is that the result "no decision", or a fifth result?
11. What are the "four layouts of SymPy's test runner"?
12. How does your method differ from the fail closed release gate in [20] and the assurance envelopes in [9]?

## 5. Checks I made

I recomputed every number I could with Python (scipy). Bounds are exact Clopper Pearson one sided 95% bounds. Differences use the Newcombe hybrid score interval (Wilson, 95%).

| Item | Paper | My result | Agree |
|---|---|---|---|
| 35/44 rate, bounds | 79.5; 67.0, 88.9 | 79.5; 67.0, 88.9 | yes |
| 10/12 rate, bounds | 83.3; 56.2, 97.0 | 83.3; 56.2, 97.0 | yes |
| 21/44 rate, bounds | 47.7; 34.6, 61.1 | 47.7; 34.6, 61.1 | yes |
| 23/44 rate, bounds | 52.3; 38.9, 65.4 | 52.3; 38.9, 65.4 | yes |
| 7/20 rate, bounds | 35.0; 17.7, 55.8 | 35.0; 17.7, 55.8 | yes |
| 5/18 (Table 4) | 27.8%, Reject | 27.8%, upper 49.8, Reject | yes |
| Fewest tasks for any Accept | 9, at 9 of 9 | 9 (8 of 8 gives lower bound 68.8) | yes |
| Cut points n=44 | Accept 37, Reject ≤25 | 37; 25 (26 gives upper 71.6) | yes |
| Cut points n=20 | 18; 10 | 18; 10 | yes |
| Cut points n=12 | 12; 5 | 12; 5 | yes |
| P(Accept), p=0.85, n=44 | 66.3% | 66.3% | yes |
| P(Accept), p=0.85, n=12 | 14.2% | 14.2% | yes |
| P(Accept), p=0.75, n=12 | 3.2% | 3.2% | yes |
| Exposure 37/44, 40/44 | 84.1, 90.9 | 84.1, 90.9 | yes |
| Difference, Newcombe | −6.8 (−21.4, +7.7) | −6.8 (−21.4, +7.7) | yes |
| Exact set 30/44, 13/44 | 68.2, 29.5 | 68.2, 29.5 | yes |
| 35/44 vs 21/44 | 31.8 (11.7, 48.6) | 31.8 (11.7, 48.6) | yes |
| 10/12 vs 7/20 | 48.3 (12.8, 69.0) | 48.3 (12.8, 69.0) | yes |
| 10/12 vs 5/18 | 55.6 | 55.6 (19.2, 75.0) | yes |
| Checklist 6/8, 1/3, 0/4 | 0.75, 0.33, 0.00 | 0.75, 0.33, 0.00 | yes |
| Checklist sums | 15 apply = 7+6+2; 8 caveats | 7+6+2=15; 6+1+0=7 met; 8+3+4=15; 15−7=8 | yes |
| Kappa 0.88 at 81/82 | 0.88 | feasible only with about 4 to 5 minority labels | yes, see W1 |
| Kappa 0.57 (77/82 labels) | 0.57 | feasible with 78/82 binary agreement | yes |
| Kappa 0.41 (76/82 labels) | 0.41 | feasible with 77/82 binary agreement | yes |

Count consistency:

- Table 1 source: 32+6+6+0 = 44. Target: 26+6+10+2 = 44. Totals 58, 12, 16, 2 = 88. Removed 32+24 = 56, kept 12+20 = 32. All agree.
- Kept target tasks: 6+2+10+2 = 20. Kept source: 6+6 = 12. Agree with text.
- Removed target 24 = 26 − 2 judged out of scope. Agrees.
- Removed plus kept resolved: source 25+10 = 35; target 14+7 = 21. Agree with Table 3.
- Table 4 middle row: removing all 26 target tasks with an accepted wrong fix leaves 18; 5 of 18 means both out of scope tasks were resolved (7−5 = 2). Consistent.
- Scope judgment: 82 = 42+40; the other 6 = 2 source + 4 target. The 2 target tasks with no incomplete patch fit among them. The text does not say what the other 2 target and 2 source tasks were (patches with no recorded behavior?). Small gap.
- RQ3: 4 rule breaking sessions; 2 passed the tests (both target), so target tests only 23 and valid 21. The only source rule breaker failed, so source tests only equals valid, 35. Consistent.
- RQ1 counts: 4 Inconclusive (score alone, defect removal, controlled, checklist) and 3 no decision (strict, lenient, gate). Agree with Table 3 and Section 8.
- Table 2 "Required by" and "Blocks" agree with Section 4.5 and 5.1 (strict blocked on 3 criteria, lenient on 1).
- Session times are all under 900 seconds (max 469). Agrees.

No number disagrees. Inconsistencies of meaning (not arithmetic): Table 3 prints scores for strict and lenient (W6); "weak tests" rated passed with 6 unchecked kept tasks (W4); order of methods in Table 3 differs from Section 4.5.

I did not check the references against outside sources, because the task limits me to the three files. Several cited works are 2026 preprints; the authors should make sure each one exists as cited.

## 6. Terms, claims and wording

Terms used before they are defined, or never defined:

- MESA: never expanded.
- "SWE-bench Verified", "resolve", "resolved": used in the abstract and Section 1; defined in Section 2.
- "source tasks" and "target tasks": the names suggest transfer but the reason is never given.
- "training cutoff", "exposure in training": used in the abstract; not explained for a reader outside machine learning.
- "seven review frameworks" (Section 1): never named.
- "five concerns behind the seven criteria" (Section 4.4): never given.
- "Agentic Benchmark Checklist" items, "mapped items": total number of items and the mapping are not given.
- "record of origin", "inquiry", "digital fingerprint", "admissible", "policy": Section 3, explained only in passing or not at all.
- "level": two meanings (evidence level of a rating; step of the method).
- "Verified": two meanings (benchmark name; MESA level).
- "task correctness", "weak tests", "grading control", "isolation": short names used in Sections 4.4 to 5.1 but not in Table 2.
- "Undocumented": defined as "the sources do not allow a level to be chosen", but the text states as a fact that the benchmark reports no uncertainty. That reads as a known failure, not as "cannot choose".
- "harness", "test runner", "test configuration files", "four layouts of SymPy's test runner", "named tests": not explained.
- "Codex command line agent", "medium reasoning effort": not explained.
- "the deciding question" (Section 4.3): introduced without a definition.
- "case" in the replay (Section 4.6, 5.1): not defined.
- Cohen's kappa and Newcombe interval: named without one line on what they show.

Claims that go further than the evidence:

- Abstract and Section 8: "removing tasks with weak tests leaves too few tasks to accept". With 12 tasks, Accept is possible at 12 of 12. Say "leaves 12 tasks, so Accept needs all 12".
- Abstract, Contribution: "We show that a decision method ... changes what a score can support". One agent, one repository, one run, and the decision stays Inconclusive under the controlled policy. Say "In one case, we show ...".
- Section 4.3: "On this benchmark, an agent can therefore pass the grading by editing the test runner alone." Shown for 11 patches on SymPy tasks only. Say "on the SymPy tasks of this benchmark".
- Section 6: "A team that needs a decision at a threshold of 0.70 therefore needs more tasks than a benchmark subset for one repository supplies after such removal." Only 44 of 75 SymPy tasks were used; the claim is not tested.
- Section 6: "The MESA policies show why more data from the same benchmark would not help". This holds for the strict and lenient policies by construction, not as a finding; under the controlled policy more tasks would help.
- Section 4.3: "The scope judgments agreed well within one model family". Agreement of two runs of one model shows stability, not correctness.
- Section 1: "SWE-bench Verified ... is a widely used benchmark for this purpose" (team acceptance decisions). No source for "for this purpose".
- Table 2: "Weak tests: Verified / passed" for kept tasks that include 6 unchecked tasks (W4).
- Section 6 calls the target result "a direct test of the requirement" without noting that its tests are also weak (W7).

Places where the wording is not plain:

- "a rating whose record of origin is missing leads to an inquiry" (Section 3). Suggest: "if we cannot tell who made a rating and from which sources, the method stops and asks for that information".
- "each patch and log still matches the digital fingerprint taken when it was made". Suggest: "the hash stored when the file was made still matches".
- "The test material could be in the training data of this model: Verified / passed" (Table 2). Mixed polarity (W5).
- "Two target tasks where a wrong fix was accepted stayed, because both Claude runs judged that the issue does not state the behavior." Clear, but it is split across a page and a table; keep it together.
- "the controlled policy is the lenient policy, plus a check of each session's patch that replaces the benchmark level rating on grading control". Long; split into two sentences.
- "Accept, Reject, Inconclusive, or no decision" versus "the input is rejected" at level 1: "Reject" and "rejected" mean different things. Use "the records are refused" for level 1.

## 7. Rule checks against the call

- Page limit: 13 pages with references, under 15 for scientific evaluation papers. Pass. The PDF page size is US Letter; the text block looks like LNCS. Pass, but the authors should confirm they used the unchanged LNCS class.
- Abstract structure: four paragraphs with the four required labels. Keywords follow. The Contribution paragraph gives the added value but no limitation, while the call asks for "added value and limitations of the results". Partial; must fix.
- Anonymity: no names, affiliations or acknowledgments; PDF metadata has no author. The companion paper is cited as "Anonymous, A. ... companion paper under review", as the call asks. The replication link is a placeholder ("zenodo.XXXXXXX"). Pass. Note: the paper depends on a companion that reviewers cannot read, so it should stand alone (W3).
- Data Availability Statement: present, at the end, with content, licenses and justified exclusions. Pass. The package is not reachable for review; an anonymous review link would let reviewers check the claims and is rewarded by the call.
- Category fit: scientific evaluation fits (the paper evaluates a decision method on a case). The paper does not name its research method from the Empirical Standards (W8).
- Generative AI: the study uses language models as checkers and judges. The call recommends the LLM guidelines; model settings, prompts and human validation are not reported (W1, W8).
- Hallucinated references: not checked against outside sources (outside my allowed files).

## 8. Scores (1 to 5)

- Relevance to requirements engineering: 4. It treats a benchmark score as evidence for a stated requirement and fits the special theme; the requirement and stakeholder are assumed, not elicited.
- Soundness: 2. The arithmetic is correct, but the central count of weak tests rests on model judgments with no human check, one rating claims more than was checked, and the design cannot show a changed decision.
- Novelty: 3. The ordered gate on records, evidence and score is new for benchmark use in RE, but its difference from release gates and assurance envelopes is not stated and its definition sits in an unseen companion paper.
- Clarity: 3. Sentences are short and numbers agree, but key terms are undefined or have two meanings, and Table 2 is hard to read without the companion paper.
- Reproducibility: 3. The described package is complete on paper, but it is not reachable for review, and prompts and model settings are absent from the paper.

## 9. Recommendation

**Weak reject.**

What decides it: W1, W2 and W4. The main finding (32 of 44 tests accept a wrong fix) rests only on language model judgments, and the rating built on it reports "passed" for tasks that were never checked. Even taken at face value, the result does not show the method changing a decision: score alone, defect removal and the controlled policy all give Inconclusive, and RQ2 has no answer. Clarity issues (W3) make the paper hard to follow for an RE reader who has not seen MESA.

What would move it to weak accept: a human check of a sample of the weak test findings (new work), or, with no new data, a reframing of the contribution as a worked demonstration on one case, an honest outcome for the unchecked kept tasks, an analysis of where the methods would diverge, and the clarity fixes in the table below.

## 10. Improvements that need no new experiment or data

| # | Improvement | Must or should | Size |
|---|---|---|---|
| 1 | Add a limitation sentence to the Contribution paragraph of the abstract (one agent, one repository, model judgments). | must fix | small edit |
| 2 | Expand MESA at first use. | must fix | small edit |
| 3 | Replace "too few tasks to accept" with "12 tasks remain, so Accept needs all 12" (abstract, Section 8). | must fix | small edit |
| 4 | Limit "On this benchmark, an agent can pass the grading" to the SymPy tasks (Section 4.3). | must fix | small edit |
| 5 | In Table 3, replace the score cells of the strict and lenient policies with a dash and a footnote. | must fix | small edit |
| 6 | State in Section 4.4 the rule that turns a failed check into "passed" after defective tasks are listed, and report the outcome for the 6 unchecked kept source tasks. | must fix | small edit |
| 7 | Say in the abstract and Section 4.3 that the weak test count comes from model judgments not checked by a person. | must fix | small edit |
| 8 | Add a short name column to Table 2 (task correctness, weak tests, exposure guard, model exposure, uncertainty, grading control, isolation) and word every criterion so that "passed" means good. Say which task set row 5 is rated on. | must fix | small edit |
| 9 | Rename the three method levels as "steps" (or similar) so "level" keeps one meaning; say which "Verified" is meant where both appear. | must fix | larger change (many places) |
| 10 | Explain "record of origin", "inquiry", "admissible" and "digital fingerprint" in plain words (Section 3). | must fix | small edit |
| 11 | Say what a team does after "no decision" versus "Inconclusive" (Section 6). | must fix | small edit |
| 12 | Say that the controlled policy and defect removal alone give the same result here, and what the levels add beyond removal. | must fix | small edit |
| 13 | Reframe the contribution claim as a demonstration on one case (abstract, Section 1, Section 8). | must fix | small edit |
| 14 | Add an analysis, from existing numbers, of the source score at which each method would accept (score alone at 37 of 44; controlled only at 12 of 12). | should fix | small edit |
| 15 | Report the cited audits' rates of weak tests next to 32 of 44 and discuss the gap. | should fix | larger change (a paragraph) |
| 16 | Give one worked example of an accepted wrong fix for a reader new to SWE-bench. | should fix | larger change (a paragraph or small box) |
| 17 | Name the seven review frameworks and the five concerns, or drop the numbers. | should fix | small edit |
| 18 | Note that weak tests on the target tasks can only raise the resolve rate, so Reject is robust. | should fix | small edit |
| 19 | Give the Newcombe interval for the exact file set difference (38.6 points, 17.8 to 55.1). | should fix | small edit |
| 20 | Explain how "unclear" maps to the binary question for kappa, and give the number of "does not state" labels. | should fix | small edit |
| 21 | Give the reason for using 44 of the 75 SymPy tasks. | should fix | small edit |
| 22 | Explain where the threshold 0.70 comes from and how the requirement's wording rules out a wrong fix that passes weak tests. | should fix | small edit |
| 23 | Define "case" in the replay and say whether level 1 refusal counts as "no decision"; use a word other than "rejected" there. | should fix | small edit |
| 24 | Add the direct test path for target tasks and the level 1 refusal to Figure 1. | should fix | small edit |
| 25 | Name the research method (Empirical Standards) and list model settings and prompts or point to the package files. | should fix | larger change |
| 26 | Move the results of the checks (end of 4.3, 4.4) to Section 5, or label them as results. | should fix | larger change |
| 27 | Order Table 3 rows as in Section 4.5. | should fix | small edit |
| 28 | Provide an anonymous link to the package for review. | should fix | small edit |
| 29 | Define harness, test runner, named tests and the four runner layouts in one or two sentences. | should fix | small edit |

---

## Comparison with round 3 (added by the revising session, not by the blind reviewer)

The text above is the blind review, unchanged. It read the paper before the last set of small fixes.

Scores, round 3 then round 4: relevance 3 and 4, soundness 2 and 2, novelty 3 and 3, clarity 2 and 3, reproducibility 2 and 3. Recommendation: weak reject both times.

| Round 3 weakness | Status | Note |
|---|---|---|
| The title question cannot be answered; no method reaches Accept | Reduced | Title, abstract and RQ1 now state what each method lets a team conclude. Round 4 W2 still notes that the study does not show a changed decision. |
| The drop from source to target has other explanations | Reduced | "Overstates capability" is gone. The Limitations section says the target tasks may be harder. |
| Only models labelled the weak tests; kept tasks called "clean" | Still open | The counts of checked and unchecked kept tasks are now in the paper. No human check exists; it is named as a next step. Round 4 W1. |
| Not self contained: codes and terms undefined | Fixed for codes, reduced for terms | No codes remain. A section explains the method. Round 4 still asked for a few terms, which are now explained. |
| Interval labels, mixed counts, 79.6% | Fixed | See the change log. |
| Citations that do not support their sentence | Fixed | See the references check. |
| Companion work in the first person; "the author" | Fixed | |
| Placeholder link | Still open | Needs the upload. |

Round 4 points fixed after the review: MESA spelled out; the method's three "levels" are now "steps", so "level" means only the level of a rating; Table 2 has short criterion names worded so that "passed" is the good result; Table 3 shows no score for the two policies that stop before the score; the rule that lists defective tasks and rates the rest as passed is stated; "record of origin", "inquiry" and the hash are explained; the difference between no decision and Inconclusive is stated; the paper says that the controlled policy and defect removal alone reach the same result here and what differs; the grading claim is limited to the SymPy tasks; the contribution is stated as shown on one case; the figure caption says how the target tasks are judged.

Round 4 points still open:

- No human check of the weak test findings (W1). The rate of 32 of 44 is higher than published audits report, and the paper does not discuss that gap.
- The rating "Verified / passed" on weak tests covers kept tasks of which half had no valid check (W4). The rating is a record of the study and was not changed.
- The reviewer asked for a limitation sentence in the abstract. The author decided to keep limits in the Limitations section only.
- No statement on the guidelines for language models in software engineering research.
