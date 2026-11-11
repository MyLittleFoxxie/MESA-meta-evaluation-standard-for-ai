# Feedback on the MESA paper from implementing it in Paper 2

## How to use this file

This file is for whoever works on `mesa_paper.tex` next, whether a person or an AI model. Paper 2 (`paper2.tex`) implements the MESA requirements traceability matrix as an executable method. Doing so exposed gaps and unclear points in the MESA paper. Each item below says what MESA says, what went wrong, how Paper 2 handled it, and what change to the MESA paper is proposed. Line numbers refer to the files as of 2026-11-08. Each item was checked against `mesa_paper.tex`, `v4/rubric/rubric-draft.md` (the frozen rubric), and the Paper 2 files named. Corrections to the original list of items are at the end. This file does not change `mesa_paper.tex`.

Terms used here. A **level** is one of Claimed, Documented, Verified, Contradicted, Undocumented, Not applicable. A **check** is an inspection or a run that tests a criterion. The **outcome** of a check is whether it passed or failed. The **scope** of a rating is the part of the benchmark the rating covers. Level names follow the MESA paper, except where the frozen rubric is quoted.

## Summary

The last column records what the MESA revision of 9 November 2026 did with each item (rubric v5 in `v5/rubric/rubric.md`, Study 3 in `v5/study/`, and `mesa_paper.tex`); the change record is `supporting/editorial/mesa-v5-revision-2026-11-09.md`.

| Item | Problem | Proposal | Priority | Status in the MESA revision |
|---|---|---|---|---|
| 1 | Two sets of level and identifier names; "Undocumented" names a level and a qualifier | Rubric adopts the paper's six levels; rename the qualifier; one identifier scheme | High | Adopted: v5 levels, qualifier *unreported*, C*nn*/B*nn* sentence |
| 2 | Check outcome is used in the rule but never defined | Define outcome as a field with fixed values, separate from level | High | Adopted: passed, failed, not performed, not recorded |
| 3 | Scope of a rating is undefined | Define four scope levels and say which the rule needs | High | Adopted: release, configuration, task, subset; coverage condition in equation 1 |
| 4 | One defective task blocks every decision | Add a per task rule | High | Adopted in the paper's traceability section |
| 5 | Detection limits do not affect sufficiency | Require recorded limits and let the requirement judge them | Medium | Adopted |
| 6 | B05 and B07 overlap on test defects | Split by direction of the defect | Medium | Adopted; B15 moved to the extrapolation inference |
| 7 | Unclear who runs a check and who signs | Record the kind of check and the rater | High | Adopted: check kind, rated by, signed by; roles stated in the paper |
| 8 | B14 depends on the model | Split benchmark safeguards from model exposure; accept tasks after the cutoff | Medium | Adopted as B14a and B14b |
| 9 | B07 rarely reaches Verified | Accept auditor cheating attempts as a check, with limits | Medium | Adopted in the rubric; not exercised in Study 3 (no code execution) |
| 10 | B12 role unclear when the team computes intervals | Say B12 covers the benchmark's own reporting only | Low | Adopted |
| 11 | B28 mixes two environments; wording differs | Split by environment; align wording | Medium | Adopted as B28a and B28b; Table 2 wording fixed |
| 12 | Applicability and Contradicted rules incomplete; "semantic task matching" unexplained | State the rules in the paper; define or drop the phrase | Medium | Adopted; phrase dropped, transfer justification named |
| 13 | Decision set mixes statuses and verdicts; name clash with levels | Separate status from verdict; rename verdicts | Medium | Adopted: evidence status and score decision (Accept, Reject, Inconclusive); "verdict" stays the Tier 2 term |
| 14 | A model as rater: first results | Name the rater and prompt; sharpen B12 wording; scope rule for B07 exploits | Medium | Adopted |
| 15 | A failed outcome blocks the per task rule; three outcome calls unclear (B14a, B14b, B28b) | Say the outcome is for the tasks left after the listed task defects; say how to record exposure and image findings | High | Adopted in `v5/rubric/rubric-v5.1.md` (9 November 2026): outcome after listed task defects; B14a failed, B14b not performed, B28b passed with limits |
| 16 | Two runs read "a defect beyond the listed tasks" differently when a source gives a defect rate without naming tasks; a harness defect found by an executed check | Say the defect must be located in a task in scope, and an unlocated rate goes in the detection limits; say how a grading defect of the whole benchmark is recorded | Medium | Partly done (11 November 2026): `mesa_paper.tex` states the rule after Equation 2 (a defect is located only when the record names the tasks or a component all tasks share; a rate without named tasks gives Inquiry Required). Open: the same sentences in the rubric text. `rubric-v5.1.md` was not changed, because the signed Paper 2 records cite its hash; a new rubric text is the author's decision |
| 17 | Study 1's framework scope unstated (18 sessions read as 24); anonymity; "an assistant"; the 210 to 13 contrast; "created after the cutoff" ambiguous; overlap with Paper 2 | Wording fixes; an anonymized artifact link; one decision on where the traceability rules live | High (anonymity), else Medium | Partly done (11 November 2026): the paper says which frameworks ran on which benchmarks, defines a comparison (the definition now includes Open verdicts, as the analysis code does), says next to the 210 to 13 contrast that sessions could not run code, has no repository link, and cites Paper 2 as an anonymous companion. Open, for the author: the name of the model behind "an assistant pass" (the records do not name it), the anonymized replication package, and the overlap of the traceability rules with Paper 2 |

## Item 1. Level names and identifiers

**What MESA says now.** `mesa_paper.tex` lines 145, 203, 212 list six levels: Claimed, Documented, Verified, Contradicted, Undocumented, Not applicable. Line 212 defines Undocumented as "insufficient evidence". The frozen rubric, `v4/rubric/rubric-draft.md` lines 28 to 35, names four of them Stated, Shown, Checked, and Insufficient evidence. Table 1 in the paper (line 223) puts both names in one header ("Documented (Shown)", "Verified (Checked)"). Line 146 and line 204 also use "undocumented" as the name of a Tier 2 qualifier ($-r$), and line 346 repeats it. The paper identifies concerns as C01 to C30 (line 140) and criteria as B01 to B29 (line 141), with C01 to C29 corresponding to B01 to B29 (line 150).

**The problem.** A record written against the rubric uses different words from a record written against the paper, so the engine cannot read both without a translation. The word Undocumented also has two meanings in the paper: a level (line 212) and a qualifier on a verdict (line 204). A reader of "Undocumented" cannot tell which is meant. Example: Paper 2's B14 draft for GPT-6.1 Sol proposes "Insufficient evidence (stored as Undocumented)" (`paper2/preparation/protocol-5/audit_forms/drafts/B14-CONFIG_02_SOL_MED.json`, `reasons` field). Earlier review records use C05, C07, C12, C14, C28 where the rubric uses B05 and so on.

**How Paper 2 handled it.** `paper2/method/evidence.py` line 36 defines `ANCHOR_ALIASES` (Stated to Claimed, Shown to Documented, Checked to Verified, Insufficient evidence to Undocumented). Line 32 defines `CONCERN_ALIASES` (C05 to B05 and so on). `paper2.tex` line 100 says the records accept both name sets, and line 178 describes the identifier map.

**Proposed change to the MESA paper.** The author decided the standard set is Claimed, Documented, Verified, Contradicted, Undocumented, Not applicable. Propose that the next version of the rubric adopt it and drop Stated, Shown, Checked, Insufficient evidence. Remove the double names from Table 1. Rename the Tier 2 qualifier. Suggested wording: "A verdict carries the qualifier *unreported* ($-r$) when it is negative only because the sources do not report the practice." Then "Undocumented" names one thing, the level. Add one sentence: "Concern C*nn* and criterion B*nn* denote the same question for *nn* from 01 to 29; the paper uses B*nn* for criteria and C*nn* only for the framework mapping."

**Open questions for the MESA author.**
- Is "unreported" acceptable as the qualifier name, or do you prefer another?
- Should the frozen rubric file be changed, or should a new rubric version be frozen with the paper's names?
- Is C30 (the Part A envelope) to remain the only concern without a B identifier?

## Item 2. The check outcome is undefined

**What MESA says now.** The traceability rule uses `Outcome(c) = Pass` and `Outcome(c) = FailedCheck` (`mesa_paper.tex` lines 296 and 303 to 305). Neither term is defined in the paper. The rubric defines Checked as "a check was done and report its coverage, findings and limits" (line 30) and says that a thorough check that found many errors still reaches Checked (line 35).

**The problem.** Level says that a check was reported. The rule needs to know whether it passed. The rubric allows Checked together with many findings, so level alone cannot give the outcome. Example: the 2024 screening of SWE-bench Verified is a reported check, so B05 is Checked; whether it passed is a separate judgment. Records written before Paper 2 had no outcome at all.

**How Paper 2 handled it.** `evidence.py` line 43 defines `CHECK_OUTCOMES = ("passed", "failed", "not_performed", "pending", "not_recorded")`. A requirement names the outcome it needs (line 298), and a missing outcome leads to inquiry. `paper2.tex` line 178: migration sets earlier records to "not recorded" and does not infer an outcome.

**Proposed change to the MESA paper.** Add a definition after line 145: "Each rating of Part B also records the *outcome* of the check, which is *passed*, *failed*, *not performed*, or *not recorded*. The outcome says whether the check found a defect that bears on the criterion. It is independent of the level. A rating at Verified may have outcome failed." Replace `Pass` and `FailedCheck` in equation 1 with *passed* and *failed*. State that outcome *failed* without a cited location does not make evidence inadmissible (see item 12).

**Open questions for the MESA author.**
- Should *failed* always imply Contradicted, or can a check fail on a minor point without a Contradicted level?
- Who decides pass or fail when the sources report findings but give no verdict?

## Item 3. The scope of a rating is undefined

**What MESA says now.** The paper mentions "benchmark snapshot" (line 147) and "within the target deployment scope" (line 296). It does not say what part of a benchmark a rating covers.

**The problem.** A rating that covers the whole release and a rating that covers six tasks are different evidence for a requirement, but the rule cannot tell them apart. Example: task `sympy__sympy-18199` has hidden tests that reject a fix limited to the issue (`paper2/preparation/protocol-4/audit_checks/b05-18199-counterexample.json`). If B05 is rated at release scope, this one task makes B05 Contradicted for the release, and under equation 1 every decision on every SWE-bench Verified task is blocked. If B05 is rated at task scope for the six selected tasks, the same defect is a detection limit of the screening and does not block them.

**How Paper 2 handled it.** `evidence.py` line 42 defines `SCOPE_LEVELS = ("release", "configuration", "task", "subset")`. A requirement lists the scope levels it accepts (line 301), and the engine checks that the scope covers the configuration and tasks used (line 303). `paper2.tex` line 210 states this as part of the study policy. The B05 draft (`paper2/preparation/protocol-5/audit_forms/drafts/B05-release.json`, lines 20 to 21 and 35) has level `task` while the file keeps the name B05-release, which shows how easily the two get confused.

**Proposed change to the MESA paper.** Define four scopes. *Release*: the published benchmark at a named version. *Configuration*: the benchmark run with one model setup, harness, and environment. *Task*: one named task. *Subset*: a named list of tasks. Rule: "Each rating names its scope. A rating counts for a requirement only when its scope contains every task and configuration the requirement uses." Say which criteria are naturally release scope (B07, B18, B20, B28), configuration scope (B14), and task or subset scope (B05).

**Open questions for the MESA author.**
- Is a rating at a narrower scope allowed to support a requirement that uses a larger set, if the requirement lists the gap as an assumption?
- Should the matrix store the scope as a field or derive it from the task list?

## Item 4. Defects on single tasks

**What MESA says now.** The rule judges each criterion as a whole (`mesa_paper.tex` lines 298 to 305). Contradicted or a failed check makes the criterion Inadmissible, and any Inadmissible criterion yields Inadmissible Evidence for the requirement (lines 316 to 317).

**The problem.** A benchmark of hundreds of tasks will nearly always contain some broken ones. Under the rule, one task with a defective test blocks every decision that uses the benchmark, even a decision made on other tasks. Example: `sympy__sympy-18199`.

**How Paper 2 handled it.** The author decided on 2026-11-08 that a task with shown defective tests is left out of the decision on the target requirement (called M3), named with its reason, and the decision uses the remaining tasks. The earlier decisions M1 and M2 keep every task. A defect counts only with a cited location and, when it carries a cheating patch, only when that patch was executed. A defect that concerns the whole benchmark still blocks. See `paper2/preparation/protocol-5/protocol.md`, paragraph "A task with broken tests is left out of M3" (line 99), and `evidence.py` `task_defects` (lines 104 to 115) and line 308 to 309.

**Proposed change to the MESA paper.** Add a per task rule: "A rating may list tasks whose tests are shown to be defective, each with a cited location. For a requirement that uses a task set $T$, a listed task is removed from $T$ and named in the record. The criterion stays Admissible if the remaining tasks still meet the requirement's minimum size. A defect that concerns the whole benchmark, such as a scoring script that accepts every patch, is not listed per task and makes the criterion Inadmissible." Add that the removal must not be chosen after seeing model scores.

**Open questions for the MESA author.**
- Does removing tasks bias the score upward when the broken tasks are the hard ones? How should the paper report this?
- What is the smallest remaining task set below which the evidence is Inquiry Required?
- Who may list a task: any reviewer, or only a signed rating?

## Item 5. Detection limits and sufficiency

**What MESA says now.** Verified asks that "coverage, findings, and limits of check reported" (`mesa_paper.tex` line 226; rubric line 45; "coverage/limits" at line 212). The sufficiency rule compares level and outcome only (lines 296, 304 to 305).

**The problem.** A check that reports limits may still be a poor check, and the rule does not look at the limits. Example: the 2024 screening of SWE-bench Verified passed every selected task, and the 2026 audit later reported flawed tests in at least 59.4 percent of the 138 problems it examined, all of which had passed the screening. The B05 draft records this as a detection limit (`B05-release.json`, field `detection_limits`, line 40). Under MESA's rule, a Verified rating with outcome passed would be Admissible with no regard to that limit.

**How Paper 2 handled it.** The engine requires a non empty `detection_limits` field for each selected criterion (`evidence.py` lines 127 to 144, and line 304) and reports a pass as "conditions met within recorded detection limits" (line 312). It does not judge whether the limits are small enough. `paper2.tex` line 210 says a Verified rating without detection limits leads to inquiry.

**Proposed change to the MESA paper.** Add to the sufficiency condition: "A check counts only if the record states its detection limits, and the requirement states which known limits it accepts." Ask the rater to write one sentence of the form "The check could not detect X." Mark ratings whose limits include a later audit that found missed defects, so that the matrix shows them.

**Open questions for the MESA author.**
- Should a later audit that contradicts a screening lower the level of the earlier rating?
- Who decides whether the limits are acceptable for a requirement: the requirements engineer or the rater?

## Item 6. The B05 and B07 boundary

**What MESA says now.** The rubric asks in B05 whether tasks and reference answers were checked (line 45) and in B07 whether the scoring implementation was checked and can be gamed (line 47). The paper's description of the scoring inference (`mesa_paper.tex` line 78) lists "test runners ... parser exploits, grading bugs, or gaming loopholes" as the content of B06, B07, B15. The rubric does not mention grading bugs, and its B15 concerns training on the test and repeated submission, not scoring.

**The problem.** In a benchmark that grades with each task's hidden tests, a defective test can fail in two directions. It can reject a correct fix, or it can accept a wrong patch. Both are "test defects", and neither the paper nor the rubric says where each goes. Example: for task 18199 the tests reject a fix limited to the issue (reject direction). A cheating patch that passes the tests while breaking a behavior the issue asks for is the accept direction.

**How Paper 2 handled it.** Paper 2 files rejection under B05 and acceptance under B07. See `protocol.md` line 99 ("B05 when they reject a correct fix, B07 when they accept a patch that breaks the issue") and `evidence.py` lines 104 to 107.

**Proposed change to the MESA paper.** State the split: "B05 covers tests that reject a correct solution or a reference answer that is wrong. B07 covers tests and scoring code that accept an incorrect solution." Correct line 78: either drop B15 from the scoring inference or explain the mapping, because the rubric's B15 is about submission rules.

**Open questions for the MESA author.**
- Is the mapping of B15 to the scoring inference intended?
- Should a test that is too narrow and a test that is too wide both count as B05, with B07 limited to code in the scorer?

## Item 7. Who may run a check and who may sign

**What MESA says now.** The rubric defines Checked by what the sources show: "the sources show that a check was done" (line 30). Every judgment records "which checks the reviewer performed" (line 37). In the paper's studies, the reviewer was Claude Sonnet 5.5 and the source checker was a Claude Fable 5.1 subagent (`mesa_paper.tex` line 253), with no human adjudication (line 355).

**The problem.** The rubric lets a reviewer perform checks (line 37) but does not let those checks count for Checked (line 30). An implementation needs a rule. Example: Paper 2's auditor ran the published harness on the unchanged source and with the reference patch for the seven tasks. This is a check, but not one that the benchmark's sources report. In addition, a rating signed by a model is a different kind of evidence from a rating signed by a person, and the paper does not say which it uses.

**How Paper 2 handled it.** `paper2.tex` departure 7 (line 112): a check the auditor performs counts for Verified, and the record states which kind it is. Line 210 repeats this. Each form records "author and assistant roles" (line 271), and the engine refuses a form without them (`evidence.py` lines 305 to 307). The assistant drafts and runs auditor checks; the author reviews and signs.

**Proposed change to the MESA paper.** Add two fields to every rating. *Check kind*: "reported by the sources", "run by the reviewer", or "both". *Rated by*: the name and kind of each rater (person or model with identifier) and who signed. Say that Verified may rest on either kind of check, and that a requirement may require a kind. State in Section 4 which roles the MESA studies filled with models, and that no person rated or signed.

**Open questions for the MESA author.**
- May a model sign a rating, or only draft it?
- Should a requirement for a safety relevant criterion demand a check by a person who is not the rater?

## Item 8. B14 depends on the model

**What MESA says now.** B14 asks whether exposure of test material in training data was assessed (rubric line 54). The paper names it "Contamination Defense" (`mesa_paper.tex` line 296) and treats it as a criterion of the benchmark that Verified needs a contamination check or held out procedure for (line 229).

**The problem.** Exposure depends on the model and its training cutoff, not only on the benchmark. For a closed model, public material rarely lets a reviewer check it. Example: the Paper 2 B14 draft for GPT-6.1 Sol finds no contamination check or held out procedure for that model on SWE-bench Verified in the sources, and proposes Insufficient evidence (`B14-CONFIG_02_SOL_MED.json`, line 51). The 2026 audit shows exposure for other models, which does not carry over to this one.

**How Paper 2 handled it.** B14 is rated separately for each model configuration (`paper2.tex` line 271; two B14 drafts exist in `paper2/preparation/protocol-5/audit_forms/drafts/`). Paper 2 also chose target tasks from pull requests merged after both providers' stated training cutoffs (`paper2.tex` line 264), so the target tasks serve as a held out set.

**Proposed change to the MESA paper.** Split B14 into two parts. *B14a, benchmark safeguards*: what the benchmark does about exposure (hidden tests, dated tasks, a private split). *B14b, model exposure*: per model, whether the test material could be in its training data. Add the rule: "Tasks created after a model's stated training cutoff count as a held out check for that model, with the cutoff source recorded." State the limit: a provider's stated cutoff is a claim, not a verified fact.

**Open questions for the MESA author.**
- Should B14b be part of Part B at all, since it is a property of a model and not of a benchmark?
- How should the matrix store a rating that exists once per model?

## Item 9. How B07 can reach Verified

**What MESA says now.** B07 needs "parser or judge validated; exploit tests reported" for Checked (rubric line 47; paper line 227). The paper says inspectable scoring code earns Documented only (line 296).

**The problem.** Benchmark authors rarely report exploit tests. If the sources are the only route to Verified, B07 stays at Documented for most benchmarks, and a requirement that needs Verified is never met. Example: for SWE-bench Verified the sources describe the scoring harness but report no test of whether patches can pass the hidden tests while breaking the issue.

**How Paper 2 handled it.** Paper 2 runs its own cheating attempts. For each source task a model, working only from the issue text and the real fix, writes an independent behavior check and at most three patches meant to pass the hidden tests while breaking a listed behavior. The tool runs every attempt and records it. A defect is shown only if the check is valid, the harness accepts a patch, and the check rejects it. See `paper2/preparation/protocol-5/protocol.md` line 97 (the paragraph is titled "B07 cheating attempts and broken tasks") and its stated limits: one attempt per task, at most three patches.

**Proposed change to the MESA paper.** Say that an exploit check run by the reviewer counts as a check for B07 (see item 7), and give a minimum form: the exploit attempts, a validity test for the independent check, all attempts recorded, and the limits stated. State that failing to find an exploit does not show that none exists.

**Open questions for the MESA author.**
- Is a model written cheating attempt enough, or should a person review the attempts?
- Is a minimum number of attempts per task needed for Verified?

## Item 10. B12 when the team computes its own intervals

**What MESA says now.** B12 asks whether uncertainty and statistical support are reported: sample size and uncertainty for primary scores, and power or significance reasoning for Checked (rubric line 52; paper lines 228 and 286). The acceptance rule computes bounds $\text{LB}_{1-\alpha}$ and $\text{UB}_{1-\alpha}$ itself from the model's score on the tasks (lines 319 to 321).

**The problem.** The decision rule does not use the benchmark authors' intervals; it needs the team's own. Then B12 as rated for the benchmark may not bear on the decision. Example: Paper 2 computes a Wilson interval from the observed resolved count. With six observations and threshold 0.70, the interval from six of six is $[0.610, 1.000]$, so no verdict of Supported is possible whatever the benchmark reports (`paper2.tex` lines 81 and 235).

**How Paper 2 handled it.** Paper 2 still selects B12 as one of five criteria and rates it for the benchmark release (`paper2.tex` line 271), and it computes the interval in its own engine (lines 195 to 205).

**Proposed change to the MESA paper.** Say what B12 is for when the team computes intervals. One option: B12 covers whether the benchmark's own reported scores are interpretable; the team's interval is computed separately and requires its own sample size rule. Add a sentence that the number of observations used in the decision, not the benchmark's size, limits the verdict.

**Open questions for the MESA author.**
- Should B12 be dropped from the mandatory profile when the team computes its own interval?
- Is a minimum number of observations a property of the requirement or of the criterion?

## Item 11. B28 and the two environments

**What MESA says now.** B28 asks whether the evaluation environment is controlled and isolated from answers (rubric line 68). It applies "when the benchmark runs systems in an environment with tools or state" (rubric line 68). The paper's table says "Systems run in tools/state env (Basis: A04)" (`mesa_paper.tex` line 231) and line 211 describes A04 as the basis, while also saying a gate by a multi turn field is a proposed extension that is not frozen.

**The problem.** The environment that grades a patch and the environment in which the agent works are different, and B28 does not say which it covers. Example: in Paper 2, B28 reviews the grading harness and the published SWE-bench images (the check lists commits after the base commit in all 75 images), not the sessions the study runs (`paper2.tex` line 271). The environment of those sessions enters only through separate validity rules (lines 266 and 270). The two statements of when B28 applies also differ: the rubric ties it to the benchmark running systems in an environment with tools or state, the paper to a Part A criterion.

**How Paper 2 handled it.** B28 is rated at release scope for the grading harness and images only. Isolation of the agent's own environment is handled by session validity rules in `paper2.tex` line 266.

**Proposed change to the MESA paper.** Split B28 into *grading environment* (can the grader be reached or altered by the agent, and does it contain answers) and *agent environment* (can the agent reach answers, history, or the network). State the applicability once, using the rubric wording, and note that A04 informs the rater but does not gate.

**Open questions for the MESA author.**
- Is the split needed for the frozen rubric, or only for the traceability use?
- Which wording of "applies when" is the standard?

## Item 12. Applicability, Contradicted, and the companion work

**What MESA says now.** A criterion is not active when the Part A condition fails (`mesa_paper.tex` lines 298 and 302). The rubric defines Not applicable as the concern not arising, "with the reason taken from Part A or from the benchmark's stated use" (line 33), and lists an "Applies when" per criterion. The rubric also says Contradicted "needs a cited location" (line 31). The paper defines Contradicted as "confirmed defect or contradiction" (line 212) and does not mention the location. Line 290 refers to "semantic task matching" in companion work.

**The problem.** The paper does not say which criteria can be marked Not applicable, nor that a reason is required. An engine that accepts a bare mark lets a team switch off a hard criterion. Equation 3 only guards against all criteria being off. The paper's missing rule about locations lets an unsupported Contradicted block a decision. Example: Paper 2 refuses Not applicable for B05, B12, B14 because the rubric applies them always (rubric lines 45, 52, 54), and treats a Not applicable mark without a reason as inquiry. The phrase "semantic task matching" is not defined, and Paper 2 does not implement it; it uses a transfer justification that names an author and a scope instead.

**How Paper 2 handled it.** `evidence.py` line 41 sets `ALWAYS_APPLIES = ("B05", "B12", "B14")`. `paper2.tex` departure 4 (line 109) takes applicability from the review record, requires a reason, and refuses Not applicable for those three. Departure 3 (line 108) requires a cited location for a Contradicted level. Departure 8 (line 113) replaces matching of tasks with a transfer justification whose content the engine does not check.

**Proposed change to the MESA paper.** (a) Add: "A rating of Not applicable gives a reason that cites Part A or the stated use. The criteria whose rubric entry says 'always' cannot be rated Not applicable." (b) Add to line 212: "Contradicted cites a location in the sources." (c) Either define "semantic task matching" in one sentence or delete it and say only that the companion work addresses the step from source tasks to the target requirement.

**Open questions for the MESA author.**
- Is a Part A gate enough reason for Not applicable, or must a person confirm it?
- What does the companion work promise, and which paper owns it?

## Item 13. Statuses, verdicts, and name clashes

**What MESA says now.** The decision set holds five values: Inadmissible Evidence, Conditional Query, Accept, Model Rejected, Inconclusive (`mesa_paper.tex` lines 308 to 312).

**The problem.** The first two describe the evidence. The last three describe the model's score against the threshold. Putting them in one set makes the result hard to read: Inconclusive can mean the evidence is poor or the sample is small. Example: a Paper 2 run yields evidence status "inquiry required" and a score verdict of Unresolved with an interval spanning 0.70, as separate outputs (`paper2.tex` lines 106 and 235). There is a second clash. Paper 2 names its verdicts Supported, Contradicted, Unresolved (lines 106, 195 to 205), and Contradicted is also a level.

**How Paper 2 handled it.** `paper2.tex` departure 1 (line 106): the first two values are evidence statuses and the last three are verdicts, reported apart. The verdict names Supported, Contradicted, Unresolved reuse "Contradicted", which is also a level name. Paper 2 does not address this clash.

**Proposed change to the MESA paper.** Report two outputs. *Evidence status*: Inadmissible, Inquiry Required, Admissible. *Verdict*, given only when the status is Admissible: Accept, Reject, Inconclusive. Choose verdict names that never equal level names: for instance Accept, Reject, Inconclusive, not Supported or Contradicted. Say that Inconclusive always carries its cause (sample size or evidence status).

**Open questions for the MESA author.**
- Should Paper 2 change its verdict names to match MESA's, or should MESA adopt Paper 2's with a different word for Contradicted?
- Should "Conditional Query" be renamed Inquiry Required to match the criterion status in equation 1?

## Item 14. First results with a model as rater (2026-11-08, before the author's signature)

**What happened.** Paper 2's RQ1 asks whether a model can produce the MESA ratings a requirement decision needs. A Claude Sonnet 5.5 run wrote the six rating forms for SWE-bench Verified (B05, B07, B12, B28, and B14 for each of two coding agents) from a fixed prompt that gave it the rubric, the saved sources, and the check records, but not the decision code or earlier forms (`paper2/preparation/protocol-5/reviewer-prompt.md`; record `audit_checks/rating-form-run-2026-11-08.json`).

**Results so far** (`audit_checks/reviewer-agreement.json`):
- Levels: B05, B07, and B28 Verified with a passed check; B12 Documented and both B14 forms Undocumented, with no check performed.
- Against earlier forms written by another model (Claude Opus 5.5): the same level on four of six forms and the same check outcome on all six. B07 rose from Documented to Verified because the B07 cheating attempts existed only for the second run. B12 moved from Undocumented to Documented, a real disagreement between the two models on what the sources show.
- B07 cheating attempts (Claude Sonnet 5.5): on 17 of 20 tasks a patch passed the hidden tests and failed an independent check, but the check often tested behaviors inferred from the real fix. Reading the issue texts, the rating run counted four defects and set aside 13 as outside the issue's scope, and named two cases as judgment calls.
- The rating run did not follow one instruction: it wrote B05 and B07 at scope level "release" with task lists, where the prompt asked for "task".

**What this means for MESA.**
- A model can fill the rubric's forms with cited quotes, and a check of its quotes against the sources is easy to automate. Its levels are not yet validated against a person: the author's changes before signing are the first comparison, and Paper 2 will report them.
- Two runs disagreed on B12, the criterion whose level depends most on reading ("is uncertainty reported?"). MESA's level definitions may need sharper wording where a source shows a sample size but no interval.
- Deciding whether a shown test defect is within the issue's scope was the hardest step and is not covered by the rubric. MESA could say that a B07 exploit must break behavior the task statement asks for (see item 6 and item 9).

**Open questions.** Should MESA require a person to check a model's ratings, and if so which part (quotes, levels, or scope judgments)? Should a rating record name the model and the prompt that produced it (see item 7)?

## Item 15. A failed outcome blocks the per task rule (2026-11-09, from Paper 2's first rating run on rubric version 5)

**What MESA says now.** The rubric defines the outcome as "whether the check found a defect that bears on the criterion" (`v5/rubric/rubric.md`, field table, line 63). A rating may list single tasks whose tests are shown to be wrong, and the decision then uses the task set less those tasks (line 72; the paper's traceability section). The evidence status is Inadmissible when "the rating is Contradicted or has outcome failed, and the record cites the location" (change record, "Traceability matrix rules now in the paper").

**The problem.** A check that finds broken tests on some tasks has found a defect, so a rater records outcome failed with a location. The criterion is then Inadmissible, and the rule that leaves out the listed tasks never takes effect: every decision becomes "no decision". Paper 2's first rating run on version 5 (Claude Sonnet 5.5, run A) did exactly this. It recorded outcome failed on B05 and B07 while listing their task defects (B05: one task; B07: five tasks), so M3 gave no decision under both policies.

**How Paper 2 handles it.** Paper 2 stopped its second rating run and waits for MESA's ruling before rerunning both runs against the clarified rubric.

**Proposed change to MESA.** Add to the outcome field and the task defect rule: "The outcome describes the check on the tasks in scope after the listed task defects are left out. Failed means a defect that bears on the criterion beyond the listed tasks. When every defect found is listed per task, the outcome is passed for the remaining tasks." This keeps "a defect of the whole benchmark makes the criterion Contradicted" (line 72) and gives the per task rule its intended effect. Study 3 listed no task defects, so its results do not change.

**Three related calls the same run had to make, which MESA could settle at the same time:**
- **B14b (exposure of a named model):** when every task was created before the model's stated training cutoff, no held out check is possible. Run A recorded level Documented with outcome failed. Is the outcome "not performed" (no check possible) or "failed" (the check found that exposure is possible)?
- **B14a (the benchmark's safeguards):** OpenAI's 2026 post reports that other frontier models could reproduce gold patches. Run A recorded outcome failed. Does exposure shown for other models make the benchmark's safeguard check fail, or does B14a concern only whether safeguards exist?
- **B28b (the agent environment as shipped):** two published task images hold commits after the base commit, and a search found no fix text in them. Run A recorded outcome failed. Is that a defect, or a passed check with the limit stated?

**Open questions.** Is the clarification a new rubric version (a new hash) or a correction note to version 5? Paper 2 will cite whichever file and hash MESA settles on.

**MESA answer (author, 9 November 2026).** Adopted as `v5/rubric/rubric-v5.1.md` (`mesa-rubric-v5.1`, sha256 `023058fcfa3190a5ab17b55f71990d33c661b0c606a6f76b9b55d46611420cdf`); `rubric.md` stays frozen for Study 3. The outcome describes the tasks left after the listed task defects. B14a: a source showing that models reproduce the test material makes the outcome failed, whatever models it names. B14b: when every task predates the stated cutoff and no contamination check for the model exists, the outcome is not performed; failed only when a source shows this model reproduces the material. B28b: later commits that a search found no fix in are recorded in the evidence, and the outcome is passed with the limits of the search stated.

## Item 16. Unlocated defect rates and grading defects in the outcome (2026-11-09, from Paper 2's review of its rating forms)

**The problem.** Paper 2's two rating runs (Claude Sonnet 5.5, same prompt, rubric v5.1) disagreed on B05's outcome. Both listed `sympy__sympy-18199` as a task defect. Run A recorded failed, because OpenAI's 2026 audit reports flawed tests in at least 59.4% of 138 audited SWE-bench Verified tasks, without naming which; run B recorded passed, because no defect is located in the other tasks in scope. Rubric v5.1 line 76 says the outcome describes "the tasks in scope after the listed task defects are left out", and line 140 says a failed outcome without a cited location of the defect requires inquiry, so run B's reading fits, but the rubric does not say how to record a rate that names no task.

A second case: Paper 2 ran an executed B28a check. On three SymPy tasks, nine patches that change only the test runner (`bin/test`, `runtests.py`) and no source code were all graded resolved by the SWE-bench harness 5.0.2 (`paper2/preparation/protocol-5/audit_checks/b28a-scoring-check/`). This is a defect of the grading of the whole benchmark, not of single tasks.

**How Paper 2 handles it.** B05 is recorded as passed, with the 59.4% rate in the detection limits; the author confirms this at signing. B28a is recorded as Verified with outcome failed, located in the check records, and no task is listed.

**Proposed change to MESA.** Add to the outcome field: "A defect counts toward the outcome only when it is located in a task in scope or in a component the tasks share, such as the scorer or the grading environment. A rate reported for tasks the source does not name goes in the detection limits." Add to the task defect rule: "A defect of a shared component is not listed per task; it makes the outcome failed for the criterion."

**Open questions.** Should a failed B28a with a located grading defect be Contradicted rather than Verified with outcome failed? The rubric allows both readings (line 57 and line 76).

## Item 17. Wording, scope, and anonymity in the MESA paper (2026-11-09, from a review of both papers and a check of MESA's use of ABC)

**MESA's use of ABC was checked and is correct in substance.** Study 1 applied ABC only to τ-bench (`v4/study/outputs`: `tau-bench-ABC`), within ABC's agentic scope, and How2Bench only to HumanEval. Table 1's counts (42 items in the paper, 44 released) and its rule for missing documentation ("Undocumented item scored 0") match the ABC paper (Section 3: "We assigned 1 point to each satisfied item and 0 otherwise"), now saved in `literature/pdfs/` with a transcription.

**The problems** (each verified against `mesa_paper.tex`):
- **Framework scope.** Lines 44 and 253 say six frameworks were applied "across four" benchmarks. A reviewer read this as 24 sessions; Study 1 has 18 because ABC ran only on τ-bench and How2Bench only on HumanEval. Say so, and define a "comparison" in one sentence (line 264).
- **Anonymity.** Line 383 gives the GitHub URL with the author's handle and the branch `refsq-v1`, followed by an "Identity Notice". REFSQ review is double-blind. Use an anonymized artifact link.
- **"An assistant"** at lines 30 and 268 should name the model.
- **The 210 against 13 contrast** (lines 30, 44, 273): the sessions could not run code, so confirmed defects were hard to record. Say this where the contrast is stated.
- **"Created after the cutoff"** (lines 233 and 306) is ambiguous: issue opened or fix merged. Paper 2's target fixes were merged after both models' stated cutoffs, while five of their issues were opened before them. Say which date counts.
- **Overlap with Paper 2.** The traceability equations, the evidence status, the removal rule, and the six-of-six example appear in both papers (`mesa_paper.tex` lines 297 to 340). A reviewer may read the two as one contribution split in two. One option: MESA keeps the traceability matrix as a short proposal, and Paper 2 holds the engine and its evaluation. This is the author's decision across both papers.
- **Optional.** Table 1 could note that ABC averages the applicable items and gives no rule to accept or reject a result.

**How Paper 2 handles it.** Paper 2 removes its own GitHub link and cites MESA's rubric file and hash. It describes automated audits (BenchGuard, ABA, BenchJack) as complements that supply checks to a review, with a mapping of their defect categories onto MESA's criteria (`supporting/editorial/paper2-mesa-refsq-review-2026-11-09.md`).

## Corrections to the original item list

- **Item 4.** The paragraph on cheating attempts in `protocol.md` is titled "B07 cheating attempts and broken tasks" (line 97), not "B07 cheating attempts". The paragraph "A task with broken tests is left out of M3" is line 99.
- **Item 4 and 3.** `protocol.md` calls `sympy__sympy-18199` one of "the 20 source tasks" (line 99), while `paper2.tex` line 271 calls it "outside the selection" and describes 75 source tasks and six selected. The two Paper 2 files disagree. Check before citing.
- **Item 6.** The rubric does not mention grading bugs. The phrase is in `mesa_paper.tex` line 78, in the Kane section, not in the B07 text. Line 78 also maps B15 to scoring, which does not match rubric B15.
- **Item 8.** The paper calls B14 "Contamination Defense" (line 296), while the rubric asks about exposure of test material (line 54).
- **Item 13.** Paper 2's own verdict name Contradicted clashes with the level name; Paper 2 does not note this itself, so the clash is a finding and not something Paper 2 handles.
- **Item 14.** Written by Claude Opus 5.5 on 2026-11-08 from the rating run's records, after the other items; it replaced a placeholder.
- **Item 1.** The alias map is confirmed. The rubric identifies criteria as B01 to B29 and concerns as C01 to C30 in the concerns file, so the identifier mismatch is between earlier records and the rubric.
- **Items 2, 3, 5, 7, 9, 10, 11, 12.** Confirmed as stated, with line numbers as given above.
