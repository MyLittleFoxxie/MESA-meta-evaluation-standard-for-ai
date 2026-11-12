# REFSQ 2027 research track: review of submission "Reviewing AI Benchmarks as Evidence for Requirements: One Rubric from Seven Frameworks"

Category declared by the authors: technical design paper (15 pages). Criteria in order: novelty, potential impact and relevance, soundness, verifiability, presentation.
Reviewer role: programme committee member. I read the call, all 15 PDF pages and the text extraction. I did not search for the authors or the submission. Web search was used only to check whether some references exist.

---

## 1. Summary of the paper

Teams that build products on AI models they did not train often judge whether a model meets a requirement from a public benchmark score. The paper asks how far a benchmark can be trusted as evidence for such a requirement. It takes seven published frameworks for reviewing AI benchmarks (BetterBench, ECBD worksheet, Scorecard, How2Bench, Agentic Benchmark Checklist, Benchmark Caliper, OECD facets), copies their 280 questions, and sorts them into 30 "concerns". Concerns are ordered by Kane's four steps of a validity argument (scoring, generalization, extrapolation, decision) plus a descriptive group. From these it derives MESA, a rubric of 39 criteria: 8 descriptive properties (Part A) and 31 evaluative criteria (Part B). The central design choice is that every Part B rating has a "level" (Verified, Documented, Claimed, Undocumented, Contradicted, Not applicable), which describes the evidence in the sources, and an "outcome" (passed, failed, not performed, not recorded), which records what a check found. The aim is to keep a gap in documentation apart from a located defect.

Two studies use language models as reviewers on snapshots of four benchmarks (HumanEval, TruthfulQA, Humanity's Last Exam, τ-bench). In Study 1 one model (Claude Sonnet 5.5) applied the frameworks. The frameworks gave the same verdict in 159 of 302 comparisons (52.6%, Krippendorff's alpha 0.14). 143 disagreements were coded by a second model. 92 were attributed to framework design (narrower questions, different rules for missing documentation). 210 of 711 answers carried the mark "unreported", against 13 answers that cite a contradiction. In Study 2 two model families (Claude Sonnet 5.5 and Gemini 3.8 Flash Medium) applied MESA twice to each benchmark. Within a family, agreement on level was 99 of 124 (Claude) and 111 of 124 (Gemini). Between families, 90.9% of pairs agree on three coarse verdicts and 60.5% on six levels. Both families found the planted defects in six small invented benchmarks. Gemini found 3 of 7 known defects. All 14 failed or contradicted ratings were confirmed by scripts written afterwards. An audit by a second Claude model found direct support for 159 of 248 Claude Part B ratings. No human rater took part. A rule for using ratings in requirements decisions (Section 6.2) is proposed but evaluated in a companion paper under review.

---

## 2. Strengths

**S1. A real problem with a clear link to evidence for requirements.** Using a benchmark score as acceptance evidence for an AI component is a live practice. Framing it with Zave and Jackson and with validity theory (Kane) is a sound way to explain why a score does not carry the weight teams give it.

**S2. The separation of "what the sources support" from "what a check found" is a useful idea.** The paper shows with its own HumanEval example why one low mark for a missing practice and for a located defect leads to different actions. The idea is simple to state and easy to adopt.

**S3. The crosswalk of 280 questions into 30 concerns is useful work that others can reuse.** Table 2 reports consistent totals (280 items, 30 concerns, 39 criteria, 386 links). The paper states that the coverage of items by concerns is a property of the construction and not a finding.

**S4. Unusual honesty about limits and about what was fixed in advance.** Section 4.3 and Section 7 separate exploratory from planned analyses. They say that the list of known defects was fixed after the Claude sessions and is reported for Gemini only. They also say that the blind human rating was planned and not done, and that the audit and the coding of causes used a model of the same family. Few submissions say this much.

**S5. Several checks have an answer that does not depend on the reviewers.** Planted defects, a list of known defects, scripts that run code, and a mechanical check of cited files and quotations are a better design than agreement alone. The authors also report a finding against their own rubric (the wording of "Verified").

**S6. Extensive material is promised in the Data Availability Statement.** It lists every response including failed attempts, prompts, manifests, scripts and deviations from the protocol, and says what is left out and why.

---

## 3. Weaknesses

### W1. The artifact, the rubric, is not shown in the paper. Decision.
Where: Section 3.2, Tables 2 and 3.
What is wrong: For a technical design paper the artifact must be conveyed clearly. The reader sees only counts per step (Table 2) and the six levels (Table 3). No criterion text, no list of the 30 concerns, no example of a filled rating, and no example of how a criterion is worded for a reviewer appear. The worked case in Section 6.2 says "three criteria bear on this" and does not name them. A requirements engineer cannot judge, adopt or criticize MESA from the paper. The whole content lives in the replication package, which the reviewer cannot open (see W9).
Why it matters: Novelty and clarity of the contribution are the first and last criteria for this category. The call says that the contribution must be conveyed clearly.
Fix: Add a table of the 31 Part B criteria (short wording) and one complete example rating with level, outcome, who ran the check, coverage, blind spots and affected tasks. Free the space by shortening Sections 2.1 and 2.2 and the repeated numbers in Section 5.

### W2. All evidence about correctness comes from language models, and several claims go beyond that. Decision.
Where: abstract, Sections 5.3, 6.1, 8, 7 (construct validity).
What is wrong: No human applied a framework or MESA. Study 1 applies frameworks that were written for human reviewers through a single model without code execution. The conclusion in Section 6.1 that "the published tools for inspecting that chain do not yet give a stable answer" and that "a team that consults one framework gets a verdict that another framework would often reverse" is a statement about humans and teams. The evidence is about one model reading snapshots. The 10% change between runs of the same framework (19 of 21, 20 of 22) shows that a share of the measured disagreement is model noise. The paper never computes the agreement that two identical reviewers would reach under this noise, so 52.6% has no ceiling to compare with. The audit (159 of 248 supported, 29 weaker, 6 contradicted by the sources) was done by a model from the same family as the reviewer. The "confirmation" scripts were written after the ratings, by authors who knew them, and only test ratings that were already negative.
Why it matters: Soundness. The paper is honest in Section 7, but the abstract, Section 6.1 and the conclusion state the results in a form that a reader will take as a finding about the frameworks and about practice.
Fix: Restate the claims as "when applied by a language model". Compute the noise ceiling for RQ1 from the repeated runs. Report the 6 audit cases with false absence together with the 28 absence ratings, because they bear directly on RQ2.

### W3. The main reliability result for the levels is weak, and the 91% figure hides it. Decision.
Where: Section 5.3, Table 5, abstract.
What is wrong: Between families the alpha on six levels is 0.55 and agreement is 60.5%. Krippendorff's usual lower bound for tentative conclusions is 0.667. Within Claude the alpha is 0.70, just above it. The paper explains the gap as a weakness in the wording of "Verified". That is a plausible reading, but it was not tested (the wording was not changed and the sessions repeated). The families also differ in agent program, in cycle (exploratory against planned) and in model tier, so the wording is not the only candidate. The 90.9% figure for three verdicts uses a mapping from six levels and four outcomes to three verdicts that the paper does not give. It merges Verified and Documented, which is the very distinction on which the families disagree, so the high figure is partly produced by the mapping. The cross family numbers have no interval, and each rating is used in four pairs, so the pairs are not independent. Gemini chose Verified for 124 of 248 ratings, which is a rating that does not separate much.
Why it matters: The level is half of the central design choice. If it cannot be rated reliably, "how well a claim is supported" is not measured by the rubric yet.
Fix: Give the mapping and its justification. Report intervals using the bootstrap over criteria that already exists. State that the level scale does not reach reliability across families. Present the wording claim as a hypothesis. A revised wording and a repeat belong in future work, but then the abstract must not present agreement as a result for the rubric.

### W4. The outcome half of the rubric is not applied as defined, and the defect detection evidence is uneven. Decision.
Where: Sections 3.2, 4, 4.2, 5.3, 6.2, Table 5.
What is wrong: (a) Sessions "could not run code" (Section 4). The rubric records who ran the check and whether it passed or failed. A model that cannot run code produces "failed" or "passed" from reading. Section 6.2 says "the confirmation script settled it", so the disagreement on HumanEval isolation (Claude failed, Gemini passed) was settled outside the rubric. (b) The level "Contradicted" is itself a defect marker, and it is counted together with a "failed" outcome as detection. This blurs the clean split of level (evidence) and outcome (check) that the paper presents as its main idea. The allowed combinations of the six levels and four outcomes are not stated. (c) The planted defects are plain and designed by the authors who wrote the criteria. One of five ("missing list of tasks") is a gap and not a defect, and it is counted as found through the level Undocumented, which contradicts the distinction the paper makes. (d) Recall is poor where it can be measured: Gemini found 3 of 7 known defects and missed the HumanEval execution call, which is the example used in the introduction and in Section 6.2. The Claude figure of 6 is circular, as the paper says. Gemini found two τ-bench defects that were not on the list, so the list is incomplete. (e) Claude raised five false alarms on the planted copies. (f) The precision evidence (14 of 14 confirmed) cannot show how many defects are missed, which the paper says.
Why it matters: RQ3 asks whether negative ratings point at real defects. The honest answer is "when reviewers report a defect it usually exists, and they miss many". The abstract says "Both found all planted defects" and omits the rest.
Fix: Rewrite the abstract and Section 5.3 summary to report precision and recall together. Define the allowed level and outcome combinations. State that in these studies outcomes are judged from reading.

### W5. The requirements engineering content is thin, and the decision rule is not evaluated here. Decision.
Where: Sections 1, 2.1, 6.2, reference [5].
What is wrong: The claim that teams decide from public scores rests on one citation about requirements engineering for AI in general [15] and none about this practice. No requirement is elicited, no requirement is mapped to criteria, and no requirements engineer takes part. The only requirements example (80% of function tasks at first attempt) is hypothetical. The rule that makes the rubric useful for requirements ("a defect makes evidence unusable only if it can change the score", "missing documentation leads to a question") is stated in Section 6.2 and evaluated in a companion paper that reviewers cannot see. Section 2.1 says an AI model "has no specification that could be inspected at all", which is too strong (model cards and published behaviour specifications exist). The special theme (AI velocity) is not addressed.
Why it matters: Relevance and potential impact. The contribution reads as AI benchmark meta evaluation with an RE frame.
Fix: Support the practice claim with evidence or soften it. Show in the paper how a requirement is turned into a choice of criteria. State clearly which part of the RE value is in the companion paper and which is claimed here, and keep the claim here to what Sections 4 and 5 show.

### W6. The sorting of items into concerns, which defines everything downstream, rests on one person and an unnamed model. Decision.
Where: Section 3.1, Table 2, Section 7.
What is wrong: One author sorted 280 items after an AI assistant drafted the sorting. The model is not named ("the records do not say"), which also contradicts the Data Availability Statement that promises prompts and settings of all sessions. The author and the draft agreed on 180 of 280 items (64%). The final result equals the draft on 234 items, so in 54 of the 100 disputed items the author took the draft. Whether the author's sorting was independent of the draft is not clear. No second human sorted. "100 items disputed" and "100 items linked to more than one concern" are the same number, and the paper does not say whether they are the same items. The concerns decide which framework answers count as "the same question", so the 302 comparisons and the finding that "one framework asks a narrower question" (50 of 143) depend on this sorting. The seven frameworks were chosen to "cover" areas, with no search. [6] is cited but not used as a framework, and I found at least one further framework-like paper by search (Benchmark², arXiv 2601.03986) that is not mentioned.
Why it matters: The crosswalk is the first of two contributions. Without a check, a reader cannot tell what part is judgment.
Fix: State the model and settings. Report agreement between author and draft per concern. Ask a second person to sort a sample of items, which is a small task, or state clearly that this is a limit of the crosswalk. State the rule for choosing frameworks.

### W7. The headline ratio of sixteen to one is a count of answers, built on the paper's own translation rules. Decision.
Where: abstract, Sections 3.3, 5.2, 6.1, 8, Table 1 caption.
What is wrong: 210 and 13 count answers from four frameworks, not defects or benchmarks. One missing practice is counted once per framework that asks about it, and the same holds for one defect, so distinct findings are fewer. The 13 are "a lower bound of a particular kind" because sessions could not run code. Two of the 13 are on items that could not be answered from a snapshot, so the ratio on usable items is nearer 19 to 1 or higher, and it moves a lot with one count. The ratio depends on four benchmarks that are mostly mature and well documented, on a reading only setup, and on the paper's own "unreported" mark added by the authors' rule. The abstract gives 210 of 711, but the four frameworks with a penalty rule gave only 559 answers, so the share among answers that could carry the penalty is 37.6% (210 of 559). Table 1's caption says five frameworks score missing documentation as failure and that "Study 1 measures" this, but Caliper is not applied, so Study 1 covers four. The translation of a score into a verdict also has no stated threshold for middle values (BetterBench 10 of 15 becomes "Satisfied"), and the paper itself says partial credit changes agreement from 159 to 125 of 302.
Why it matters: The ratio is quoted in the abstract, discussion and conclusion as what frameworks "mostly record", which is a claim about frameworks in general.
Fix: Report distinct findings next to answers. Use 210 of 559 in the abstract. State the threshold rule for scores. Say that the ratio describes this setup and does not rank frameworks.

### W8. Numbers that do not agree with each other. Mostly minor.
See section 5 below for the full list. The ones that matter: Table 5 shows 27 (Claude) and 24 (Gemini) ratings at "Undocumented or Claimed", while Section 5.2 gives 21 + 5 = 26 and 21 for "ratings that rest on absent information". The audit reports 54 ratings that "report an absence", against 28 in Section 5.2. The false alarm denominator ("of 50 chances") is not explained. The abstract says "six small test benchmarks" with planted defects, and only five have one. Confirmation counts (10 Claude and 4 Gemini failed outcomes, 2 and 3 Contradicted) are not reconciled, and it is not stated whether the five Claude false alarms are among the 14. One of the 31 criteria (exposure of a named model) is not applicable in all sessions by design, so it adds trivially agreeing ratings.
Why it matters: A reviewer who recomputes finds gaps, and this lowers trust in the other counts. It is also a decision for the table of results to be readable.
Fix: Reconcile or explain each count. Exclude the criterion that cannot be rated, or report agreement with and without it.

### W9. The material for verification cannot be opened, and the LLM reporting is incomplete. Minor.
Where: Data Availability Statement, Section 4.
What is wrong: The link is a placeholder (https://doi.org/10.5281/zenodo.XXXXXXX). The call rewards sharing and the criteria include verifiability, so reviewers need a working anonymous link. Model names, versions, run dates, settings, the two agent programs and the "worked example" are not given in the paper. The call recommends the LLM Guidelines Initiative, and the paper does not say whether it followed it. The HumanEval commit that contains the exec() call is not named in the text.
Fix: Give a working anonymous link. State model identifiers, dates and settings in a short table. Add a statement on the LLM guidelines. Name the commit.

### W10. Writing: the paper does not let a newcomer follow it, and the voice is not consistent. Minor, with W1 as the main part.
Where: throughout. Details in section 5 (writing) below.
Fix: Introduce each framework in one line, explain "snapshot", "session", "verdict", "comparison" and "answer" in the introduction, fix voice, and add a Study 1 results table.

---

## 4. Questions to the authors

1. Which model drafted the concerns, with which prompt? Were the draft and the author's own sorting made without sight of each other? Are the 100 disputed items and the 100 items with several links the same items?
2. How exactly are the six levels and four outcomes mapped to the three verdicts used for the 90.9% figure? Please give the figure for the mapping that keeps Verified apart from Documented.
3. What is the rule for translating a mid range score (such as 10 of 15) into a verdict in Study 1? How many Satisfied verdicts rest on partial credit?
4. Does "Open" count as a verdict in a comparison? How many of the 302 comparisons involve it?
5. What are the 50 "chances" for false alarms? Where did Claude raise its five false alarms (which copies and runs)? Are they included among the 14 confirmed ratings?
6. Why do Table 5 (27 and 24) and Section 5.2 (26 and 21) differ? Why does the audit count 54 absences against 28?
7. How many distinct defects, and how many distinct missing practices, lie behind the 13 and the 210 answers?
8. The HumanEval confirmation shows that "a wrong answer passes when it returns an object that compares as equal to anything". Does that show the isolation failure (exec in the same process) or a weak comparison in the tests? Does either change the pass rate of any real model, and by how much?
9. What do the 15 failed Claude attempts on the planted copies have in common? Could the setting that failed correlate with the defect?
10. Why are Part A audit results (64 ratings per family) not reported, although the audit covered 312 ratings?
11. How many quotations did each family cite in total, so that 303 (Claude) and 300 (Gemini) matches can be read as shares? Two of the 445 files cited by Gemini do not exist. What were they, and do the ratings that cite them still stand?
12. Is the companion paper [5] submitted by the same authors to this conference? What part of the contribution here depends on it?

---

## 5. Checks I made

### 5.1 Counts and percentages

| Item | Paper | My result | Status |
|---|---|---|---|
| Table 1 items | 47+20+68+55+44+28+18 | 280 | Correct |
| Table 2 concerns, criteria, links | 30, 39, 386 | 1+2+6+10+11 = 30; 8+2+6+11+12 = 39; 10+46+58+173+99 = 386 | Correct |
| Criteria split | 39 = 8 + 31 | 29 evaluative concerns + 2 split = 31 | Correct |
| Links against items | 100 items with 2 or 3 concerns | 386 = 180 + 2×94 + 3×6 is possible | Possible, not stated; the caption says only "two" |
| Sorting | 180 agree, final equals draft on 234 | 64.3% and 83.6% | Correct; implies author took the draft in 54 of 100 disputed items |
| Framework use of concerns | 27 + 3 | 30 | Correct |
| Study 1 sessions | 18 | 4×4 + 1 + 1 = 18, plus 2 repeats = 20 | Correct; abstract says "six frameworks to four benchmarks", but two were applied to one benchmark each |
| Agreement | 159 of 302 = 52.6% | 52.65% | Correct |
| Partial credit rule | 125 of 302 | 41.4% | Correct as percentage |
| Majority rule | 143 of 302 | 47.4% | Correct; lower than the strict rule, so the claim "the rule is not the cause" holds |
| By concern group | 17/19, 117/221, 25/62 | 19+221+62 = 302; 17+117+25 = 159 | Correct (89.5%, 52.9%, 40.3%) |
| Table 4 | 50+42+42+8+1 | 143 = 302 − 159 | Correct; 50+42 = 92 correct (64.3%) |
| Repeats | 19 of 21, 20 of 22 | 4 of 43 changed = 9.3% | "One in ten" is correct |
| Answers with penalty rule | 559 of 711, 210 unreported | 78.6%; 210/559 = 37.6%; 210/711 = 29.5% | Correct; abstract uses the smaller denominator |
| Ratio | "sixteen times" | 210/13 = 16.2 | Correct; without the 2 unanswerable items 210/11 = 19.1 |
| Part B levels, Claude | 46+138+27+2+35 | 248 | Correct |
| Part B levels, Gemini | 124+63+24+3+34 | 248 | Correct |
| 28 absent ratings | 21+5+2 | 28 | Correct, but Table 5 shows 27 at "Undocumented or Claimed" against 26 in the text |
| Gemini absent ratings | 21, of which 20 Undocumented | Table 5 shows 24 at "Undocumented or Claimed" | Not reconciled |
| Within family | 99, 111, 83, 104 of 124 | 79.8%, 89.5%, 66.9%, 83.9% | Correct; table caption says agreement is "high", which fits Gemini better than Claude (67% on level and outcome) |
| Part A | 26 and 30 of 32 | 81.3%, 93.8% | Correct (8 properties × 4 benchmarks = 32) |
| Cross family pairs | 124 × 4 = 496 | 496 | Correct |
| 451 of 496 | 90.9% | 90.93% | Correct |
| 300 of 496 | 60.5% | 60.48% | Correct |
| Excluding the criterion that is not applicable by design (if it was Not applicable in all sessions) | not reported | within family: 95/120 = 79.2%, 107/120 = 89.2%; cross family 435/480 = 90.6%, 284/480 = 59.2% | Small effect; should be reported |
| Audit | 159+54+29+6 | 248 | Correct (159 = 64.1%; 11 of 46 Verified = 23.9% weaker) |
| Audit scope | 312 ratings | 248 Part B + 64 Part A = 312 | Consistent, but Part A audit results are not given |
| Planted defects | 5 defects × 2 runs | 10 runs | Correct; "six benchmarks" in the abstract overstates, as one has no defect |
| Claude planted copy runs | 12 valid after 15 failed | 6 × 2 = 12; 27 attempts | Consistent; no data on Gemini failures |
| Confirmation | 10 + 4 = 14; 9 code or data + 5 passages = 14 | 14 | Correct; relation to 2 and 3 "Contradicted" and to the 5 Claude false alarms is not explained |
| False alarm denominator | "of 50 chances" | 12 runs (10 with defect + 2 clean) | Not explained |
| Abstract length | no limit in the call | about 280 words | Long for LNCS; over 40% is numbers |

### 5.2 Terms used before they are defined or never defined
- "Comparisons" and "answers" appear in the abstract and are defined only in Section 4.1.
- "Level", "outcome", "verdict" and "Verified" appear in the abstract and the introduction before Table 3 and Section 3.3.
- "Part B" is used in the caption of Table 3 before Part A and Part B are introduced in Section 3.2.
- Each of the seven frameworks is cited by number and never described. Table 1 gives only items, scope and the rule for silence. "OECD facets" and "Caliper" are used before any description.
- "Meta-Evaluation" in the name MESA is not explained.
- "Snapshot", "session", "agent program", "worked example", "first cycle" and "exploratory cycle" are not defined or only half defined.
- "Kane's four steps" is used in Section 2.2, but Table 2 has five rows (Description is the fifth and is not a Kane step). The Decision step is defined in Section 2.2 by "documentation, licence and upkeep", and Table 2 lists "isolation" under Decision, which the definition does not cover and which reads as a scoring issue.
- Krippendorff's alpha is explained, but the scale used for the "ordered levels" is not (where do Contradicted and Not applicable sit?).

### 5.3 Claims that go further than the evidence
- Abstract: "Both found all planted defects in six small test benchmarks" (five have a defect; defects are plain; Gemini found 3 of 7 known defects and missed the HumanEval call; Claude raised five false alarms). "Running code confirmed the defects they reported in benchmark code" (9 of 14; the other 5 by comparing passages).
- Abstract and Section 6.1: "can give opposite verdicts on the same benchmark", "a team consulting one framework gets a verdict another would reverse". The evidence is one model reading snapshots with a translation to three verdicts defined by the authors.
- Section 5.3: "a weakness of the rubric's wording and not noise". Not tested and confounded with agent program, cycle and model tier.
- Section 5.3: "the rubric is about as repeatable as the frameworks it draws on". Counts on 21 and 22 concerns for one benchmark.
- Section 6.2: "The score should not be used as it stands." The paper shows that a wrong answer can pass. It does not show an effect on any model's score. The rule it proposes turns on what "can change" the score.
- Section 2.1: "no specification that could be inspected at all".
- Section 2.3 and introduction: "none of them compares the review frameworks question by question, and none separates missing documentation from located defects". This negative claim needs a described search. ECBD already records silence without a score (Table 1), which the paper notes.
- Section 1: teams "treat a high score as evidence", with no source on the practice.
- Section 5.2: "the rubric kept the two apart". The rubric separates them by construction. The evidence for accuracy is the audit, where 6 ratings reported an absence that the sources contradict.

### 5.4 Rule checks against the call

| Rule | Result |
|---|---|
| Page limit 15 including references | Met. The PDF has 15 pages and the reference list ends on page 15 with half a page free. Adding the rubric (W1) requires cuts elsewhere. |
| LNCS format | Looks like LNCS. No sign of a layout problem. |
| Abstract in four labelled paragraphs | Met. The four labels match the call exactly. |
| Keywords after the abstract | Met. "Acceptance Testing" is a loose fit. |
| Anonymity | Mostly met: "Anonymous Author(s)", placeholder affiliation and contact, no acknowledgments, own work cited as "Anonymous, A." Weak points: "A companion paper" in Section 6.2 and the title of [5] (with "meta-evaluation" and "requirement decisions") tie the submission to a second submission by the same group. The Disclosure of Interests says "the authors" while Section 3.1 and Section 7 say "one author". Zenodo records usually carry author metadata, so the real link must be checked. |
| Data Availability Statement at the end | Present, in an unnumbered section after the Conclusion and before the references. The link is a placeholder. |
| Hallucinated references | I found no sign of invented references. I confirmed by search that [13] (arXiv 2606.09809), [14] (MAKE 8(6) 141), [20] (ACL Anthology 2026.evaleval-1.25), [23] (arXiv 2602.05043) and [28] (NIST AI 800-2 ipd) exist. [8] has the arXiv number 2501.10711, but the versions I could see carry the title "How Should We Build A Benchmark?", and I could not see version 5. I could not confirm [3] (Alonso and Church, SIGIR Forum 58(2)) and its DOI, nor [2] (the Benchmark Caliper repository), so these two need a check. The remaining references are works I know (Zave and Jackson, Kane, Berry, Vogelsang and Borg, Maiden and Ncube, Hayes and Krippendorff, HumanEval, TruthfulQA, HLE, τ-bench, BetterBench, ECBD, AMLAS). |
| Generative AI and LLM guidelines | The paper uses models as research instruments and for the draft sorting. It does not refer to the LLM Guidelines Initiative or say how it follows it. |
| Category fit | The paper says technical design. Sections 4 and 5 are about 6.5 pages of empirical evaluation, and the soundness questions are those of a scientific evaluation. This is acceptable but should be said clearly. |

### 5.5 The writing

- One careful person? Mostly yes. The sentences are short and plain, limits are stated, and the structure repeats cleanly. But the voice shifts between "we", "one author", "the author" and "the authors", and the counts disagree in places (W8). The rubric and the evidence are described in different depth: pages 8 to 10 carry many numbers in running text.
- Can a requirements engineer who has not seen the seven frameworks follow it? Not fully. The frameworks are never described, no criterion is shown, and the key terms (level, outcome, verdict, snapshot, session) are not set out before they are used. The HumanEval example in Section 1 and Section 3.3 helps a good deal, and Table 3 is clear.
- Does each table answer a question the text raises? Table 1 answers "how do frameworks treat silence". Table 2 answers "what do the concerns cover" but does not say what the concerns are. Table 3 defines the central notion. Table 4 answers "why do frameworks disagree" and is clear, although the coder is a model. Table 5 mixes four questions (repeatability, level use, planted defects, known defects) and has no counts per benchmark. Study 1, the first study, has no results table by framework pair or by benchmark, so RQ1 is carried by running text. There is no figure.
- Is each term introduced before use? No (see 5.2).

---

## 6. Scores (1 poor to 5 excellent)

| Criterion | Score | Reason |
|---|---|---|
| Relevance to requirements engineering | 3 | The topic is evidence for acceptance of AI components, which fits RE for AI, but no requirement, no requirements engineer and no decision is studied, and the RE rule sits in an unseen companion paper. |
| Soundness | 2 | The evidence rests on model raters with no human gold standard, a single sorter, unreliable level ratings across families, weak recall of defects, and counts that do not agree. |
| Novelty | 3 | The crosswalk and the split of evidence level from check outcome are new in combination, but the split is simple and partly present in ECBD and OECD, and the related work search is not described. |
| Clarity | 3 | The prose is plain and honest, but the artifact is missing, terms come late, the frameworks are not described, and the voice is not uniform. |
| Reproducibility | 3 | The package described is thorough, but the link is a placeholder, model and agent details are not in the paper, and runs of closed models are not repeatable. |

---

## 7. Recommendation

**Weak reject.**

Reasons: The idea is useful and the authors are open about limits, and I would like to see the work at the conference after revision. But the contribution as submitted cannot be judged because the rubric is not in the paper (W1). The claims about reliability and defect detection go further than model only evidence allows (W2, W3, W4). The part that relates to requirements decisions is evaluated elsewhere (W5). The crosswalk rests on one person and an unnamed model (W6), and the headline ratio is built on the paper's own translation rules (W7). Several counts do not agree (W8). Most of this can be repaired in text and analysis already available, so I do not recommend a strong rejection. Under the criteria for technical design papers, novelty and relevance are medium and soundness and verifiability are below the level of acceptance.

## 8. Approval status in plain words

Today the paper would not be accepted. It sits below the line, and the programme committee would be split between weak reject and borderline. What decides it: (1) whether the rubric and one worked rating appear in the paper; (2) whether the abstract, discussion and conclusion state results as "model applied" findings and report defect recall next to precision; (3) whether the numbers are reconciled and the mapping to verdicts is given; (4) whether the RE value is shown in this paper or clearly claimed only for the companion; and (5) whether reviewers can open the replication package. If all five are fixed, I would move to weak accept. A human check of a sample would move it further.

## 9. Improvements that need no new experiment or data

| # | Improvement | Priority |
|---|---|---|
| 1 | Add a table of the 31 Part B criteria and one complete example rating (level, outcome, who ran the check, coverage, blind spots, affected tasks). Cut Sections 2.1 and 2.2 and some numbers in Section 5 to make room. | Must fix |
| 2 | Reconcile all inconsistent counts (27 against 26, 24 against 21, 54 against 28, "50 chances", 14 against 10+4 and the Contradicted counts, Table 1 caption "five" against four applied, 18 against 20 sessions) and explain how the 14 confirmed ratings relate to the 5 Claude false alarms. | Must fix |
| 3 | Rewrite the abstract so that it matches the results: five planted defects, not six; Gemini 3 of 7 known defects and missed the HumanEval call; five Claude false alarms; confirmation by running code for 9 of 14; "applied by a language model". | Must fix |
| 4 | State the mapping from levels and outcomes to the three verdicts and the scale used for alpha. Give an interval for the cross family figures. | Must fix |
| 5 | Replace "the published tools do not give a stable answer" and "a team would get reversed verdicts" with statements that name the setup. Compute the noise ceiling from the repeated runs. | Must fix |
| 6 | Give a working anonymous link to the package. Put model names, versions, dates, settings and agent programs in a table in the paper. Name the HumanEval commit. | Must fix |
| 7 | Describe each of the seven frameworks in one line and define level, outcome, verdict, comparison, answer, snapshot and session at first use. | Must fix |
| 8 | Name the model that drafted the concerns, state whether the sorting was independent, and report agreement per concern. State the rule for choosing the seven frameworks. | Should fix |
| 9 | Report agreement with and without the criterion that cannot be rated in these sessions. | Should fix |
| 10 | Report counts of distinct findings behind the 13 and the 210, and use 210 of 559 beside 210 of 711. | Should fix |
| 11 | State the rule for mid range scores in Study 1 and how many verdicts rest on partial credit. | Should fix |
| 12 | Define the allowed combinations of level and outcome, and say that in these studies the outcome is judged from reading. Treat "Contradicted" explicitly. | Should fix |
| 13 | Present the Verified wording explanation as a hypothesis. | Should fix |
| 14 | Add a table of Study 1 results by benchmark and by framework pair. Split Table 5 into repeatability and defect checks. | Should fix |
| 15 | Report the Part A audit results and the denominators for quotation matches. | Should fix |
| 16 | Soften the "no specification at all" statement, the "none separates gap from defect" claim and the claim about team practice, or add sources. | Should fix |
| 17 | Say which part of the RE contribution lies in the companion paper [5]. Consider removing "companion" and the descriptive title from the reference to protect anonymity. | Should fix |
| 18 | Add a statement on the LLM guidelines. Verify references [2], [3] and [8]. | Should fix |
| 19 | Use one voice ("we") throughout and remove the plural and singular "author" mix. Shorten the abstract. | Should fix |
| 20 | Explain why "isolation" sits under the Decision step, or move it under Scoring. | Should fix |

---

## 10. Comparison with round 3 (added by the revising session, not by the blind reviewer)

Sections 1 to 9 above are the blind review, unchanged. It read the paper as it stood before the last set of small fixes. This section compares it with the round 3 review and records what was done afterwards.

Scores, round 3 then round 4: relevance 3 and 3, soundness 2 and 2, novelty 3 and 3, clarity 2 and 3, reproducibility 4 and 3. Recommendation: weak reject both times. Reproducibility fell because the blind reviewer could not open the package link, which is a placeholder until the upload.

| Round 3 weakness | Status | Note |
|---|---|---|
| W1 No human reference | Still open | Stated in the abstract and in the threats section, with the blind check that was not carried out. Round 4 W2 raises it again. |
| W2 Known defect list fixed after the Claude sessions | Fixed | The paper gives the timeline and reports the Gemini figure (3 of 7) as the test. |
| W3 "14 of 14 by execution" | Fixed | Reported as nine by running a script and five by comparing passages, in the text and now in the abstract. |
| W4 Planted defect test small | Reduced | The paper says the test is small and shows no ceiling. The abstract no longer says six benchmarks. |
| W5 Requirements engineering content thin | Reduced | A worked case on one requirement was added. Round 4 W5 still finds that the decision rule is not evaluated here. |
| W6 Density | Reduced | Clarity rose from 2 to 3. Round 4 W1 and W10 still ask for the criteria and for earlier definitions. |
| W7 Study 1 rests on one model and the authors' translation rules | Reduced | Stated as a limit. The claims in the discussion now name the setup. |
| W8 Unequal session conditions | Reduced | The agent programs, the effort setting and the 15 failed attempts are in the paper. |
| W9 Reading of the gap between families | Fixed | The mapping from levels to verdicts is stated, and the explanation is given as a reading that the data cannot test. |
| W10 One person sorted the items | Still open | Stated. The model that drafted the sorting is not in the records. |
| W11 Internal identifiers | Fixed | No commit numbers, file names, defect codes or criterion codes in the text. |
| W12 Small errors | Fixed | The Data Availability Statement is complete except for the link. |

Round 4 points fixed after the review: the abstract (five planted defects, 9 of 14 by code, 210 against 13); the count differences between the text and the results table (27 and 24 against 28 and 21, the 54 of the audit, the 50 chances); the caption of the framework table; the level to verdict mapping; one voice for the authors; agent programs and effort setting; seven statements that the reviewer found too strong; short names for all 30 concerns in the concerns table.

Round 4 points still open:

- The 31 evaluative criteria and one full example rating are not printed (round 4 W1). About twelve lines are free on page 15, which is not enough for a table of 31 rows. This needs a cut elsewhere and is a decision for the author.
- No interval for the cross family figures, no agreement per concern, no Study 1 table by benchmark. Each needs a new computation that would have to be checked.
- The package link is a placeholder.
- No statement on the guidelines for language models in software engineering research that the call recommends.
- The companion paper and its title link the two submissions. Both are anonymous, and the call allows anonymous citation of own unpublished work.

## 11. Author decision after this comparison (11 November 2026, evening)

The author decided that the paper presents the finished experiment only. The statements of limits named in the table above (no human rater in the abstract, the timeline of the known defect list, when the confirmation scripts were written, the failed attempts, the differences between the sessions, the blind rating that was not carried out) were taken out of the paper. One section "Limitations" before the conclusion replaces the threats section, and evaluation with human reviewers is named as a next step. The known defect check is reported for Gemini only (3 of 7), so the Claude figure, which was not a test, is no longer in the paper. A figure of the method was added. For round 3 weaknesses W1, W3, W4 and W8 the status "stated in the paper" therefore no longer holds: the facts are in the records of the replication package and not in the text.
