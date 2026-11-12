# REFSQ 2027 Research Track: Review of Paper 2 (round 3)

Title: "Can a MESA Benchmark Audit Predict Decision Reliability on New Issues? A Controlled Study on SymPy"

Category assumed: scientific evaluation paper (the paper does not state its category). Length: 13 pages including references, within the 15 page limit. Abstract has the four required parts. Keywords are present. A Data Availability Statement is present.

Reviewer expertise: requirements engineering, empirical methods, evaluation of coding agents.

---

## 1. Summary of the paper

The paper asks whether an audit of a coding benchmark with the MESA rubric (a rubric the authors introduce in two companion papers under review) leads to better acceptance decisions than a raw pass rate. The stakeholder requirement is that an unsupervised coding agent fixes SymPy bug reports with a resolve rate of at least 0.70, judged by a one sided 95% exact binomial rule. The study runs one agent (GPT-6.1 Sol in Codex CLI) on 44 SWE-bench Verified SymPy tasks ("source") and on 44 SymPy issues created after the model's stated training cutoff ("target"), plus one pilot task. Before the runs, language models check the hidden tests for weakness (a deliberately incomplete patch that passes), rate whether the bug report states the broken behavior, probe for training exposure, and test whether edits to the test runner change grading. The authors then compare eight ways of reading the source result: raw score, audit only filtering, the Agentic Benchmark Checklist (ABC) with and without a gate, and three MESA policies (strict, lenient, controlled). The source rate is 35/44 (79.55%, Inconclusive); after removing 32 tasks judged to have weak tests it is 10/12 (Inconclusive). The target rate is 21/44 (47.73%, Reject), and 7/20 after the same filtering. The paper concludes that SWE-bench Verified rates overstate capability on new issues, that weak tests are widespread, and that a case level control on runner file edits lets MESA reach an admissible decision where fixed policies block.

## 2. Strengths

1. The question matters for the REFSQ 2027 theme. Teams do pick coding agents from leaderboard numbers, and the paper ties that choice to an explicit requirement with a threshold and a decision rule.
2. The decision rule is stated before the data and is exact. The cut points for n = 44, 12 and 20 are correct (Section 5, check C1). The paper also shows honestly that filtering to 12 tasks makes Accept almost unreachable (14.2% power at a true rate of 0.85).
3. The held out target set after the stated training cutoff is a good design idea. It gives a direct test of the same requirement on new issues from the same repository.
4. The paper reports failures of its own controls. Slot 61 is a correct fix inside SymPy's own runner module that the runner file rule flags. This is useful for practitioners who plan to use such rules.
5. The paper reports results three ways (scope rule, all demonstrated defects removed, none removed). This makes the effect of the filtering visible.
6. Most numbers in the paper are internally consistent. Nearly all percentages, cut points, Newcombe intervals and table sums agree with my recomputation (Section 5).
7. The runner edit test on four layouts (Section 4.2) is a concrete and reusable finding: on SymPy, edits to runner files alone can make the harness grade a task as resolved.

## 3. Weaknesses

**W1. The study cannot answer its title question, and RQ1 shows no difference between arms that matters.**
Where: title, abstract (Question/problem), Section 5.1, Table 5, Section 5.2 ("not_comparable").
Why it matters: The title asks whether a MESA audit predicts decision reliability on new issues. By the paper's own agreement rule, both raw and filtered source arms are "not_comparable" with the target. No source arm gives Accept. The raw pass rate is already Inconclusive, so no arm would have led to a wrong acceptance that MESA then prevented. Every arm gives Inconclusive or no decision. The abstract asks whether MESA yields "more cautious and defensible" decisions, but the data show only that MESA withholds where the raw rule is already Inconclusive. The study cannot show added value for MESA over a raw rule, or over ABC. In addition, M3_lenient and M3_controlled look like policies made to pass the gates that blocked the stricter policy. The paper does not say whether they were fixed before the runs.
Decides recommendation: yes.

**W2. The drop from source to target is confounded, so it cannot be read as "overstated capability".**
Where: Section 5.2 ("severely overstate capability on unseen post-cutoff issues"), Conclusion (third finding), abstract.
Why it matters: Source tasks went through SWE-bench Verified human screening, which removed unclear issues and tests that reject valid fixes. Target tasks had only automated base fail and fix pass checks (Threat 5). Target tasks also seem harder: median runtime 76 s against 49 s, median steps 14 against 10, and exact file set matches much rarer. A lower target rate can come from harder tasks, from unclear issues, or from tests that reject valid fixes. It need not come from exposure or benchmark artifacts. The paper audits weak tests (B07), which would raise the target rate, but does not audit tests that reject valid fixes on the target. The exposure probe (Table 3) shows no difference in "any file named" and a large difference in exact matches, which the paper does not interpret. The claim of overstated capability needs these explanations ruled out or stated as alternatives.
Decides recommendation: yes.

**W3. The weak test defects rest only on model judgments, and the "clean" sets are half unchecked.**
Where: Section 4.1, Table 2, Threat 1, Conclusion ("pervasive weak-test defects").
Why it matters: 32 of 44 source tasks (73%) are labelled as having weak tests. This is far higher than rates in most prior audits the paper cites, and needs validation. The defect label depends on a check script written by Gemini from the issue and the reference fix, and on two Claude ratings. No human checked any item; the author signed the forms without review. The incomplete patches came from the same model as the agent under test (Threat 2), which weakens the claim of "cross family" independence. The 12 retained source tasks are 6 with a valid check and no defect plus 6 with an invalid check. The 20 retained target tasks include 12 that were not checked at all (10 invalid, 2 without a candidate). Calling these sets "clean" overstates what was shown. Also, a weak test does not mean the agent's patch on that task was wrong. Running check.py on the agent's own patches would have been the direct test, and the paper does not report it.
Decides recommendation: yes, together with W1 and W2.

**W4. The paper is not self contained for a requirements engineer.**
Where: Sections 1 to 4, Figure 1, Tables 1, 4 and 6.
Why it matters: The paper relies on two companion papers under review [2, 3] for the meaning of MESA, the three levels, the criterion codes (B05, B07, B12, B14a, B14b, B28a, B28b), the statuses (Verified, Documented, Undocumented; passed, failed, not_performed), "anchor", "Admissible", "Inquiry Required" and "Withheld". SWE-bench terms (FAIL_TO_PASS, PASS_TO_PASS, hidden tests, harness) and ABC parts (T, O, R and items such as T.5 or O.d.2) are not explained. A reader who has not seen MESA, SWE-bench or ABC cannot follow Sections 3.2 and 4.3 or Table 4. Section 6 of this review lists the terms. A reviewer cannot judge the method without the companion papers, which the reviewer cannot see.
Decides recommendation: partly. It lowers clarity a lot and would be a must fix even if W1 to W3 were solved.

**W5. Interval labels are inconsistent, and one "non overlapping" claim depends on that choice.**
Where: Table 5 header "95% Exact CI", Section 5.1, Table 3, abstract.
Why it matters: The intervals in Table 5 and Section 5.1 are two one sided 95% bounds, which together form a 90% two sided interval. Table 3 uses two sided 95% intervals. With two sided 95% intervals, 10/12 [51.59%, 97.91%] and 7/20 [15.39%, 59.22%] overlap. The abstract's "non-overlapping intervals" for the +48.33 pp gap is true only for the 90% intervals. The Newcombe interval for the difference does exclude zero, so the conclusion survives, but the wording is wrong.
Decides recommendation: no.

**W6. Several counts in the text do not add up or are not explained.**
Where: Sections 4.1, 4.2, 4.3, Table 4.
Why it matters: "three ... diffs ... and two ... diffs" becomes "All 11 candidate diffs" (3 + 2 = 5). B28b cites "75 source images" for 44 source tasks plus one pilot. The blind rating sheet covers 42 source and 40 target tasks, but Table 2 implies 44 source and 42 target tasks had a Stage 1 candidate; the missing 2 + 2 are not explained. B05 excludes sympy__sympy-18199, but the paper does not say whether this task is in the 44 source tasks and how it changes n. "Seven source interpretation arms" lists six numbered items that cover eight named arms. These gaps make the audit hard to verify (details in Section 5).
Decides recommendation: no, but each must be fixed.

**W7. Citations do not always support the sentence they are attached to.**
Where: Sections 1 and 2.
Why it matters: "OpenAI's February 2026 audit [25]" points to a July 2026 entry; the February 2026 entry is [26]. "one frozen contract [37]" points to a METR note on merge quality. "Empirical audits of SWE-bench [14, 30, 1]" cites a general literature review [14] and a paper on the Chatbot Arena leaderboard [30]. ECBD [20] is cited as a dynamic benchmark that draws newer issues, but its title describes evidence centered benchmark design for NLP. The opening claim that "requirements engineers increasingly treat coding benchmark leaderboards as operational evidence" cites a requirements for AI essay [6], a mapping study [12] and a quality model [18], none of which seem to report this practice. I judged these from titles only and did not look the works up.
Decides recommendation: no. The call warns about hallucinated references, so the authors should check every entry.

**W8. Reporting of model use is thin for a study where models do most of the judging.**
Where: Sections 3, 4.1, 4.2; Data Availability.
Why it matters: Models write exploit patches, write the check scripts, rate scope, probe exposure, draft the audit forms and author runner diffs. The paper gives model names, one reasoning setting and one CLI version. It does not give prompts, sampling settings, dates of use, or how refusals were handled beyond one sentence. The call recommends the LLM Guidelines Initiative for such studies. The Zenodo link is a placeholder ("XXXXXXX"), so reviewers cannot inspect the package. The study is also a single run per task on one repository.
Decides recommendation: no, but it lowers reproducibility.

**W9. Tables and the figure do not each answer a question raised in the text.**
Where: Figure 1, Tables 1, 4, 6.
Why it matters: Figure 1 is a row of four boxes with codes ("89 Slots Max 99", "B28a (+ Control)") and answers no question the text asks. Table 1 repeats Section 3.1 almost word for word. Table 4 is dense with abbreviations ("Doc/np", "Ver/fail", "Undoc / not_perf") and mixes Sonnet draft disagreements with policy roles. Table 6 joins two unrelated analyses: the B07 sensitivity (which answers part of RQ2) and a replay test whose columns ("Integrity", "Evidence", "Score Dec.", "Targeted Change") are not explained and whose 100% result is expected by construction. Table 2 and Table 3 do answer clear questions, and Table 5 answers RQ1 and RQ2, but Table 5 would be clearer if it showed that all source arms end without a decision or Inconclusive.
Decides recommendation: no.

**W10. Double blind wording.**
Where: Section 1 ("In companion work [3, 2], we unified ..."), Sections 4.1 and 6 ("The author signed").
Why it matters: The call asks that own work is cited in the third person. "We unified" in first person tells reviewers that [2] and [3] are by the same authors. The singular "the author" also tells reviewers the team size. This is not grounds for desk rejection in my view, but should be fixed.
Decides recommendation: no.

## 4. Questions to the authors

1. Were M3_lenient and M3_controlled, and the list of runner files for no_scoring_file_changes, fixed before any session ran? Where is this recorded?
2. Did you run check.py on the agent's own patches for the 32 source and 24 target defect tasks? How many of the agent's "resolved" patches on those tasks fail check.py?
3. How do you rule out that the target tasks are simply harder or less clearly stated than SWE-bench Verified tasks, which were screened by humans? Did you compare issue length, files changed, lines changed, or test counts across splits?
4. How many target tasks have tests that reject a valid fix (the B05 type of defect)? Was B05 checked on the target at all?
5. Why do 42 source and 40 target tasks appear on the rating sheet when 44 and 42 tasks had a Stage 1 candidate?
6. Where does the number 11 come from in "All 11 candidate diffs"? Which diffs were run on which tasks?
7. What are the 75 images in B28b, given 44 source tasks and one pilot?
8. Is sympy__sympy-18199 one of the 44 source tasks? If so, is it among the 32 removed tasks or the 12 retained ones?
9. What do the statuses Verified, Documented and Undocumented mean, and what is a "Verified anchor"?
10. Why do M1 and M2 "coincide because all tasks originate from sympy/sympy"? What is M1?
11. What is the "strict comparative agreement rule", and what result would have counted as the audit predicting the target decision?
12. What is the "rehearsal" in Threat 3, and which records did it create before the agent was chosen?
13. Were slots 10, 61 and 80 among the retained tasks?
14. Can you report the share of source tasks where the model named the exact modified files, compared with a baseline such as file names that appear in the issue text?

## 5. Checks I made

All arithmetic was done in Python (scipy). "One sided 95% bounds" means the Clopper Pearson lower and upper bounds at 0.05 each, which together form a 90% two sided interval.

### Agree with the paper

| Item | Paper | Recomputed |
|---|---|---|
| nmin = 9 rule | 0.7^9 = 0.0404, 0.7^8 = 0.0576 | 0.0404, 0.0576 |
| Cut points n = 44 | Accept ≥ 37, Reject ≤ 25 | 37, 25 |
| Cut points n = 20 | Accept ≥ 18, Reject ≤ 10 | 18, 10 |
| Cut points n = 12 | Accept 12/12, Reject ≤ 5 | 12, 5 |
| Cut points n = 18 (not printed) | 5/18 gives Reject | Accept ≥ 17, Reject ≤ 8; 5/18 is Reject |
| Power n = 44, p = 0.85 | 66.3% | 66.34% |
| Power n = 12, p = 0.85 and 0.75 | 14.2%, 3.2% | 14.22%, 3.17% |
| 35/44 | 79.55%, [67.02, 88.89] | 79.55%, [67.02, 88.89] (one sided bounds) |
| 10/12 | 83.33%, [56.19, 96.95] | 83.33%, [56.19, 96.95] (one sided bounds) |
| 21/44 | 47.73%, [34.64, 61.06] | 47.73%, [34.64, 61.06] (one sided bounds) |
| 23/44 | 52.27%, [38.94, 65.36] | 52.27%, [38.94, 65.36] (one sided bounds) |
| 7/20 | 35.00%, [17.73, 55.80] | 35.00%, [17.73, 55.80] (one sided bounds) |
| 5/18 | 27.8% | 27.78% |
| 37/44, 40/44 exact CI (Table 3) | [69.9, 93.4], [78.3, 97.5] | [69.93, 93.36], [78.33, 97.47] (two sided 95%) |
| 30/44, 13/44 | 68.2%, 29.5% | 68.18%, 29.55%; ratio 2.31, so "more than twice" holds |
| Newcombe 35/44 vs 21/44 | +31.82 [+11.75, +48.60] | +31.82 [+11.75, +48.60] |
| Newcombe 10/12 vs 7/20 | +48.33 [+12.79, +69.03] | +48.33 [+12.79, +69.03] |
| Newcombe 37/44 vs 40/44 | −6.8 [−21.4, +7.7] | −6.82 [−21.36, +7.65] |
| Table 6 differences | +48.3, +55.6, +31.8 | +48.33, +55.56, +31.82 |
| 80/82, 77/82, 76/82 | 97.56%, 93.90%, 92.68% | 97.56%, 93.90%, 92.68% |
| Kappa 0.883 with 80/82 | — | implies chance agreement 0.79; plausible, cannot verify without marginals |
| Table 2 columns | 44, 44, 88 | 32+6+6+0 = 44; 26+6+10+2 = 44; 58+12+16+2 = 88 |
| Table 2 removed and retained | 32 / 24 / 56; 12 / 20 / 32 | 44−32 = 12; 44−24 = 20; 26−24 = 2 kept non defects |
| ABC items | 7 met, 6 not, 2 unknown, 18 N/A | 7+6+2+18 = 33; applicable 15 = 8+3+4; met 6+1+0 = 7 |
| ABC part scores | T = 0.75, O = 0.33, R = 0.00, 8 caveats | 6/8, 1/3, 0/4; 2+2+4 = 8 caveats listed |
| Slots | 99 max | 1+44+44+10 = 99 |
| Runtime exclusions | 23/44 → 21/44 after slots 61, 80 | 23 − 2 = 21 |
| "+31.82 to +48.33" in abstract | — | matches the two differences |

### Do not agree, or cannot be reconciled from the paper

| # | Where | Issue |
|---|---|---|
| D1 | Table 5 header, Section 5.1 | Intervals are labelled "95% Exact CI" and "one-sided 95% exact binomial CI", but both ends are shown. They are a 90% two sided interval. Two sided 95% intervals are 35/44 [64.70, 90.20], 10/12 [51.59, 97.91], 21/44 [32.46, 63.31], 23/44 [36.69, 67.54], 7/20 [15.39, 59.22]. Table 3 uses two sided 95%, so the tables use different conventions. |
| D2 | Abstract, Section 5.2 | "Non-overlapping intervals" for 10/12 vs 7/20 holds only for the 90% intervals (56.19 > 55.80). Two sided 95% intervals overlap (51.59 < 59.22). |
| D3 | Table 6, row "None removed" | 35/44 is shown as 79.6%. 35/44 = 79.545%, which rounds to 79.5% (Table 5 says 79.55%). |
| D4 | Table 3, last row | Column header promises a 95% CI for the difference, but "+38.6 pp" has none. My Newcombe 95% interval is [+17.8, +55.1]. |
| D5 | Section 4.2 | "three ... diffs ... and two ... diffs" then "All 11 candidate diffs": 3 + 2 = 5, not 11. |
| D6 | Section 4.1 vs Table 2 | 82 rated tasks (42 source, 40 target). Table 2 shows 0 source and 2 target tasks without a candidate, so 44 source and 42 target tasks had a candidate. 2 + 2 tasks are missing without explanation. |
| D7 | Table 4, Section 4.3 | B28b checks "75 source images", but the study has 44 source tasks plus 1 pilot. 75 equals all SymPy tasks in SWE-bench Verified, which is not the study set. |
| D8 | Section 3.2 | "seven source interpretation arms": six numbered items, eight named arms (M1, M2, audit only, ABC, ABC_with_gate, M3_strict, M3_lenient, M3_controlled), seven rows in Table 5 for source. |
| D9 | Section 2 | "OpenAI's February 2026 audit [25]": reference [25] is dated July 2026; [26] is February 2026. |
| D10 | Abstract vs Section 5.3 | Abstract counts "89 sessions"; Section 5.3 counts "4 of 88 study sessions". Both can be right (pilot excluded), but the switch is not stated. |
| D11 | Table 4 vs Section 3.2 | Table 4 says B14b is "omitted in Controlled". Section 3.2 says B14a and B14b are omitted in Lenient, and Controlled keeps Lenient's scope, so it should say "omitted in Lenient/Controlled" as for B12 and B14a. |

A derived figure the paper could report: on the target, the agent resolved 14 of the 24 removed defect tasks (58%) against 7 of the 20 retained (35%). On the source it resolved 25 of 32 removed (78%) against 10 of 12 retained (83%). This pattern supports weak tests inflating target scores, which is relevant to W2 and W3.

## 6. Terms, identifiers, dense sentences and claims

### Used before definition or never defined

| Term | First use | Status |
|---|---|---|
| MESA, "MESA rubric" | Title, abstract | Expanded in Section 1, never explained |
| M2, M3 | Abstract | Defined in Section 3.2, only by role |
| M1 | Section 3.2 | Never defined; "coincide because all tasks originate from sympy/sympy" is unexplained |
| ABC | Abstract | Expanded in Section 1; parts T, O, R explained only by name in Section 2 |
| B05, B07, B12, B14, B14a, B14b, B28a, B28b | Figure 1 (page 3) | Meaning only partly inferable in Section 3.2; never defined |
| C05, C07, C12, C14, C28 ("MESA concerns") | Section 3.2 | Never defined; relation to B codes unclear |
| Level 1, 2, 3 | Section 1 | Named only; contents of Level 1 ("Hashes, IDs, Policy") appear only in Figure 1 |
| Admissible, Inadmissible | Abstract | Never defined |
| Withheld | Figure 1 | Never used or defined in text |
| Inquiry Required | Section 5.2 | Never defined |
| Verified, Documented, Undocumented; passed, failed, not_performed | Section 3.2, 4.3 | Never defined |
| "Verified anchor", "passed check outcome" | Section 3.2 | Never defined |
| "release level" vs "case level" | Section 3.2, 4.2 | Never defined |
| SWE-bench Verified, hidden tests, harness | Abstract, Section 1 | Not explained for an RE reader |
| FAIL_TO_PASS, PASS_TO_PASS | Table 1 | Never defined |
| θ, nmin | Abstract | Defined in Section 3 |
| pp | Abstract | Never expanded |
| Newcombe CI | Section 4.2 | Method not named or cited |
| REQ-P6-SYMPY-BUGFIX, CONFIG_02_SOL_MED | Section 3 | Identifiers with no use for the reader |
| "frozen manifest", "frozen contract", "form signatures" | Sections 2, 4 | Never defined |
| "rehearsal" | Threat 3 | Never mentioned before |
| "excluded historical fixtures" | Section 3.1 | Never defined |
| "study-material marker", "network-command marker", ".codex", "rg", "uv" | Section 5.3 | Never explained |
| Stage 1, Stage 2 | Section 4.1 | Defined in place, fine |
| "Drafts A and B" vs "Sonnet A, B" | Section 4.3, Table 2 | Two names for the same runs, not linked |
| "not_comparable", "strict comparative agreement rule" | Section 5.2 | Never defined |
| "observation diffs" | Section 3.2 | Never defined |
| T.5, T.6, O.d.2, O.f.3, R.3, R.4, R.9, R.10 | Section 4.3 | Item codes with no content |
| "three-way agreement" | Abstract | Reads as three raters; means three categories |

### Sentences with too many abbreviations or codes

- Abstract: "Cross-family weak-test checks and two independent Claude Sonnet 5.5 scope ratings (80/82 exact three-way agreement; checked against GPT-6.1 Sol) remove 32 of 44 source tasks and 24 of 44 target tasks as accepting wrong patches."
- Abstract: "Runner-file edits alter grading on all four SymPy runner layouts, keeping strict and lenient MESA policies Inadmissible; confirming no scoring-file modifications per observation renders M3_controlled Admissible on the 12 retained source tasks (10/12 resolved, 83.33%, Inconclusive because n = 12 requires 12/12 to Accept)."
- Section 3.2, item 3: "Scores all 33 ABC items [40] mapped to the five selected MESA concerns (C05, C07, C12, C14, C28)."
- Section 3.2, items 4 and 5: "Enforces Verified anchor and passed check outcome on all seven criteria (B05, B07, B12, B14a, B14b, B28a, B28b)." and "Restricts gating to test validity and environments (B05, B07, B28a, B28b; permitting Documented on B07) while omitting uncertainty (B12) and contamination (B14a, B14b)."
- Section 4.3: "B05 was settled as Verified / passed after listing sympy__sympy-18199 as a task defect [25] (matching the GPT-6.1 Sol rating run; Drafts A and B conservatively marked Documented / not_performed)."
- Section 4.3: "ABC scored T = 0.75 (6/8 applicable), O = 0.33 (1/3), and R = 0.00 (0/4) with 8 caveats (T.5, T.6, O.d.2, O.f.3, R.3, R.4, R.9, R.10)."
- Section 5.1: "M3_controlled checks no_scoring_file_changes across all 12 retained source patches (100% clean) and advances to Admissible, returning Inconclusive on 10/12 resolved (83.33%, CI [56.19%, 96.95%]) because 12/12 was required at n = 12."
- Table 4, every row.

### Claims that go further than the evidence

| Claim | Where | Problem |
|---|---|---|
| "SWE-bench Verified SymPy resolve rates near 80% severely overstate capability on unseen post-cutoff issues" | Section 5.2, Conclusion | Confounded with task difficulty and human screening (W2); one model, one repository, one run |
| "pervasive weak-test defects (32 of 44 tasks)" | Conclusion | Model judgments only, no human check (W3) |
| "clean retained source tasks", "clean retained tasks" | Sections 5.2, 7 | Half of these tasks were never checked (W3) |
| "yield more cautious and defensible requirement decisions" (question) and "cleanly separates evidentiary admissibility from pass rates" | Abstract, Section 5.1 | All arms end Inconclusive or without decision (W1) |
| "M3_controlled resolves release-level runner mutability cleanly" | Conclusion | Checked on 12 patches; the same rule gives a false positive on slot 61 |
| "supporting Verified / passed for the held-out target set under B14b" | Section 4.2 | Based on a non significant difference; absence of a difference is not evidence of no exposure |
| "without single-family confirmation bias" | Section 4.1 | Stage 1 patches come from the agent's own model (Threat 2) |
| "Requirements engineers increasingly treat coding benchmark leaderboards as operational evidence" | Section 1 | Cited works do not seem to report this practice (W7) |
| "target collapse holds robustly" | Section 5.2 | Robust to the three filtering choices only, not to the confounds in W2 |
| "decisive Reject" | Abstract, Sections 5.2, 7 | Statistically correct for the target, but "decisive" invites reading it as a property of the agent in general |

## 7. Scores (1 = poor, 5 = excellent)

| Criterion | Score | Reason |
|---|---|---|
| Relevance to requirements engineering | 3 | Fits the "RE and AI velocity" theme, but the RE part is one threshold requirement and little discussion of stakeholders or how teams use the result. |
| Soundness | 2 | Decision rule and statistics are correct, but the main comparison is confounded and the defect labels rest only on model judgments. |
| Novelty | 3 | Combining audit gates with a held out target test is new; the single parts (weak tests, contamination, runner edits) are known. |
| Clarity | 2 | Dense with undefined codes from unseen companion papers; a requirements engineer cannot follow Sections 3.2 to 4.3. |
| Reproducibility | 2 | Seeds and hashes are mentioned, but prompts, settings and the package (placeholder link) are not available, and several counts do not reconcile. |

## 8. Recommendation

**Weak reject.**

What decides it: W1, W2 and W3 together. The study does not show that a MESA audit changes or predicts a decision, because every source arm already ends without an acceptance. The drop on new issues, the main empirical finding, has explanations other than overstated benchmark scores that the paper does not address. The weak test labels that drive the filtering rest on model judgments with no human check, and half of the "clean" tasks were never checked. W4 adds that the paper depends on two unseen companion papers for its core terms. The work is careful in its statistics and honest about its own control failures. A version that reframes the claims, explains its terms for RE readers and reports the agent patch checks could be a good fit for a later venue, or for this one as a shorter paper.

## 9. Improvements that need no new experiment or data

| # | Improvement | Priority |
|---|---|---|
| 1 | Reframe the title, abstract and RQ1 to match what the data show: all source arms end without an acceptance, so the study cannot show that MESA prevents a wrong Accept. | Must fix |
| 2 | Replace "overstate capability" with a statement that lists the alternative explanations (harder tasks, no human screening on target, tests that reject valid fixes) and add them to the threats. | Must fix |
| 3 | Stop calling the 12 and 20 retained tasks "clean"; report how many were checked and found sound against how many were not checked. | Must fix |
| 4 | Add a short self contained section that defines MESA, the three levels, each B code used, each status value, Admissible, Inquiry Required and Withheld, with one example. | Must fix |
| 5 | Explain SWE-bench, hidden tests, FAIL_TO_PASS and PASS_TO_PASS, and the ABC parts in two or three plain sentences each. | Must fix |
| 6 | Fix the interval labels: say "90% two sided interval (one sided 95% bounds)" in Table 5 and Section 5.1, or report two sided 95% throughout; correct "non-overlapping intervals" in the abstract. | Must fix |
| 7 | Reconcile the counts: 11 diffs, 75 images, 42 and 40 rated tasks, sympy__sympy-18199, "seven arms", 79.6% in Table 6, B14b row in Table 4. | Must fix |
| 8 | Check every reference against its source and fix citation targets ([25] vs [26], [37], [14], [30], [20], and the claim at the start of Section 1). | Must fix |
| 9 | State whether M3_lenient, M3_controlled and the runner file list were fixed before the runs, and point to the record. | Must fix |
| 10 | Rewrite in third person the sentences about the companion papers, and avoid "the author". | Must fix |
| 11 | State the paper category (scientific evaluation) and follow the matching empirical standard. | Should fix |
| 12 | Report from existing data the resolve rates on removed against retained tasks (14/24 against 7/20 on target; 25/32 against 10/12 on source). | Should fix |
| 13 | Report from existing logs whether the agent's patches pass check.py on tasks where check.py is valid. This uses existing artifacts and needs no new session. | Should fix |
| 14 | Add a 95% interval for the +38.6 pp exact match difference and interpret the exact match result for B14a and B14b. | Should fix |
| 15 | Replace Figure 1 with a figure that shows the flow of the 88 tasks through the checks to the retained sets (counts at each step), which answers a question the text raises. | Should fix |
| 16 | Remove Table 1 or reduce it to the cut points; it repeats Section 3.1. | Should fix |
| 17 | Split Table 6 into the sensitivity analysis and the replay test, define the replay columns, and say what the replay test was meant to show. | Should fix |
| 18 | Spell out Table 4 statuses in words and drop the Sonnet draft column or move it to the package. | Should fix |
| 19 | Add a short paragraph on what a requirements engineer should do with these results when choosing an agent. | Should fix |
| 20 | Report prompts, sampling settings and dates of model use in the package, following the LLM Guidelines Initiative, and give an anonymized link that works for review. | Should fix |
| 21 | Remove internal identifiers (REQ-P6-SYMPY-BUGFIX, CONFIG_02_SOL_MED, slot numbers where not needed) from the main text. | Should fix |
| 22 | Explain "three-way agreement" as agreement over three rating categories, and name the Newcombe method with a citation. | Should fix |
