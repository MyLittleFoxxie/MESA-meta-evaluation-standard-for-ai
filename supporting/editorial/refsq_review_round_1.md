# REFSQ review, round 1 (11 November 2026)

Round 1 of the review loop for the two REFSQ 2027 papers. The reviews are of the papers as they stood before this round's changes, compiled with the corrected bibliography.

How the reviews were made: six subagents (Claude Sonnet 5.5), one per paper and point of view. Each saw only the PDF of one paper, a text extraction of it, and a summary of the REFSQ 2027 call for papers. None saw the repository, the other paper, or any answer or change. Their web checks of references mostly failed on a usage limit, so reference checks in the reviews are from the reviewers' memory unless they say otherwise. The meta reviews and the answers are by the session that made the changes (Claude Fable 5.2), so the meta reviews are not blind.

The call: REFSQ 2027 research track, papers due 12 November 2026, 15 pages including references for technical design and scientific evaluation papers, double blind, mandatory Data Availability Statement, abstract in four paragraphs. The 2027 call was found, so the 2026 call was not used.

## Scores

| Paper | Requirements engineering | Empirical methods | AI evaluation | Expected decision |
|---|---|---|---|---|
| MESA paper | reject (medium confidence) | weak reject (medium) | reject (medium) | Reject |
| Paper 2 | reject (medium) | reject (high) | reject (medium) | Reject |

## Meta review: MESA paper

Expected decision: reject. The reviewers agree on three points that decide it.

1. **No human reference.** Every rating, every disagreement code and the source audit come from language models of one family. Study 1 therefore shows how frameworks differ when one model applies them, and Study 2 shows that one model repeats itself. Neither shows that the rubric is right or that people would agree.
2. **The traceability matrix is a named contribution and is not evaluated.** It has one example row, and its evaluation is deferred to a companion paper.
3. **The requirements engineering contribution is thin.** The paper audits benchmarks; the link to requirements work rests on one formula and a few citations.

Items that weighed on the scores and could be fixed in the text: inconsistent counts (26 logs against 28 sessions, the 234 matches, "maximum score" against a score of 10), a definition of the criteria set that did not match the example, agreement figures that include trivially agreeing pairs, the 210 of 711 share with a denominator that includes frameworks that cannot produce it, and doubt about the HumanEval example.

## Meta review: Paper 2

Expected decision: reject. If submitted as it stands on 12 November it would not be accepted. All three reviewers say so, for the same reasons.

1. **No results for the research questions.** No agent session has run. As a scientific evaluation paper it has nothing to evaluate. As a technical design paper its preliminary evaluation is the executed checks, a power table and a simulation with assumed parameters.
2. **The MESA outcome is fixed in advance and is the same for every agent.** B28a failed for the whole release, so both policies return No decision whatever the sessions show. The gate also ignores the study's own session validity rule, which blocks the exploit.
3. **No power.** At 14 to 20 tasks and a threshold of 0.70, an agent with a true rate of 0.75 is Inconclusive about 97% of the time.
4. **The review records are not independent.** One model family drafted the forms and wrote the exploit patches; one author signed.

Fixable items: the Accept cut points at N = 90 and 120 were wrong by one, the abstract and conclusion read as 7 removed tasks when there are 6, "pre-registered" was claimed for a protocol that is not frozen, SWE-bench was not cited, the companion paper was not cited with a placeholder, and one cited study was described loosely.

## Answers as the author

Each item: accepted (changed in this round), rejected (with the reason), or left for you.

### MESA paper

| # | Item | Raised by | Decision | What was done or why |
|---|---|---|---|---|
| M1 | No human raters; agreement is repeatability of one model | all three | Left for you | Needs a human rating study. The abstract now states this limitation, and the Limitations section says Study 1 shows how frameworks differ when one model applies them. |
| M2 | Traceability matrix not evaluated; companion not cited | all three | Accepted in part | The text now says the matrix is not evaluated here and cites the companion paper with an anonymous placeholder. Whether the matrix stays in this paper is your decision (feedback item 17). |
| M3 | Thin link to requirements engineering; title reads as AI for RE | RE | Accepted in part | Cited Berry (REFSQ 2022) and Gotel and Finkelstein on traceability. The title is left for you. |
| M4 | Criteria set given as B01 to B04 but the example uses five other criteria | RE, AI evaluation, empirical | Accepted | The relation now takes the profile the requirements engineer selects from Part B. |
| M5 | 26 logs against 28 sessions | all three | Accepted | Data Availability now says the logs of the 28 sessions. |
| M6 | 180 + 56 = 236, paper says 234 | all three | Accepted | The sentence now reports the record as it is: the final mapping equals the draft on 234 items (`v4/mapping/mapping-summary.md`). The two counts measure different things; the old wording implied a sum. |
| M7 | "Maximum score" in the Introduction against a score of 10 in Section 3.2 | RE | Accepted | The record has 10 of 15. The Introduction now says so. |
| M8 | HumanEval example doubtful: the exec line is commented out upstream | RE, AI evaluation, empirical | Rejected, with a clarification | In the frozen snapshot (commit `b9453e8`, `human_eval/execution.py` line 50) the call is active, while the README says it is commented out. The paper now gives the commit and the line, and cites the HumanEval paper. |
| M9 | 80% Part B agreement includes agreeing N/A pairs | all three | Accepted | Added 82 of 106 applicable pairs (77%). |
| M10 | Ordinal alpha without a stated order; no intervals | empirical, AI evaluation | Accepted in part | The order used by the analysis is now stated, with a source for the statistic and the note that no intervals were computed. Computing intervals would be a new analysis on frozen records; left for you. |
| M11 | 210 of 711 uses a denominator that includes ECBD and OECD | AI evaluation | Accepted | Added 38% of the 559 answers in the four frameworks that can produce the qualifier. |
| M12 | Section 6.1 says disagreement is largely from conflating unreported with negative; the coding says granularity is larger | RE | Accepted | Rewritten to give both causes with their counts. |
| M13 | Repeat sessions not used as a noise floor | AI evaluation | Accepted | Added one sentence: about one concern verdict in ten changes between runs of the same framework. |
| M14 | "Outcome failed" although no check ran | RE, empirical | Accepted in part | The text now says the check was a static inspection. Whether a static inspection should count as a check with outcome failed is a rubric question (feedback item 16). |
| M15 | RQ2 "zero unmapped items" holds by construction | all three | Rejected | True, and the paper presents the mapping as a construction. The limitation paragraph already says it is one author's taxonomy. No room for more. |
| M16 | How2Bench and ABC ran on one benchmark each; comparisons not independent; strict conjunction chosen by the authors | empirical | Rejected for this round | The design is stated, and the majority rule is reported as a sensitivity check. More analysis needs new work on the records. |
| M17 | Missing related work on benchmark validity and contamination | AI evaluation | Rejected for lack of room | The paper is at the page limit. Candidates are in the references record. |
| M18 | Abstract's fourth paragraph states no limitations | AI evaluation | Accepted | Added. |
| M19 | Abstract lists three contributions, Introduction four | empirical | Left as is | The Introduction separates the verdict tiers from the rubric. Minor. |
| M20 | Data Availability has no link | AI evaluation, RE | Left for you | The replication package does not exist yet. |
| M21 | Prompts, sampling settings and model versions not reported | empirical | Left for you | They are in the records and belong in the replication package. |

Found by the author session while checking numbers against the records, not raised by a reviewer:

- The definition of a pairwise comparison said both frameworks give a Satisfied or Unsatisfied verdict. `v4/study/analyze.py` also counts Open verdicts, and 29 of the 143 disagreements in `disagreement-log.csv` have one Open side. The definition now matches the code.
- "Four frozen Python benchmark snapshots": TruthfulQA and Humanity's Last Exam are not Python benchmarks. The word was removed.
- Feedback item 16: the rule for a defect rate without named tasks is now stated after Equation 2.
- Feedback item 17: the sentence next to the 210 to 13 contrast now says the sessions could not run code.

### Paper 2

| # | Item | Raised by | Decision | What was done or why |
|---|---|---|---|---|
| P1 | No sessions, so no results for RQ1 or RQ2 | all three | Left for you | Needs the freeze, your authorization and the sessions. The abstract, Section 1.2 and the conclusion now say plainly what exists. |
| P2 | MESA outcome fixed in advance; gate constant on this benchmark; no credit for the session validity rule | all three | Left for you, with a proposal | Stated in the abstract and the Limitations. `paper2/preparation/protocol-6/proposal.md` proposes a third policy that accepts a per-session control. Not implemented: it changes the method and needs your decision and signature. |
| P3 | No power at N = 14 to 20 | empirical, AI evaluation | Left for you, with a proposal | The paper already reports this. The proposal gives two ways to spend the 90 sessions on one agent with more tasks. |
| P4 | Accept cut points at N = 90 and 120 | empirical, AI evaluation | Accepted | Corrected to 72 and 94. The probabilities were already right. |
| P5 | Abstract and conclusion read as 7 removed tasks; there are 6 | all three | Accepted | Reworded in the abstract, discussion and conclusion. |
| P6 | "Pre-registered" claimed for a protocol that is not frozen | empirical | Accepted | Removed. |
| P7 | B14a Inadmissible without an executed counterexample | RE, empirical | Accepted as a wording fix | The rule now says a counterexample must have been executed where the defect rests on one. The engine was not changed; if you read the rule as requiring a counterexample for every failed outcome, B14a would be Inquiry Required under the strict policy, and the strict status would still be Inadmissible through B28a. |
| P8 | B05 "Verified, passed" on 21 tasks though one was examined | empirical, AI evaluation | Accepted in part | The text now says the other tasks were run only with the reference fix. The rating itself is a signed record. |
| P9 | "17 of 20" includes 11 tasks that are not defects | AI evaluation | Rejected | The paper says so in the same sentence in Section 4.3, and the abstract now gives both numbers together. |
| P10 | Requirement not well formed: population, origin of 70% and 15 minutes, drafted by a model | RE | Left for you | The requirement is a signed record. |
| P11 | Thin link to requirements engineering; some citations do not support their claim | RE | Accepted in part | Cited Berry (REFSQ 2022) and SWE-bench; removed one citation from the claim it did not support. |
| P12 | Related work describes the SWE-Bench Illusion loosely | AI evaluation | Accepted | Corrected. |
| P13 | Companion paper not cited with a placeholder | AI evaluation, RE | Accepted | Cited. |
| P14 | Paper category | all three | Accepted | Section 1.2 now says it is a technical design paper and what its preliminary evaluation is. |
| P15 | Review records come from one model family and one signer; forms signed from run A | all three | Left for you | Disclosed in the Limitations. The proposal suggests reporting agreement between runs A and B. |
| P16 | Direct test is not ground truth; B05 and B07 not applied to target tasks | AI evaluation | Left for you, with a proposal | Proposal item P6-4. |
| P17 | Simulation mostly shows that MESA abstains | empirical, AI evaluation | Accepted in part | The paper said so; one sentence now adds that the simulation is not evidence about real reviews. |
| P18 | Missing related work | AI evaluation | Accepted in part | Added Wang et al. (ICSE 2026) and the METR note. |
| P19 | Data Availability has no link | all three | Left for you | The package does not exist yet. |

## Changes and files

| File | Change |
|---|---|
| `mesa_paper.tex` | Items M2 to M14 and M18, the four author findings, and cuts to stay within 15 pages (contribution list, the paragraph on level and outcome, the prose that repeated Equations 2 and 3, the role paragraph, Sections 2.1 and 2.3, 6.1, the conclusion) |
| `paper2.tex` | Items P4 to P8, P11 to P14, P17, P18, and cuts to stay within 15 pages (term list, case record list, Level 1, related work, replay, simulation paragraph, Limitations paragraph 3, Data Availability) |
| `references.bib` | Eight entries corrected, ten added |
| `supporting/editorial/references_review_2026_11.md` | New: Step 1 record |
| `paper2/preparation/protocol-6/proposal.md` | New: proposal, not in force |
| `paper2_runbook.md` | Section 9 (W4, W5, W10, W12, the review round, the table correction) and the change log |
| `README.md` | Current state |
| `mesa_paper_feedback_from_paper_2.md` | Status of items 16 and 17 |

Not changed: research questions, code, tests, protocol 5, policies, signed forms, records, frozen files.

## What you would need to sign again

Nothing in this round changes what a signed record says. Two places where the paper now words a rule differently from before, for you to confirm: the Level 2 rule on counterexamples (P7), and the located defect rule in the MESA paper (feedback item 16).


## Checks and page counts after the changes

Run on 11 November 2026 after the round 1 changes.

| Check | Result |
|---|---|
| `python3 verify_manuscripts.py` | No missing citation or reference, no unclosed brace, in both papers |
| `python3 v4/mapping/check.py` | Passed; `git status` shows no changed file under `v4/` |
| `python3 v4/study/test_harness.py` | OK |
| `python3 v5/study/test_harness.py` | Passed |
| `python3 -m unittest discover -s paper2/tests -p 'test_*.py'` | 181 tests, 1 failure, 1 skipped. The failure is `test_home_searches_in_any_spelling_and_study_paths_in_outputs`, which depends on the home path of the machine and failed the same way before any change |
| `python3 surveys/colleague-review/verify.py` | Passed |
| Page count, MESA paper | 15, with room for about 9 more lines |
| Page count, Paper 2 | 15, with room for about 9 more lines |

Build: TeX Live 2023 with `latexmk -pdf`, in a Linux container. TeX Live 2026, the reference build, was not installed there. The runbook records that TeX Live 2023 broke pages as MiKTeX 25.12 did on 10 November. Compile once on Overleaf before submitting.

## Reviews as written

The six reviews follow unchanged.


---

### MESA paper: reviewer for requirements engineering

#### REFSQ 2027 research track: review of the submission "Unifying Benchmark Evaluation Protocols: A Meta Evaluation Standard for Artificial Intelligence in Requirements Engineering"

Reviewer role: program committee member, requirements engineering researcher.
Files read: the call, the PDF (all 15 pages) and the text extraction. I did not look at the replication package. I used web search only to check references.

##### 1. Summary of the paper

The paper takes seven published review frameworks for AI benchmarks (BetterBench, ECBD, Scorecard, How2Bench, ABC, Caliper, OECD facets). It maps their 280 items onto 30 shared concerns (386 links) and derives a rubric called MESA with 39 criteria (8 descriptive, 31 evaluative). Each evaluative rating records an evidence level (Claimed, Documented, Verified, Contradicted, Undocumented, N/A) and, separately, a check outcome. The central idea is to keep "absent reporting" apart from "located defects". A "Requirements Traceability Matrix" (RTM) design (Section 6.2, Equations 2 to 4) turns the ratings into a gate for a requirement: Inadmissible, Inquiry Required or Admissible. Only after the gate does a confidence interval on the model score get compared with a threshold.

Evidence offered:
- Study 1: 18 sessions in which Claude Sonnet 5.5 applied six frameworks to four benchmarks (HumanEval, TruthfulQA, HLE, tau-bench). Frameworks agreed on 159 of 302 pairwise comparisons (53%). A second model (Claude Fable 5.1) coded the cause of the 143 disagreements.
- Study 2: eight sessions applying MESA twice per benchmark. Repeatability is 81% on Part A and 80% on Part B levels (alpha 0.80 and 0.70), and 67% on level plus outcome. A subagent audit of the 312 judgments found 0 fabricated quotes.
- One instantiated RTM row for HumanEval (Table 5).

##### 2. Paper category under the call

The paper does not state a category. The best fit is a technical design paper (15 pages): the main artifact is the MESA rubric with the RTM design, and the studies serve as a preliminary evaluation. Some of the content also reads as a scientific evaluation paper (RQ1 and RQ3), so the soundness criteria for empirical work apply to the studies.

Criteria for technical design papers, in the order the call gives:
1. Novelty. Partly met. Merging seven checklists is a consolidation. The separation of evidence level from check outcome and the "unreported" qualifier are the new elements, and they are small and not tied to prior art on evidence and assurance. The RTM is described as conceptual, with the implementation and evaluation "presented in companion work".
2. Potential impact and relevance. Weakly met for REFSQ. The artifact helps people who audit AI benchmarks. The link to requirements engineering is a framing (Section 2.1, Section 6), not a requirements engineering method or result. The special theme (RE at AI velocity) is only touched through the first sentence and Section 6.1.
3. Soundness. Not met. All judgments in both studies come from one model family with no human rater and no ground truth. RQ2 is answered by construction. Several numbers and statements conflict (see Section 6).
4. Verifiability. Partly met. A Data Availability Statement exists, but its session count does not match the paper, and the LLM setup is under specified.
5. Presentation. Not met for the REFSQ audience. The text is dense with identifiers (C01 to C30, A01 to A08, B01 to B29, tiers, qualifiers), and terms change between sections.

##### 3. Strengths

- S1. The problem is real and the running example is a good one. Frameworks that treat "not reported" like "found to be wrong" do give contradictory verdicts, and the HumanEval example in the introduction makes this concrete.
- S2. Separating "what evidence exists" from "what a check found" (Section 3.3) is a useful modelling choice. It matches how assurance arguments separate claims from evidence, and it is stated precisely enough to be criticised.
- S3. The paper reports its counts openly, including a negative result that hurts MESA: 6 absences that the source contradicts, 11 of 46 Verified ratings with weaker support, and 67% agreement on level plus outcome. The Limitations section names the same model family, the single mapper and the lack of human raters.
- S4. The mapping effort is large, and Table 3 gives the link counts by framework and stage. The totals in Table 3 add up (rows and columns both give 386).
- S5. A Data Availability Statement is present, and a replication package is promised.

##### 4. Weaknesses

###### W1 (decision). The requirements engineering contribution is thin and the title misleads. Title, Section 2.1, Section 6
What is wrong: The title says "Artificial Intelligence in Requirements Engineering", which reads as AI for RE. The paper is about auditing AI benchmarks to select a model. None of the four benchmarks is an RE artifact, and no requirements engineer is involved in any study. The RE content is one use of the Jackson and Zave notation (Equation 1), the word "requirement" in Equations 2 to 4, and a matrix called an RTM. Section 6 hands the real RE questions to "human requirements engineering judgment" without addressing them: how a requirement on a model is written, how it selects criteria, who decides the threshold theta.
Why it matters: For a technical design paper, relevance and impact come second in the order of criteria. A REFSQ reader finds a benchmark methodology paper.
Fix: Retitle. Show the RE step with a worked example from elicitation to acceptance criteria (see W3). Position the work against RE for ML (requirements for ML components, performance requirements and thresholds), requirements driven selection of off the shelf components, and assurance cases.

###### W2 (decision). Weak link to RE theory and prior RE work. Sections 1, 2.1, 6.2, reference list
What is wrong: Only [11] (a mapping study) and [27] (Zave and Jackson) come from RE. Equation 1 writes W, E, O_bench(M,B) with the turnstile marked "ind" and calls it inductive, while the Zave and Jackson relation is deductive and relates specification, domain assumptions and requirements. The paper does not say what W, E and O are in Jackson's terms, or why G_AI is both a "capability requirement" and a goal. The RTM carries the name of a long studied artifact, but the paper cites no traceability work, discusses no link types, coverage or maintenance, and "RTM" here is an evidence gate function. Keywords include "Acceptance Testing", with no acceptance testing literature. Work on selecting components against requirements, and on requirements for ML components, is absent.
Why it matters: The RE contribution cannot be assessed against what is known, and novelty claims in RE are not supported.
Fix: Add the RE literature above, reformulate Equation 1 or drop the claim of an extension of Jackson and Zave, and rename the RTM or show what traceability properties it has.

###### W3 (decision). The RTM design is unevaluated and the gate has no demonstrated use. Section 6.2, Equations 2 to 4, Table 5
What is wrong:
- One row, one benchmark (HumanEval), one outcome that the authors knew in advance. Equation 4, n_min, theta and alpha are never instantiated, and no model is named.
- Section 6.2 says the criteria set C is B01 to B04, but the profile in Table 5 and the text is {B01, B03, B07, B14b, B28a}. How a requirement selects its profile is not defined.
- The rule makes any located defect in an active criterion block the whole benchmark. The defect found, an in process exec() in the harness (B28a), is a safety property of running candidate code. It does not obviously invalidate a pass@1 score for a model that does not tamper with the tests. There is no severity or relevance weighting by requirement.
- Sufficiency for B07, B14a, B14b, B28a and B28b needs level Verified with outcome passed. Section 4.2 and Section 7 say no session executed checks. Most real benchmarks would end in "Inquiry Required", and the paper does not show the gate discriminates between benchmarks.
- Removing tasks with located defects before scoring (T'_r) lets the reviewer drop tasks after the fact. There is no rule that this is done blind to model results.
- The abstract claims the RTM as a contribution while Section 6.2 sends the implementation and evaluation to "companion work", which is not cited as "A. Anonymous" as the call requires.
Why it matters: This is the part of the paper that a requirements engineer would use, and it is a sketch.
Fix: Instantiate the whole pipeline on at least two requirements and two models, with a coding agent benchmark from the special theme. Define profile selection and defect severity. Either cite the companion work as anonymous work or state that it is out of scope and remove it from the contribution list.

###### W4 (decision). The evidence does not support the claims about MESA. Sections 4, 5.2, 5.3, Section 7
What is wrong:
- Every rating, every disagreement code and every audit comes from Claude models. Section 7 admits this. Two runs of one model with the same prompt are not two independent raters. Alpha is computed on 32 and 106 pairs with no interval. Alpha of 0.70 on levels is below the 0.80 level usually asked for reliability, yet the text and abstract call the result repeatable.
- The ordinal alpha treats "the five evaluative levels as an ordinal scale". Contradicted and Undocumented do not sit on a scale with Claimed, Documented and Verified, and the order used is not given.
- The 80% Part B figure includes 17 agreeing N/A pairs. Four of these are B14b, which is N/A in all sessions by prompt design (Section 4.2). Without the N/A pairs the level agreement is 82 of 106, which is 77%.
- The check outcome field is defined as what a verification check found. In Study 2 no check ran, so values such as "outcome failed" on B28a (Table 5, both runs, line 50) come from reading code. Table 5 also shows level Documented with outcome failed, a combination Section 3.3 does not define. The Tier 3 decision therefore rests on a field whose meaning in these sessions is unclear.
- The audit checks that a quote exists and supports the rating, performed by a model from the same lineage. "0 fabricated quotes" says little about whether the ratings are right. There is no human audit and no benchmark with known defects against which MESA is scored.
- MESA is never compared with the frameworks on the same task. Study 1 measures framework disagreement and Study 2 measures MESA repeatability. Taken at face value, BetterBench and Scorecard repeat at 90% and 91% on concerns, and MESA at 67% on level plus outcome. The measures differ, and the paper does not say which is better.
Why it matters: Soundness is the third criterion, and the paper gives no basis to say MESA gives better or more reliable verdicts than what it replaces.
Fix: Add human raters (at least two requirements engineers or benchmark maintainers) on a subset, report agreement with intervals, apply the same measure to MESA and to the frameworks, add benchmarks with documented defects as ground truth, and remove N/A pairs from headline figures.

###### W5 (decision). RQ2 and the main story in Section 6.1 do not follow from the data. Sections 5.1, 5.2, 6.1
What is wrong:
- RQ2 asks how completely items can be unified. The answer is "zero unmapped items", but the 30 concerns were built bottom up from the same 280 items by one author plus an unnamed assistant (Section 3.2). Zero unmapped follows from the procedure. There is no check of mapping quality.
- Section 6.1 says the checklists disagree "largely because they conflate unreported documentation with negative test outcomes". By Section 5.1 the missing documentation rule accounts for 42 of 143 disagreements (29%), and item granularity for 50 (35%).
- The granularity effect comes from the paper's own aggregation rule (strict conjunction). Under the majority rule, agreement drops from 53% to 49%, which is the opposite of what the granularity explanation predicts. The text does not discuss this.
- The comparison of 210 answers with unreported against 13 contradictions has different bases. All sessions were read only with no code execution (Section 4.1), so few contradictions could be found. The 13 count log lines over six cells (Section 5.2 and Section 7). The ratio shows how the protocol was run, not how the frameworks behave.
- The OECD facets are a descriptive classification (Section 2.3 says raters agree more on these), yet Section 3.2 recodes them as Satisfied or Unsatisfied and includes them in the agreement figure. ECBD questions are open ended and are recoded by a rule ("Satisfied when evidence is cited").
- The 117 of 221 pairs on B01 to B16 plus 17 of 19 on B18 and B19 leave 62 comparisons unreported, and these agree on 25 (40%).
Why it matters: The motivation for MESA and the claim to relevance both rest on this reading of the data.
Fix: Rewrite the claims to match the coded causes, report agreement for each framework pair and each concern, report results by recoding rule, and drop or justify the OECD and ECBD recoding.

###### W6 (decision). Fit with the special theme and the claim of speed are not supported. Abstract, Section 1, Section 6.1
What is wrong: The first sentence says the bottleneck "shifts upstream to validating whether candidate models satisfy system requirements" and cites [11], a mapping study on RE for AI based systems (2024) that does not make this claim. No source shows that teams use benchmark scores as acceptance evidence in the way described. The paper says automated review works "at AI speed" but reports only a cost of 2.23 USD for eight sessions. It reports no time, no human effort and no effect on any requirements cycle. The theme asks about RE in high velocity development with AI assisted coding. The paper handles model selection, with a saturated function level benchmark as the running case.
Why it matters: Relevance and fit decide the position of this paper among submissions on the theme.
Fix: Show evidence for the practice (practitioner data, a source on procurement), measure review effort with and without MESA, and use a benchmark from AI assisted coding in the example.

###### W7 (decision). The HumanEval running example may not show what the paper says, and the rubric definition does not fit it. Section 1, Section 3.3, Table 5
What is wrong: The central example (execution script runs untrusted code with exec() in the same process, versus the paper's gVisor sandbox) is cited only to the repository [21]. The HumanEval paper is not in the reference list. As I recall the released script, the exec line is commented out by default behind a warning that users should sandbox the run themselves. I could not open the file under my review rules, so I mark this as a recollection. If it is right, the repository does not contradict a claim of the paper, it only releases a different artifact, and the rating "Contradicted" would be wrong. Separately, Section 3.3 defines Contradicted as a claim contradicted by an artifact, while the abstract and RQ2 treat it as "located defects". A defect without a claim (a weak assertion) has no home in the definition.
Why it matters: If the headline example is mis rated, so are the claims it illustrates, and the study of 13 contradictions inherits the same question.
Fix: Cite the HumanEval paper, quote the exact line and comment, state the version, and define defect and contradiction separately.

###### W8 (minor). Terms and numbers are used inconsistently. See Section 6 for the list.
Examples: "Contradicted" versus "defect"; "protocol", "framework", "checklist" and "instrument"; four names for the missing evidence state (Undocumented, unreported, Open, Inquiry Required); concern C07 called "Scoring Validation", "Harness Gaming" and "Exploit checks". Fix: one glossary, one term per idea.

###### W9 (minor). LLM guidelines and reporting. Section 4
What is wrong: The call recommends the LLM Guidelines Initiative. The paper gives model names and "medium effort" only. It gives no model identifiers, dates, temperature or sampling, no prompt text and no statement on how the assistant that drafted the mapping was used. "Claude Fable 5.1" is not a name I can check, so the setup cannot be reproduced from the paper. The paper names the SIGSOFT "Empirical Standard for Standards and Taxonomies" without a citation, and I could not identify a standard of this name. Fix: follow the guidelines, report the items they list, cite the standard exactly.

###### W10 (minor). Benchmark selection and scope. Section 4.1, Section 7
Four benchmarks with no stated selection rule. HLE and TruthfulQA are question sets, so "four frozen Python benchmark snapshots" (Section 7) is not accurate. Caliper is part of the 280 items and the mapping but is never applied, so six of the seven frameworks are tested. Fix: give a selection rule and add benchmarks for coding agents.

###### W11 (minor). Layout and presentation.
Equation 3 on page 12 runs past the right margin. The abstract holds about 20 numbers and the Contribution paragraph gives no limitations, which the call asks for. Table 1 has two unlabelled count columns ("Paper" and "Items"). Fix: shorten the abstract, add limits to the last paragraph, label the columns.

##### 5. Questions for the authors

- Q1. What is a requirement on a foundation model in your approach, who writes it, and how does it lead to the profile {B01, B03, B07, B14b, B28a}? Show the steps from a stakeholder need to Table 5.
- Q2. Why should a located harness defect (B28a) make a pass@1 score inadmissible for a model that does not tamper with the harness? Would you weight defects by relevance to the requirement?
- Q3. In Study 2 no check ran. What does "outcome failed" mean in those sessions, and how is Documented with outcome failed defined?
- Q4. Which human raters could reproduce a subset of the ratings, and what agreement would you accept as enough?
- Q5. Why does the majority rule lower agreement (148 of 302) if granularity causes the disagreement?
- Q6. What is the "assistant" in the mapping step (a model, which one)? How many authors map the items, given "the author" in Section 3.2?
- Q7. The RTM is claimed as a contribution but built in "companion work". Is that work under review at this or another venue, and what does this paper add?
- Q8. The data statement lists "26 study session logs" while the paper describes 28 sessions. Which are missing?
- Q9. What do the 54 "plausible absences" in the audit consist of, given that only 28 ratings are described as resting on absent information?
- Q10. How long does a MESA review take with and without the model, and what would a requirements engineer do differently with the result?

##### 6. Checks I made

Arithmetic that adds up:
- Table 3: every row and column sums to the stated totals, and the grand total is 386. Links minus items (386 minus 280) is 106.
- 159 plus 143 equals 302; 159/302 is 52.6%; 143/302 is 47%. 50 plus 42 plus 42 plus 8 plus 1 equals 143; 92/143 is 64%.
- 711 answers equal 188 + 80 + 272 + 72 + 55 + 44, which uses 47 items for BetterBench and 44 for ABC. 41 + 123 + 23 + 12 = 199; 199 plus 11 BetterBench "score 5" answers equals 210. 13/711 is 1.8%; 9 + 2 + 2 = 13.
- Study 2: 8 criteria times 4 benchmarks times 2 runs gives 64; 31 times 8 gives 248; 124 pairs and 32 pairs are right. 26/32, 99/124, 83/124, 101/124 and 94/124 round to the stated percentages. 21 + 5 + 2 = 28. Audit categories for Part B (159, 54, 29, 6) sum to 248; Part A (55 and 9) to 64.
- The 100 differences in mapping split as 56 + 28 + 4 + 12 = 100; the criteria split (8 + 31 = 39) and the 11 terms in Table 2 are right.

Counts that do not add up or conflict:
- Section 3.2 and Section 7: the draft matched on 180 items, and the reconciliation kept the draft on 56, so the draft matches 236, not the stated 234 of 280.
- Table 1: the "Paper" column sums to 277 and the "Items" column to 280. The abstract and the introduction say "280 published items", but only 277 are items in the published papers.
- Data Availability: "26 study session logs". The paper describes 18 + 2 + 8 = 28 sessions, plus one pilot.
- Section 1 says BetterBench "awards its maximum score" on its validation item for HumanEval. Section 3.2 says BB-12 scored 10, which the recoding rule maps to "Satisfied (partial)"; 15 is the top value.
- Section 1 says Scorecard marks "four of its eight scoring items"; Section 3.2 lists SC-65 to SC-68 and Table 3 gives 12 Scorecard links in scoring.
- Audit: 54 "plausible absences" against 28 ratings described as resting on absent information, of which 6 were contradicted. The 35 N/A ratings may explain part of this, but the text does not say.
- 46 of 248 ratings are Verified although no session ran a check, and 11 of these are described as weaker.
- Section 6.2 defines C as B01 to B04; Table 5 and the text use five criteria.
- The abstract lists three contributions; the introduction lists four.
- "No single concern is covered by all seven frameworks (Table 3)": Table 3 is organised by stage, not by concern, so it cannot show this.

Terms used inconsistently:
- Framework, protocol, checklist, instrument, standard (MESA has no normative status).
- G_AI as "capability requirement" and as goal.
- Verdict (Tier 2), Decision (Tier 3, Table 2) and Status (Equation 3); Decision also names Accept, Reject and Inconclusive (Equation 4).
- Answer, rating, classification, judgment; session, run, repetition.
- Contradicted (claim against artifact) versus located defect.
- C07: "Scoring Validation" (Section 1, 3.2), "Harness Gaming" (Table 3), "Exploit checks (accept wrong fix)" (Table 4). B05 and B28a concern scoring accuracy, yet Section 2.2 places them under extrapolation and decision, so the mapping to Kane's stages looks arbitrary.

Claims without support:
- The shift of the bottleneck (cited to [11], which does not state it); that teams use benchmark scores as acceptance evidence; "at AI speed"; "disagree ... largely because they conflate".
- That the exec() example contradicts the HumanEval paper (see W7).

References:
- I checked by search that these exist: [4], [6] partly, [9], [10], [11], [14], [17], [20], [22] to [26], [28]. Most details match.
- [5]: arXiv 2501.10711 exists, and the versions I could find carry the title "How Should We Build A Benchmark? Revisiting 274 Code-Related Benchmarks For LLMs". The title in the list ("Code benchmarks should prioritize rigor, reliability, and reproducibility", version 5) could be a later version, and I could not confirm it.
- [16]: the arXiv versions I found are titled "Benchmarking AI Models in Software Engineering: A Review, Search Tool, and Enhancement Protocol". The list gives "... and unified approach for elevating benchmark quality". Check the title.
- [2]: I could not confirm the DOI or the page range for Alonso and Church in SIGIR Forum 58(2).
- [1], [18], [21] are repositories. The HumanEval paper (Chen et al.) and the TruthfulQA paper are missing, although the text speaks of "its paper". [1] is a repository, not a published framework.
- I found no sign of invented references, so desk rejection for hallucinated references does not apply.

Rules:
- Page limit: 15 pages including references, which meets the technical design limit. LNCS layout looks right apart from Equation 3 on page 12 running into the margin.
- Abstract: four labelled paragraphs in the required order, but the Contribution paragraph gives no limitations.
- Keywords follow the abstract.
- Anonymity: no names or affiliations ("Anonymous Author(s)", "contact@example.org"). The "companion work" is not cited as "A. Anonymous". "The author" in the singular (Section 3.2, Section 7) sits oddly next to "Authors".
- Data Availability Statement: present and at the end. It names an anonymised repository that I did not open. The session log count does not match (see above). It gives no information on model versions or prompts, and does not say whether benchmark snapshots can be redistributed.
- Generative AI: the use of an "assistant" in the mapping is not described, and the LLM guidelines are not followed (W9).

##### 7. Score

Reject.

##### 8. Reviewer confidence

Medium: I know requirements engineering and empirical standards well, but I know the benchmark quality literature less, and I did not open the replication package or the HumanEval files.

##### 9. Recommendation

I recommend rejection. The idea of keeping missing evidence apart from found defects is useful, and the mapping effort and the open reporting of weak results count in the paper's favour. As submitted, the paper is a benchmark auditing method with little requirements engineering content, and its evidence does not support the claims. All ratings, codings and audits come from one model family, the check outcome field has no defined meaning when no check ran, RQ2 holds by construction, the main explanation for disagreement is stronger than the coded causes, and the RTM is a sketch with one row. Several counts conflict (234 versus 236, 26 versus 28 logs, "maximum score" versus partial).

The smallest set of changes that would move my score up one step, to weak reject:
1. Fix the conflicting counts and statements listed in Section 6 and rewrite Section 6.1 to match the coded causes (29% missing documentation rules).
2. Add a human rating of a subset by at least two people, report agreement with intervals and without trivial N/A pairs, and define what the outcome field means in sessions without executed checks.
3. Replace the title and add the RE foundation: prior work on requirements for ML components, component selection against requirements, traceability and assurance, plus one worked example from a requirement to a gate decision on a coding agent benchmark with a named model.
4. Cite the HumanEval paper and quote the exact artifact lines behind the example, or change the example.
Weak accept would need the RTM evaluated with practitioners and a comparison of MESA with the original frameworks against known benchmark defects.

---

### MESA paper: reviewer for empirical methods

#### REFSQ 2027 research track: review of "Unifying Benchmark Evaluation Protocols: A Meta-Evaluation Standard for Artificial Intelligence in Requirements Engineering" (MESA)

Reviewer role: empirical methods. Files read: the call, the PDF (15 pages) and its text extraction. A web search was used only for a few reference checks (Section 6).

##### 1. Summary of the paper

The paper takes seven published checklists for reviewing AI benchmarks (BetterBench, ECBD, Scorecard, How2Bench, ABC, Benchmark Caliper, OECD facets). It transcribes their 280 items and maps them to 30 "concerns" (386 links). From these it derives a 39 criterion rubric called MESA: 8 descriptive criteria (Part A) and 31 evaluative criteria (Part B). Part B ratings combine an evidence level (Claimed, Documented, Verified, Contradicted, Undocumented, Not applicable) with a separate check outcome (passed, failed, not performed, not recorded). The aim is to separate "unreported" from "located defect". A conceptual Requirements Traceability Matrix (RTM, Eqs. 2 to 4) gates acceptance of a model on a benchmark score (Inadmissible, Inquiry Required, Admissible).

Two studies are reported, and every rater in them is a language model.
- Study 1: Claude Sonnet 5.5 (Claude Code, medium effort, read only tools) applied six of the seven frameworks to four benchmark snapshots (HumanEval, TruthfulQA, HLE, tau-bench) in 18 sessions. The authors report that frameworks agree on 159 of 302 pairwise concern comparisons (53%). A second model ("Claude Fable 5.1") coded the cause of the 143 disagreements; 92 are attributed to item granularity (50) and missing documentation rules (42). They also report 210 of 711 answers carrying an "unreported" qualifier against 13 "contradicted" answers.
- Study 2: the same model applied MESA twice to each benchmark. The authors report 26/32 matching Part A classifications (nominal alpha 0.80), 99/124 matching Part B levels (ordinal alpha 0.70) and 83/124 matching level plus outcome pairs. The second model then audited all 312 judgments against the sources: 159/248 Part B ratings "directly supported", 54 "plausible absences", 29 "weaker support", 6 "contradicted absences", 0 fabricated quotes.

The paper claims that MESA separates absent reporting from located defects, that it is repeatable, and that it can feed an RTM design for requirements decisions about AI components.

##### 2. Paper category under the call

The paper does not name a category. The best fit is a Technical design paper (15 pages): the main contributions are new artifacts (rubric, three tier verdict scheme, RTM design) with a preliminary evaluation. It also presents itself as an empirical study (RQ1 to RQ3, "ACM SIGSOFT Empirical Standard"), so a reviewer could equally read it as a Scientific evaluation paper. I assess it as a design paper and note where the other reading is harsher. Criteria in the order the call gives:

1. Novelty: moderate. A synthesis of existing checklists is not novel in itself, and the call says lack of novelty alone is no ground for rejection. The one new idea is recording evidence level and check outcome separately so that "not reported" is distinct from "found defective". That idea is conveyed clearly in Sections 3.3 and 5.2, but the paper's own data barely exercise it (W2).
2. Potential impact and relevance: weak to moderate. The link to the REFSQ theme ("Aligning RE and AI Velocity") is thin. The benchmarks are generic model benchmarks, not RE benchmarks. The RE content is Section 2.1 (Jackson and Zave notation, Eq. 1, which is never used again) and the RTM, which is conceptual and whose "executable implementation and empirical case evaluation" is deferred to "companion work" (Section 6.2). No practitioner is involved.
3. Soundness: weak. All raters and coders are one model family with no human reference. The mapping is reconciled by one author plus an unnamed assistant. Agreement statistics are pooled and inflated. The RTM equations are partly inconsistent with the rubric. See W1 to W8.
4. Verifiability: partial. A replication package is promised but not visible to me, and the text gives too little detail to repeat the work (prompts, versions, snapshot identifiers, concern list). The Data Availability Statement conflicts with the text on the number of logs (W7).
5. Presentation: dense and number heavy. The abstract has about 20 figures. Key definitions are scattered, and Table 3 does not list the 30 concerns.

Under the Scientific evaluation reading, soundness would be judged against the Empirical Standards for the method used. The paper cites no Empirical Standards document in its references and does not state which standard it follows (Section 6).

##### 3. Strengths

- S1. The question is worthwhile. Benchmark scores are used as acceptance evidence, and separating "not reported" from "contradicted by an artifact" is a real measurement problem. Connecting this to Kane's argument based validity is sensible.
- S2. Clear counting. Most totals reconcile (Section 6): Table 3 row and column sums, 280 items, 711 answers, 312 judgments, 143 disagreements.
- S3. Honest limitations section (Section 7). It states that agreement measures "algorithmic repeatability" and not human reliability, that the concern taxonomy comes from one author plus an assistant, and that the 13 contradictions are log instances.
- S4. Useful design choices: freezing the rubric before the main sessions, a pilot on a synthetic benchmark, first attempt completion reported, an audit that checks cited quotes against sources, and a sensitivity check for the aggregation rule (49.0% vs 52.6%).
- S5. The audit reports its own failures: 6 absences contradicted by the sources and 29 weaker support ratings are not hidden.
- S6. The abstract follows the required four paragraph structure, the page limit is met (15 pages including references), and a Data Availability Statement exists.

##### 4. Weaknesses

###### W1 (decision). The raters, coders and auditor are all language models of one family, with no human reference standard (Sections 4.1, 4.2, 5, 7)
What is wrong: Study 1 answers (711), Study 2 ratings (312), disagreement coding (143) and the source audit are all produced by Claude models ("Sonnet 5.5", "Fable 5.1 subagent"). Limitations admit "without human raters". No human gold set exists for any unit. "Agreement" therefore measures run to run stability of one stochastic process. It does not measure whether a rating is correct, or whether two human experts would reach the same verdict. The reviewer model was probably trained on HumanEval, TruthfulQA, HLE and tau-bench repositories and papers, so contamination of the "reading" cannot be excluded. The auditor shares the family with the reviewer (self preference, shared blind spots), and its own accuracy is never checked. The LLM guidelines recommended in the call are not followed: no temperature or sampling settings, no exact model identifiers or dates, no prompt text in the paper, no handling of non determinism beyond one repeat, no human validation of model outputs. "Medium effort" is a tool setting, not a reproducible parameter.
Why it matters: RQ1 (frameworks disagree), RQ2 and RQ3 rest on this data. Without a human check, the headline numbers cannot be separated from model behaviour.
Fix: have two or more human experts independently rate a stratified sample (for example 2 benchmarks, all criteria) and report human to human and human to model agreement. Have a human check a random sample of the audit judgments and report the auditor's accuracy. Report exact model identifiers, sampling settings, prompts and dates in the paper.

###### W2 (decision). The central distinction (located defect vs unreported) is barely exercised and is not repeatable in the paper's own example (Sections 5.2, 5.3, Table 5)
What is wrong: In Study 2 only 2 of 248 Part B ratings are Contradicted, and the one shown in detail (B28a on HumanEval) was rated Contradicted in run 1 and Documented in run 2 (Table 5, Section 6.2). Run 2 also has check outcome "failed" with level "Documented", which contradicts Section 3.3, where "failed" is the result of a verification check. The Inadmissible status is reached in both runs only because Eq. 2 lets either "Contradicted" or "outcome failed" trigger it. That redundancy hides the disagreement on the very distinction the paper sells. In Study 1 the "13 contradicted answers" come from native frameworks (Scorecard, BetterBench, ABC) that have no "Contradicted" value. How an answer became "contradicted" is not explained. The comparison "210 vs 13" is also a product of the review mode: sessions had no code execution (Section 4.2), so located defects can rarely be found, while reporting gaps are found easily. Further, ECBD (80 answers) and OECD (72) can never carry the qualifier by the recoding rules, and 13 contradictions come from three frameworks only, so 711 is not a common denominator. The rate among eligible answers is about 210/559 = 38%, not 30%.
Why it matters: the abstract and Section 6.1 present "210 vs 13" as evidence that frameworks "conflate unreported documentation with negative test outcomes". This is not supported (see also W4).
Fix: report, per framework and per benchmark, how many answers could have carried each label. Include human validated defect cases (for example known HumanEval harness issues, seeded defects) and report whether MESA and the native frameworks detect them. Report agreement on Contradicted vs Undocumented specifically.

###### W3 (decision). Reliability statistics are pooled, inflated and partly ill defined (Section 5.3, Abstract)
What is wrong:
- Alpha is computed over pooled units from different criteria with different category sets (Part A has 8 criteria, some free text: "23 exact text matches" yet 26 matches). Pooling inflates chance corrected agreement. With 81% raw agreement, alpha 0.80 implies expected agreement near 6%, which is implausible for criteria with 2 or 3 categories (A02, A03, A04, A07, A08). The coefficient should be per criterion, or with a clearly specified pooled coding.
- Three of the 26 "matches" are not exact text matches. The matching rule is not given.
- 80% Part B agreement (99/124) includes 17 trivial Not applicable pairs (B14b is N/A by construction in all runs). On the 106 applicable pairs the figure is 82/106 = 77%.
- The ordinal alpha (0.70) treats five levels as ordinal, but Contradicted and Undocumented have no defined position (Eq. 2 uses "level >= Documented" and "level >= Verified", which orders only Claimed < Documented < Verified).
- Scope matching 124/124 (100%) suggests a constant or templated field.
- n = 32 and n = 106 units, no confidence intervals, units not independent (same benchmark, same criterion family, same model).
- Level plus outcome agrees on only 67%, and this is relegated to the last number in the abstract.
- "Part B evidence levels and fields matched on 99 of 124" is ambiguous (levels only, or levels and fields?).
Why it matters: RQ3 is answered mainly by these numbers.
Fix: compute alpha (or Gwet's AC1, kappa) per criterion and per benchmark with bootstrap intervals; exclude N/A pairs from the headline; define the ordinal order or use nominal alpha; report the level only, outcome only and joint figures in one table; state matching rules.

###### W4 (decision). The RQ1 design confounds frameworks, benchmarks and model noise, and the headline numbers are not interpretable as framework conflict (Sections 4.1, 5.1)
What is wrong:
- Frameworks are not crossed with benchmarks: BetterBench, ECBD, Scorecard and OECD ran on all four, but How2Bench only on HumanEval and ABC only on tau-bench, and Caliper never. So "seven frameworks" in the abstract and title are six in the data, and 28 of 280 items (Caliper) never entered Study 1.
- The unit of analysis, "pairwise concern comparison" (benchmark x concern x two frameworks, both Satisfied or Unsatisfied after recoding), is not independent: a framework appears in many pairs, compound items feed several concerns, one reviewer session produces all answers for a benchmark. The 302 are the result of dropping all pairs where either side is Open; the dropped number and the possible maximum are not reported.
- The within framework noise floor is 90 to 91% (BetterBench 19/21, Scorecard 20/22 on HumanEval only), so 9 to 10% of disagreements arise with the same framework and same model. No human applied baseline exists, so the 47% disagreement mixes real framework differences, model variation and the authors' own recoding.
- The disagreement causes depend on the authors' aggregation rule (strict conjunction). "Item granularity" causing 50 disagreements follows partly from that rule. The sensitivity check only reduced agreement (49.0%) and did not test other rules, or the BetterBench mapping (10 to "Satisfied, partial").
- The recoding is called "deterministic", yet "Unsatisfied (with -r when unreported)" requires a judgment of whether the negative answer is due to silence. Who decides this?
- Breakdown reported selectively: B18 and B19 agree on 17/19; B01 to B16 on 117/221. The remaining 62 pairs show 159 - 17 - 117 = 25 agreements (40%), unreported.
Why it matters: the claim that published frameworks "frequently reach opposite conclusions" is the motivation for the whole paper.
Fix: cross frameworks and benchmarks fully (or restrict to the common set), have humans apply at least one framework on a subset to get the noise floor, report the pair frame, add cluster robust intervals, vary the recoding rules, and list the 62 pairs left out of the breakdown.

###### W5 (decision). Mapping, taxonomy construction and the "completeness" result are not independent evidence (Sections 3.2, 5.2, 7)
What is wrong: The concerns were "grouped bottom-up" from the 280 items, then RQ2 reports that all 280 map with "zero unmapped items". That is true by construction and does not answer "how completely can framework questions be unified". The mapping was drafted by an unnamed assistant (a model?), then reconciled by "the author". The two matched on 180 of 280 items (64%) before reconciliation; 100 differed, of which only some are "compound secondary" (76 items are compound, so at least 24 differ on the primary concern). No agreement coefficient and no second human. The text says the final mapping matches the draft on 234 of 280 items, but 180 + 56 (draft kept) = 236, so the arithmetic is off by 2 (unless two kept items were revised later). Item counts are not comparable across frameworks: Scorecard's 68 "items" are 22 principles plus 46 sub-bullets (parents and children both counted), and Scorecard supplies 272 of 711 answers and 123 of 199 failing answers. OECD facets are classification facets (descriptive), yet they supply 32 links and "evaluative" verdicts. Part A (C30) is built from OECD alone, so it unifies nothing.
Why it matters: every downstream number (386 links, 302 pairs, 711 answers) depends on this mapping.
Fix: have two humans independently map a sample, report kappa on primary concern and on link sets, publish the full 30 concern list with item level mapping, handle parent child items explicitly, and drop "completeness" as a finding.

###### W6 (decision). The source audit shows weaker support than the paper concludes, and the unit "quote found" is trivial (Section 5.3)
What is wrong: Only 64% of Part B ratings (159/248) and 86% of Part A (55/64) are "directly supported"; 68.6% of all 312 judgments. 29 are "weaker support", including 11 of 46 Verified ratings (24%). Six of the reviewer's "Undocumented" claims were false (information existed in sources). "0 fabricated quotes" is checked on 286 quotes and could be checked by a string matcher; the abstract's "0 fabricated" is a weak result next to the 36% not directly supported. The categories "plausible absence" and "weaker support" are defined by the model auditor with no rubric given. The counts for absence do not reconcile: "28 ratings resting on absent information" (21 Undocumented, 5 Claimed, 2 Documented) versus 54 plausible plus 6 contradicted absences = 60 (and 35 Not applicable). A rating "Documented" or "Claimed" that "rests on absent information" contradicts the definitions in Section 3.3. 46 Verified ratings in sessions with no code execution also need explanation, because Section 3.3 defines Verified as a check carried out or reported with coverage and limits.
Why it matters: RQ3 asks whether ratings "can be verified against repository code". The answer is "mostly, according to another model".
Fix: have humans re-judge a sample of audit categories; give the audit rubric; reconcile the 28 vs 60 counts in one cross tabulation (reviewer label x auditor label); state what Verified means under static inspection.

###### W7 (decision for verifiability, otherwise minor). Replication from the description is not possible, and the Data Availability Statement is inconsistent with the text
What is wrong: Missing in the paper: prompts, tool definitions, repository commit hashes or snapshot dates (the benchmarks are cited only as repositories [18], [21], [26], and HLE by arXiv), the full list of 30 concerns, per criterion rules for B01 to B29 (Table 4 shows 9 of 31), how Part A categories were allowed to vary, the pilot, the exact model identifiers, and the CI method in Eq. 4. The Data Availability Statement promises "26 study session logs", but the study has 18 + 2 repeat + 8 = 28 sessions (plus the pilot). It is unclear whether the 2 repeat sessions are withheld. It also promises four benchmark snapshots, but redistribution of HLE and TruthfulQA data may be restricted (licence statement missing). "REFSQ 2027 Open Science Policy" is not named in the call summary. No link or placeholder is given, so I could not inspect the package. A total API cost of 2.23 USD for eight sessions (about 0.28 per session) over four benchmarks suggests shallow repository reading, which is not discussed.
Fix: put prompts and the concern list in an appendix or the package, state the exact commits, correct the log count, address licensing.

###### W8 (minor to decision, formal). The RTM (Section 6.2, Eqs. 2 to 4, Table 5) is conceptual, internally inconsistent, and is claimed as a contribution
What is wrong: Evaluation is deferred to "companion work" that is not cited (the call asks for a placeholder such as "A. Anonymous" for non public work), which also raises an overlap question the call does not regulate. The abstract counts the RTM among three contributions, while the introduction lists four. Internal problems:
- "C (B01-B04)" are the construct criteria, but R1's profile contains B01, B03, B07, B14b, B28a, and B07, B14b, B28a are not in B01 to B04.
- Eq. 2 labels N/A only if Active(c) = 0, yet Table 5 rates B14b N/A "in session (no model named)" while the text says it "flags inquiry"; by Eq. 2 an active criterion without a rating is Inquiry Required.
- Located defects under B05/B07 should be removed as task level defects (T'_r = T_r minus D(c)), but by Eq. 2 any located defect makes the criterion Inadmissible before tasks are removed, so the task removal branch is never reached.
- Cov(c, r) takes the union of a task set and a configuration and tests it for inclusion in a scope, mixing types; n_min, alpha and the interval method are unspecified.
- Table 5 is a single entry from one benchmark, built from the same sessions that produced the disagreeing ratings.
- Eq. 1 uses undefined O_bench and is never used. Jackson and Zave's W, S |- R is not instantiated (no S).
- The section 6.1 statement that the approach works "at AI speed" has no timing or effort data.
Why it matters: relevance to REFSQ rests largely on this section.
Fix: either remove the RTM from the contributions and call it a sketch, or evaluate it (even with a small practitioner study), fix the notation, and cite the companion work anonymously.

###### W9 (minor). Claims in the text are inconsistent or unsupported
- Introduction: BetterBench "awards its maximum score on its single validation item"; Section 3.2 traced example: BB-12 "scores 10" (maximum is 15 in the recoding rule).
- Section 6.1 says disagreements arise "largely because they conflate unreported documentation with negative test outcomes", but the paper's own coding attributes 42 of 143 (29%) to missing documentation rules.
- "No single concern is covered by all seven frameworks (Table 3)": Table 3 is aggregated by stage, not by concern, so it cannot show this.
- Conclusion reports 81% and 80% repeatability but omits 67% for level plus outcome and that 80% includes N/A pairs; "independent source auditing" is by the same family.
- The abstract Contribution paragraph lacks the limitations the call asks for there.
- HumanEval characterization: the paper says the script runs candidate code "in the same Python process and namespace as the test assertions". The released script, as far as I recall, runs checks in a child process via multiprocessing with a reliability guard, and the exec call is shipped commented out with a warning. I could not verify this because the fetch failed, so I flag it as a point for the authors to check. The central running example (Table 5, B28a Inadmissible) depends on it. The HumanEval paper (Chen et al.), which the text says describes gVisor, is not in the reference list; [21] is only the repository.
- The Limitations call HLE a "Python benchmark".
- "Decision" names both the Tier 3 gate status and the Accept/Reject score decision; "Verified" is both a level and, in the introduction, linked to outcome "failed", which Section 3.3 defines only for executed checks.

##### 5. Questions for the authors

- Q1. What do human experts conclude? Can you report human to human and human to model agreement on a sample of Study 2 ratings, and the auditor's accuracy against humans?
- Q2. Which model produced the "assistant pass" for the 280 item mapping? Why do 180 + 56 draft matches give 236, not 234?
- Q3. How was an answer from a native framework (Scorecard, BetterBench, ABC) labelled "contradicted" in Study 1, given that these frameworks have no such value? Who or what decided "unreported" in the "deterministic" recoding?
- Q4. How is alpha computed (pooled or per criterion, which coding of the free text Part A fields, which matching rule for the three non exact matches, which order for the ordinal levels)? Please give per criterion values with intervals.
- Q5. How many (benchmark, concern, framework pair) combinations were possible, and how many were dropped because a side was Open? What are the agreement figures for the 62 comparisons outside B01 to B16 and B18 to B19?
- Q6. How does MESA's repeatability compare to the 90 to 91% of BetterBench and Scorecard on the same unit (concern verdict)? MESA's Part B level agreement (80%, or 77% excluding N/A) is lower.
- Q7. How can the 28 ratings "resting on absent information" (with Claimed and Documented among them) be reconciled with the 54 plausible plus 6 contradicted absences in the audit? What does "Verified" mean without code execution?
- Q8. Is the HumanEval characterization (shared process and namespace) correct for the released script? Run 2 of B28a gives "Documented" with outcome "failed": by which rule?
- Q9. Where are the 2 repeat sessions in the "26 session logs"? Are the benchmark snapshots redistributable under their licences?
- Q10. What is the companion work, and how does it overlap with Section 6.2?
- Q11. What does the study say about RE specifically? Would the results change for benchmarks of RE tasks (elicitation, classification, traceability)?

##### 6. Checks I made

Arithmetic that adds up:
- Table 1 items: 47 + 20 + 68 + 55 + 44 + 28 + 18 = 280. Paper counts: 46 + 20 + 68 + 55 + 42 + 28 + 18 = 277 (text explains 47 vs 46 and 44 vs 42).
- Table 3: rows 10, 46, 58, 173, 99 sum to 386; columns 56, 29, 88, 69, 67, 45, 32 sum to 386; each row and column sum is correct. 386 - 280 = 106 extra links. The Caliper numbers fit the text (28 primary + 17 secondary = 45).
- B-criteria: 29 + 2 splits = 31; 8 + 31 = 39; stage lists add to 29 concerns (2 + 6 + 10 + 11).
- Sessions: 16 + 1 + 1 = 18; answers: 47x4 + 20x4 + 68x4 + 18x4 + 55 + 44 = 711; judgments 8 x 39 = 312 = 64 + 248; pairs 4 x 8 = 32 and 4 x 31 = 124.
- Percentages: 159/302 = 52.6%; 92/143 = 64.3%; 50 + 42 + 42 + 8 + 1 = 143; 148/302 = 49.0%; 143/302 = 47.4%; 17/19 = 89.5%; 117/221 = 52.9%; 19/21 = 90.5%; 20/22 = 90.9%; 41 + 123 + 23 + 12 = 199; 199 + 11 = 210 (29.5%); 13/711 = 1.8% and 9 + 2 + 2 = 13; 26/32 = 81.3%; 99/124 = 79.8%; 94/124 = 75.8%; 101/124 = 81.5%; 83/124 = 66.9%; 55/64 = 85.9%; 159 + 54 + 29 + 6 = 248 and the percentages sum to 100; 246 + 40 = 286; 17 + 17 + 1 = 35 N/A ratings fit 18 N/A pairs; 124 - 18 = 106.
- Abstract numbers agree with the body.

Arithmetic or counts that do not add up, or are inconsistent:
- Mapping: 180 + 56 = 236, text says 234 (Section 3.2, Section 7).
- Session logs: 26 in the Data Availability Statement vs 28 sessions described.
- Absence counts: 28 (Section 5.3) vs 54 + 6 = 60 in the audit (or 35 + 21 = 56 if N/A is added).
- Contributions: three in the abstract, four in the introduction.
- 80% (99/124) includes 17 N/A pairs; 82/106 = 77% on applicable pairs; the unreported rate on eligible answers is about 38%, not 30%.
- Part A: 23 exact text matches against 26 reported matches.
- BetterBench: "maximum score" (introduction) vs "scores 10" with 15 as the top (Section 3.2).

Terms used inconsistently: "Decision" (Tier 3 gate and Eq. 4 outcome); "Verified" and "failed" (Section 3.3 definition vs Table 5 run 2); "evidence levels" six vs five; "frameworks" seven (abstract, title) vs six applied; "Python benchmark" for HLE and tau-bench; "criteria C (B01 to B04)" vs profile in Table 5; "Not applicable" vs "Active(c) = 0".

Claims without support: "Frameworks conflate unreported documentation with negative outcomes ... largely" (Section 6.1); "No single concern is covered by all seven frameworks (Table 3)"; "deterministic recoding" while "when unreported" needs judgment; "AI speed"; "0 fabricated quotes in independent source auditing"; the claim that MESA improves on the frameworks (no comparison on any outcome).

References:
- [9] Evaluation Cards (arXiv 2606.09809): found by search, exists.
- [5] arXiv 2501.10711: the paper exists, but the title I found in search results was "How Should We Build A Benchmark?" (earlier versions); the cited title "Code benchmarks should prioritize rigor, reliability, and reproducibility" (version 5) is not confirmed by my search.
- [16] arXiv 2503.05860: exists; the title found is "Benchmarking AI Models in Software Engineering: A Review, Search Tool, and Enhancement Protocol", while the paper cites "... and unified approach for elevating benchmark quality" (possibly a later version, not confirmed).
- [2] Alonso and Church, SIGIR Forum 58(2): my search did not locate the paper or the DOI; unverified, so I cannot say it exists. Please check.
- [11] Habiba et al.: a mapping study on RE for AI systems (2024); it is cited for the claim that "the engineering bottleneck shifts upstream" with AI coding assistants, which it cannot support. [24] and [2] are cited for the claim that leaderboard scores do not establish requirement satisfaction; this is tangential.
- [25] Wand and Weber (representation theory) is cited as grounding but is not used in the text.
- No reference for the HumanEval paper, for the SIGSOFT Empirical Standards, for the LLM guidelines recommended in the call, or for the companion work.
- My search for a "Standards and Taxonomies" standard among the SIGSOFT Empirical Standards did not confirm that such a standard exists; the authors should cite the exact standard.
- I did not verify the other references (their format and DOIs look plausible). 2026 dated references (several arXiv 26xx IDs, EvalEval 2026, NIST draft) appear plausible but I did not check them all.
- I do not see signs of many hallucinated references.

Rule checks:
- Page limit: 15 pages including references (limit 15). OK.
- Format: appears LNCS. OK.
- Abstract: four paragraphs with the required headings. The Contribution paragraph lacks limitations. Keywords present.
- Anonymity: no author names; "Anonymous Author(s)"; a placeholder email; no obvious self citations. The "companion work" is uncited, and no anonymization placeholder is given. "The author" (singular) in Section 3.2 is acceptable.
- Data Availability Statement: present, but vague (no link or warning), and the log count is inconsistent (W7).
- Generative AI: the paper uses LLMs as research instruments, but does not follow the recommended LLM guidelines. No statement on use of AI for writing or for the "assistant pass".

##### 7. Score

weak reject

##### 8. Reviewer confidence

medium. The methodological problems are visible on paper, but I could not inspect the replication package, and I could not verify the HumanEval claim or all reference details.

##### 9. Recommendation

The paper addresses a real problem and is mostly transparent in its counting, and its limitations section is honest. The evidence does not yet support its claims, however. Every judgment, from the 711 framework answers to the 143 disagreement causes and the 312 audited ratings, comes from one model family, with no human reference. The mapping rests on one author and an unnamed assistant. Pooled and N/A inflated agreement statistics make the repeatability look better than it is, and MESA's repeatability is lower than that of the native frameworks it is meant to improve on. The key distinction between located defects and unreported information is shown on two Contradicted ratings, one of which differs between runs. The RTM is unevaluated and has internal inconsistencies, and the relevance to RE is thin. The smallest set of changes that would move my score up one step (to borderline) is: (1) a human rated sample (at least two experts, a stratified subset of Study 2 and of the mapping) with human to human and human to model agreement; (2) agreement recomputed per criterion, excluding N/A pairs, with intervals and a defined ordinal order, plus a like for like comparison with the native frameworks' repeatability; (3) a cross tabulated reconciliation of the absence counts, the "contradicted" definition in Study 1 and the log count; and (4) either removing the RTM from the contributions or fixing its notation and evaluating it, together with prompts, versions and the concern list in the paper or package.

---

### MESA paper: reviewer for AI evaluation

#### REFSQ 2027 research track: review of "Unifying Benchmark Evaluation Protocols: A Meta-Evaluation Standard for Artificial Intelligence in Requirements Engineering" (MESA)

Reviewer perspective: AI evaluation (benchmarks, measurement validity, evaluation of language models and agents).

Note on method: I read the call, all 15 pages of the PDF and the text extraction. My attempt to check references on the web failed (the fetch tool hit a usage limit, and one DOI lookup failed at the publisher site). So I did not verify any reference online. Where I comment on a reference or on a benchmark fact below, I say what rests on my own knowledge and mark it as unverified.

##### 1. Summary of the paper

The paper proposes MESA, a "meta-evaluation standard" for reviewing AI benchmarks as evidence that a model satisfies a requirement. The authors transcribe 280 items from seven published review frameworks (BetterBench, ECBD, Scorecard, How2Bench, ABC, Caliper, OECD facets). They map the items to 30 "concerns" with 386 links, and derive a 39 criterion rubric (8 descriptive Part A, 31 evaluative Part B). The rubric records an evidence level (Claimed, Documented, Verified, Contradicted, Undocumented, N/A) separately from a check outcome (passed, failed, not performed, not recorded). The paper frames this with Kane's argument based validity, and adds a "Requirements Traceability Matrix" (RTM), a set of rules (Eqs. 2 to 4) that turns ratings into Inadmissible, Inquiry Required or Admissible, and only then compares a score to a threshold.

Two studies use one LLM (Claude Sonnet 5.5, read only file access, no code execution) as the reviewer.

- Study 1: 18 sessions applying six frameworks to four benchmarks (HumanEval, TruthfulQA, HLE, tau-bench). The frameworks "agreed on 159/302 pairwise comparisons (53%)". An LLM coder attributes 92/143 disagreements to item granularity (50) and missing documentation rules (42). 210/711 answers carry an "unreported" qualifier versus 13 contradictions.
- Study 2: eight sessions applying the MESA rubric twice per benchmark. Agreement is 26/32 on Part A (alpha 0.80), 99/124 on Part B levels (alpha_o 0.70), and 83/124 on level plus outcome. An LLM "source checker" finds 159/248 Part B ratings directly supported, 6 contradicted absences and 0 fabricated quotes.

The RTM is shown on one HumanEval example and is not evaluated (the paper says the implementation and case evaluation are in "companion work").

##### 2. Paper category under the call

Best fit: Scientific evaluation paper (15 pages), because the empirical content (Studies 1 and 2) is the bulk of the paper and the authors cite the SIGSOFT Empirical Standard for Standards and Taxonomies. The paper itself reads as a Technical design paper (new standard, rubric, RTM, "preliminary evaluation"). The category is not stated, which is a presentation issue. I assess it under both, in the order the call gives.

Scientific evaluation criteria, in order:
- Soundness: not met. The evidence is one LLM reviewer reading files, with no human reference, no human second rater of the mapping, and pooled, non independent comparisons (W1 to W5).
- Potential impact: partly met. Acceptance gating of benchmark evidence for model selection is a relevant topic under the special theme, but the RE link is thin (W9).
- Verifiability: partly met. A Data Availability Statement exists and claims logs and scripts, but there is no link, the log count is inconsistent, and model identifiers are not verifiable (W8).
- Novelty: moderate. Separating "not reported" from "located defect" is useful. The mapping of existing frameworks is incremental, and related work on benchmark validity is missing (W6).
- Presentation: below standard. Dense, inconsistent labels, many numbers in the abstract, and several internal contradictions (W7).

Technical design criteria, in order:
- Novelty: moderate (see above).
- Potential impact and relevance: moderate.
- Soundness: the RTM rules are internally inconsistent (W5) and the preliminary evaluation does not test the artifact that is claimed as contribution 3.
- Verifiability and presentation: as above.

Under either reading the paper does not clear the bar as submitted.

##### 3. Strengths

S1. The distinction between absent reporting and a located defect is a real problem in benchmark review. Recording evidence level and check outcome as separate fields, and requiring a cited location for a defect, is a sound design idea.

S2. Using the same frozen snapshot for several frameworks is a good design for studying framework disagreement. The paper reports a within framework repeat (90% and 91%), which gives a noise floor, even though it is not used (W2).

S3. The source audit reports weak results openly: only 64% of Part B ratings were directly supported, 11 of 46 Verified ratings had weaker support, and 6 absences were contradicted by the sources. The Limitations section states that repeatability is not human inter-rater reliability.

S4. Part A and Part B separation follows the EFPA test review model, which is a defensible import from psychological test review. The counts in Tables 1 and 3 are internally consistent (see section 6).

S5. The running HumanEval example makes the proposal concrete, and a Data Availability Statement is present.

##### 4. Weaknesses

W1 (decision). The empirical "framework conflict" result is produced by an LLM applying frameworks that were written for humans, and it cannot be separated from reviewer error. Where: Section 4.1, Section 5.1, Limitations. Every framework verdict comes from one model, one run, read only, no code execution, "without altering native prompts". BetterBench, Scorecard and similar tools assume that assessors can run code, read the paper and repo, and sometimes contact authors. The within framework repeat shows 9 to 10% of concerns flip between runs of the same framework, yet disagreement between frameworks (47%) is interpreted as a property of the frameworks. There is no human assessment and no check against published assessments (BetterBench published its own human scores for a set of benchmarks that, to my recollection, includes HumanEval and TruthfulQA; unverified). Why it matters: the headline number (53% agreement) and the causal story (granularity and missing documentation rules) do not support the claim that frameworks "reach contradictory verdicts". Fix: have two or more human experts apply at least two frameworks to the four benchmarks; compare the LLM output against published human scores; report LLM run to run noise per framework and subtract or model it.

W2 (decision). Agreement statistics are unreliable as reported. Where: Section 5.1, abstract. (a) The 302 pairwise comparisons are not independent (same benchmark, concern, reviewer model; each framework appears in many pairs), and no confidence interval is given. (b) A comparison only exists when both frameworks give Satisfied or Unsatisfied, so the denominator depends on how often each framework is mapped to Open; ECBD maps absence to Open and so mostly drops out. (c) The sensitivity check with a majority rule gives lower agreement (148/302, 49.0%), which contradicts the explanation that strict conjunction over many items causes disagreement (50 cases) and is not discussed. (d) The paper reports high agreement on B18 and B19 (17/19) and low on B01 to B16 (117/221). Those two groups cover 240 pairs and 134 agreements, so the remaining 62 pairs (B17, B20 to B29) have 25 agreements (40%), which is not mentioned. (e) BetterBench's 0/5/10/15 scores are cut into Satisfied and Unsatisfied with an arbitrary threshold (5 is Unsatisfied, 10 is "Satisfied (partial)"), and "Satisfied (partial)" is not in the verdict set {Satisfied, Unsatisfied, Open}. Fix: bootstrap by concern and benchmark, report per framework pair counts, justify the cut points and test other cuts, and report agreement with Open treated as a category.

W3 (decision). The 210 versus 13 comparison does not show what the paper says it shows. Where: Section 5.2, Intro, Section 6.1 ("disagree on 47% ... largely because they conflate unreported documentation with negative test outcomes"). (a) The denominator 711 includes ECBD (80) and OECD (72) answers, which cannot carry the "unreported" qualifier under the paper's own rules (ECBD maps absence to Open; OECD is descriptive). On the four frameworks that can (BB 188, SC 272, H2B 55, ABC 44, total 559) the share is 210/559 = 38%. (b) A read only LLM with no execution is structurally unable to find many located defects, so the count of 13 measures the reviewer's detection power, not the rarity of defects in benchmarks. (c) Reporting oriented frameworks ask about reporting by design, so penalizing silence is not a "conflict" with defect finding; they measure different constructs. (d) The causal claim in 6.1 ("largely because") is not tested: the disagreement coder coded 50 and 42 cases, which together are 92, not the 143 disagreements, and "missing documentation rules" are 42, i.e. 29%. Fix: restate the claim as descriptive, report with correct denominators, and add a human located defect set (known benchmark flaws) to estimate detection rates.

W4 (decision). The reliability study of the rubric does not support "repeatability" in the sense a measurement paper needs, and the audit is circular. Where: Section 5.3, Table 5, Limitations. (a) Two runs of one stochastic model are a test retest of the model, not rater reliability; there is no human rater, so there is no evidence that MESA ratings mean what the criteria define. (b) Alpha is reported with no confidence interval on 32 and 106 units; alpha_o = 0.70 is below the conventional 0.80 and the paper sets no threshold in advance. (c) The ordinal alpha treats "five evaluative levels" as ordered, but Contradicted and Undocumented have no defined place on a Claimed < Documented < Verified scale; this is invalid unless justified. (d) Agreement is inflated by structure: 17 of the 99 matches are N/A pairs, and B14b is N/A in all eight sessions because the prompt named no model (4 forced agreements); among applicable pairs agreement is 82/106 = 77%. Scope agrees 124/124, which suggests a degenerate field. (e) The two fields that drive the gate are the least stable: check outcome 76% and level plus outcome 67%. (f) The audit is done by an LLM of the same vendor family as the reviewer, and "0 fabricated quotes" is the easy part (a string match would do); the hard part is that 36% of Part B ratings are not directly supported and 6 of the 21 Undocumented ratings (if all 6 contradicted absences are among them, 29%) were wrong, which is exactly the separation of "absent" from "present" that MESA claims to provide. (g) The 28 ratings "resting on absent information" include 5 Claimed and 2 Documented, and 54 "plausible absences" in the audit exceeds the 21 Undocumented ratings; the categories are not reconciled. Fix: add at least two human raters on a subset (alpha with confidence intervals), define the ordering or use a nominal alpha for Part B, report agreement excluding N/A and B14b, run the audit with a human or a deterministic check, and reconcile the count of absence ratings.

W5 (decision). The RTM and its decision rules (Section 6.2, Eqs. 2 to 4, Table 5) are inconsistent and untested. (a) The text defines C as "B01 to B04", but the example profile is {B01, B03, B07, B14b, B28a}, and Step 1 removes task defects under B05 or B07 while B05 is not in the profile and B14a is omitted. (b) B14b is rated N/A in Study 2 (Active = 0 at rubric level) but treated as "flag inquiry" in Table 5, so Eq. 2's Active(c) has two meanings. (c) Def(c) is "Contradicted OR failed", but Table 5's B28a is Contradicted in run 1 and Documented in run 2; the gate gives the same result only because of the OR. Under the rubric's own Table 4, Documented for B28a means "grading environment described", which is hard to reconcile with outcome "failed" at the same time. (d) A single located defect makes the whole benchmark Inadmissible, with no notion of materiality or effect on scores; most benchmarks have some such defect (HLE label noise, tau-bench task issues, weak HumanEval tests are well known), so the gate would reject almost everything, and a possible exploit vector is treated as inflated scores without evidence that scores are affected. (e) Eq. 4 is a deductive gate on top of Eq. 1, which is declared inductive; the paper does not say how the two fit. (f) The only evidence is one worked example on one benchmark with outputs of the same two sessions; the RTM is called a contribution (abstract, contribution 3) while the implementation and evaluation are deferred to "companion work". Fix: either drop the RTM as a contribution and keep it as a sketch in the discussion, or define it consistently, add materiality and severity, and evaluate it on a set of benchmarks with known outcomes.

W6 (decision). Use of measurement theory is thin and related work is missing. Where: Sections 1, 2.1, 2.2, 2.3. Kane's framework is used as a list of four stage labels. In Kane's approach, validity is judged for a specific interpretation and use, with claims, warrants and backing, but MESA's Part B rates benchmarks generically, and licensing, maintenance and replication are placed under "Decision inference", which is not Kane's usage. No validity argument is built for any benchmark, and "grounded in ... representation theory [25]" (Wand and Weber on ontological expressiveness of modelling grammars) is mentioned once and never used. Messick, Cronbach and Meehl, and Borsboom style validity theory are absent. Missing related work on benchmark quality, validity and contamination (all from my own knowledge, none checked): Raji et al. 2021 (everything in the whole wide world benchmark); Bowman and Dahl 2021; Jacobs and Wallach 2021 (measurement and fairness); Blodgett et al. 2021; Wallach et al. 2025 (evaluating generative AI as social science measurement); Eriksson et al. 2025 (can we trust AI benchmarks); Jacovi et al. 2023 (stop uploading test data in plain text); Sainz et al. 2023 (NLP evaluation in trouble); Oren et al. 2023 (proving test set contamination); Xu et al. 2024 (contamination survey); Zhang et al. 2024 (GSM1k); Liu et al. 2023 (EvalPlus, on weak HumanEval tests); work on SWE-bench quality (SWE-bench+, test insufficiency); and the ABC authors' own finding that tau-bench counts some empty or do nothing responses as success (to my recollection; this directly bears on the paper's tau-bench session with ABC and the claim that only 2 ABC answers were contradicted). Fix: build the Kane argument for at least one requirement with claims and warrants, justify each stage allocation, and position MESA against this literature, especially contamination detection, which MESA treats only by asking whether a check is reported (B14a, B14b).

W7 (decision for presentation, otherwise minor). Whether the rubric measures what it says it measures. Where: Sections 3.3, 5.3, Table 4. The rubric rates reported evidence, not validity. "Verified" is awarded when a verification is "reported or executed", so a read only reviewer can assign it from authors' text; "check outcome" values (passed, failed) are then derived by static reading, without execution, and the Limitations section says so. The rubric therefore cannot separate "absent from the paper" from "absent from the reviewer's access". Check kind includes "run by reviewer", which cannot occur in read only sessions, so I do not know what 81% agreement on check kind means. Several criteria cannot be exercised (B07 dynamic exploit runs, B14b), so 2 of 31 Part B criteria were not operating in the study. Part A categories seem to be free text ("23 exact text matches" out of 26), so the nominal alpha is on loosely defined labels. Fix: define evidence access levels (author reported, statically inspected, executed) as part of the level, remove or relabel outcomes that need execution, and give a codebook with category sets for Part A.

W8 (minor to decision). Verifiability and reporting of the LLM method. Where: Sections 4.1, 4.2, Data Availability. The call recommends the LLM Guidelines Initiative and Springer's AI policy. The paper gives model names ("Claude Sonnet 5.5", "Claude Fable 5.1") but no versions or dates, sampling settings, prompts, tool configuration, repository commit hashes for the four "frozen" snapshots, or how much of each repository the sessions actually read. A total cost of 2.23 USD for eight sessions (about 0.28 USD per session) makes me ask how deeply the tau-bench or HLE repositories were read. The "assistant" that drafted the mapping is not named. A closed model with no open model replication limits verifiability. The Data Availability Statement promises "26 study session logs", but the paper describes 28 sessions (18 + 2 + 8), plus the coder and checker runs. The statement has no link or warning, but it exists. Fix: report the information above, add an open weights replication, and correct the count.

W9 (minor). Link to requirements engineering and the special theme. The RE content is a relabelling (RTM, requirement, traceability) of a benchmark review process. The citation [11] (a mapping study of RE for AI based systems) is used for "the engineering bottleneck shifts upstream"; I doubt it says this (unverified). The leaderboard illusion [24] is about Chatbot Arena rankings, and is cited for the claim that a score "does not establish that a model satisfies a system requirement" (loose, from my knowledge). No practitioner input exists, and the title ("Meta-Evaluation Standard") over claims for something that is a taxonomy and one study. Fix: either evidence the RE use with practitioners or reduce the claims.

W10 (minor). The mapping, the core artifact of the paper, was built by one author with an assistant draft. Initial agreement was 180/280 (64%), with no chance corrected statistic, and no second human. "Zero unmapped items" (RQ2) holds by construction because the concerns were derived bottom up from the same items, so RQ2 is not an empirical result. The six excluded items (BB-45, BB-46, H2B-45, CAL-IC-4, CAL-OO-4, CAL-OC-4) are mapped but not aggregated, which weakens "zero unmapped". Caliper (28 items, 45 links) is cited as a software repository [1], not as a published paper, and was not used in any session; the OECD facets are a descriptive classification, so recoding them as Satisfied or Unsatisfied is a construction of the authors. Fix: second human mapper, report kappa, and say plainly that RQ2 is a design property.

W11 (minor). Factual claims about the benchmarks (tied to the "benchmark facts" check). The HumanEval example (Intro, Section 3.3, Table 5: "line 50", "exec() runs untrusted code in the test namespace") rests on the repository file, and the paper's references list only the repository [21], not the HumanEval paper, although the text repeatedly refers to "the HumanEval paper" (and likewise "the TruthfulQA paper" for [18]). I could not check the repository. From memory (unverified), the released execution script has the exec call commented out by default behind a safety disclaimer, runs each sample in a child process with a reliability guard, and the "not a security sandbox" comment sits in the guard function. If so, the statement "runs untrusted candidate completions via exec()" needs qualification, and the example conflates two separate issues: host security (sandbox) and grading integrity (candidate code sharing a namespace with the test). The paper should quote the lines, give the commit, and separate the two issues. Also, the Introduction says BetterBench "awards its maximum score" on the validation item, but Section 3.2 says that a score of 10 maps to "Satisfied (partial)" and 15 is the top score (Section 3.2 lists scores of 15, 10, 5 and 0).

##### 5. Questions for the authors

Q1. How do LLM sessions with BetterBench and Scorecard compare with the published human scores of those frameworks for the same benchmarks?
Q2. What is the within framework flip rate for all frameworks, and how much of the 47% disagreement remains after accounting for it?
Q3. Why does the majority rule lower agreement (49.0%) if strict conjunction over many sub-items is the cause of 50 disagreements?
Q4. What is the pairwise agreement for B17 and B20 to B29, and how many comparisons were dropped because a framework gave Open?
Q5. Which categories do Contradicted and Undocumented take on the ordinal scale used for alpha_o? What are alpha values and confidence intervals on applicable pairs only, excluding B14b?
Q6. What values did "check kind" and "check outcome" take in read only sessions, and how can "run by reviewer" occur?
Q7. Of the 6 contradicted absences, how many were among the 21 Undocumented ratings? What are the 54 "plausible absences"?
Q8. Which exact lines and commit of the HumanEval execution script were read as "line 50"? Is the exec call active or commented out in that snapshot?
Q9. Why are there 26 logs in the Data Availability Statement when 28 sessions are described?
Q10. What does the RTM add that could not be done with a table of ratings and a manual rule? Where is the "companion work", and does it overlap with this paper (it should be cited as "A. Anonymous")?
Q11. Was the rubric (for example B28a) designed after the HumanEval harness was read? If so, how is HumanEval a fair test?

##### 6. Checks I made

Arithmetic that adds up:
- Table 1 items: 47+20+68+55+44+28+18 = 280. Paper column: 46+20+68+55+42+28+18 = 277 (explained in Section 2.4 by 47 versus 46 and 44 versus 42). Scorecard: 22 + 46 = 68.
- Table 3: each row and each column sums as printed (46, 58, 173, 99, 10; 56, 29, 88, 69, 67, 45, 32) and the total is 386. Links minus items = 106, equal to the sum of the per framework surplus (9+9+20+14+23+17+14). Caliper: 28 primary links plus 17 secondary links = 45, consistent with "13 items with secondary links".
- Criteria: 8 + 29 + 2 splits = 39; Kane stage groups cover 2+6+10+11 = 29 evaluative concerns. Table 2 lists 11 terms as stated.
- 711 answers = 188 (BB, 4 x 47) + 80 (ECBD) + 272 (SC) + 72 (OECD) + 55 + 44. 41+123+23+12 = 199; 9+2+2 = 13; 210/711 = 29.5%; 13/711 = 1.8%.
- 159 + 143 = 302 (52.6%); 50+42+42+8+1 = 143; 92/143 = 64%; 148/302 = 49.0%; 19/21 = 90%; 20/22 = 91%; 117/221 = 53%; 17/19 = 89%.
- 4 x 8 = 32 and 4 x 31 = 124 units, doubled to 64 and 248 ratings; 26/32 = 81%; 99/124 = 80%; 101/124 = 81%; 94/124 = 76%; 83/124 = 67%. The 35 N/A ratings are consistent with 17 agreeing pairs plus one one sided pair. Audit: 159+54+29+6 = 248; 55+9 = 64; 3+2+2+1+1 = 9; 21+5+2 = 28; 2+1+2+1 = 6.

Arithmetic or counts that do not add up:
- Section 3.2: the author matched the draft on 180 items; reconciliation "kept the draft on 56", so 180 + 56 = 236, but the paper (and Section 7) says "matching the draft on 234 of 280". The 100 differences split 56+28+4+12 = 100 correctly.
- Data Availability: "26 study session logs" versus 28 sessions in Sections 4.1 and 4.2.
- Abstract and Section 5.3: "99/124 Part B levels" in the abstract but "evidence levels and fields" in the text; the quantity is ambiguous.
- Source audit: 286 quotes for 312 judgments; the 26 judgments without a quote are not explained.
- The 54 "plausible absences" exceed the 21 Undocumented ratings (see W4).
- The 210/711 share uses a denominator that contains answers which cannot carry the qualifier (38% on 559 answers).

Terms used inconsistently:
- C07 is called "edge cases", "Scoring Validation", "Harness Gaming" and "exploit checks (B07)".
- Verdict has three values, but "Satisfied (partial)" and "-r" qualified forms are used as if they were values. "Rating", "answer", "classification", "verdict", "decision", "status" are used with overlapping meaning, despite the claim in Section 3.1 that labels are never reused.
- "Not applicable" is defined as "concern does not arise", but B14b is N/A because a prompt omitted a model; in Table 5 the same B14b is flagged for inquiry.
- Documented is defined as an inspectable artifact present, but is used for 2 ratings "resting on absent information" and for B28a with outcome "failed".
- "Maximum score" (Intro) versus "10 is partial" (Section 3.2).
- "Seven published" frameworks, although Caliper is a repository and was never applied.
- The abstract lists three contributions; the Introduction lists four.

Claims without support:
- "grounded in ... representation theory [25]": not used.
- "frameworks reach contradictory verdicts": not separated from LLM noise (W1).
- "disagree on 47% ... largely because they conflate unreported documentation with negative test outcomes": not tested (W3).
- "Raters agree far more often on observable operational properties" attributed to [7,6]: I could not check; the paper then does not test it either.
- "Bottleneck shifts upstream [11]": doubtful source (unverified).

References: not verified online (tool limit). Observations from the list only:
- [18] TruthfulQA, [21] HumanEval and [1] Caliper are repository citations; the HumanEval and TruthfulQA papers are discussed but not cited.
- Several references are dated 2026 (for example [9] arXiv:2606.09809, [14] a July 2026 workshop paper with pages 128 to 160, [17] arXiv:2602.05043, [10], [20], [22]'s Nature 649). I could not confirm that they exist or say what is claimed. The call allows checking for hallucinated references, so the PC chair should have these checked. The page range 128 to 160 (33 pages) for a workshop paper looks unusual.
- [2] Alonso and Church: the DOI lookup failed; the venue and page numbers (SIGIR Forum 58(2), 1 to 27) are not verified.
- [5] is cited as "version 5 (2026)" of a preprint from January 2025.
- [26] gives both the paper and the repository; [12] cited for "inductive assurance argument" (AMLAS) is plausible but not checked.

Rule checks against the call:
- Page limit: 15 pages including references. Within the 15 page limit for both candidate categories.
- LNCS layout: appears to be LNCS.
- Abstract: four labelled paragraphs in the right order. The fourth paragraph states contributions but no limitations, although the call asks for "added value and limitations". Keywords are present.
- Anonymity: no names or affiliations ("contact@example.org" placeholder). The "companion work" is not cited with an "A. Anonymous" placeholder, contrary to the call.
- Data Availability Statement: present at the end, but no link or anonymity warning, and the log count is inconsistent.
- Generative AI: LLMs were used as the object of method and for an unnamed "assistant" draft; the paper does not refer to the LLM guidelines or give the reporting that the call recommends.
- Overlap policy: the call states no policy on companion submissions; the paper's reference to companion work still affects how I judge the contribution.

##### 7. Score

Reject (one step below weak reject; closer to weak reject on the idea, reject on the evidence for the stated claims).

##### 8. Reviewer confidence

Medium: I know the benchmark quality and measurement literature well and checked all counts, but I could not verify references or the HumanEval repository content online.

##### 9. Recommendation

I recommend rejection in the current form. The idea of recording "not reported" apart from "located defect" with a cited location is worth developing. The evidence does not support the claims: the framework conflict study uses one read only LLM with no human reference and no use of its own noise floor, the repeatability study measures test retest of the same model and the rubric levels cannot be shown to mean what they claim, and the RTM, which is named as a contribution, is inconsistent and not evaluated. The smallest set of changes that would move my score up one step (to weak reject): (1) add human raters (at least two) on a subset of the four benchmarks, for both the mapping and the MESA ratings, and compare LLM output with published human framework scores; (2) correct the denominators and statistics (210/559, N/A and B14b removed, alpha with confidence intervals, a defined ordering or nominal alpha, reconcile the 54, 21 and 6 counts and the 234 versus 236, 26 versus 28 discrepancies); (3) either remove the RTM from the contributions or make Eqs. 2 to 4 and Table 5 consistent and add a materiality rule; and (4) add the missing literature on benchmark validity and contamination and a verified, corrected treatment of the HumanEval example with commit and line quotes.

---

### Paper 2: reviewer for requirements engineering

#### REFSQ 2027 research track: review of submission "Applying Meta-Evaluation Benchmark Reviews to Requirement Decisions: An Executable Method"

Reviewer role: program committee member, requirements engineering. Files read: the call summary, paper2.pdf (15 pages, all viewed), paper2.txt. Web search used only for reference checks.

##### 1. Summary of the paper

The paper takes MESA, a benchmark review rubric described in a companion submission (39 criteria, with a conceptual traceability matrix), and builds a "decision engine" around it. The engine has three levels. Level 1 checks input integrity (hashes, identity, duplicates). Level 2 gives an evidence status per criterion (Admissible, Inquiry Required, Inadmissible). Level 3 computes a 95% Wilson interval on retained tasks and returns Accept, Reject, Inconclusive, or "No decision" when evidence is not admissible.

The case is one requirement: "Working alone on a bug report from the SymPy repository, the coding agent changes the code so that the tests the maintainers later wrote for that bug pass, for at least 70% of bug reports, within 15 minutes each." Source evidence is 20 of the 75 SymPy tasks in SWE-bench Verified. The direct test is 20 SymPy pull requests merged in 2026, after the stated cutoffs of two coding agents.

The paper reports these executed items:
- An LLM generated exploit check on the source tasks. Patches that omit part of the fix passed the hidden tests on 17 of 20 tasks. Six of these were counted as task defects because the omitted behaviour is stated in the issue.
- One overbroad test (sympy__sympy-18199).
- 9 of 9 runner hijack patches scored as resolved.
- Eight signed rating forms, one ABC checklist and the signed requirement, all produced by Claude drafts and signed by one author.

On this evidence both MESA policies return "No decision". Four comparison outputs (raw rate, audit only, ABA, ABC) do issue decisions. The paper adds exact binomial tables (Table 4) and a synthetic Monte Carlo study (Table 5) using assumed review accuracy.

The 90 coding agent sessions, which are the only data for RQ1 and RQ2, have not run. The paper says so (Table 1, Sections 4.5 and 7). It shows that the engine runs, that the signed records exist, and that most decisions at N between 14 and 20 will be Inconclusive.

##### 2. Paper category under the call

Page count is 15 including references, so only Technical design papers (15 pages) and Scientific evaluation papers (15 pages) fit. Experience reports (12 pages), Vision papers (8 pages) and Research previews (8 pages) would all breach their page limits, which is a desk rejection ground.

**Technical design paper (best fit).** Criteria in the call's order:
1. Novelty. A decision rule that withholds a verdict when review evidence is defective is a modest idea. Gating plus a Wilson bound is simple, and the paper's own simulation says most of the benefit comes from abstaining. The three "operational rules" in Section 2.1 (signed transfer justification, log hashes, dual policy) are engineering hygiene, not RE concepts. Partly met.
2. Potential impact and relevance. Relevant to the theme in a broad sense. Impact is weak as submitted. The engine returns "No decision" for any SWE-bench Verified case, because the B28a failure is a release wide property (see W2). Not shown.
3. Soundness. Gaps in the rule definitions, the requirement and the rating process (W3 to W6). Not met.
4. Verifiability. The replication package is described but not linked. Raw logs behind the headline counts are withheld, with digests only. Partly met.
5. Presentation. Dense, jargon heavy, undefined codes (B05, B07, B28a), and a companion paper needed to read it. Not met.

A technical design paper needs a "preliminary evaluation". Here that evaluation is an engine demonstration on one repository, plus a simulation that assumes the answer. The sessions that would give an evaluation have not run.

**Scientific evaluation paper.** Criteria in order:
1. Soundness. The study has no results for RQ1 or RQ2. The outcomes of the central method are known before any session runs (Section 4.5 "Known Pre-Session Outcomes"). Not met.
2. Potential impact. Limited for the same reason.
3. Verifiability. As above.
4. Novelty. Moderate.
5. Presentation. Weak.

Under the SIGSOFT Empirical Standards for an experiment or case study, a paper without data is a protocol, not a study. As submitted this category fails on its first criterion.

**What "sessions have not run" means for each category.**
- Technical design: possible, but only if the contribution is claimed as the method and the evaluation is a clearly labelled demonstration. The current RQs promise an answer the paper cannot give.
- Scientific evaluation: not possible. There is no result to judge. Section 4.5 shows that the MESA output cannot change whatever the sessions return.
- Research preview: the right fit by content (a well defined plan with limitations), but the paper is 15 pages against a limit of 8.
- Experience report and Vision paper: no experience or roadmap is offered, and the lengths do not fit.

##### 3. Strengths

**S1.** The paper takes the evidence behind an acceptance decision seriously. It separates "the evidence is defective" (No decision) from "the agent failed" (Reject) and from "too few tasks" (Inconclusive). That distinction (Section 3.2, Section 6.2) is a useful RE point and is stated clearly.

**S2.** The Wilson arithmetic is correct. I recomputed the cut points and probabilities in Table 4 for every N, and they match. The n_min value of 9 (LB = 0.701 at 9 of 9, 0.676 at 8 of 8) and the 0.481 bound for 14 of 20 are also correct. The honest message that N = 14 to 20 gives more than 90% Inconclusive at p = 0.75 is a valuable warning for practitioners.

**S3.** The paper is open about its limits. The Limitations section admits that the empirical case "demonstrates how the engine filters defective tasks... rather than demonstrating improved decision accuracy". It also states the model assisted preparation, the single signer, the scratch folder overlap and the ABC contamination.

**S4.** The choice of a post-cutoff direct test, with a separate count for the 15 tasks whose issues opened after the cutoffs, shows awareness of leakage.

**S5.** Replay conditions (provenance removed, identity mismatch) and a ledger with a frozen manifest are a sensible design for auditability, if the sessions run.

**S6.** Data Availability Statement is present at the end and lists contents in detail.

##### 4. Weaknesses

**W1 (decision). No results for the two research questions; the paper's own design fixes the MESA outcome in advance.**
Where: Abstract, Table 1 (Pending row), Sections 4.5, 7.
What is wrong: RQ1 and RQ2 rest on the 90 sessions, which have not run. Section 4.5 states that M3_strict and M3_lenient return No decision "fixed in advance", and "not comparable" for RQ2. So the sessions cannot change the verdict for the method the paper proposes. The remaining comparison, among M2, audit_only, ABA and ABC, only compares numbers that the benchmark audits already give. In addition, ABC and M2 have identical N and identical cut points, so ABC is not a separate decision method (ABC reports caveats and issues no decision); the "six outputs" are really four distinct decision rules.
Why it matters: the paper reads as a technical design paper with a protocol attached. It cannot be judged as a study, and the abstract's promise ("agrees with post-cutoff testing (RQ2)") is not delivered.
Fix: remove RQ2 and RQ1 as study questions, or run the sessions before submission. If kept as a design paper, state the contribution as the method and use the executed checks as a demonstration, with the RQs reworded as what the demonstration shows.

**W2 (decision). The gate rejects the benchmark by construction, and the rule for "Inadmissible" is not applied consistently.**
Where: Section 3.2 Level 2 (rule 2), Section 4.3 (B28a, B14a), Table 3, Section 4.4.
What is wrong:
1. B28a is "a release wide property of the grading harness", so every SWE-bench Verified case ends in Inadmissible. The engine's answer on this benchmark is therefore constant, whatever the tasks or agents.
2. The paper's own session validity rule (Section 4.4) marks any session that modifies test runner scripts as invalid. That removes the exploit B28a describes for the study sessions, but the gate ignores this mitigation. It also never asks whether a cooperating agent, not an adversary, makes the hijack relevant to this requirement.
3. Rule (2) says Inadmissible requires that "the defect cites a verified location, and any counterexample patch was executed". B14a is Verified/failed on the strength of published audits [15,21] only, with no executed counterexample, yet Table 3 lists it as blocking. Either "any" is read as vacuously true, or B14a should be Inquiry Required. Table 3 and Section 3.2 disagree.
4. The "Verified/failed" and "Verified/passed" labels are confusing next to "17 passes", where a "pass" is a defect.
Why it matters: a gate that cannot return anything but No decision on the only benchmark tested tells a requirements engineer nothing. It also weakens the "executable" claim.
Fix: make criterion relevance depend on the requirement (a stated threat model), apply the validity rule as a mitigation, fix the Level 2 definition, and rename outcomes (for example "benchmark satisfies the criterion" and "benchmark violates it").

**W3 (decision). The requirement and its acceptance rule are not well formed.**
Where: Section 1 (quoted requirement), Section 3.1, Eq. (2).
What is wrong:
- The oracle is "the tests the maintainers later wrote". Those tests are not available when the requirement is stated, and they are what the requirement defines as correct. Then B05 (tests too broad) and B07 (tests too weak) measure the tests against the issue text, which is a different oracle from the one the requirement names. The paper never reconciles these. Under the requirement as written, a test that is wider than the issue is not a defect; it is the definition.
- "At least 70% of bug reports" has no population (which bug reports, which difficulty mix, how sampled).
- The statistical rule (95% Wilson, LB at least 0.70) is not in the requirement text. It is added in the engine.
- The 70% and 15 minute values have no stakeholder or cost rationale.
- No fit criterion for the compute, model configuration or tooling.
- The requirement was drafted by Claude Opus and signed by the one author (Section 7). No stakeholder, elicitation or validation step exists.
Why it matters: this is the part of the paper that should carry the RE contribution. A requirements engineer cannot tell whether a "70% of bug reports" requirement is verifiable with an N of 14 to 20 (the paper's own Table 4 says it is not, for p = 0.75).
Fix: give the requirement a template (Volere fit criterion or ISO 29148 style), state population and acceptance rule inside it, say who owns the 70% and why, and discuss test as oracle versus issue as oracle.

**W4 (decision). Weak link to RE theory and prior RE work.**
Where: Sections 1, 2.2, 6.
What is wrong: the related work is almost wholly ML evaluation and safety assurance. RE references are [9] (a mapping study of RE for AI) and [14] (an ML quality model). No reference on requirements verification and validation, acceptance criteria and fit criteria, quality requirement quantification for ML, requirements traceability (Gotel and Finkelstein), requirements measurement, or evidence in decision making. "Traceability" is a keyword, but the paper never shows what is traced to what (requirement, criterion, form, observation, decision). The central claim, "the bottleneck shifts upstream to validating whether a candidate agent satisfies system capability requirements [9,14]", is not what those sources say as far as I can tell: [9] is a 2024 mapping study of RE for AI based systems, [14] a quality model for ML components. The claim "teams frequently substitute public benchmark scores as fast acceptance evidence [7,11,25]" is also not supported by those three sources (an evaluation reporting proposal, an LLM4SE literature review, and the leaderboard illusion paper).
Why it matters: the REFSQ audience will ask what is requirements engineering here and not model evaluation.
Fix: position the work against RE acceptance testing and quality requirement literature, show the trace links on an example, and replace or support the two claims with evidence.

**W5 (decision). The review evidence is produced by one LLM family, one human signer, and without independence; reliability is not measured.**
Where: Section 4.3, Section 7.
What is wrong:
- The B07 patches, the forms (runs A and B), the ABC record and the engine code are all from Claude models. Runs A and B use the same model and prompt, so agreement ("the same 6 tasks") is replication, not inter rater agreement.
- The "stated in the issue" judgement that decides which of the 17 tasks count as defects is made by the LLM and corrected by one author who also designed the method (34 field edits recorded, not analysed).
- Run A had sessions overlapping in a shared scratch folder. The ABC session read the MESA rating rules first, so the comparator is not independent of the method under test.
- B28b "passed" rests on one line (git history inspected).
- The paper gives no prompts, temperatures or seeds, and does not follow the LLM guidelines the call recommends.
Why it matters: the headline counts (17 of 20, 6 defects) are measured by the same pipeline the paper proposes. Their validity is not checked.
Fix: use at least two independent human raters on a subset, report agreement, release the prompts and the 34 edits with reasons, and run ABC without sight of MESA.

**W6 (decision). Inconsistent and weakly supported headline numbers for the defect counts.**
Where: Abstract, Section 1, 4.3, Conclusion, Table 3.
What is wrong:
- The abstract says "6 breaking issue-stated behaviors on signed B07, plus 1 B05 task", and the Conclusion says "6 of which break issue-stated requirements and are removed... alongside 1 B05 overbroad-test task". That reads as 7 tasks. But sympy__sympy-18199 is in the six B07 tasks (Section 4.3) and is the B05 task, and Table 3 removes 6 tasks (20 to 14). The union is 6, not 7.
- B07 is rated "Verified, passed" on the 14 retained tasks, although 11 of them are tasks where the authors' own exploit patches passed the hidden tests. The rating says the benchmark is fine on those tasks; the evidence says 85% of the sample accepts incomplete patches. Only the "stated in the issue" definition makes it pass.
- B05 is "Verified, passed" after one executed check, on a task found by a third party audit [21] that reports a 59.4% flaw rate on 138 tasks. One flagged task in 20 is not consistent with that rate and is a detection limit, not an assurance.
- ABA flags -13031 too, which MESA keeps. The paper says only that MESA "removes 5 additional tasks".
Fix: report 6 consistently, define the labels so a "passed" rating cannot sit next to 11 demonstrated exploits, and run B05 on more than one task.

**W7 (decision). Study design cannot discriminate, and the Monte Carlo result is mostly assumed.**
Where: Section 4, Table 4, Section 5.2, Table 5.
What is wrong:
- At N of 14 to 20, Table 4 shows more than 90% Inconclusive at p = 0.75. The target test (N = 20 or 15) will therefore almost surely be Inconclusive, so any "agreement" in RQ2 is nearly trivial. "Agree" is not defined.
- One session per agent per task, so run to run variance of the agent is not handled.
- Only 20 of 75 source tasks are used, though the budget would allow more, and only 2 agents.
- Table 5: false acceptance falls from 20.8% to 5.4% because M3 decides in about 6.8% of trials (coverage). The text concedes that "most of the reduction... comes from abstaining" and the gain over random withholding is about one point. The detection rate (85%), false alarm rate (5%) and the jump from 0.72 to 0.86 are assumptions that drive the result.
- Text and table disagree or are unclear: Section 5.2 lists Δ in {-0.15, -0.05, 0} but Table 5 shows two values; "576-cell sweep at d = 0.30... all 72 noncompliant cells" is not explained; the 0.44% versus 1.42% false rejection figures and the "100 seeds" means are not in any table.
Fix: define agreement, pre-state the analysis with power, use all 75 tasks or justify 20, repeat sessions, and either drop Table 5 or present it as a sensitivity analysis with the assumptions stated first.

**W8 (decision). A RE practitioner could not use the method as described.**
Where: Sections 3 and 4.3, whole paper.
What is wrong: no example of a rating form or engine output is shown. Cost is not reported: eight signed forms, executed exploit checks and a frozen manifest, with no hours, no tooling needed and no guidance for a repository that is not SWE-bench. The "five method families" are not alternatives a practitioner would pick between. There is no user study or practitioner feedback.
Why it matters: the call stresses practical RE relevance, and the theme is "AI velocity". A method with this much sign-off and an always-withhold outcome on the main benchmark runs against velocity.
Fix: show a complete worked example (requirement, one form, the engine report), report effort, and discuss how it scales.

**W9 (minor). Fit with the theme is stated, not argued.**
Section 6 is titled "Aligning Requirements Validation with AI Velocity", but only the first paragraph links to velocity. The paper is about qualifying a tool (a coding agent) with benchmark evidence, not about RE cycles, elicitation, or refinement under AI coding. State the link explicitly, or narrow the claim.

**W10 (minor). Clarity for the REFSQ audience.**
The abstract uses MESA, ABC, B05, B07, B28a, "Wilson bounds" and "Tier 3" without definitions. The paper needs the companion submission to understand the rubric (39 criteria, 7 frameworks). It defines seven fixed terms in the introduction, but the codes and the three policy names (POLICY-P5-STRICT, M3_withheld, audit_only) appear much more widely than needed. Tables 3 and 4 use output codes that differ from the text.

**W11 (minor). Rule and format issues.**
- The abstract has four labelled paragraphs, but the Contribution paragraph lists three items and gives no limitation, which the call asks for.
- The companion submission (MESA) is cited in prose but is not in the reference list; non public work should be cited with a placeholder such as "A. Anonymous".
- Layout: the first bullet in Section 1 and the equation (2) run into the right margin, and the POLICY-P5-LENIENT name overflows on page 7. The running head omits the word "Benchmark" from the title.
- The abstract says "pre-registered protocol", but nothing has been registered or frozen. Registered where, and when?
- The Data Availability Statement has no access location, and the raw logs behind 17 of 20 and 9 of 9 are withheld (digests only).

**W12 (minor). Target task sampling is not explained.**
Section 4.2 gives the pool as 1 May to 5 November, 108 eligible of 322, "the first 20 checked in deterministic order", yet all 20 were merged between 13 June and 5 November. If the order were a hash order and merges were spread evenly, the chance that none of 20 falls in the first 43 days of a 189 day window is about 0.5% (my estimate, assuming uniform merges). Say what the order is. Also, 5 of the 20 pull requests close issues opened before the cutoffs, so the cutoff argument is weaker than the abstract says ("post-cutoff target tasks").

##### 5. Questions for the authors

**Q1.** Under your requirement, the maintainers' tests are the oracle. Why then are tests that go beyond the issue text (B05) or that omit issue behaviour (B07) defects, and not part of the definition?

**Q2.** Who owns the 70% and the 15 minutes, and what decision depends on them? Why is a Wilson lower bound the right acceptance rule, and why is it not in the requirement text?

**Q3.** Since B28a fails for every SWE-bench Verified release, what would make your engine return anything other than No decision here? What does a practitioner do next?

**Q4.** Is the union of removed tasks 6 or 7? Please reconcile the abstract and conclusion with Table 3.

**Q5.** B07 is rated Verified/passed on 14 tasks, 11 of which accepted your incomplete patches. How should a reader interpret "passed"?

**Q6.** How was "stated in the issue" decided for each of the 17 tasks, by whom, and what did the 34 edits change?

**Q7.** What exactly does "agree" mean in RQ2, given that Table 4 predicts Inconclusive for both source and target in more than 90% of cases?

**Q8.** How is the "deterministic order" of target pull requests defined, and why are none of the 20 merged before 13 June?

**Q9.** Why 20 of 75 source tasks, and one session per agent per task?

**Q10.** How much practitioner effort does one case need, and have you tried it on a repository other than SymPy?

**Q11.** What do [9] and [14] say that supports "the bottleneck shifts upstream to validating whether a candidate agent satisfies system capability requirements"?

##### 6. Checks made

**Arithmetic and counts that add up**
- Wilson cut points in Table 3 and Table 4 (N = 14, 15, 18, 20, 30, 45, 60, 90, 120): I recomputed them and they match. The probabilities (Accept, Reject, Inconclusive) for p = 0.75, 0.65, 0.85 also match to the rounding shown, including the 97.2% at N = 14 and N = 20, and 78.8% at N = 62.
- n_min = 9: LB(9/9) = 0.7009, LB(8/8) = 0.6756. Correct. LB(14/20) = 0.481. Correct. Eq. (1) is the standard Wilson formula with z = 1.95996.
- ABC: 8 + 9 + 10 + 6 = 33 items; 9 + 6 = 15 caveats; part scores 5/8, 2/11, 1/4 sum to 8 met out of 23 applicable (33 minus 10). Consistent.
- 17 of 20 with 6 defects leaves 11 set aside; 6 minus -18199 gives "5 additional" over ABA. Consistent. 20 minus 6 gives 14; 20 minus 2 (ABA) gives 18. 20 target tasks minus 5 earlier issues gives 15.
- Sessions: 2 + 40 + 40 + up to 8 = 90. Consistent.
- Page count is 15 including references. Within the limit for the two 15 page categories.

**Counts that do not add up or are unclear**
- The abstract and conclusion suggest 7 removed tasks ("6... plus 1 B05 task"); Section 4.3 and Table 3 give 6 (see W6).
- Section 5.2 lists three Δ values; Table 5 shows two. The "576 cell sweep" and "72 noncompliant cells" are not explained. The 0.88 and 1.14 point means across 100 seeds and the 0.44% and 1.42% false rejection figures appear in no table. Table 5 values themselves I could not reproduce without the scripts.
- Section 4.2 window starts 1 May, but all selected tasks merged on or after 13 June (W12).
- "Five method families producing six evaluated outputs": the paper also uses M3_withheld as a seventh, counterfactual output (equal to audit_only). ABC and M2 produce identical decisions.

**Terms used inconsistently**
- "Passed" means a defect when an exploit patch passes, but means a good outcome on a rating form. "Verified/failed" means the benchmark violates the criterion.
- "Source decision", "pre-gate score decision", "M3_withheld" and "audit_only" are used for the same quantity in places. "Requirement" means both the SymPy statement and the "requirement profile" of criteria.
- "Inadmissible" is defined by an executed counterexample, but is applied to B14a without one.
- Title "Meta-Evaluation Benchmark Reviews" in the title, "Meta-Evaluation Reviews" in the running head.

**Claims without support**
- "teams frequently substitute public benchmark scores... [7,11,25]" and the bottleneck claim [9,14] (W4).
- "pre-registered" (no registration).
- "executed checks found cheating patches": the patches and the independent tests were written by an LLM and the raw logs are not released.
- "none provides an executable gate" (Gap 1) is a claim of absence with a short survey and no systematic search.

**References that look wrong or could not be confirmed**
- Existence confirmed by search: [21] (OpenAI post on SWE-bench Verified), [30] (ABA, arXiv 2605.26079), [7] (Evaluation Cards, arXiv 2606.09809). I did not check whether [21] reports the 59.4% flaw figure on 138 tasks, or whether [30] flags -13031 and -18199, so those two claims are unverified.
- [5] (Ding, arXiv 2610.30635): the search returned a paper with this title but under a different arXiv number (2606.28430 appeared in the results) and I could not confirm the author or number. Possible wrong identifier. Please verify.
- [11] (Hou et al., TOSEM): the paper exists (arXiv 2308.10620), but I could not confirm the DOI 10.1145/3689498 shown. I recall a different TOSEM article number, so the DOI may be wrong.
- [34] title is given as "...best practices in building rigorous agentic benchmarks"; I believe the published title uses "for building". Minor.
- Not checked: [2], [8], [14], [17], [18], [19], [23], [26], [28] (2026 sources I could not reach in the time available). [2] is called VNVSpec in the text but the reference title does not contain that name.
- Models named (Gemini 3.8 Flash, GPT-6.1 Sol, Antigravity CLI) and their cutoff dates are vendor claims I cannot verify. No sign of many hallucinated references from the ones I checked, but the sample is small.

**Rule checks**
- Page limit: 15 pages with references. Fine for the two 15 page categories; over the limit for Research preview, Vision paper and Experience report.
- Abstract: four paragraphs with the required labels. Contribution paragraph lacks limitations (W11). Keywords follow the abstract.
- Anonymity: author block anonymous; no acknowledgments; "contact@example.org" is a placeholder. The companion paper is cited without the "A. Anonymous" placeholder and not in the references. The package is "provided with this submission" but has no link, so I could not open it.
- Data Availability Statement: present, at the end, detailed. Raw logs are withheld, only digests given.
- Generative AI: use of Claude models is disclosed in Section 7. The LLM guidelines recommended by the call are not followed (no prompts, versions or variance).
- Layout: some overflow into the margin (W11).

##### 7. Score

**Reject**

(One step above weak reject is not justified: the key study is missing and the central method returns a constant answer on the case tested. I would go no lower because the arithmetic is correct and the paper is honest about its state.)

##### 8. Reviewer confidence

**Medium.** I am familiar with RE acceptance testing and with the empirical standards, and I recomputed all statistical tables, but I could not open the replication package, I could not verify several 2026 sources, and I did not read the companion MESA paper.

##### 9. Recommendation

I would not accept this paper exactly as submitted. It claims to answer two research questions, but the sessions that would answer them have not run, and the paper itself says the output of the proposed method is fixed in advance and "not comparable" for RQ2. What exists is a decision engine, correct Wilson tables, and a set of LLM produced and author signed review records, none of which are validated. The requirement that anchors the method has an oracle that conflicts with the defects the method checks, and the link to RE theory and prior RE work is thin.

The smallest set of changes that would move my score to weak reject (one step up):
1. Reframe the paper as a technical design paper. Drop RQ2 and reword RQ1 as what the demonstration shows, and remove "pre-registered" until a registration exists.
2. Rewrite the requirement with a stated population, acceptance rule and rationale, and resolve the conflict between "the maintainers' tests define success" and the B05 and B07 defect rules.
3. Fix the inconsistent counts (6 versus 7 removed tasks), the Level 2 rule for B14a, and the "passed" labels that sit beside demonstrated exploits.
4. Add a short worked example of a form and engine report, and RE literature on acceptance criteria, verification and traceability, with the two unsupported citations repaired.

To reach borderline or higher, the sessions would also need to run, with at least two independent raters on a subset and a defined meaning of "agree" for RQ2.

---

### Paper 2: reviewer for empirical methods

#### REFSQ 2027 research track: review of submission "Applying Meta-Evaluation Benchmark Reviews to Requirement Decisions: An Executable Method"

Reviewer role: program committee member, empirical methods. Files read: the call, paper2.pdf (all 15 pages), paper2.txt. Web search was used only to check references.

##### 1. Summary of the paper

The paper builds on a companion submission (MESA, a 39 criterion rubric for reviewing benchmarks) and turns it into a "decision engine". The engine has three levels: input integrity (hashes, identities), evidence status (Admissible, Inquiry Required, Inadmissible, from signed per criterion rating forms) and a score decision (Accept, Reject, Inconclusive from a 95% Wilson interval against a threshold, otherwise No decision). The case study is one requirement: a coding agent resolves at least 70% of SymPy bug reports within 15 minutes. Evidence comes from 20 SWE-bench Verified SymPy "source" tasks. Two agents are planned (Gemini 3.8 Flash and GPT-6.1 Sol). 20 post-cutoff SymPy tasks serve as the "direct test".

Two research questions: RQ1, how reviewing a benchmark with MESA or ABC, beyond an automated audit, changes the accept/reject decision; RQ2, whether a decision from a reviewed benchmark agrees with the direct post-cutoff test.

What exists today: no coding agent session has run (Table 1, Sect. 4.1, Sect. 7). The paper reports these results:
- Signed rating forms. Claude Sonnet 5.5 drafted them, and one author signed them after 34 edits.
- An LLM generated exploit check: on 17 of 20 source tasks a deliberately incomplete patch passes the hidden tests. For 6 of these the omitted behaviour is stated in the issue, and these 6 are removed as defects.
- 9 of 9 test runner modification patches are scored "resolved" by the SWE-bench harness (B28a, marked failed).
- Exact binomial power tables (Table 4).
- A Monte Carlo simulation with assumed review accuracy (Table 5).

Because B28a (and B14a) is marked failed, both MESA policies return "No decision" on this case, whatever the agents do. The paper itself says the case "demonstrates how the engine filters defective tasks (20 to 14) and explains abstention, rather than demonstrating improved decision accuracy" (Sect. 7).

##### 2. Paper category under the call

Candidate categories: scientific evaluation, technical design, research preview.

**Scientific evaluation paper (15 pages).** Criteria in order: soundness, potential impact, verifiability, novelty, presentation.
- Soundness: not met. The study that would answer RQ1/RQ2 has not run. The MESA outcome (No decision) is fixed by the pre-session B28a form, so the sessions cannot change it. At N = 14 to 20 the Wilson rule returns Inconclusive about 90 to 97% of the time for an agent at p = 0.75 (Table 4), so the sessions cannot discriminate between the baseline methods either. What the paper evaluates today is a method on one benchmark slice, with LLM generated forms, and a simulation whose conclusion is built into its assumptions.
- Impact: potentially real (benchmark scores as acceptance evidence fit the "AI velocity" theme), but a method that returns No decision on every SWE-bench Verified case has little demonstrated impact.
- Verifiability: partly met. A replication package is described, but the raw logs behind the central executed checks are withheld, and the protocol is not frozen.
- Novelty: moderate. The gate is new in packaging. The ingredients (task audits, Wilson bounds, contamination warnings) are not.
- Presentation: dense, with inconsistent terms (Sect. 6 below).
- Under the Empirical Standards the paper would be judged as an experiment/benchmark study with a preregistered plan. A preregistered plan without data is not a result. The standard also expects the analysis to be able to answer the question, which fails here.

**Technical design paper (15 pages).** Criteria: novelty, impact, soundness, verifiability, presentation. This is the better fit for what exists (schemas, engine, 181 tests). But the call asks for a "preliminary evaluation" of the artifact. Here the evaluation of the artifact's value is absent. Only the artifact's mechanics are shown, and the paper frames its contribution as an empirical comparison (RQ1/RQ2), not as a design. The novelty is thin because the decision logic is a conjunction of checks plus a Wilson interval, and the rubric itself sits in an unseen companion paper.

**Research preview (8 pages).** Criteria: novelty, soundness of the research plan including limitations and risks, potential for discussion, presentation. This is the honest category for "main sessions have not run". The plan is detailed, and the limitations section is candid. But the paper has 15 pages including references, so under this category it exceeds the 8 page limit and would be a desk rejection. It would need to be cut by about half.

**Verdict on category.** As written it is a scientific evaluation paper without its evaluation. Submitted as a technical design paper it would be reviewed mainly on novelty and the missing preliminary evaluation. Submitted as a research preview it breaks the page limit. In no category does the paper meet its criteria as submitted.

##### 3. Strengths

- S1. Candid status reporting. Table 1 separates what was adopted, implemented, executed and pending. Section 7 states plainly that MESA withholds, so the case does not show better decisions.
- S2. The power analysis is honest and correct. Sect. 5.1 and 6.2 show that N = 14 to 20 cannot support a 70% requirement at 95% confidence. This is a useful point for practitioners who use small benchmark subsets. I reproduced the table (Sect. 6 below).
- S3. Separation of "No decision" (evidence defect) from "Inconclusive" (statistical). The argument that flawed tests do not prove a Reject is sound (Eq. 2 discussion).
- S4. Sampling of source tasks by a deterministic hash order, with a stated pilot and rehearsal task outside the sample (Sect. 4.2). This limits author discretion.
- S5. The paper reports the model assisted preparation openly (Sect. 7): who generated which artifact, the shared scratch overlap, and the single signer.
- S6. A ledger with a hard cap of 90 sessions, validity rules fixed before runs (Sect. 4.4), and a planned control with test only resolution.
- S7. Reporting target results on both 20 and 15 tasks to handle issues opened before the cutoff.

##### 4. Weaknesses

###### Decision

**W1 (decision). The research questions cannot be answered by the design.** Where: Sect. 1.1, 4.5, 7, Table 3.
- RQ1 asks how MESA changes the decision. The outcome is already known and fixed: both MESA policies return No decision because B28a is "Verified, failed" for the whole SWE-bench release (Sect. 4.5 is titled "Known Pre-Session Outcomes"). No session result can change it. A method that abstains on every case of the benchmark it is applied to cannot be compared on "the decision".
- RQ2 asks whether a reviewed benchmark's decision agrees with the direct test. MESA issues no decision, so it drops out ("not comparable"). RQ2 then compares only M2, audit_only, ABA and ABC, none of which is the method proposed. They are also the same Wilson rule on different task subsets.
- There is no ground truth for the agents' true compliance, so even when a decision is issued one cannot say whether abstaining was right or wrong.
- With two agents the "agreement" evidence is at most two data points per method, and most are likely to be Inconclusive on both sides (W2).
- Fix: change the question to what the evidence supports, for example "which gate criteria block decisions on SWE-bench Verified, and how many tasks does executed review remove". Or redesign: a policy variant where mitigated criteria (for example B28a, which Sect. 4.4 already neutralises by invalidating sessions that modify runner scripts) are treated as controlled, so the engine can issue a decision; use more tasks and agents; and add a reference comparison with known truth.

**W2 (decision). Sample size and the decision rule give no power.** Where: Eq. 1, Table 4, Sect. 4.2 and 6.2.
- Accept requires the lower bound at or above 0.70. At N = 14 that means 14 of 14; at N = 20, 19 of 20 (I verified the cut points). For a true p = 0.75 the chance of an Accept is 1.8% at N = 14 and 2.4% at N = 20. A Reject (UB below 0.70) needs at most 6 of 14 or 9 of 20.
- So the direct test on 20 tasks (15 in the cleaned subset) will return Inconclusive for most agents with true rates between roughly 0.5 and 0.9. Agreement between "Inconclusive" and "Inconclusive" is not evidence of transfer.
- The authors know this (Sect. 6.2) but still choose N = 20 and one run per task. SymPy has 75 eligible Verified tasks; running all 75 gives about 12.7% (p = 0.75) and 85% (p = 0.85) Accept probability (my computation), still weak at 0.75.
- The paper does not state what outcomes would count as support for RQ2, so no analysis can fail.
- Fix: state success criteria before the run, report the expected distribution of outcomes for plausible agent rates, use a lower confidence level or a one sided/Bayesian rule that is justified for the requirement, add repeated runs per task, and enlarge N, or reframe the study as estimation (interval widths) rather than decisions.

**W3 (decision). The "preregistered" claim does not hold, and the decision rule and task removals were fixed after results were seen.** Where: Abstract ("pre-registered protocol"), Table 1, Sect. 4.1, 4.5.
- The protocol is not frozen ("sessions pending freeze"). No external registry or timestamp is named. The "cryptographic manifest" is held by the author alone.
- Everything that determines the MESA side of RQ1 (the exploit results, the removal of the 6 tasks, the B28a failure, the B14a failure) was observed on 9 Nov 2026, before the plan was written. The rule for what counts as a B07 defect ("stated in the issue description rather than inferred solely from the reference fix", Sect. 4.3) was applied after seeing 17 of 20 passes and decides whether 6 or 17 tasks are removed. That is a degree of freedom of the authors, not a preregistered rule.
- Which tasks the baselines drop (ABA's 2) was also known.
- Fix: say "plan written after the pre-session checks" and register only the session analysis; freeze and deposit the manifest with a third party timestamp before any session, and list which results are confirmatory.

**W4 (decision). LLM produced review records are the main evidence, and they are neither independent nor validated.** Where: Sect. 4.3, Sect. 7.
- Claude Sonnet 5.5 wrote the exploit patches, the independent check tests, the B28a patches, the form drafts (runs A, B) and the ABC answers. The same model family (Opus 5.5) wrote the engine and the transfer justification, and helped write the paper.
- Judging whether an omitted behaviour is "stated in the issue" (the 6 versus 11 split) is a human requirements judgement. It was made by a model, then confirmed by one author after 34 edits (not shown). Runs A and B agreeing on the same 6 tasks is one model with one prompt run twice, so it is not inter rater agreement.
- The signed forms come from run A, which the paper says was affected by overlapping sessions in a shared scratch folder (Sect. 7). Run B was repeated cleanly, but the signed set is from the contaminated run.
- The ABC session read the MESA rating prompt rules before answering (Sect. 7). ABC is therefore not an independent comparator and probably not run as ABC's authors intend.
- The independent test for each task was written with the reference fix in view, and no check of those tests (human review, mutation, second model) is reported. A patch that "fails the independent check" may fail because the check itself is over specific.
- Fix: sign forms from the clean run, or sign both and report differences; have at least two humans rate the 20 B07 decisions blind to the model drafts and report agreement (kappa); use a different model family for generation versus judging; rerun ABC without MESA material; report the 34 edits.

**W5 (decision). The criterion outcomes that decide the engine's output are not supported by the evidence in the paper, and the engine rule contradicts the table.** Where: Sect. 3.2 Level 2, Table 3, Sect. 4.3.
- B05 is rated "Verified, passed" on the remaining tasks although the executed check covers one task (sympy-18199) of 21 in scope. The paper itself cites a 59.4% flaw rate in an OpenAI audit as a "detection limit". I checked that source: the 59.4% is on 138 tasks that o3 did not solve consistently over 64 runs, a hard subset, and the paper does not say so. Even so, it shows that "Verified, passed" on 19 unexamined tasks is unjustified.
- Level 2 rule (2) makes a criterion Inadmissible only if the check failed, the defect cites a verified location, and a counterexample patch was executed. B14a (contamination) is "Verified, failed" on the basis of published audits (check kind "reported"); no counterexample was executed. By the paper's own rule B14a would be Inquiry Required, not Inadmissible. Table 3 says the strict policy is blocked by "B14a and B28a failed". The wording of rule (2) (a list with "or" and "and") is also ambiguous.
- B28a: a failure of a release-wide harness property is recorded as Inadmissible even though the paper's session validity rule (Sect. 4.4) invalidates any session that modifies runner scripts or test configuration. The engine has no way to record a compensating control, which makes the gate never open for this benchmark.
- The 9 of 9 result is not informative: it demonstrates by construction that a patch which edits the runner is scored by the runner, a known property from BenchJack [29]. No evidence is given that any of the studied agents would do this.
- Fix: apply the executed evidence rule consistently (downgrade B14a or state why reported evidence suffices), execute or sample B05 on more tasks or lower the rating, and add a mitigated state with explicit conditions.

**W6 (decision). The simulation only restates its assumptions, and it is under specified.** Where: Sect. 5.2, Table 5.
- Review quality is assumed (85% detection, 5% false alarm, 10% missing documentation), and defective evidence is assumed to inflate the source rate from 0.72 to 0.86. No empirical anchor is given for any of these numbers. The finding that MESA reduces false acceptance is then a consequence of the abstention it is programmed to do.
- The M3 coverage is 6.2 to 7.0% (Table 5), so M3 abstains in about 93% of trials. False acceptance of 5% against 20.8% for M2 is mostly "does not accept". The paper concedes this (Sect. 5.2: "Most of the reduction ... comes from abstaining altogether"), and the selective advantage over matched coverage random abstention is about one percentage point, which is the only informative quantity. The false acceptance per case metric does not credit power; the trade-off (accepting compliant agents) is shown for one cell only (false rejection 0.44% versus 1.42%, d = 0.30, Δ = 0), which is not in Table 5.
- Δ = 0 is announced as a scenario but missing from Table 5.
- It is not defined how Δ enters: if the defective source rate is 0.86 and Δ = -0.15, the target is 0.71, which is compliant. If Δ applies to the 0.72 baseline, the target is 0.57. "Noncompliant" is not defined.
- The baselines are weak: random and proximity withholding at matched coverage. The obvious comparator, audit_only with the same Wilson rule (and a simple stricter confidence level), is not simulated, although it is the main contender in the empirical part.
- Fix: define the generative model fully (equations, how Δ and d act), add audit_only and a stricter confidence baseline, report both error rates and power over all cells including Δ = 0, anchor parameters in the executed checks (for example detection estimated from the 20 tasks), and show sensitivity to detection rate.

###### Minor

**W7 (minor). The selection of tasks, agents and the direct test.** Where: Sect. 4.1, 4.2.
- The requirement speaks about "bug reports", but source tasks are a curated benchmark (human screened for well specification), and target tasks are chosen by a filter (linked issue, source and test files modified), a different construction. Neither is a random sample of SymPy bug reports, so the Wilson interval does not describe the requirement population.
- The target tasks are not audited for the same B05/B07 defects. The paper treats them as the "direct test" and ground truth, but the same hidden tests oracle problems apply.
- "First 20 checked in deterministic order": the ordering is not stated. The 322 / 108 counts cannot be reproduced from the text.
- 5 of 20 target issues were opened before the cutoffs, so the claim in Sect. 1 ("after the stated training cutoffs of both evaluated models") is not true for all 20. Cutoffs are vendor stated and unverified. Merge window text differs: "13 June" (Sect. 1), "1 May" (Sect. 4.2).
- Two agents of unequal tier, one CLI each, are chosen without a rationale. Agent and CLI are confounded. One run per task ignores agent nondeterminism and gives no variance estimate.
- The comparison on source versus target mixes differences in contamination, difficulty and construction. The paper states this (Sect. 7) but the design cannot separate them.

**W8 (minor). Construct validity of the central terms and of RQ1's comparison.** Where: Abstract, Sect. 1.1, Table 3.
- "Audit" and "review" are not defined consistently. The audit_only arm is the authors' own LLM executed B05/B07 check, which is a part of MESA, not the "automated audit" of RQ1 (that is ABA). So RQ1 compares MESA with part of itself and with ABA.
- "Cheating patches" (abstract) are incomplete patches written by a model that was given the reference fix. That is a different thing from agents that cheat.
- ABC is given a "decision" by definition (the raw rate with caveats), which is a straw man because ABC does not claim to decide.
- The mapping of B05 to the extrapolation inference and B07 to scoring in Table 2 is debatable (rejecting valid solutions is a scoring error).

**W9 (minor). Reproducibility.** Where: Data Availability, Sect. 4.3, 4.4.
- The Data Availability Statement exists but the raw session and harness logs, on which the hashes and B07/B28a results rest, are excluded. The replication package cannot be checked by this reviewer, and none of the prompts for runs A and B are described in the text.
- The replay (Sect. 4.4) tests the implementation on one agent's source records, and its pass criteria are not stated.
- The relation to the companion paper is unclear. The rubric, criteria text and rating form definitions live there. The companion is not cited or in the references, so this paper cannot be assessed or repeated on its own.

**W10 (minor). Layout and cross reference problems.** Where: pp. 2, 6, 7.
- Text runs into the right margin on p. 2 (sympy-21930 line), p. 6 (Eq. 2) and p. 7 (POLICY-P5-LENIENT). The call says non LNCS layout is a desk rejection ground; this looks like a typesetting slip but should be fixed.
- Title versus running head differ ("Meta-Evaluation Benchmark Reviews" versus "Meta-Evaluation Reviews").

**W11 (minor). Claims without support in the introduction and related work.** Where: Sect. 1, 2.2.
- "Bottleneck shifts upstream" is supported by [9] (a 2024 mapping study of RE for AI systems) and [14] (a quality model); neither shows this.
- "Teams frequently substitute public benchmark scores" is supported by [7], [11], [25]: an evaluation reporting paper, a literature review, and a paper about chatbot leaderboards. None provides practice evidence. There is no evidence that practitioners use SWE-bench Verified for acceptance.
- "None provides an executable gate ..." (Gap 1) and "none has evaluated..." (Gap 2) are strong novelty claims made without a systematic search.
- The paper does not engage with the RE literature on acceptance criteria or requirement validation beyond [9]; the REFSQ link is weak.

##### 5. Questions for the authors

- Q1. Which result of the planned sessions could change the answer to RQ1 or RQ2? Please state, per method, the outcomes that would count as support and as failure.
- Q2. If the study is to produce decisions at N = 14 to 20, why choose a 95% Wilson lower bound for a 70% requirement? What confidence level or N would you consider adequate, and why not run all 75 eligible SymPy tasks?
- Q3. Would the engine issue a decision if B28a were recorded as mitigated by the session validity rules of Sect. 4.4? If not, is the engine usable on any benchmark that shares the SWE-bench harness?
- Q4. Why were the forms signed from run A, which overlapped in a shared scratch folder, and not from run B? How many of the 34 edits change a rating, and which?
- Q5. How was the 6 versus 11 split on B07 validated by a human other than the signer? What was the agreement, if any, between two humans?
- Q6. What justifies "Verified, passed" for B05 on 19 tasks when only one task was executed? How does the 59.4% flaw rate (measured on a hard 138 task subset) enter the rating?
- Q7. By the Level 2 rule an executed counterexample is needed for Inadmissible. Which counterexample was executed for B14a?
- Q8. How does Δ enter the simulation, what are the true target rates in each cell, and what is "noncompliant"? Where are the Δ = 0 rows?
- Q9. How were the 20 target tasks ordered ("deterministic order") and how will you check them for B05/B07 defects?
- Q10. Is the companion MESA submission accepted, rejected or pending, and which parts of this paper depend on it?

##### 6. Checks made

**Wilson formula and cut points** (Eq. 1, z = 1.95996; Python recomputation):
- 9/9: LB = 0.7009 (paper 0.701). 8/8: LB = 0.6756 (paper 0.676). So n_min = 9 holds, and 8 cannot reach Accept. Correct.
- 14/20: LB = 0.481 (paper 0.481). Correct.
- Cut points (Accept at or above, Reject at or below): N = 14: 14, 6; N = 15: 14, 7; N = 18: 17, 8; N = 20: 19, 9; N = 30: 26, 16; N = 45: 38, 25; N = 60: 49, 35. All match Table 4.
- **Errors in Table 4 cut point column:** N = 90 should be Accept at or above 72 (LB(71/90) = 0.694, LB(72/90) = 0.706), the paper says 71. N = 120 should be 94 (LB(93/120) = 0.692, LB(94/120) = 0.701), the paper says 93. The probabilities printed in those rows (16.5%, 92.6%; 23.3%, 98.1%) match the corrected cut points, so the cut point column is a typo.

**Binomial probabilities in Table 4** (exact, recomputed for all rows):
- N = 14, p = 0.75: Accept 1.8%, Inconclusive 97.2% (Reject, not shown, 1.0%). p = 0.65: Reject 7.5%, Inconclusive 92.2%. p = 0.85: Accept 10.3%, Inconclusive 89.7%. Match.
- N = 15: p = 0.75 Accept 8.0%, Inconclusive 90.3%; p = 0.65 Reject 11.3%, Inconclusive 87.3%; p = 0.85 Accept 31.9%, Inconclusive 68.1%. Match.
- N = 18: 3.9/95.5; 6.0/93.6; 22.4/77.6. Match.
- N = 20: 2.4/97.2; 5.3/94.5; 17.6/82.4. Match.
- N = 30, 45, 60, 90, 120 also match (for 90 and 120 with the corrected cuts). Example N = 60: 14.8/84.9; 17.1/82.5; 81.9/18.1.
- Text: first N with more than 80% power at p = 0.85 is 60 (81.9%); N = 62 gives 78.8%. Correct. N = 75 (all eligible tasks): Accept at or above 61, 12.7% at p = 0.75, 85.3% at p = 0.85.
- Table 4 gives only Accept (or Reject) and Inconclusive, so the rows do not sum to 100%. The label "N = 14 (audit_only, M3)" is misleading since M3 withholds. Both N = 14 and N = 20 show 97.2% Inconclusive at p = 0.75; this is a coincidence of rounding, not a typo.

**Counts:**
- 20 minus 6 removed tasks = 14. Correct for Table 3. But the abstract says "6 breaking issue-stated behaviors on signed B07, plus 1 B05 task" and the conclusion says "6 of which ... are removed ... alongside 1 B05 overbroad test task". The B05 task (sympy-18199) is in the list of 6 B07 tasks (Sect. 4.3), so the union is 6, not 7. If it were 7, N = 13. Wording in abstract and conclusion is wrong or misleading.
- 17 passes minus 6 stated in the issue = 11 set aside. Consistent.
- ABA removes 2 (13031, 18199): N = 18. MESA's B07 removes 5 more than ABA's overlap (18199 shared). Consistent, but 13031 is flagged by ABA and not removed by MESA, and this is not discussed. I could not confirm the two flagged task IDs from the ABA abstract (the full paper may list them).
- Session budget: 2 + 40 + 40 + 8 = 90. Correct. The text does not say whether the 2 pilot sessions enter the analysis.
- ABC: 8 + 9 + 10 + 6 = 33 items; part scores 5/8 + 2/11 + 1/4 = 8 met, denominators 23 = 33 minus 10 not applicable; caveats 9 + 6 = 15. Consistent.
- Eight MESA forms: B05, B07, B12, B14a, B28a, B28b = 6, plus B14b for two agents = 8. Consistent. Nine records with the ABC form.
- Target tasks: 20 minus 5 = 15. Consistent.

**Terms used inconsistently:**
- "Tier 3" is used for both the evidence status gate and the score decision in the definitions (Sect. 1, items 6 and 7); the method section calls them Level 2 and Level 3; Table 1 says "three-stage".
- "Method 1", "Method 2 (M2)" in Sect. 3.4 are never defined; "M3" is used as one method (Tables 4, 5) and as M3_strict/M3_lenient/M3_withheld (Table 3).
- "Audit", "review", "check" and "meta-evaluation" are mixed (see W8). "Task defects" is used for B05 and B07 forms and for the removal rule.
- "The author" (singular) versus "we" and "the authors" (Disclosure).
- "Post-cutoff" is used for tasks of which 5 have pre-cutoff issues.
- Title differs from running head.

**Claims without support:** "pre-registered" (W3); "none provides" novelty claims (W11); "cheating patches" (W8); "teams frequently substitute leaderboard scores" (W11); the 85% detection and the 0.86 inflation (W6); "Verified, passed" for B05 (W5); the MESA claim of "30 shared concerns and 39 criteria" rests on the companion.

**References:**
- Verified to exist with matching title (and authors where seen): [5] Ding, arXiv 2610.30635, but it studies SWE-Milestone and four other benchmarks, not SWE-bench Verified, so it supports only the general "tests depend on unstated details" point; [17] Mohl et al., arXiv 2607.27518; [28] BenchGuard, arXiv 2604.24955; [30] ABA, arXiv 2605.26079 (reports flagging more than 25.7% of tasks over 168 benchmarks); [21] OpenAI blog, exists and covers contamination and sympy-18199 "too wide" tests, but 59.4% refers to 138 hard tasks (see W5).
- Well known references that I recognise and that look correct: [1], [3], [4], [6], [10], [11], [12], [13], [15], [16], [24], [25], [31], [32], [33], [34].
- Not checked, because the search quota ran out: [2] arXiv 2607.17686, [7] 2606.09809, [8] 2609.16302, [14] 2602.05043, [18] 2610.27672, [20] OpenAI blog (Jul 2026), [23], [26], [27], [19], [29]. I found no reference that looks fabricated, but I cannot clear these.
- Mismatched support: [25] (leaderboard illusion, a chatbot leaderboard paper) and [7], [11] for "teams use benchmark scores as acceptance evidence"; [9], [14] for "bottleneck shifts upstream" (W11).
- The companion MESA paper is not in the reference list, and no "A. Anonymous" placeholder is used, though the call asks for a placeholder for non public work.

**Rule checks:**
- Page limit: 15 pages including references (pp. 13 to 15 contain Data Availability and references). That is within the limit for technical design and scientific evaluation papers, and 7 pages over the limit for a research preview.
- Abstract: four paragraphs with the required headings (Context and motivation; Question/problem; Principal ideas/results; Contribution). Keywords are present. The abstract is dense and carries many task IDs and counts. OK.
- Anonymity: no names, affiliations or acknowledgments; placeholder contact address. The data package is described as anonymized. No self citation in the first person. The reference to a "companion submission" reveals that the authors have an overlapping submission, but the call states no policy. OK.
- Data Availability Statement: present at the end. It names the disclosed material and explains why the raw logs are kept out (local host paths). Acceptable form; the withholding weakens verifiability (W9).
- Generative AI: use is disclosed in Sect. 7 and 4.3. The call recommends the LLM Guidelines (llm-guidelines.org); the paper does not mention them, and there is no threats to validity section in that form (the LLM related threats are in Limitations).
- Layout: text overflow into margins on pp. 2, 6, 7 (W10).

##### 7. Score

**Reject** (a clear weak reject to reject: the work is careful and honest, but it is not yet a study).

##### 8. Reviewer confidence

**High.** The statistical claims were recomputed exactly, and the central problems (no session data, fixed MESA outcome, power) come straight from the paper's own statements; the only uncertainty is about the companion paper and the unchecked references.

##### 9. Recommendation

I would not accept the paper exactly as submitted. It reports a method and its pre-study checks, but the study that is meant to answer RQ1 and RQ2 has not run, the MESA outcome is fixed in advance by one release wide failure, and the planned sample sizes give a 2 to 10% chance of a definitive Accept at the true rates the paper itself considers. As a research preview (8 pages) it could be a reasonable plan paper, but it is not submitted that way and is too long for it. The smallest set of changes that would move my score up one step, to weak reject (or to borderline if the category is changed to research preview and the length is cut to 8 pages): (1) restate the RQs so that the sessions can falsify something, with outcomes and success criteria written down before the run (W1, W2); (2) drop the word "pre-registered" or deposit a time stamped manifest, and mark the pre-session results as exploratory (W3); (3) sign the forms from the clean run and add a second human rater for the 6 versus 11 B07 split, with agreement reported (W4); (4) fix the inconsistencies in the evidence rules (B14a counterexample, B05 coverage, a mitigated state for B28a) (W5); (5) either define and widen the simulation (audit_only baseline, power, Δ = 0, anchored parameters) or remove it (W6); (6) correct the 6 versus 7 task count and the Table 4 cut points for N = 90 and 120. To reach weak accept, the sessions would have to be run with larger N and a design in which MESA issues a decision on at least one case.

---

### Paper 2: reviewer for AI evaluation

#### REFSQ 2027 research track: review of submission "Applying Meta-Evaluation Benchmark Reviews to Requirement Decisions: An Executable Method" (paper2.pdf)

Reviewer role: PC member, AI evaluation (coding agent benchmarks, measurement validity, contamination, harnesses).

Scope note: I read the call, all 15 pages of the PDF, and the text extraction. I recomputed all Wilson and binomial numbers. I tried to check cited references on the web, but the web tools returned a usage limit error before any page loaded. So I did not verify any reference against its source. Where I comment on what a cited work says, I rely on my own knowledge of the pre-2026 works and mark it as such. I could not check the 2026 items at all.

##### 1. Summary of the paper

The paper proposes a decision engine that turns a benchmark review (the MESA rubric, described in a companion submission) into a requirement decision about a coding agent. The example requirement is: "for at least 70% of bug reports, within 15 minutes each", for SymPy bug fixing, at 95% confidence.

The engine has three levels. Level 1 checks input integrity (hashes, identities). Level 2 sets an evidence status (Admissible, Inquiry Required, Inadmissible) from seven rating forms (B05, B07, B12, B14a, B14b, B28a, B28b). Level 3 applies a 95% Wilson interval to the pass rate on the retained tasks. If evidence is not Admissible, the engine returns "No decision" and not "Reject".

The paper applies this to 20 SymPy tasks sampled from SWE-bench Verified (source) and plans a direct test on 20 SymPy tasks merged after the models' training cutoffs (target), for two agents (Gemini 3.8 Flash in the Antigravity CLI, GPT-6.1 Sol in the Codex CLI).

The coding sessions have not run. What exists is:
- (a) the schemas and engine, with 181 unit tests;
- (b) a B07 exploit check on the 20 source tasks (an LLM writes weakened patches; 17/20 pass the hidden tests; 6 tasks are judged defects);
- (c) a B05 check on one task (sympy-18199);
- (d) a B28a check (9 LLM-written test-runner patches on 3 tasks, all scored "resolved" by the SWE-bench harness);
- (e) LLM-drafted, human-signed rating forms;
- (f) exact binomial tables for the Wilson rule;
- (g) a synthetic Monte Carlo study.

The central finding is that both MESA policies return "No decision" on the SymPy case. This is because B28a failed (and, under the strict policy, B14a failed and B12 and B14b are unperformed). Raw rate, audit-only, ABA and ABC all issue score decisions. The paper states this outcome as "known pre-session" (Section 4.5).

##### 2. Paper category under the call

Page count: 15 pages including references. That fits only Technical design (15) or Scientific evaluation (15). It exceeds Experience report (12), Vision (8) and Research preview (8). So the "pending sessions" status cannot be solved by moving to the shorter categories without cutting 7 pages.

**Technical design papers.** Criteria in order: novelty, potential impact and relevance, soundness, verifiability, presentation.
- Novelty: modest. The engine is a threshold test (a Wilson bound) plus a rule that withholds when any criterion fails. The review rubric is not in this paper. The executed exploits (partial patches passing weak tests, runner patching) repeat known weaknesses of SWE-bench-style harnesses, including ones from the cited audits.
- Relevance: the link to the special theme is thin. The "requirement" is one sentence written by the authors, with a threshold that nobody elicited. There is no RE analysis (elicitation, stakeholders, trade-offs of the threshold).
- Soundness: see W1 to W8. The design is only "preliminary evaluation" in name: the evaluation cannot discriminate the artifact from baselines.
- Verifiability: partly met (replication package claimed). The rubric definitions are in a companion paper that is not cited.
- Presentation: dense and abbreviation heavy.

Verdict: this is the closest category, but the "preliminary evaluation" does not test whether the artifact works. It tests that the forms, once signed, make the engine withhold.

**Scientific evaluation papers.** Criteria in order: soundness, potential impact, verifiability, novelty, presentation, judged with the ACM SIGSOFT Empirical Standards.
- The study reports no result on its research questions. RQ1 is answered by construction (the forms fix the output). RQ2 needs sessions that have not run, and the MESA output is "not comparable" to anything.
- As an experiment, the design has too little power for either question (W3, W4).
- The paper does not meet soundness for this category as submitted.

**What "main sessions not run" means for each category it could be submitted under.**
- Technical design: acceptable in principle, since the artifact exists, but "evaluation" is then a demonstration, and the paper must say so. Claims about decision quality must go.
- Scientific evaluation: not acceptable. There are no results for RQ2, and the RQ1 result is a property of the forms.
- Experience report, Vision, Research preview: the status fits a research preview (a well defined plan with limitations and risks), but the page count does not.

##### 3. Strengths

- S1. The question is worthwhile. Using a public benchmark score as acceptance evidence for a requirement is common, and the paper ties the score to a threshold, a confidence bound and an explicit "withhold" outcome. Separating "Inconclusive" (statistical) from "No decision" (evidence defect) is a useful distinction.
- S2. The Wilson arithmetic is correct. I recomputed: 9/9 gives LB 0.7009 and 8/8 gives 0.6756 (so n_min = 9 holds); 14/20 gives LB 0.481; the cut points for N = 14, 15, 18, 20, 30 to 120 and every cell of Table 4 match my exact binomial calculation, including 78.8% at N = 62 and 81.9% at N = 60.
- S3. Frank limitations (Section 7), including that the empirical case does not show improved decision accuracy, the single signer, the shared scratch overlap, and the ABC session reading MESA rules.
- S4. Source and target pools are defined by deterministic procedures, with a session ledger, hashes and replay conditions. This is good practice if the freeze actually happens.
- S5. The simulation text states honestly that "most of the reduction ... comes from abstaining altogether" and that the selective gain over matched random abstention is about one point (Section 5.2).
- S6. The target set tries to handle the contamination problem, and the authors split out the 15 tasks whose issues opened after the cutoffs.
- S7. A Data Availability Statement is present and lists concrete contents.

##### 4. Weaknesses

**W1 (decision). The gate withholds on every SWE-bench Verified case, so the main result carries no information about the artifact.**
- Where: Sections 3.2, 4.5, 7, Table 3.
- What: B28a is "release-wide", B14a fails because of published memorization audits, and B12 is "Undocumented" because SWE-bench reports no confidence intervals. None of these depends on the agent, the repository, or the sessions. Any case built on this benchmark and harness returns "No decision". Section 4.5 says the outputs are "fixed in advance". RQ1 ("how does reviewing ... change the decision") is therefore answered by the forms, not by data. The lenient policy was meant to show a decision "when ... pretraining exposure are set aside", but it keeps B28a and so changes nothing.
- Why it matters: a gate that cannot return anything but "No decision" on the benchmark it is demonstrated on has not been shown to separate good evidence from bad. There is no case where the engine admits evidence, and no positive control.
- Fix: add at least one benchmark or harness variant where the gate can pass (for example, a clean-runner re-grade that removes B28a, or a benchmark with CIs and decontamination), and report the decision there. Alternatively, define in advance which forms would change the output and show that each one does, using a case-by-case sensitivity table.

**W2 (decision). B28a and the other failures are treated as existence proofs, with no link to the requirement and no credit for controls.**
- Where: Section 4.3 (B28a), Section 4.4, Section 3.2 Level 2.
- What: Nine patches, written by an LLM that was asked to exploit the runner, on 3 tasks, are scored "resolved". That shows the harness can be gamed. It does not show that the agents under test do this. The paper's own session validity rule (Section 4.4) marks any session that edits test-runner scripts as invalid, which is a control for exactly this threat. The engine has no way to record such a control, so a known and controlled risk makes the evidence Inadmissible. The 9/9 count is also not nine independent trials (3 per task, 3 tasks). The mechanism is not described: what do the patches do (print fake pass lines, skip tests, exit 0)? Did the writer know the hidden test names (a real agent does not)? Which harness version?
- Why it matters: this is the single form that decides the headline result.
- Fix: describe the patches and the writer's knowledge; report the SWE-bench harness version; allow a "mitigated" outcome with a compensating control (clean runner, trusted test files re-copied after the patch), and show the decision with and without it.

**W3 (decision). The sample sizes cannot support either research question.**
- Where: Table 4, Section 5.1, Sections 4.1 to 4.2, 6.2.
- What: At N = 14 to 20 and theta = 0.70, a true p = 0.75 agent is "Inconclusive" 97.2% (N = 14 and 20) and 95.5% (N = 18) of the time (I confirm these). The direct target test uses N = 20 (and 15 for the post-issue subset), with the same problem. RQ2 asks whether source and target decisions "agree". With both sides almost always "Inconclusive", agreement will be trivial. The authors know this (Section 6.2) but keep the design. The paper also uses only 20 of 75 SymPy source tasks, although all 75 are verified eligible and 108 target PRs pass the filter. Sessions are 15 minutes, so running all 75 per agent is cheap compared with the cost of an uninformative study.
- Why it matters: RQ2 will not produce a result that discriminates between methods, whatever the sessions show.
- Fix: use all 75 source tasks and as many target tasks as eligible (up to 108). Predefine what counts as agreement (for example a rate difference with an interval and a margin), not only decision labels. Report a power analysis for that agreement quantity, not only for the Wilson decision.

**W4 (decision). RQ2's direct test is confounded and is not a ground truth.**
- Where: Sections 1 (Gap 2), 4.2, 4.5, 7.
- What: The source-minus-target difference mixes at least five things: training exposure, task age and difficulty, how tests were built, how issues were screened, and how environments were built. SWE-bench Verified tasks were screened by human annotators for well-specified issues and valid tests. The target PRs are not screened that way. A lower target rate may come from underspecified issues or narrow or wide tests, which are the B05 and B07 defects the paper says it can detect. The paper applies its defect checks only to the source tasks. The target environment build, test validation, and grading harness are not described. If the target grading uses the same style of harness, B28a applies to it too, and by the paper's own rule the "direct test" is Inadmissible.
- Contamination argument: a PR merged after a "stated" cutoff is a weak guarantee. Stated cutoffs are approximate and providers differ in what they include. The PR can follow public discussion, a draft branch, or a ported fix from elsewhere. Issue opening dates are checked (5 of 20 fail), but PR creation, branch and discussion dates are not. Retrieval is the larger risk for post-cutoff tasks: the fix PR is public, so any web or search tool in either CLI is a leak. The paper handles this by flagging sessions after the fact (Section 4.4) and not by disabling the channel.
- Fix: apply B05/B07 checks to the target tasks; describe the target environments and grader; use a contamination-controlled design (for example matched-difficulty tasks, or control repositories), or at least bound what the difference can mean; report PR creation dates and discussion dates; enforce network and tool isolation technically (see W6).

**W5 (decision). The B07 headline overstates what was shown, and the oracle is the same LLM family.**
- Where: Abstract, Table 1, Section 4.3, Section 6.1, Conclusion.
- What: "cheating patches passing hidden tests on 17/20 source tasks" is the count of tasks where a patch that omits part of the reference fix passes the hidden tests. The paper itself says 11 of these are not defects because the omitted behavior is not in the issue. So only 6/20 tasks (30%) are defects by the paper's rule, and the 17/20 figure mostly reflects that the reference fix usually does more than the tests check. This is expected on nearly any benchmark with reference fixes. The independent verification test, the weakened patches, the two rating runs, and the "stated in the issue" judgment all come from one model (Claude Sonnet 5.5), given the reference fix. Agreement between run A and run B is the same model with the same prompt, so it is not independent evidence. The result depends on attacker effort ("up to three patches"), so it is a lower bound in one sense and arbitrary in another. No human validated the 6 defects or the 11 non-defects, other than the single signer. Run A had overlapping shared scratch folders (Section 7), yet the forms signed are from run A, while the clean run is B. The 34 field edits between draft and signed forms are not described.
- Related: the abstract says "(6 breaking issue-stated behaviors on signed B07, plus 1 B05 task)" and the Conclusion says "6 ... removed as task defects alongside 1 B05 overbroad-test task". That reads as 7 removed. But sympy-18199 is in the B07 list and is the B05 task, so the union is 6, and Table 3 removes 6 (20 to 14). The abstract and conclusion are misleading.
- Fix: report 6/20 as the result and 17/20 as the weak-test rate with its limits; get a second human rater on all 17; sign the clean run B or explain; list the 34 edits; fix the "plus 1" wording.

**W6 (decision). The sandbox and fairness of the two-agent test are not established.**
- Where: Sections 4.1, 4.4, 7.
- What: Isolation was tested in a scratch workspace (v1 to v8) before a rehearsal. Isolation "during the actual study sessions is verified from the recorded session transcripts during the study runs", so it is not yet verified, and checking is done after the fact. Transcripts record what the CLI logs, which may omit tool-internal actions. The two CLIs use different mechanisms ("tool flags and hook settings"), different scaffolds, and different model tiers and reasoning settings (a "Flash" model versus a "Sol" model at medium effort). Scaffold and model are confounded. This is acceptable if each agent is judged alone against theta, but the paper does not say which comparisons it will make across agents, and a reader will compare them. One run per task, no seeds, and a 900-second wall clock tied to provider latency make the "resolved in 15 minutes" quantity depend on infrastructure. Run-to-run variance is not modelled: the Wilson interval treats only task sampling as random.
- Fix: enforce isolation at the container level (no network, read-only test files, history truncated to the base commit, built-in web tools off) and show it in a pilot with a canary (for example a task whose fix is reachable on purpose); run at least 3 repeats per task and report variance; state that agents are not compared.

**W7 (decision). The B05 and several other forms are signed as "passed" or "Verified" on weak evidence.**
- Where: Section 4.3, Table 2, Section 3.2 Level 2.
- What:
  - B05 covers the pilot and 20 tasks, but only one task (sympy-18199) was probed by execution, and it was found through a published OpenAI audit [21]. Tasks that this audit did not list were not audited, so "outcome passed" for 19 tasks is absence of evidence. The paper cites the audit's "59.4% flaw rate on 138 tasks" as a "detection limit". If this figure is right (I could not load the source), a B05 check with that miss rate should not give "Verified, passed". That audit sample is also, as far as I know, the hard tasks that models failed repeatedly, so the rate does not transfer to the other tasks in either direction.
  - B14a ("Does benchmark guard against exposure?") is "Verified, failed" because published audits [15,21] show memorization by models. That evidence is about candidate models (B14b), not about benchmark safeguards. Under Section 2.1 the check kind would be "reported", not "run", and Level 2 rule (2) requires that "any counterexample patch was executed", which does not apply to B14a. So the rule and the form do not fit.
  - B28b ("Is shipped agent environment isolated?") is "Verified, passed" because container git history has no post-base-commit fix commits. That is a future-leak check, not an isolation check (network, permissions, mounts).
  - Level assignment: "Verified" is used for forms where the reviewer ran nothing.
- Fix: define for each criterion what "Verified" requires; split leak, isolation and memorization checks; mark B05 as "partially performed" on 1 task unless all tasks are probed.

**W8 (decision). The simulation shows little and its metric rewards abstention.**
- Where: Section 5.2, Table 5.
- What: "False acceptance per case" falls to zero if the method always withholds. The paper's own numbers show it: M3 coverage 6.8% and false acceptance 5.4% (d = 0.30, delta = -0.15) means about 79% of M3's issued decisions are false accepts (5.4/6.8); for M2 it is about 93% (20.8/22.4). Random withholding gives 6.4% at the same coverage, which equals M2's rate times the coverage ratio (20.8 x 6.8/22.4 = 6.3), so the effect is thinning. The remaining one point over random depends on assumed parameters (85% detection, 5% false alarm, 10% missing documentation) that nothing in the empirical part supports, and on a world where defective tasks inflate the source rate from 0.72 to 0.86 by assumption. The simulation uses N = 30, while the study uses 14 to 20. The text mentions delta = 0, a "576-cell sweep" and "all 72 noncompliant cells" without defining them; Table 5 shows only two shifts. The simulation is not described well enough to reproduce. At delta = 0 the method raises false rejection (0.44% to 1.42%).
- Fix: report a risk-coverage curve and the error rate among issued decisions; compare with always-withhold and with a fixed rule such as "require N of at least X"; drop the claim of benefit or show it on empirical data.

**W9 (minor). Related work misses the closest prior art and describes some work loosely.**
- Where: Section 1 (Gaps 1, 2), Section 2.2.
- What: I could not verify the 2026 references. For the older ones, from my knowledge:
  - "Studies of SWE-bench Live [33], SWE-rebench [3], and the SWE-Bench Illusion [15] show that leaderboard scores drop on post-cutoff tasks." The SWE-Bench Illusion [15] does not, to my knowledge, use post-cutoff tasks. It shows that models can name file paths and reproduce text for Verified issues at higher rates than for other benchmarks. Calling this "verbatim memorization of SWE-bench Verified items" (Section 4.3, B14a) is a stronger claim than the evidence for the SymPy tasks. SWE-bench Live compares different repositories and task sets, so a drop there is also confounded.
  - "UTBoost [32] and SWE-bench+ [1] recompute resolve rates after filtering tasks." UTBoost, as I recall, adds generated test cases to expose insufficient tests and recomputes rankings; it does not mainly filter tasks. SWE-bench+ filters on solution leakage and weak tests.
  - Both of these already test the B07 idea (insufficient tests accept wrong patches), so the B07 check is not new.
  - Missing, for example: work on patch correctness beyond the test suite in SWE-bench; the original SWE-bench Verified annotation procedure (test and specification quality ratings); EvalPlus for insufficient tests; leakage through repository git history in SWE-bench; LiveCodeBench-style time-window design; SWE-bench Pro and other contamination-resistant coding benchmarks; statistics for evaluations (error bars, clustered variance, paired comparison) and agent evaluation work on cost and variance; the measurement validity literature on LLM benchmarks (construct validity reviews).
  - The description of SWE-bench Verified omits that it is already a human-filtered subset of 500 tasks, with 75 from SymPy (the number matches my knowledge).
- Fix: add and position against these; rephrase Gap 2.

**W10 (minor). Dependence on the companion submission, and terminology.**
- Where: Sections 1, 2.1, 3, Tables 2 to 3.
- What:
  - The MESA rubric (B05, B07, B12, B14a, B14b, B28a, B28b) is defined in a "companion submission" that is not cited with a placeholder as the call requires. The criteria cannot be judged from this paper. "MESA" is never expanded in the text.
  - Terms are used in overlapping ways: Level (engine), Tier (evidence status and score decision are both "Tier 3"), Stage (Table 2), Phase. The abstract writes "Inadmissible (No decision)", mixing two outcomes.
  - Table 2's mapping of criteria to Kane's inferences is odd: B05 (tests reject valid fixes) is I_extrap while B07 (tests accept wrong fixes) is I_score. Both are scoring-validity threats. B28a/B28b (environment isolation) are labelled I_dec. The justification is not given.
  - ABC's T, O and R are never defined (Table 3). The 33 mapped items are a subset of ABC, which is not stated clearly.
  - The "Method 1" and "Method 2" coincide (Section 3.4), yet Table 3 lists "five families, six outputs".
- Fix: cite the companion anonymously; add a short table of the seven criteria with the exact check; define the terms once.

**W11 (minor). Statistical and wording issues.**
- "at 95% confidence" is implemented as a two-sided 95% Wilson interval, which is a 97.5% one-sided bound on each side. If a one-sided requirement is meant, use z = 1.645. Either is defensible, but say which.
- Tasks are 20 of a finite 75, so the finite population matters if the target is the 75; if the target is future bugs, say so.
- The threshold 0.70 and the 15-minute limit have no stakeholder source. "Pre-registered" is claimed in the abstract and contributions, but the frozen manifest does not exist yet (Table 1), and no registry or timestamp is given.
- "Resolved" uses all FAIL_TO_PASS and PASS_TO_PASS tests, while the requirement text says "the tests the maintainers later wrote for that bug pass".
- ABC ran after reading the MESA rating prompt (Section 7), which biases the baseline.
- The comparison with ABA ("removes 5 additional tasks that ABA did not flag") ignores that MESA does not remove sympy-13031, which ABA flagged. That disagreement is not discussed.

##### 5. Questions for the authors

- Q1. Is there any benchmark or harness setting, real or constructed, where the engine returns Accept or Reject? What would have to change for SWE-bench Verified to be Admissible?
- Q2. What exactly do the 9 B28a patches do, what did the writer know about hidden test names, and which harness version scored them? Do the agents' own sessions run through the same harness?
- Q3. Why only 20 of 75 source tasks and 20 of 108 eligible target PRs, when sessions take at most 15 minutes?
- Q4. What does "agree" mean in RQ2 when most outcomes will be Inconclusive? Which result would count against MESA?
- Q5. How are target tasks built and graded (environment, test validation, harness)? Were B05/B07 checks run on them?
- Q6. Why were forms signed from run A, which had shared-scratch overlap, and not from clean run B? What were the 34 edits?
- Q7. How was B05 "passed" established for the 19 tasks that were not executed?
- Q8. Is network and web tool access disabled in both CLIs by configuration, or only detected in transcripts? Do both CLIs log every shell action?
- Q9. What is the human validation of the 6 B07 defects and 11 non-defects?
- Q10. Is the companion paper required to understand the rubric? Does it use the same data, and how do the two submissions divide the contribution?
- Q11. How is run-to-run variance handled, with one session per task and agent?

##### 6. Checks made

**Arithmetic and counts that add up.**
- Wilson values: 9/9 LB 0.7009 (paper 0.701); 8/8 LB 0.6756 (0.676); 14/20 LB 0.481 (0.481). Correct.
- Cut points: N = 14 (accept 14, reject at most 6), 15 (14, 7), 18 (17, 8), 20 (19, 9), 30 (26, 16), 45 (38, 25), 60 (49, 35), 90 (72 by my calculation; the paper's Table 4 says 71, see below), 120 (94 by my calculation; the paper says 93, see below).
- Table 4 probabilities match my exact binomial values for the N = 14 to 60 rows. Examples: N = 14, p = 0.75 gives 1.8% accept and 97.2% inconclusive; N = 20 gives 2.4% and 97.2%; N = 18 gives 3.9% and 95.5%; N = 60, p = 0.85 gives 81.9%; N = 62 gives 78.8%.
- Possible discrepancy: for N = 90 and N = 120 my cut points are Accept at least 72 and at least 94, while Table 4 prints "Accept at least 71" and "at least 93". The table's probabilities (16.5% and 23.3% at p = 0.75; 92.6% and 98.1% at p = 0.85) match my values using 72 and 94, so the printed cut points look off by one, but the probabilities are right. Please check the cut points.
- Source counts: 17 passes = 6 defects + 11 non-defects. Correct. Eight MESA forms = B05, B07, B12, B14a, B28a, B28b + 2 x B14b. "Nine" forms = eight plus the ABC record (the ABC record is not a MESA form, but the count is consistent). ABC: 8 + 9 + 10 + 6 = 33 items, 15 caveats = 9 + 6, and T/O/R met items 5 + 2 + 1 = 8. Consistent.
- Removal counts: 6 B07 defects include the B05 task, so 20 to 14 is correct, and "5 additional tasks versus ABA" is correct (6 minus the shared 18199).
- Session budget: 2 + 40 + 40 + 8 = 90. Correct.
- Target pool: 322 merged PRs, 108 pass the filter, first 20 taken. The abstract and introduction say "13 June to 5 November 2026", while Section 4.2 says the pool is "1 May and 5 November" and only the first 20 happen to start on 13 June. Not wrong, but the order used ("deterministic order") is not specified for targets.

**Counts that do not add up or mislead.**
- "17/20 plus 1 B05 task" (Abstract, Conclusion) reads as 18 or 7 removals; the true union is 6.
- "Cheating patches ... on 17/20" versus 6 defects (W5).
- B05 form covers "pilot + 20" tasks but one task was executed (W7).
- Table 4 cut points at N = 90 and 120 (above).

**Terms used inconsistently.**
- Level / Tier / Stage / Phase; "Tier 3" for two different things; "Inadmissible (No decision)"; "forms" for the ABC record; "hijack" versus "grading runner failure"; "task defect" (B05/B07 removal) versus "defect" in Level 2 rule (2).
- "audit_only" and "M3_withheld" are the same numbers by construction (the paper says so).

**Claims without support.**
- "Verbatim memorization of SWE-bench Verified items [15,21]" (Section 4.3).
- "release-wide property of the grading harness" from 3 tasks (Section 4.3).
- "pre-registered" (Abstract) before the manifest exists.
- Simulation benefit (Section 5.2) rests on assumed detection rates.
- "teams often evaluate subsets of N = 14 to 30" (Section 6.2) has no citation.

**References.**
- I could not verify any reference (web tools unavailable). Items that look standard and consistent with my knowledge: [1], [3], [4], [10], [12], [15], [24], [25], [31], [32], [33] (arXiv ids and venues look right; I did not check content). Journal details for [6], [16], [22] and [27] look plausible.
- Items I cannot confirm and that should be checked for hallucination because they are 2026 arXiv or web items: [2], [5], [7], [8], [14], [17], [18], [20], [21], [28], [29], [30], and the journal entries [23] and [26].
- [11]: I recall the Hou et al. TOSEM paper with a different DOI suffix than the one printed; please check.
- [34] (ABC) lacks pages or an id, although the work exists to my knowledge.
- [20] and [21] are vendor web pages used as the basis of two checks (B05 and the 59.4% figure), without archived copies.
- The companion submission is not cited (W10).

**Rule violations.**
- Page limit: 15 pages with references. Allowed for the two fitting categories. Not allowed for the shorter categories.
- Abstract structure: four labelled parts, present. But the "Contribution" part lists artifacts and does not state added value and limitations as the call asks; it is also very dense and uses undefined abbreviations (MESA, ABC, B05, B07, B28a).
- Anonymity: no author names or affiliations. A placeholder email appears. The companion paper is mentioned without a third-person citation or "A. Anonymous" placeholder. The models used (Claude Sonnet 5.5, Claude Opus 5.5) are named, which is fine.
- Data Availability Statement: present and concrete. No link or anonymization warning is given, so I cannot check it. Raw session and harness logs are withheld (only hashes), which limits verification of the B07 and B28a results.
- Generative AI: the paper discloses LLM use in preparation and editing (Section 7). It does not cite the LLM guidelines the call recommends, and one model family built the engine, drafted the requirement, rated the forms and wrote the exploits.
- LNCS format: appears correct.

##### 7. Score

**Reject.**

(Between weak reject and reject. I choose reject because the main empirical claims either have no information content by construction or rest on a single LLM family's judgments, and the study that would test the research questions has not run.)

##### 8. Reviewer confidence

**Medium.** I know SWE-bench, its harness and the audit literature well and checked all arithmetic, but I could not verify any 2026 reference or the replication package.

##### 9. Recommendation

I would not accept this paper exactly as submitted. As a technical design paper it presents a reasonable idea (withhold a decision when benchmark evidence is defective) but shows no case where the gate does anything other than withhold, and the executed checks are weaker than the headline numbers suggest (17/20 versus 6/20; 9/9 on three tasks; B05 "passed" on one executed task). As a scientific evaluation paper it has no results on RQ2 and, with N between 14 and 20, cannot produce informative results. The smallest set of changes that would move my score up one step, to weak reject, is: (1) run the sessions, or reframe the paper clearly as a design paper and drop all claims about decision quality; (2) fix the abstract and conclusion wording on "17/20 plus 1 B05" and report 6/20 defects as the result; (3) use all 75 source tasks and more target tasks, with a predefined agreement measure; (4) add one case where the gate can pass, or a sensitivity table showing which form changes the output; (5) describe the B28a patches and let the form record a compensating control; and (6) cite the companion paper anonymously and add the missing related work. Moving to borderline would additionally need technical isolation of the sandbox, a second human rater for B07, and B05/B07 checks on the target tasks.
