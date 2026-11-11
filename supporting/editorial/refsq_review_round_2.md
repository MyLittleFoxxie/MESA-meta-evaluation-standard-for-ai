# REFSQ review, round 2 (11 November 2026)

Round 2 reviews the papers as changed in round 1 (commit `2f0dd22`). Six new subagents (Claude Sonnet 5.5) wrote the reviews. Each saw only the PDF of one paper, a text extraction, and the summary of the call for papers. None saw the round 1 reviews, answers or changes, or the other paper. In this round their web checks worked. The comparison with round 1 and the answers are by the session that made the changes (Claude Fable 5.2), written after the reviews.

## Scores

| Paper | Requirements engineering | Empirical methods | AI evaluation | Expected decision |
|---|---|---|---|---|
| MESA paper, round 1 | reject | weak reject | reject | Reject |
| MESA paper, round 2 | reject (medium confidence) | reject (medium to high) | weak reject (medium) | Reject |
| Paper 2, round 1 | reject | reject | reject | Reject |
| Paper 2, round 2 | reject (medium) | reject (high) | reject (medium) | Reject |

The round 1 changes did not move the expected decision of either paper.

## Comparison with round 1

### Resolved (raised in round 1, not raised again, or confirmed correct in round 2)

MESA paper:
- 26 logs against 28 sessions.
- "Maximum score" against a score of 10.
- The criteria set given as B01 to B04.
- Doubt about the HumanEval example: the round 2 AI evaluation reviewer checked the upstream repository and confirmed that the `exec()` call is active at about line 50.
- The companion paper is cited; limitations are in the abstract (both noted as present).
- Agreement on applicable pairs, the denominator of 559, and the order of the ordinal scale are now stated. Reviewers still criticise the statistics themselves (below).
- Counts: the round 2 reviewers recomputed Tables 1 and 3, 711, 559, 302, 143 and the Study 2 counts and found them consistent.

Paper 2:
- The power table: two round 2 reviewers recomputed every Wilson cut point and every cell and found them all correct.
- 6 removed tasks, not 7.
- "Pre-registered" is no longer claimed. One reviewer still notes that the freeze is pending.
- The companion paper and SWE-bench are cited.
- No hallucinated reference was found in either paper by the reviewers who checked.

### Not resolved (the items that decide the score)

MESA paper:
- No human rater and no reference standard; one model family reviews, codes and audits. All three.
- The traceability matrix is a contribution and is not evaluated. All three.
- Thin requirements engineering contribution; the title suggests AI for RE. RE reviewer.
- MESA is not compared with the frameworks on the same measure; its repeatability (80%, 67% with outcome) is below the 90% of the repeat runs of BetterBench and Scorecard. Empirical reviewer.
- "Zero unmapped items" holds by construction; the 210 against 13 contrast is not like for like. All three.
- Read only sessions cannot support levels such as Verified for checks that need execution. AI evaluation reviewer.
- Pooled nominal alpha across criteria with different categories; ordinal order without a basis; no intervals. Empirical and AI evaluation reviewers.
- One located defect makes a benchmark Inadmissible without asking whether it affects the score for the requirement. RE and AI evaluation reviewers.

Paper 2:
- No session has run; RQ2 is not answered. All three.
- The gate withholds by construction on this benchmark, and no case shows it can return Admissible. All three.
- No power at 14 to 20 tasks; only 20 of 75 source tasks used. All three.
- The requirement and its acceptance rule: no stakeholder, no reason for 70%, 95% and 15 minutes, population undefined. RE reviewer.
- B07 is "Verified, passed" on 14 tasks of which 11 have a passing incomplete patch; B05 was executed on one task. Empirical and AI evaluation reviewers.
- Target tasks are not checked for B05 and B07. All three.
- One model family and one signer; signed forms come from run A. Empirical and AI evaluation reviewers.

### Problems the round 1 changes caused or left

- MESA paper: the reworded sentence on the mapping still read as 180 + 56 = 236 against 234. All three reviewers flagged it again. The record explains it: two of the 180 items on which draft and author agreed gained a second concern in the final mapping. Fixed in this round.
- MESA paper: "confirmed" in the abstract overstates a model check. Fixed.
- MESA paper: 286 quotes against 312 judgments, and 28 absence ratings against 54 + 6 in the audit, read as conflicts. They count different things. Clarified.
- Paper 2: the new sentence on the policy that would credit the session validity rule drew the comment that such an amendment would be made after seeing the withheld result. The sentence now says so.
- Paper 2: two reviewers now say the paper fits a research preview better than a technical design paper. A research preview has a limit of 8 pages.

## Answers as the author, round 2

| # | Item | Decision | What was done or why |
|---|---|---|---|
| MESA: 234 against 236 | Accepted | The sentence now gives 178 + 56 = 234 and the reason. Checked against `v4/mapping/mapping.csv`. |
| MESA: "confirmed" in the abstract | Accepted | Now "found direct support for". |
| MESA: 286 quotes against 312 judgments | Accepted | The text now says 286 quotes were cited across the judgments. |
| MESA: 28 against 60 absences | Accepted | The 54 plausible absences are broken down by level (33 Not applicable, 18 Undocumented, 3 Claimed), from `v5/study/analysis/source-check-summary.json`. |
| MESA: the 62 pairs outside the reported groups agree on 25 (40%) | Accepted | Added. It follows from 302, 221, 19 and 159, 117, 17. |
| MESA: Table 5 pairs Documented with outcome failed | Accepted in part | The Limitations now name it as a combination the level definitions do not foresee. Changing the rubric is feedback item 16. |
| MESA: Alonso and Church could not be confirmed | Rejected | Checked in this round: the paper is in SIGIR Forum volume 58, number 2 (December 2024), by Omar Alonso and Kenneth Church. |
| MESA: ABC has 42 items in arXiv version 5 against "44 released" | Rejected | Table 1 gives both counts (42 in the paper, 44 in the released template); feedback item 17 records that this was checked. |
| MESA: pooled nominal alpha; no intervals; no chance correction for the 302 pairs | Left for you | Needs a new analysis of frozen records and a choice of statistic. |
| MESA: no severity or relevance rule in the gate | Left for you | A design decision about the rubric and the matrix. |
| MESA: human raters; evaluation of the matrix; comparison with the frameworks on one measure; title | Left for you | As in round 1. |
| Paper 2: "cheating patches" in the abstract | Accepted | Now "incomplete patches passing the hidden tests". The body already explains the rule. |
| Paper 2: SWE-bench Verified cited to the SWE-bench paper | Accepted | Also cites the OpenAI post that introduced SWE-bench Verified (already in `references.bib`). |
| Paper 2: the 59.4% rate is from tasks one model did not solve consistently | Accepted | Said so in Section 4.3. |
| Paper 2: a two sided 95% interval used for a one sided decision | Accepted | The text now states that each comparison has level 97.5%. |
| Paper 2: amendment after seeing results | Accepted | The Limitations sentence now says the policy was proposed after the forms were signed. |
| Paper 2: paper category (research preview) | Left for you | See the report: 8 pages would mean cutting half the paper. |
| Paper 2: sessions, power, gate constant, requirement record, B07 and B05 ratings, target task checks, single signer | Left for you | As in round 1; `paper2/preparation/protocol-6/proposal.md` covers the gate, the power and the target checks. |

## Why the loop stopped after round 2

The plan sets two stop rules: a round that finds no item that would change the decision, or four rounds. Round 2 still found such items, so the first rule is not met. The loop was stopped anyway, because every remaining item of that kind is one that only you can act on: it needs agent sessions, human raters, a design decision, a new analysis of frozen records, or a signature. Rounds 3 and 4 would review the same substance and return the same decision.

## Changes and files

| File | Change |
|---|---|
| `mesa_paper.tex` | The six accepted items above; four sentences shortened so that the page count does not depend on two lines |
| `paper2.tex` | The five accepted items above; two sentences shortened for the same reason |
| `paper2_runbook.md`, `README.md` | Round 2 recorded |

Not changed: research questions, code, tests, protocols, policies, signed forms, records, frozen files, `references.bib`.

## Checks and page counts after the changes

Run on 11 November 2026 after the round 2 changes.

| Check | Result |
|---|---|
| `python3 verify_manuscripts.py` | No missing citation or reference, no unclosed brace, in both papers |
| `python3 v4/mapping/check.py` | Passed; `git status` shows no changed file under `v4/` or `v5/` |
| `python3 v4/study/test_harness.py`, `python3 v5/study/test_harness.py` | Passed |
| `python3 -m unittest discover -s paper2/tests -p 'test_*.py'` | 181 tests, 1 failure, 1 skipped; the same path dependent test as before any change |
| `python3 surveys/colleague-review/verify.py` | Passed |
| Page count, MESA paper | 15; stays at 15 with up to 9 more lines of text |
| Page count, Paper 2 | 15; stays at 15 with up to 12 more lines of text |

Build: TeX Live 2023 with `latexmk -pdf`, as in round 1. `mesa_paper.pdf` and `paper2.pdf` in the repository root were replaced with this build. Compile once on Overleaf (TeX Live 2026) before submitting.

## Reviews as written

The six reviews follow unchanged.


---

### MESA paper: reviewer for requirements engineering

#### REFSQ 2027 research track: review of "Unifying Benchmark Evaluation Protocols: A Meta-Evaluation Standard for Artificial Intelligence in Requirements Engineering" (MESA)

Reviewer perspective: requirements engineering researcher. Special attention to the RE contribution, link to RE theory and prior RE work, usability by a requirements engineer, clarity for the REFSQ audience, and fit with the special theme.

##### 1. Summary of the paper

The paper argues that teams use public benchmark scores as acceptance evidence that a foundation model satisfies a capability requirement, and that seven published benchmark review frameworks (BetterBench, ECBD, Scorecard, How2Bench, ABC, Caliper, OECD facets) disagree with one another, partly because they treat missing documentation differently. The authors do four things.

1. They map the 280 items of the seven frameworks onto 30 "concerns" (386 links) and derive a 39 criterion rubric (8 descriptive criteria A01 to A08, 31 evaluative criteria B01 to B29 with splits). Each evaluative rating has an evidence level (Claimed, Documented, Verified, Contradicted, Undocumented, N/A) and a separate check outcome. The rubric is called MESA.
2. They run 18 review sessions (six frameworks, four benchmarks: HumanEval, TruthfulQA, HLE, tau-bench) and report 159 of 302 pairwise concern verdicts in agreement (53%). A model coder attributes 92 of the 143 disagreements to item granularity (50) and missing documentation rules (42). They report 210 of 711 answers carrying an "unreported" qualifier (-r) and 13 answers recording contradictions.
3. They run MESA twice per benchmark (8 sessions) and report 81% agreement on Part A (alpha 0.80), 80% on Part B levels (alpha 0.70) and 67% on level plus outcome. A second model audits the 312 judgments against the sources: 55 of 64 Part A and 159 of 248 Part B are "directly supported".
4. They propose a "Requirements Traceability Matrix" (RTM), a decision function (Eq. 2 to 4) that turns audited criteria into Inadmissible, Inquiry Required or Admissible before a score threshold is applied. They show one worked row (Table 5) for HumanEval and an "IDE Python synthesis, pass@1 >= 80%" requirement. The RTM is not evaluated and is said to be implemented in a companion paper under review.

All reviews, codings and audits were produced by models of one family, with no human raters (stated in the abstract and Section 7).

##### 2. Paper category under the call

The paper does not name its category. Two fit.

**Technical design paper (15 pages).** This is the closest fit. The artifacts are the MESA rubric and the RTM decision procedure. Criteria in the call's order:

- Novelty. A harmonized rubric across seven frameworks is a modest but real synthesis. The RTM decision rule is new as a formulation, but it is a gate function over rubric outputs, not a traceability construct (see W4). The executable method is split off into a companion submission (reference [5]), so the paper keeps the design and leaves the part a practitioner would run to another paper.
- Potential impact and relevance. Relevance to RE is asserted more than shown. No requirements engineer, no requirement elicitation or specification step, and no RE benchmark appears anywhere in the study (W1, W3).
- Soundness. Weak. The only evaluation is a model checking a model (W2).
- Verifiability. Promising on paper (replication package with logs and scripts), but no link or artifact can be inspected from the PDF, and model identifiers cannot be checked (W9).
- Presentation. Dense, heavily numeric, and hard to read for a REFSQ audience (W8).

The paper meets the category only in part. It has a design and an evaluation, but the evaluation is of the rubric's repeatability, not of the thing the paper claims to deliver (a better acceptance decision).

**Scientific evaluation paper (15 pages).** Soundness is the first criterion and the paper is weakest there. The SIGSOFT Empirical Standards (cited as [1]) ask for validity threats, human coding with agreement among independent coders, and a clear unit of analysis. Here there is one author mapping the items, one model doing the reviews, a second model coding disagreements and a third audit by the same family of models. The claims in RQ1 to RQ3 are mostly about model behavior, and Section 7 says so. It does not meet this category as submitted.

**Research preview or vision (8 pages).** The content would fit the early stage idea better than the other categories: a design, a pilot, and the human study as future work. At 15 pages the paper is over the 8 page limit for those categories, so it cannot move there without cutting.

**On the main study not having run.** The sessions the paper reports did run (28 sessions). What has not run is the study that matters to the stated contribution: no requirements engineer applied MESA or the RTM, and the RTM was not applied to any case beyond one row. For each category:

- As a technical design paper, "preliminary evaluation" can be satisfied by a pilot, so this is tolerable if the paper is honest that the evaluation is repeatability only. The abstract does state the limits.
- As a scientific evaluation paper, the missing human study is fatal to soundness.
- As an experience report, there is no practitioner experience at all, so it does not apply.

##### 3. Strengths

**S1.** The problem is real and well chosen for an RE audience. Benchmark scores used as acceptance evidence for a capability requirement is a concrete problem, and the separation of "not reported" from "located defect" is a useful distinction (Section 1, HumanEval example).

**S2.** The HumanEval example is concrete and checkable in principle: a commit hash, a file and a line number are given (Section 1, Table 5).

**S3.** Separating evidence level from check outcome (Section 3.3) is a sensible modeling decision that lets "Verified but failed" be recorded without calling the evidence missing.

**S4.** The paper is open about its main limits: model-only raters, one family of models, RTM not evaluated, -r pooling (Section 7, abstract).

**S5.** The arithmetic mostly holds up. I recomputed the main counts (see Section 6) and nearly all agree across abstract, text and tables. The item and link tables (Table 3) add up in rows and columns.

**S6.** The promise of a replication package with logs and deterministic scripts (Data Availability) is good practice, and the low cost (2.23 USD for eight sessions) shows the rubric can be run cheaply.

**S7.** The audit of cited quotes (Section 5.3) reports negative results too (6 contradicted absences, 29 weaker ratings, 11 of 46 Verified ratings with weak support) instead of only the headline.

##### 4. Weaknesses

**W1 (decision). The RE contribution is thin and the title overstates it.** Location: title, Sections 1, 2.1, 6.

- The title says "for Artificial Intelligence in Requirements Engineering", which a REFSQ reader will read as AI for RE tasks. The paper is about RE for AI components: choosing a model against a capability requirement. None of the four benchmarks studied is an RE benchmark and no RE task is evaluated.
- The work that is described is benchmark review methodology (an ML evaluation topic). The RE part is the last two pages (Sections 6.1, 6.2), and the RTM is not evaluated.
- None of the activities a requirements engineer does appear: eliciting the threshold theta, deciding which criteria apply to a requirement, negotiating with a maintainer, handling change when a benchmark is updated.
- Fix: retitle (for example around "acceptance evidence for model capability requirements"), state the RE problem and the intended user in Section 1, and either evaluate with RE practitioners or cut the RE claims to what the evidence supports.

**W2 (decision). The evaluation cannot support the claims, because every judgment is made by models of one family and nothing is checked against human judgment.** Location: Sections 4, 5, 7; abstract.

- Study 1 measures how a model applies frameworks, not how humans or frameworks differ. The paper concedes this (Section 7). Yet the abstract and Section 6.1 present "published review checklists disagree on 47% of shared comparisons" as a finding about the frameworks. About one verdict in ten changes between two runs of the same framework (Section 5.1: 19 of 21, 20 of 22), and that noise is not separated from the 143 disagreements.
- The 53% agreement figure also depends on the authors' own recoding rules: Satisfied (partial) is folded into Satisfied, and strict conjunction makes any unmet sub-item fail a concern. With majority rule the figure is 49% (148/302). The rules are decisions of the authors, so "50 disagreements due to granularity" is partly an effect of a rule the authors chose. No chance-corrected measure (for example kappa) is given for the 302 pairs, and pairs are not independent (same model, same benchmark, same concern across several pairs).
- Study 2 measures repeatability of one model, not correctness. The audit by a second model of the same family checks that a quote exists in the source; it does not establish that the rating is right. Only 159 of 248 Part B ratings (64%) were "directly supported" by the audit's own standard. The abstract says "confirmed", which reads better than 64% with 54 "plausible" absences that were not verified.
- Krippendorff alpha for two runs of one model with 106 non-independent pairs and no interval is not an inter-rater statistic. The ordinal ordering Contradicted < Undocumented < Claimed < Documented < Verified is not justified (is a contradicted claim worse than missing evidence?).
- Fix: add at least a small human validation (two RE or ML evaluation experts rating a subset, with agreement against the model and against each other), report confidence intervals, and move the "frameworks disagree" claim to a claim about model-applied frameworks unless humans confirm it.

**W3 (decision). The link to RE theory and prior RE work is shallow and in places wrong.** Location: Section 2.1, Eq. (1), references [16], [34], [7], [32], [15].

- Eq. (1) writes the benchmark argument as W, E, O_bench(M,B) |-ind G_AI and the paper never uses it again. The symbol |-ind is not defined beyond "inductive assurance argument". The Zave and Jackson formulation (W, S |- R) is about specifications written by requirements engineers. The paper does not discuss what the analogue of S is, how W is elicited for a model, or how verification differs from validation here. The sentence "[34,16]" attributes the reference model to both Zave and Jackson and a systematic mapping study on RE for AI.
- The first sentence of the paper says the bottleneck "shifts upstream to validating whether candidate models satisfy system requirements [16]". Reference [16] is a mapping study on RE for AI systems. I could not find that it supports a claim about AI assisted coding moving the bottleneck. The claim is a restatement of the conference theme with a citation attached.
- Wand and Weber [32] ("representation theory") is named as a ground for MESA in the introduction and is not used anywhere in the design or analysis. Berry [7] is used in one sentence.
- Prior RE work on requirements for ML components is not discussed. Examples I would expect: Vogelsang and Borg on requirements engineering for ML, Heyn et al. on RE challenges for AI intensive systems, work on non-functional requirements for ML systems, and work on performance and data requirements for ML components. Assurance case work (GSN style) is mentioned through AMLAS but not compared with the RTM.
- The paper calls its decision function a "Requirements Traceability Matrix" with a citation to Gotel and Finkelstein [15]. A traceability matrix records links between requirements and other artifacts so that their relations can be followed and kept up to date. The RTM here is a one shot gating function over evidence records. It has no notion of link maintenance, change impact or coverage over a requirements set. This is a naming problem that a REFSQ reader will notice.
- Fix: rewrite Section 2 around RE for ML components and satisfaction arguments, cite the RE for ML literature, define each symbol in Eq. (1), and rename or justify "RTM".

**W4 (decision). The RTM (Eq. 2 to 4, Table 5) is not shown to be usable by a requirements engineer, and its one worked example points to a flaw in the gate rule.** Location: Section 6.2, Table 5.

- The profile tau_C(r) is chosen by "the requirement engineer" but no guidance says which of the 39 criteria apply to which requirement type, so the central human step is left open.
- Def(c) is true whenever a check outcome is "failed" with a location. Table 5 then makes HumanEval "Inadmissible" for "IDE Python synthesis, pass@1 >= 80%" because `exec()` runs candidate code in the same namespace as the test assertions. That is a security and gaming exposure of the harness. Whether it changes the validity of the pass@1 score for this requirement is not argued. The rule treats every failed isolation check as blocking, with no weighting by how the defect could affect the score. If nearly any widely used benchmark is Inadmissible under such a rule, the gate has little discriminating power and a team in a fast release cycle (the special theme) will bypass it.
- Table 5 is internally awkward. In run 2 B28a is rated "Documented" with outcome "failed", but Section 3.3 says the outcome records what a verification check found, and Documented means an artifact is present without a check. B14b is listed in the profile and then marked "N/A in session ... applies to R1 without rating", while Eq. (2) says Active(c) = 0 when c is Not applicable. The table and the equation disagree on how an N/A rating from the session is treated.
- Only one benchmark and one requirement are shown, although Study 2 produced ratings for four benchmarks. A table of statuses for all four benchmarks under a few realistic requirements would show whether the gate is informative.
- Eq. (3) and (4) are standard confidence interval logic over scores. The paper does not say how Score(M, T') and its interval are computed for pass@k or for non-binary scores.
- The executable method sits in a companion paper under review, so the practical part is not in this submission.
- Fix: weight or condition Def(c) on relevance to the requirement, show statuses for all four benchmarks, resolve the Table 5 and Eq. (2) inconsistencies, and test the RTM with at least a small usability exercise with RE practitioners (even five participants).

**W5 (decision). The main empirical headline for RQ2 is partly circular and the comparison "210 versus 13" is not meaningful.** Location: Section 5.2, abstract.

- RQ2 asks how completely framework questions can be unified, and the answer is "zero unmapped items". The 30 concerns were built bottom-up from the same 280 items by one author with a draft from an assistant, so zero unmapped is true by construction.
- The 210 answers carrying -r are produced by the recoding rule (negative verdict that rests on absent documentation gets -r), so the count describes the rule, not the world. The 13 contradictions are a floor, because sessions could not run code and had read only access (the paper says so). The abstract sets 210/711 against 13 as if both measured the same kind of thing. The paper itself says -r pools unmet reporting requirements with unverified practices (Section 7).
- The claim that MESA "separates" the two categories is not tested: no comparison shows that MESA verdicts resolve the disagreements found with the other frameworks. Study 2 uses MESA only and never reports MESA verdicts against the legacy frameworks on the same benchmarks. The paper's central pitch ("unify") has no experiment that compares MESA with the seven frameworks on agreement.
- Fix: run MESA on the same sessions as Study 1 and report disagreement with and without MESA recoding, or reframe RQ2 as a descriptive coverage result.

**W6 (decision). Fit with the special theme "Aligning RE and AI Velocity" is weak.** Location: Section 1, Section 6.1.

- The theme concerns AI assisted coding changing RE cycles, human and AI collaboration in RE, and RE at high velocity. The paper borrows the theme sentence, then studies benchmark documentation quality.
- Nothing is measured about velocity (time, effort, delay in a release cycle) or about RE cycles. A 39 criterion rubric plus a maintainer inquiry step (Inquiry Required) adds process, and the paper does not discuss whether a team under release pressure would use it. The only speed related fact is the 2.23 USD cost of eight model sessions.
- The one theme topic that could fit ("benchmarks, evaluation frameworks and datasets for RE at AI speed") is not addressed, because no RE benchmark is examined.
- Fix: either tie the work to the theme with evidence (for example effort of applying MESA by a practitioner versus ad hoc leaderboard use, or apply MESA to benchmarks for RE tasks), or remove the framing.

**W7 (minor). Mapping construction rests on one author and the numbers do not reconcile.** Location: Section 3.2, Section 7.

- The text says the author's mapping matched the draft on 180 items and differed on 100; the draft was kept on 56, so the final mapping equals the draft on 180 + 56 = 236 items. The paper says 234 (twice, in Section 3.2 and in Section 7). This may be a rounding or counting slip, but the paper claims precision everywhere else.
- 106 extra links come from 76 compound items, which is plausible. For Caliper, 28 items give 45 links with "13 carrying secondary links"; that needs 17 extra links from 13 items, which is possible but not explained.
- No second human coder checked the mapping, and the mapping is the base of RQ1 and RQ2. Fix: have a second coder map a sample (for example 60 items) and report agreement, and correct 234 or 236.

**W8 (minor). Clarity for the REFSQ audience.** Location: Sections 3, 5; Tables 2 to 4.

- Many terms are close to one another: framework, item, concern, link, criterion, answer, classification, rating, verdict, decision, session. Section 3.1 says labels are "never reused", but "Decision" in Table 2 covers both the gate status and the score decision, and "Satisfied/Unsatisfied" overlaps with the RE use of requirement satisfaction.
- The paper is hard to read: the abstract carries 14 numbers; the same counts (159/302, 143, 210, 13) are repeated in the abstract, Section 1, Section 5, Section 6.1 and Section 8.
- The abstract lists three contributions while the introduction lists four (the introduction adds "three tiers of verdict"). Section 2.3 and 2.4 mostly list related work without comparing it to MESA.
- The word "standard" suggests a ratified document. The artifact is a rubric proposed by one group. Fix: shorten the numbers, reduce the term count, align the contribution lists, and use "rubric" or "protocol".

**W9 (minor). Reproducibility of the model based method is under-reported.** Location: Section 4, Data Availability, references.

- Models are named "Claude Sonnet 5.5" and "Claude Fable 5.1" without version identifiers, dates, sampling settings or prompts. The call recommends the LLM Guidelines Initiative (llm-guidelines.org), which asks for these, for non-determinism handling, and for human validation of LLM output. The paper does not follow it.
- The reviewer model has probably seen HumanEval, TruthfulQA and HLE documentation during training, so a "read-only" session may not isolate what the model reads from what it remembers. The paper does not discuss this threat.
- The Data Availability Statement says the package is "provided with this submission". There is no link in the PDF, so I could not check it.
- Fix: add a threats to validity section, model identifiers and dates, prompts in an appendix or the package, and a link.

**W10 (minor). Claim about the running example needs a statement of provenance.** Location: Section 1.

- The paper says the HumanEval README states the execution call is commented out, "yet" at the frozen commit line 50 runs `exec()`. My recollection of the upstream repository is that the `exec` call ships commented out by default and users must enable it. If the frozen commit is a modified copy or a fork, the paper should say so, because the headline example, Table 5 and the only Inadmissible result depend on it. Fix: state the repository, commit and whether the line is uncommented upstream.

**W11 (minor). Reference list.** Location: references [5], [8], [13], [20], [23], [27].

- Reference [5] is "Author(s), A.", while the call asks for a placeholder like "A. Anonymous". The companion paper under review also holds the executable method, so the overlap between the two submissions should be stated to the program committee (the call states no policy).
- Several 2026 and arXiv only sources are cited as the basis for benchmark frameworks ([13], [20], [23], [27]). I found each of these on the web (see Section 6), but [8] is cited under a title that differs from earlier versions on arXiv, and [27] is an initial public draft. The authors should say which version they used.

##### 5. Questions for the authors

**Q1.** What, concretely, would a requirements engineer do differently with MESA and the RTM than with a leaderboard lookup plus an informal check? Is there any evidence, even from a pilot with practitioners, that the 39 criteria can be applied in a time that fits a release cycle?

**Q2.** How is tau_C(r), the set of criteria for a requirement, chosen? Is there a default profile per requirement type?

**Q3.** Why is a failed isolation check (B28a) enough to make HumanEval Inadmissible for a pass@1 requirement? Which criteria would you expect to block other widely used benchmarks, and how many of the four benchmarks are Inadmissible for some realistic requirement under your gate?

**Q4.** Can you apply MESA's Tier 2 recoding to the Study 1 data and report disagreement with and without MESA? Without this, what shows that MESA reduces the disagreements rather than renaming them?

**Q5.** How much of the 47% disagreement remains after you account for run to run variation, as shown by the repeat sessions? Can you give a chance corrected agreement for the 302 pairs?

**Q6.** In the audit, what is the standard for "directly supported" versus "plausible absence"? Who decided, and was any sample checked by a human?

**Q7.** In Section 5.3, 286 quotes are accounted for (246 + 40) but 312 judgments were audited. What happened to the other 26? Also, 28 Part B ratings "rest on absent information" while the audit lists 54 plausible and 6 contradicted absences (60). What is the difference between the two groups?

**Q8.** Table 5 gives B28a as Documented with outcome failed in run 2. How does that fit your own definition of Documented (no verification check)?

**Q9.** Does the draft and final mapping match on 234 or 236 items?

**Q10.** What is the relation of this submission to the companion paper [5] under review? What would be lost if only one were accepted?

**Q11.** Is the `exec()` call at line 50 present and uncommented in the upstream commit b9453e8, or is it a local change?

##### 6. Checks I made

I recomputed the numbers with Python.

**Counts that add up**

- Items: 47 + 20 + 68 + 55 + 44 + 28 + 18 = 280 (matches Table 1 "Items"; the "Paper" column sums to 277, which the text explains for BB and ABC).
- Table 3: all row totals (10, 46, 58, 173, 99) and column totals (56, 29, 88, 69, 67, 45, 32) add to 386. Concern count 29 + 1 = 30. Criteria count 29 B criteria + 2 splits = 31 Part B, plus 8 Part A = 39.
- Study 1 answers: 4 x 47 + 4 x 20 + 4 x 68 + 4 x 18 + 55 + 44 = 711. The 559 answers for the four frameworks with -r rules: 188 + 272 + 55 + 44 = 559.
- 159 + 143 = 302; 159/302 = 52.6%; 143/302 = 47.4%; 148/302 = 49.0%.
- Disagreement coding: 50 + 42 + 42 + 8 + 1 = 143; 92/143 = 64.3%.
- 199 = 41 + 123 + 23 + 12; 210 = 199 + 11 BetterBench "5" answers (the 11 is implied, not stated); 210/711 = 29.5%; 210/559 = 37.6%; 13 = 9 + 2 + 2; 13/711 = 1.8%.
- B01 to B16: 117/221 = 52.9%; B18 and B19: 17/19 = 89.5%.
- Study 2: 8 sessions x 8 = 64 Part A; 8 x 31 = 248 Part B; pairs 32 and 124. 26/32 = 81.3%; 99/124 = 79.8%; 83/124 = 66.9%; 82/106 = 77.4%; 99 = 82 + 17; 106 + 18 = 124. The 35 N/A ratings fit 17 agreeing pairs (34) plus one half pair.
- Audit: 159 + 54 + 29 + 6 + 0 = 248; percentages 64.1, 21.8, 11.7, 2.4; 55 + 9 = 64; 55/64 = 85.9%; 64 + 248 = 312.
- Session total: 18 + 2 + 8 = 28.
- Repeat stability: 19/21 = 90.5%; 20/22 = 90.9%.
- Traced example C07: C(4,2) = 6 pairs, two agree, four disagree: consistent.

**Counts that do not add up or are unclear**

- Mapping: 180 + 56 = 236, not 234 (Sections 3.2 and 7).
- Audit quotes: 246 + 40 = 286 quotes, 312 judgments audited; 26 judgments are not accounted for.
- Section 5.3: 28 Part B ratings "resting on absent information" versus 54 + 6 = 60 absence ratings in the audit table.
- Sections 3.2 and 4.1: the "18 sessions" exclude the two repeat sessions, so Study 1 has 20 sessions; the abstract's "18 sessions" is correct only for the main comparison, and the number of sessions that Study 1 consumed is not stated in one place.
- The Caliper links (28 items, 45 links, 13 items with secondary links) need 17 extra links from 13 items; not explained.
- The abstract reports 80% for Part B levels, which includes 17 of 18 N/A pairs. On applicable pairs it is 77%.

**Terms used inconsistently**

- "Decision" is a Tier 3 gate status and a score decision (Table 2, Eq. 4).
- "Satisfied" is used for framework verdicts and, in RE, for requirement satisfaction.
- "Rating" (Tier 1), "answer", "classification" and "judgment" (Section 5.3) overlap.
- B28 in Table 3 versus B28a/b elsewhere.
- Abstract lists three contributions; the introduction lists four.
- Section 3.1 says Part A criteria map to C30 only; Table 3 gives C30 as "OECD Profile Facets" with 10 links, while there are 8 Part A criteria and 18 OECD items.

**Claims without support**

- "The engineering bottleneck shifts upstream to validating whether candidate models satisfy system requirements [16]": the cited mapping study is about RE for AI and I found no support for the shift claim.
- "Grounded in ... representation theory [32]": not used.
- The title and Section 6.1 claim MESA addresses AI velocity: nothing is measured about velocity.
- "Confirmed" in the abstract for audit results of 64%.
- "Teams rely on public benchmark scores as acceptance evidence": no survey, interview or source is given for current practice (the citations [31, 3] argue that leaderboards are weak evidence, not that teams use them as acceptance evidence).

**References**

I checked by web search that the following exist and match authors, venue and year: Scorecard of AI Benchmark Quality (ACL Anthology 2026.evaleval-1.25), Evaluation Cards (arXiv 2606.09809), Quality Model for ML Components (arXiv 2602.05043), the code benchmark paper behind How2Bench (arXiv 2501.10711, title changed across versions), the ABC paper (NeurIPS 2025 D&B, arXiv 2507.02825), Berry at REFSQ 2022 (Springer, doi 10.1007/978-3-030-98464-9_2), the Gomez et al. paper in MAKE 8(6), 141, NIST AI 800-2 initial public draft, and BetterBench and the construct validity paper (found through search results). I did not verify the remaining references one by one (Kane, Zave and Jackson, Gotel and Finkelstein, Wand and Weber, Hayes and Krippendorff, TruthfulQA, HLE, tau-bench look standard and have plausible volumes and pages). I found no hallucinated reference. The pages of Berry's paper and the exact claim attributed to it ("the evaluation measures, their thresholds, and the context are the requirements specification") I did not verify against the text.

**Rule checks**

- Page limit: 15 pages including references; fits the 15 page categories. It would exceed 8 pages for Vision or Research preview.
- Abstract: four labeled paragraphs (Context and motivation; Question/problem; Principal ideas/results; Contribution). Keywords present. The abstract is very number heavy.
- Anonymity: authors withheld. The paper says "the author" (singular) in Section 3.2, which is not an identity leak. Reference [5] is written "Author(s), A." rather than the placeholder form the call asks for. No acknowledgments. No identifying links.
- Data Availability Statement: present at the end, but it says the package is "provided with this submission" and gives no link; I could not inspect it.
- Generative AI: LLM use is reported, but the model identifiers, prompts, settings and dates that llm-guidelines.org asks for are not.
- Layout: looks like LNCS.

##### 7. Score

**Reject.** W1 to W6 are all decision level, and several can be fixed only by new studies, not by small edits.

##### 8. Reviewer confidence

**Medium.** I am confident about the RE related points and the arithmetic, and less certain about benchmark review methodology and about the details of the upstream HumanEval repository and the model names, which I could not verify.

##### 9. Recommendation

I would not accept the paper as submitted. It addresses a useful problem and the rubric may be useful to benchmark reviewers, but as an RE paper it offers a thin RE contribution: the RTM is neither a traceability construct nor evaluated, no requirements engineer takes part, the theory link is weak, and the fit with the "AI velocity" theme is thin. The empirical part measures repeatability and agreement of models with each other, so the claims in RQ1 to RQ3 are claims about model behavior. The smallest set of changes that would raise my score by one step, to weak reject: (1) add a human validation on a subset (at least two human raters on a sample of Study 2 ratings and the mapping, with agreement and intervals); (2) run MESA's recoding against the Study 1 data so that "MESA reduces conflicts" is tested, or drop that claim; (3) report RTM statuses for all four benchmarks and fix the Def(c) rule and the Table 5 and Eq. (2) inconsistencies; (4) retitle and rewrite Sections 1, 2.1 and 6 around RE for ML components, with the RE for ML literature, and remove or evidence the AI velocity framing; and (5) fix the counting slips (234 versus 236, 286 versus 312, 28 versus 60) and add model identifiers, prompts and the repository link. To reach weak accept, a pilot with RE practitioners on the RTM would also be needed.

---

### MESA paper: reviewer for empirical methods

#### REFSQ 2027 research track: review of "Unifying Benchmark Evaluation Protocols: A Meta-Evaluation Standard for Artificial Intelligence in Requirements Engineering"

Reviewer perspective: empirical methods in software engineering (design, sampling, unit of analysis, reliability statistics, language models as raters, validity threats, repeatability).

##### 1. Summary of the paper

The paper proposes MESA, a standard for reviewing AI benchmarks as evidence that a model meets a requirement. It makes four claims.

1. Seven published review frameworks (BetterBench, ECBD, Scorecard, How2Bench, ABC, Caliper, OECD facets) contain 280 items. These are mapped through 386 links onto 30 "concerns" and turned into a 39 criterion rubric (8 descriptive criteria, Part A; 31 evaluative criteria, Part B). The rubric records an evidence level (Claimed, Documented, Verified, Contradicted, Undocumented, N/A), a check outcome, and other fields. A qualifier "unreported" (-r) is meant to separate missing documentation from located defects.
2. Study 1: Claude Sonnet 5.5, run through Claude Code with read-only file tools, applied six frameworks to four benchmarks (HumanEval, TruthfulQA, HLE, tau-bench). The frameworks agreed on 159 of 302 pairwise concern comparisons (52.6%). A second model ("Claude Fable 5.1") coded the primary cause of the 143 disagreements: 50 item granularity, 42 missing documentation rules, 42 ambiguous text, 8 thresholds, 1 source scope. Of 711 item answers, 210 carry -r and 13 record "contradicted" evidence.
3. Study 2: the same reviewer model applied the MESA rubric twice to each benchmark (8 sessions). Run to run agreement was 26/32 on Part A (nominal alpha 0.80), 99/124 on Part B levels (ordinal alpha 0.70), and 83/124 on level plus outcome. A Fable 5.1 "source checker" audited all 312 judgments: 55/64 Part A and 159/248 Part B were "directly supported", and no quote was fabricated.
4. A Requirements Traceability Matrix (RTM) with three gating steps (Equations 2 to 4) turns audited evidence into Inadmissible, Inquiry Required or Admissible before a score is compared with a threshold. It is illustrated on one HumanEval entry (Table 5) and is not evaluated.

What the paper shows: a taxonomy built by one author with an LLM draft, and a set of repeatability and citation checks on one LLM in one configuration. It does not show that MESA is valid, that it reduces framework disagreement, that humans would use or rate it the same way, or that the RTM helps any decision.

##### 2. Paper category under the call

The best fit is **Technical design paper** (15 pages), because the main artifact is MESA with an RTM design and a "preliminary evaluation". The paper also presents itself under the **Scientific evaluation** heading ("Following the ACM SIGSOFT Empirical Standards [1]"), but it never says which standard applies.

All 28 sessions of Study 1 and Study 2 have run. What has not run is anything with humans (human raters, practitioners using the standard) and any evaluation of the RTM (Section 6.2 says "it is not evaluated in this paper"). That matters for each category.

- **Technical design, criteria in call order.**
  - Novelty: moderate. The separation of "absent" from "located defect" and of level from outcome is a useful idea, but it is an incremental merge of known checklists.
  - Potential impact and relevance: the RE link is thin. The RE content is Equation 1, the Jackson-Zave framing, and a conceptual RTM. No requirements engineering benchmark, no requirements practitioner and no RE task appears in the evaluation.
  - Soundness: weak (see W1 to W8).
  - Verifiability: unproven. The Data Availability Statement promises a package but gives no link.
  - Presentation: dense and mostly clear, with inconsistencies (see section 6).
  - Verdict on this category: partially met. The preliminary evaluation covers the rubric only, not the RTM, which is one of the three listed contributions.
- **Scientific evaluation.** Soundness comes first and is not met. The unit of evidence is one language model's repeatability. There is no human ground truth, no stated threats to validity section, and no sampling logic for frameworks or benchmarks. The paper would be rejected under this category.
- **Research preview.** The RTM and the human validation would fit here. The "soundness of the research plan including limitations and risks" criterion would be easier to meet, but the paper is written as a completed evaluation with a 15 page body.
- **Vision and experience report.** Neither applies.

##### 3. Strengths

- **S1.** The central distinction is worth having. Separating "the paper does not say" from "the artifact contradicts the claim" (level versus outcome, -r qualifier) addresses a real flaw in score based checklists. The HumanEval example in the introduction makes the point concrete.
- **S2.** Most reported counts are internally consistent. I recomputed the item totals (47+20+68+55+44+28+18 = 280), all row and column sums of Table 3 (386), the 711 and 559 answer counts, the 199+11 = 210 decomposition, 50+42+42+8+1 = 143, and the Study 2 pair counts. The details are in section 6.
- **S3.** Limitations are stated candidly in the abstract and Section 7. The paper says that the agreement figures measure repeatability of one model, not human reliability or correctness, and that the RTM is not evaluated.
- **S4.** Reporting is open about the design in several useful ways. Sessions were run once with no discarded attempts, the mapping reconciliation counts are given, the sensitivity analysis (majority rule, 49.0%) goes against the headline, and the rubric was reportedly frozen before Study 2.
- **S5.** Applying frameworks "without altering native prompts" and recoding by deterministic rules is a sound idea in principle, because it keeps the comparison from being tuned to MESA.
- **S6.** The traced example in Section 3.2 and Table 5 lets a reader follow the pipeline end to end.

##### 4. Weaknesses

###### Decision

**W1 (decision). Language models are the only raters, coders and auditors, and there is no human anchor anywhere (Sections 4.1, 4.2, 5, 7).**
- What is wrong: the reviewer is Sonnet 5.5, the disagreement coder and source checker are Fable 5.1, and the initial mapping draft came from an unnamed "assistant". Both model roles are the same vendor family, as Section 7 admits. Study 1 therefore measures how one model applies frameworks, not how frameworks differ for reviewers. The paper's headline "frameworks reach contradictory verdicts" (Abstract, Introduction, Section 6.1) is stated as a fact about the frameworks, but it can also be a property of this model, in this prompt, with static reading and no execution. Some frameworks require running code or contacting authors, so a read-only model is a different instrument from the one the framework designers intended.
- Why it matters: every quantitative claim in the paper (53%, 64%, 210 versus 13, alpha 0.80 and 0.70, 86% and 64% support) is conditional on this one model. The title and the conclusion are written more broadly.
- Fix: at minimum, have two or more human reviewers apply a sample (for example two benchmarks, three frameworks plus MESA) and report human to model and human to human agreement. Alternatively, retitle and reframe the contribution as "LLM applied frameworks", drop the claims about frameworks in general, and move the RE conclusions to a hypothesis.

**W2 (decision). The reliability statistics are not computed or interpreted in a way that supports "repeatable" (Section 5.3, Abstract).**
- Test-retest of one model is called "agreement". It is intra-rater consistency under the same prompt, not inter-rater reliability, and it cannot detect shared systematic bias. The paper says this in Section 7 but still reports alpha as the answer to RQ3.
- Part A alpha of 0.80 is a pooled nominal alpha over 32 pairs across eight different criteria (purpose, scoring method, reference, containedness and so on), each with its own category set. Observed disagreement is 6/32 = 0.19. For alpha to reach 0.80 the expected disagreement must be about 0.94, which means almost no chance agreement. That is only possible if the pooled values are nearly all distinct, which fits the text "23 exact text matches" (free text). A pooled alpha over heterogeneous variables with free text values is not interpretable. Per criterion alpha is not possible with 4 pairs each, so the honest statistic is raw agreement per criterion with counts.
- Part B ordinal alpha of 0.70 is below the 0.80 level conventionally required, and Krippendorff's own guidance allows only tentative conclusions between 0.667 and 0.8. The paper does not discuss this, gives no confidence interval ("no intervals computed"), and treats the 106 pairs as independent although they are nested in four benchmarks and 31 criteria.
- The ordinal ordering "Contradicted, Undocumented, Claimed, Documented, Verified" is asserted without justification. "Contradicted" is a located defect, not "lowest evidence", and only 2 of 248 ratings are Contradicted. The ordering therefore barely matters for alpha but matters for the interpretation.
- The denominators are mixed. The abstract's "99/124 Part B levels" and the body's "levels and fields matched on 99 of 124" are the same number under two descriptions. alpha is computed on 106 pairs, not 124.
- Scope matches on 124/124 (100%), which suggests the field is constant or copied from the template and carries no information.
- Four of the 124 pairs are N/A by construction, because B14b was N/A in all eight sessions (Section 4.2). The 17 of 18 N/A agreement is partly structural. Without the four structural pairs, 95/120 = 79%. This is minor numerically but shows that agreement counts include non-judgments.
- Fix: report raw agreement per criterion and per benchmark, per criterion kappa or alpha only where the category set is shared, bootstrap intervals, and the distribution of levels. Say plainly that 67% level plus outcome agreement and alpha 0.70 are modest for a gate that makes a binary Inadmissible call.

**W3 (decision). By the paper's own numbers MESA is not more repeatable than the frameworks it replaces, and no comparison is made (Sections 5.1, 5.3).**
- The same-framework repeats on HumanEval give 19/21 (90%) for BetterBench and 20/22 (91%) for Scorecard at concern level. MESA's repeatability is 80% on levels and 67% on level plus outcome. The units differ (concern verdict versus rating), so a direct comparison is not possible, but the paper's claim of a "unified standard" that is better at separating absence from defects is never tested against the frameworks on any measure.
- There is no measure that MESA reduces disagreement. MESA was applied only in Study 2 and its output is not compared with the Study 1 framework verdicts. The mapping to MESA (Table 3) is itself the thing being evaluated, and no outcome shows that MESA captures what the frameworks capture or that its ratings are right.
- Fix: apply MESA and the frameworks to the same benchmark snapshots with the same raters, compute within and between agreement on a shared unit (for example the 29 concerns), and state a baseline, including a chance corrected one. Without that, RQ2 and RQ3 do not support the contribution "separating absent reporting from located defects".

**W4 (decision). The key construct, -r versus Contradicted, is not validated, and the 210 versus 13 comparison is not a like for like count (Sections 3.2, 5.2, 6.1, Abstract).**
- The counts come from different instruments. The 210 answers are recoded from native framework answers in Study 1. The 13 are "contradicted" answers, but most frameworks (BetterBench scores, ECBD worksheets, OECD facets) have no contradicted answer type, and the paper does not give the recoding rule that produces one. Nine of the 13 come from Scorecard, two from BetterBench, two from ABC, and "six benchmark-concern cells" are involved, which says the 13 are repeated logs of at most six defects (Section 7 concedes "log instances rather than unique bugs").
- The sessions could not run code. So "13" is a floor set by tool limits, and the ratio 210:13 mainly reflects what a read-only reader can see.
- The -r qualifier itself "pools unmet reporting requirements with unverified practices" (Section 7). It therefore does not isolate what the paper says it does.
- Absence may be a reviewer failure. The source audit found 6 absences that the sources contradict (for example sampling parameters that the HumanEval paper does contain). So some -r are the model's search failures, not benchmark reporting gaps. The audit covers Study 2 only, so the share of false absences in the 210 Study 1 answers is unknown.
- RQ2 is answered by construction. "All 280 items map onto the 30 concerns with zero unmapped items" is guaranteed because the concerns were built bottom-up from those 280 items (Section 3.2). It says nothing about completeness or validity of the taxonomy.
- Fix: report a human audit of a random sample of -r answers and of Contradicted answers (precision of each), give the recoding rule that yields Contradicted from each framework, and replace the RQ2 answer with a validity check of the mapping (see W5).

**W5 (decision). The mapping, the basis of the whole standard, is a single author plus an LLM draft with no reliability measure and an arithmetic slip (Section 3.2, Table 3, Section 7).**
- The mapping onto 30 concerns is by one author with an unnamed assistant draft. Raw agreement is 180/280 (64%) with no chance corrected statistic. The paper says the final mapping "equals the draft on 234 of 280 items" and also that reconciliation "kept the draft on 56". But 180 + 56 = 236, not 234. The two numbers cannot both be right. The Limitations repeat 234.
- 76 compound items produce 106 extra links, and the strict conjunction rule then makes the number of links per framework drive its verdicts (see W6). The links for Caliper are described as "All 28 map to C23/B23, with 13 carrying secondary links", but Table 3 shows 45 Caliper links (40+1+4). So the 13 items carry 17 secondary links, which the text does not say.
- The concerns themselves are not listed in the paper. Only 9 of 31 Part B criteria appear (Table 4), the C01 to C30 names are not given, and Table 3 groups them by stage, so a reader cannot check or reuse the mapping from the paper.
- Fix: have a second human map at least a random 25% of items independently, report kappa, and publish the full mapping table (concern, criterion, linked items) as an appendix or in the artifact with a stable link.

**W6 (decision). The headline agreement rate (53%) and the "item granularity" cause are partly produced by the authors' own aggregation rule and by dependent comparisons (Sections 3.2, 5.1).**
- Under "strict conjunction", a framework with more items on a concern is more likely to be Unsatisfied. The coder then finds that 50 of 143 disagreements arise from granularity. This is an effect of the aggregation rule chosen by the authors, not a property of the frameworks. The majority rule check lowers agreement (49.0%), so the choice of rule moves the result by several points, and the paper does not report other rules (any, all, weighted).
- No chance corrected agreement is given for the three category (Satisfied, Unsatisfied, Open) verdicts, so 53% cannot be read without base rates.
- The 302 pairs are not independent. They share benchmarks, concerns and frameworks, and Scorecard (68 items) is in more pairs than the others. No confidence interval is given. Only four frameworks run on all four benchmarks, How2Bench runs only on HumanEval, ABC only on tau-bench, Caliper not at all. So "seven frameworks" is really four frameworks on four benchmarks plus two single benchmark runs.
- Reported subsets leave out part of the data: B01 to B16 give 117/221 and B18 to B19 give 17/19. That is 240 pairs, and the other 62 pairs (concerns beyond those, for example B17 and B20 to B29) have 159 − 134 = 25 agreements, i.e. 40%. This lowest agreement group is not mentioned.
- Run to run noise is not removed. With 10% verdict flips within a framework, part of the 143 disagreements is noise. The paper acknowledges this in one sentence but does not estimate how much (the repeat covers one benchmark and two frameworks, 21 and 22 concerns).
- Disagreement coding is single label ("primary cause") by one LLM, with no codebook, no second coder and no validation. "Item granularity" and "missing documentation rules" overlap with the strict conjunction rule and with each other.
- Fix: report agreement under several aggregation rules, chance corrected agreement, bootstrap intervals clustered by benchmark and concern, agreement for all concern groups, and a human coded sample of disagreement causes with kappa.

**W7 (decision). The sample of frameworks and benchmarks, and reuse of the same benchmarks for design and evaluation, limit what any result supports (Sections 3.2, 4.1, 7).**
- Framework selection has no search strategy or inclusion criteria. Section 2.3 names NIST AI 800-2, Evaluation Cards, BenchFrame and BQAI, but they are not selected and the paper does not say why.
- Four benchmarks (HumanEval, TruthfulQA, HLE, tau-bench) are a convenience sample of well known text benchmarks. None is a requirements engineering benchmark, although the paper is framed for RE acceptance decisions. HumanEval is old, widely discussed and probably in the training data of the reviewer model, and so are the review papers. Contamination of the reviewer by both benchmarks and frameworks is not discussed.
- The same four snapshots were used to build and tune the rubric and to evaluate it. HumanEval is the running example in the Introduction, in Section 3.2 (C07), and in Table 5. Several rubric features look shaped by it: the B28a/B28b split, the "check kind" and "detection limits" fields, the B05/B07 task defect rule, and the "runs candidate code" applicability. The paper says the rubric was frozen "before the eight sessions" but not whether it was changed after Study 1 on the same benchmarks. There is no held out benchmark.
- Only HumanEval snapshot has a commit hash (b9453e8). The other three snapshots are not identified in the paper.
- Fix: state selection rules for frameworks, add at least one benchmark that was not used in design (and one RE related benchmark if the RE claim is kept), state when the rubric was frozen relative to Study 1, and identify all snapshots.

**W8 (decision). The source audit does not measure correctness, and its headline "0 fabricated quotes" is weak (Section 5.3, Abstract).**
- The checker (Fable 5.1, same family as the reviewer, with no human check) is given the reviewer's own cited quotes and asked whether they support the rating. This tests quote existence and local support. It does not test recall (what the reviewer failed to cite) or whether the rating is right.
- Quote existence is mechanical. The paper states that "deterministic verification scripts" exist, and 246 of 286 match verbatim after normalization. So the zero fabrication result needs no language model. The language model part is the semantic judgment, and that is where the results are weaker: only 159 of 248 (64%) Part B ratings are directly supported, 29 (12%) are weaker support, 6 (2%) are absences contradicted by the sources, and 11 of 46 Verified ratings (24%) overstate verification. Verified is the level that gates acceptance.
- 54 "plausible absences" (22%) are unverifiable by definition.
- Audit categories (directly supported, plausible absence, weaker support, absence contradicted, unsupported) have no stated decision rules. "Unsupported" is defined as fabricated, which makes 0 close to trivial. A rating whose absence claim is false is classed as "contradicted absence", not "unsupported", although it is an error.
- Counts do not reconcile (see section 6): 312 judgments but 286 quotes, and 28 ratings "resting on absent information" versus 54 + 6 = 60 absences in the audit.
- The abstract leads with "0 fabricated quotes", which a reader will take as a sign of correctness.
- Fix: audit with at least one human on a random sample, state decision rules for each category, report error rates (6 false absences, 29 weak, 11 overstated Verified) as the headline in the abstract, and measure recall by a human reading a sample of sources independently.

###### Minor

**W9 (minor). The motivating HumanEval claim is a categorization choice and may be stated too strongly (Introduction, Section 3.3, Table 5).**
- The paper says the HumanEval paper describes a gVisor sandbox, the README says the call is commented out, and line 50 of execution.py runs exec(). This is a mismatch between the README and the code, and the repo itself warns users to sandbox. The paper rates it "Contradicted" against the paper's description of OpenAI's internal sandbox, not against a claim that the released harness is sandboxed. A reviewer could rate the same facts as Documented with a failed outcome, and the paper's own runs did exactly that (run 1: Contradicted, run 2: Documented, Table 5).
- Because of that, the key example in the paper is itself unstable across the two repetitions. The RTM only gives a stable Inadmissible because Equation 2 uses a disjunction (level Contradicted or outcome failed). It also means every benchmark that executes candidate code in process would be Inadmissible, and no threshold on how common this is was checked.
- "Check kind: run by reviewer" for what is a static inspection conflicts with Section 4.2 ("static repository inspections rather than executed ... runs") and with Table 4, where Verified on B07 requires that "exploits [were] tested".

**W10 (minor). Reproducibility from the description is not possible without the artifact (Sections 3.3, 4, Data Availability).**
- Missing: the reviewer prompts and tool definitions, exact model identifiers and dates, temperature and sampling settings, how "medium effort" is defined, how much of each snapshot the model read (HLE is 2,500 questions; tau-bench is a large repository), the native prompts per framework, the recoding rules for each framework in full, the disagreement coder codebook, and the audit protocol.
- The cost of 2.23 USD for eight sessions (about 0.28 USD each, including HLE and tau-bench) is surprising and suggests shallow reading. The number of files read per session should be reported, because "Undocumented" depends on what was opened.
- "Claude Fable 5.1" and Sonnet 5.5 may not be available later, and model behavior drifts, so a rerun of the 28 sessions may not be possible. State what in the package supports repeating the analysis from the logs only.
- The Data Availability Statement says the repository is "provided with this submission" but gives no link or identifier, so I cannot verify the claimed contents (mapping, recoding rules, rubric, snapshots, logs, scripts).

**W11 (minor). No threats to validity section, and "Empirical Standards" are named but not applied (Sections 4, 7).**
- Section 4 names the ACM SIGSOFT Empirical Standards but does not name the applicable standard or check against it. A Threats to validity section that separates construct (is "agreement of one model" reliability?), internal (prompt and order effects, same model coding its own output), external (four benchmarks, one model), and conclusion validity (no intervals, dependent pairs) would fit a few lines each.
- The LLM Guidelines Initiative recommended by the call is not cited or followed (model version, prompts, temperature, human validation, data release).

**W12 (minor). Terminology and notation conflicts make the framework hard to follow (see section 6).**
- "Open" is used for "not applicable" (Section 3.2), for "absent evidence" (ECBD) and for the MESA row in Table 1 ("Recorded as Undocumented (open question)"). These are three different states.
- "Satisfied (partial)" is a fourth verdict not defined in Table 2.
- Concern C07 is "scoring validation" in the Introduction and Section 3.2, "edge cases" in the same section (SC-65), and "Harness Gaming" in Table 3.
- Equation 3 uses tau_active(r) where Equation 2 uses Active(c).
- "The author" (singular, Sections 3.2 and 7) versus "The authors" (Disclosure).

**W13 (minor). The RTM (Section 6.2, Equations 2 to 4, Table 5) is a design with no evidence and one instance, and the RE contribution rests on it.**
- The thresholds in Suff(c, r), the choice of which criteria enter tau_C(r), n_min and the confidence interval method are left to the user without guidance. The companion paper [5] is under review and is cited as a source of the executable implementation, which makes the RTM harder to evaluate in isolation and raises the overlap question (the call states no policy on this).
- Fix: either remove the RTM from the list of contributions in the abstract, or add a small evaluation (for example practitioners or a retrospective on known benchmark defects), or present the paper as a research preview.

##### 5. Questions for the authors

- **Q1.** Which model produced the "assistant" mapping draft (Section 3.2)? Was the draft visible to the author before the author mapped the items? How was "independently" enforced?
- **Q2.** Section 3.2 says the draft was kept on 56 items and matched on 180, and that the final mapping equals the draft on 234. Which number is right?
- **Q3.** What temperature, seed and model snapshot were used? Were the two Study 2 runs fully independent (fresh context, no shared files)? Was the rubric changed in any way after Study 1 was seen?
- **Q4.** What does the pooled alpha of 0.80 on Part A treat as one variable? How many distinct values are there, and what is the per criterion raw agreement?
- **Q5.** What are the counts of each level (Claimed, Documented, Verified, Contradicted, Undocumented) in each run? With 2 Contradicted ratings of 248, what does the ordinal alpha say about that level?
- **Q6.** How does Study 1 produce a "contradicted" answer for frameworks with no such answer type (BetterBench, ECBD, OECD)? Are the 13 contradicted answers included in the 210 -r answers or separate?
- **Q7.** In Section 5.3, "28 Part B ratings resting on absent information" and in the audit 54 + 6 = 60 absences. How are these defined?
- **Q8.** 312 judgments, 286 quoted: what was audited for the 26 judgments without a quote?
- **Q9.** What was the agreement among the 62 pairs outside B01 to B16 and B18 to B19 (25 of 62 by my calculation)?
- **Q10.** What would a human rater with the same read-only access conclude on the same HumanEval snapshot? Would a human call the exec() finding Contradicted or Documented with failed outcome?
- **Q11.** Is the exec() line uncommented in your frozen commit b9453e8 only, or in the public default branch too? (The README text I could read says it is "deliberately commented out", while the current default branch appears to show it uncommented.)
- **Q12.** Why was Caliper mapped but not applied, and why were How2Bench and ABC applied to one benchmark each? How do these choices affect the 302 pairs?
- **Q13.** What is the relation of this submission to the companion paper [5] (shared data, shared claims)?

##### 6. Checks I made

**Counts that add up (recomputed with Python).**
- Items: 47+20+68+55+44+28+18 = 280. The "in the paper" counts (46, 42) give 277, so the 280 uses released template counts, which is stated.
- Table 3: column sums 56, 29, 88, 69, 67, 45, 32 = 386. Row sums 10, 46, 58, 173, 99 = 386. Consistent with 280 items plus 106 extra links from 76 compound items.
- Criteria: 8 + 31 = 39. 29 B criteria + 2 splits (B14a/b, B28a/b) = 31. The stage scopes in Table 3 and Section 2.2 list 29 base criteria.
- Terms in Table 2: 11 rows, as the text says.
- Study 1 answers: BB 188 + ECBD 80 + SC 272 + H2B 55 + ABC 44 + OECD 72 = 711. The four frameworks "whose rules can produce -r" total 559. The 2 repeat sessions are not in the 711 (with them the total would be 826). The 18 sessions plus 2 repeats plus 8 Study 2 sessions = 28.
- 199 = 41+123+23+12. 210 = 199 + 11 (BetterBench score 5 answers, implied, not stated). 210/711 = 29.5%, 210/559 = 37.6%, 13/711 = 1.8%. 13 = 9+2+2.
- 159 + 143 = 302. 159/302 = 52.6%. 143/302 = 47.4% (the "47%" in Section 6.1). 148/302 = 49.0%. 50+42+42+8+1 = 143. 92/143 = 64%.
- 117/221 = 52.9%. 17/19 = 89.5%.
- Repeats: 19/21 = 90.5%, 20/22 = 90.9%.
- Study 2: 8 sessions x 8 = 64 Part A. 8 x 31 = 248 Part B. 4 benchmarks x 8 = 32 and x 31 = 124. 26/32 = 81.3%. 99/124 = 79.8%. 83/124 = 66.9%. 17+82 = 99. 18+106 = 124. 35 N/A ratings = 17x2 + 1, consistent with 17 of 18 N/A pairs agreeing. 94/124 = 75.8%. 101/124 = 81.5%. Joint 83 lies between 69 and 94, so it is feasible.
- Audit: 55+9 = 64. 159+54+29+6+0 = 248. 64+248 = 312. 246+40 = 286.

**Counts or statements that do not add up or are inconsistent.**
1. Section 3.2 and Section 7: "kept the draft on 56" with 180 matches gives 236, not 234 of 280.
2. Section 5.3: 28 Part B ratings "resting on absent information" (21 Undocumented, 5 Claimed, 2 Documented) versus 54 plausible absences + 6 contradicted absences = 60 in the audit.
3. Section 5.3: 312 judgments are audited, but 286 quotes are reported, so 26 judgments have no quote.
4. Section 3.2: "All 28 Caliper items map to C23/B23, with 13 carrying secondary links". Table 3 shows 45 Caliper links, so the 13 items carry 17 secondary links (40 in extrapolation, of which at most 28 are C23; 1 in generalization; 4 in decision).
5. Abstract and Section 5.3: "99/124 Part B levels" versus "levels and fields matched on 99 of 124 pairs". Alpha uses 106 pairs.
6. Introduction: Scorecard marks "four of its eight scoring items unsatisfied", while Table 3 gives Scorecard 12 links under Scoring (and C07 uses SC-65 to SC-68). Also "C07" is scoring validation in one place and edge cases in another.
7. Section 5.1: 134 of the 302 pairs are reported (117 + 17 = 240 pairs); the remaining 62 pairs have 25 agreements (40%), not mentioned.
8. Section 3.2 traced example: "Of 42 = 6 pairs" is a typesetting error for the binomial coefficient (4 choose 2).
9. Table 5: B28a is "Contradicted (run 1) / Documented (run 2), outcome failed in both". A level Documented ("grading environment described") with a failed outcome is a strange combination that the rubric (Table 4) does not define. Check kind "run by reviewer" is used for static inspection.
10. Equation 3 uses tau_active(r) while Equation 2 uses Active(c); Table 2 calls the Tier 3 output "Decision" while Equation 3 is "Status" and Equation 4 is "Decision".

**Claims without support.**
- "Published review frameworks frequently reach opposite conclusions" (Introduction): supported only for one model on four benchmarks.
- "MESA's unreported qualifier separates ..." (RQ2 answer): no validation of the separation.
- The title and the Section 6.1 claim that the findings "show why this is fragile" for teams: no practitioner data.
- "Agreement ... measures repeatability", which the paper itself limits in Section 7, but the abstract and conclusion lead with percentages.

**Rule checks (call for papers).**
- Page limit: 15 pages including references, matches the 15 page limit for technical design and scientific evaluation papers. Layout looks like LNCS.
- Abstract: four labelled paragraphs (Context and motivation, Question/problem, Principal ideas/results, Contribution including limitations). Keywords are present. The abstract is very number heavy for the Principal ideas paragraph.
- Anonymity: "Anonymous Author(s)" and placeholder affiliation. Reference 5 is cited as "Author(s), A." (the call asks for a placeholder like "A. Anonymous") and as a companion paper under review, so the work overlaps. The singular "the author" in Sections 3.2 and 7 versus "the authors" in the Disclosure is a minor inconsistency. The model names are product names, not an identifying detail.
- Data Availability Statement: present, but it gives no link or identifier, and I could not check it.
- Generative AI: the paper discloses model use fully in the method, but cites neither the Springer AI policy nor the LLM Guidelines Initiative.

**References.**
- Checked and found to exist with matching content: Ghosh et al., Evaluation Cards (arXiv:2606.09809); Lewis et al., Quality model for ML components (arXiv:2602.05043, and its abstract matches the use of ISO 25059 vs component attributes); Cao et al., Code benchmarks should prioritize rigor (arXiv:2501.10711v5, which does propose HOW2BENCH with 55 checklists); Bean et al., Measuring what matters (arXiv:2511.04703); Koohestani et al. (arXiv:2503.05860, which proposes BenchFrame and HumanEvalNext, so the paper's description "benchmark repair and quality indexing" fits BenchFrame only partly).
- Checked the HumanEval repository page: the README text says the execution call is "deliberately commented out", while the default branch execution.py currently shows exec(check_program, exec_globals) uncommented at about line 50 with a comment telling users to uncomment it. So the paper's statement of a README versus code mismatch is plausible. I could not check the commit hash b9453e8 itself.
- Not verified (the lookup failed or was rate limited): Alonso and Church (SIGIR Forum), Scorecard (EvalEval 2026, doi 2026.evaleval-1.25), Gomez et al. (MAKE 8(6) 141). Other references (Kane 2013, Hayes and Krippendorff 2007, Zave and Jackson 1997, Gotel and Finkelstein 1994, Wand and Weber 1993, Berry 2022, BetterBench, ECBD, TruthfulQA, HLE, tau-bench) are known to me and look correct. I found no hallucinated reference.
- Reference 8 gives "version 5 (2026)" and reference 6 says NeurIPS 2025; the arXiv page I read shows the paper without confirming the venue.

##### 7. Score

**Reject**

(Weak reject is possible if the reviewers weigh the novelty of the absent versus defect distinction heavily. As submitted I rate soundness too low for the category.)

##### 8. Reviewer confidence

**Medium to high.** I can check the design, counts and reliability computations in full from the text, but I could not open the replication package, the prompts or most of the benchmark snapshots, and I did not run the sessions.

##### 9. Recommendation

I would not accept the paper as submitted. The idea of separating missing documentation from a located defect is good, and the arithmetic is mostly careful. But every empirical result comes from one model family acting as reviewer, coder and auditor. The mapping that defines the standard rests on one author and an LLM draft with a counting slip. The headline agreement figures depend on the authors' own aggregation rule and on dependent pairs. And the reliability statistics (a pooled nominal alpha of 0.80 on 32 pairs, an ordinal alpha of 0.70 with no interval) cannot carry the claim of a repeatable standard. The audit shows a non trivial error rate (6 false absences, 29 weak ratings, 11 of 46 Verified ratings overstated), but the abstract leads with "0 fabricated quotes". The RTM, which is the RE contribution, is not evaluated. The smallest set of changes that would move my score up one step to weak reject (and make acceptance possible after revision) is: (1) add a human validation on a sample (two humans plus the model on at least two benchmarks, and a second human on a random quarter of the mapping), with chance corrected agreement and bootstrap intervals; (2) replace the pooled alpha with per criterion raw agreement and report the full level distribution and the lower agreement groups; (3) fix or explain the counting inconsistencies (234 versus 236, 28 versus 60 absences, 312 versus 286 quotes, "levels" versus "levels and fields"); (4) state the aggregation rule sensitivity and the run to run noise adjusted disagreement, and compare MESA's repeatability with the frameworks' on a shared unit; (5) reframe the claims as being about LLM applied frameworks, lead the abstract with the audit error rates, and either drop the RTM from the contributions or submit the paper as a technical design paper with the RTM clearly labelled unevaluated; (6) provide an anonymous link in the Data Availability Statement and the prompts, model identifiers, sampling settings and snapshot identifiers needed to rerun the sessions.

---

### MESA paper: reviewer for AI evaluation

#### REFSQ 2027 research track: review of the MESA submission (reviewer perspective: AI evaluation and measurement validity)

Submission: "Unifying Benchmark Evaluation Protocols: A Meta-Evaluation Standard for Artificial Intelligence in Requirements Engineering" (15 pages, LNCS).
Files read: the call, the PDF (all 15 pages), the text extraction. I did not see the anonymized replication package named in the Data Availability section, so everything below rests on the paper alone.

##### 1. Summary of the paper

The paper argues that teams use public benchmark scores as acceptance evidence for model capabilities, so they must check whether a benchmark and its scoring harness support the requirement. It takes seven published benchmark review frameworks (BetterBench, ECBD, Scorecard, How2Bench, ABC, Benchmark Caliper, OECD facets), transcribes 280 items, and maps them through 386 links onto 30 "concerns". From these it derives MESA: a 39 criterion rubric (8 descriptive criteria A01 to A08, 31 evaluative criteria B01 to B29 with two split criteria), six evidence levels (Claimed, Documented, Verified, Contradicted, Undocumented, N/A), a separate "check outcome", an "unreported" qualifier (-r) for recoded negative verdicts, and a three tier scheme ending in gate statuses (Inadmissible, Inquiry Required, Admissible). A Requirements Traceability Matrix (RTM) is given as formulas (Eq. 2 to 4) that gate a score decision, but it is not evaluated.

The evidence is two studies, all run by one language model family with read only file access and no code execution. Study 1 (18 sessions, plus 2 repeats) applies six frameworks to HumanEval, TruthfulQA, HLE and tau-bench. The frameworks agree on 159 of 302 pairwise concern verdicts (52.6%). Of the 143 disagreements, a model coder attributes 92 to item granularity (50) or missing documentation rules (42). 210 of 711 item answers carry -r and 13 record a contradiction. Study 2 (8 sessions) applies the rubric twice to each benchmark: 26/32 Part A classifications match (nominal alpha 0.80), 99/124 Part B levels match (ordinal alpha 0.70), and 83/124 level plus outcome pairs match. A model "source checker" finds all quotes present and rates 214 of 312 judgments as directly supported. The authors state that no human raters were used and that the RTM is not evaluated.

##### 2. Paper category under the call

Candidate categories: technical design paper (15 pages) and scientific evaluation paper (15 pages). The paper is 15 pages including references, so it fits either limit. It does not fit the research preview, vision or experience report categories (the page limits are 8, 8 and 12, and it has neither a roadmap nor lessons learned).

The main sessions have run: all 28 sessions are reported. What has not run is the human validation and the RTM evaluation. This matters per category:

- Technical design paper (best fit; the contribution is an artifact, MESA, with a "preliminary evaluation"). Criteria in the call's order:
  - Novelty: moderate. Harmonizing review frameworks and separating unreported information from located defects is a useful idea, and evidence level versus check outcome is a neat distinction. But the 30 concerns are a relabeling of the frameworks' own items, and the RTM is mostly a decision rule on top.
  - Potential impact and relevance: potentially good for the theme (benchmarks and evaluation frameworks at AI speed). The relevance to RE rests on the RTM, which is unevaluated, and none of the four benchmarks is an RE benchmark.
  - Soundness: not met. See W1 to W8.
  - Verifiability: partly met. The claimed package is not visible to me, and the model identifiers are not stable (W11).
  - Presentation: dense, with many numbers and inconsistent terms (see section 6).
- Scientific evaluation paper (what the structure of RQ1 to RQ3 suggests, and the paper cites the Empirical Standards). Soundness is the first criterion, and it fails: there is no reference standard, no human rater, one model plays reviewer, coder and checker, and the statistics are not interpretable as stated. Under the Empirical Standards the study would be a weak "experiment" or "case study" with no stated threats mapped to validity types. As a scientific evaluation paper I would reject.
- If the RTM part is counted as a design contribution, it is unevaluated, so it counts as a proposal only (the abstract admits this). The paper should then be read as a technical design paper whose evaluation covers only the rubric, and only in terms of repeatability, not validity.

##### 3. Strengths

S1. The distinction between "not reported" and "located defect" is a real problem in benchmark audits, and the paper states it cleanly. The HumanEval running example (static finding at execution.py line 50) is concrete, and the fact itself checks out: on the current master the `exec(check_program, exec_globals)` call is live at about line 50, under a comment that tells the user to uncomment it. (I checked this through the cited repository [28].)

S2. Honest limitations. The abstract and Section 7 say that all reviews, codings and audits were done by models of one family, that no human raters were used, that agreement measures repeatability and not correctness, and that the RTM is not evaluated. Many papers in this area hide these points.

S3. Reporting of arithmetic is mostly consistent. Table 3 row and column totals, the 711 answers (188+272+80+72+55+44, i.e. the 16 main plus 2 single framework sessions, excluding the 2 repeats), the 312 judgments (64+248), the 35 N/A ratings (17 agreeing pairs x 2 + 1) and the audit categories all add up (section 6).

S4. Separating level and outcome, and recording scope, detection limits and the "check kind" (reported by authors or run by reviewer), is a good record schema. It forces a reviewer to say what was actually done.

S5. Repeat runs were done at all (Study 1 repeats: 19/21 and 20/22 concerns stable; Study 2 two runs per benchmark). The authors do not hide that about one verdict in ten flips between runs of the same framework.

S6. Using the Kane argument based view and an EFPA style split between descriptive and evaluative criteria is the right direction for the field. It connects benchmark review to measurement practice.

##### 4. Weaknesses

W1 (decision). The rubric has no validity evidence; it is evaluated only for repeatability of one model.
Where: Section 5.3, abstract, RQ3. What: RQ3 asks whether ratings "can be verified against repository code", but the only checks are (a) two runs of the same model agree and (b) another model of the same family finds the quotes. Neither shows that MESA ratings are right. There is no reference standard, no seeded defect test, no human expert rating of even a small sample, and no comparison with known benchmark problems. Examples that were available: HumanEval's weak tests (EvalPlus showed that extended tests change pass@1 and rankings), the label errors found in HLE and in MMLU style sets, TruthfulQA's known multiple choice and judge issues, and known task and policy errors in tau-bench (a later tau2 release revised tasks, as I understand it). The paper does not say whether MESA flagged any of these, so I cannot judge face validity. The paper reports no benchmark specific finding other than the HumanEval harness line. Why it matters: a repeatable but wrong rubric is not a standard. Fix: (i) a seeded defect study (inject known flaws, such as a leaked test set, an unsandboxed harness, label noise, or a weakened assertion, into copies of benchmarks and report detection rate and false alarm rate of the reviewer); (ii) a stratified human expert sample (even 30 to 50 criterion cells) with agreement against the model; (iii) report which known published defects MESA does and does not find on the four benchmarks.

W2 (decision). One model family plays reviewer, coder and checker, and the checker audits against the same sources the reviewer read.
Where: Section 4.2, 5.1, 5.3, Section 7. What: "Claude Sonnet 5.5" reviewed all 28 sessions; "Claude Fable 5.1" subagents coded the 143 disagreements and audited the 312 judgments. Correlated errors and shared blind spots (same pretraining, same preference for certain wording) are not controlled. Self preference and same family agreement bias in model judges is documented in the LLM as a judge literature. The audit verb "confirmed" in the abstract overstates what a model check proves. Also, the 54 "plausible absences" (22% of Part B) are by definition not verified; "plausible" is the checker's opinion that something is not in the sources. The disagreement coding (which supports the headline "64% from granularity and missing documentation rules") is a single model labeling with no second coder, no reliability figure and no codebook in the paper. Why it matters: the main RQ1 and RQ3 claims depend on these labels. Fix: have two humans code a random 30 to 40 of the 143 disagreements and report kappa; have a human check a random sample of audit labels; add a different model family as at least one of the checkers and report cross family agreement.

W3 (decision). Read only access without code execution cannot support the rubric's own "Verified" level for many criteria, and cannot test the issues the paper says matter.
Where: Section 4.1, 4.2, 3.3 (Table 4), Section 7. What: Table 4 defines Verified for B05 (error checks "coverage, findings, limits reported"), B07 ("exploits tested"), B14a ("contamination check or held out set reported") and B28a ("isolation verified in code"). A reviewer with only a file lister and a file reader cannot run an exploit, cannot compute n-gram or membership overlap, cannot parse the dataset beyond what the repository holds, and cannot test a judge or parser. So Verified can only mean "the authors say they checked", which is a reporting level, not verification. The paper concedes this for B07 and B14b but the abstract and RQ3 treat "Verified" ratings (46 of 248) as if they carried the plain meaning. Also, B14b (candidate model exposure, the central contamination criterion) was N/A in all 8 sessions because no model was named, and B14a only records what the benchmark authors report. So contamination, one of the main threats in the benchmark validity literature, was not assessed in the study at all. The paper also does not say what the frozen snapshots contain: HLE's questions are not in its code repository (they sit in a hosted dataset), so task quality criteria (B03 task realism, B05 error checks, B15 shortcuts) could not be inspected for HLE unless the data was added. The reader cannot tell. Why it matters: "a model with read only access can support the claims" is false for the dynamic criteria, and the gate (Tier 3) depends on exactly those criteria. Fix: state for each of the 31 criteria whether it is decidable from static inspection, from execution, or from data; restrict the claims to the static subset; add one execution capable run on one benchmark to show how the ratings change; say what is in each snapshot.

W4 (decision). The headline comparison 210 versus 13 (RQ2, abstract, Section 6.1) is largely produced by the design, not found.
Where: Section 5.2, 3.2, Section 7. What: (a) -r is attached by deterministic recoding rules to every unfavourable native verdict that "rests on absent documentation", and the paper itself says -r "pools unmet reporting requirements with unverified practices". A count of -r is therefore a count of negative answers under the rules of four frameworks (BetterBench 0 and 5 scores, Scorecard, How2Bench, ABC), not a count of absent reporting. (b) The 13 "contradiction" instances can only arise where a reviewer wrote something beyond the framework's native answer, since those frameworks have no Contradicted value; this conflicts with "without altering native prompts" (Section 3.2) and the paper does not explain how a Contradicted rating is attached to an answer of, say, Scorecard. (c) The reviewer could not execute code, so by construction it cannot find execution only defects; 1.8% is then a lower bound set by the tool restriction. (d) The comparison is across answers from frameworks with different item counts (Scorecard supplies 272 of 711 answers) and is not normalized per benchmark or per concern. (e) "RQ2: separating" is answered by definition: the qualifier separates the two classes because it is defined to. Why it matters: this is presented as an empirical result that justifies MESA. Fix: report how a Contradicted instance is produced for each framework; report the -r composition (how many are absent versus a failed check not reported versus a defect of the rubric item itself); drop or reword "separates" to "records"; and do not present 13/711 as a rate of contradiction in benchmarks.

W5 (decision). RQ2 "How completely can framework questions be unified" is answered by construction, and the unification is a single author's judgment.
Where: Section 3.2, Table 3, Section 5.2, Section 7. What: "All 280 items map onto the 30 concerns with zero unmapped items" is guaranteed, since the concerns were grouped bottom up from the same items and a concern was added (C30) for the OECD descriptive facets. The mapping was drafted by an assistant model, then mapped independently by "the author"; they differed on 100 of 280 items (36%). The paper reports no chance corrected agreement for this step, no second human, and no sensitivity of Study 1 to the mapping. The 29 B criteria equal the 29 evaluative concerns one to one (plus two splits), so "deriving a 39 criterion rubric" from the mapping is a renaming rather than an independent derivation; there is no content validity step (expert review, coverage of the measurement literature, item analysis). Caliper puts all 28 items on C23 (40 of its 45 links go to the extrapolation stage) and was never applied, so it adds nothing to Study 1; ECBD and OECD are design and classification schemes, not scored quality checklists (OECD supplies 10 of 32 links to Part A only), so only four of the seven frameworks are comparable review instruments. The claim of unifying "seven" frameworks is therefore stronger than the evidence. Fix: two or more independent human mappers with kappa; report Study 1 results by mapping version; say plainly that Caliper and the OECD facets are not part of the agreement analysis; explain why 29 evaluative concerns is the right granularity.

W6 (decision). The agreement statistics in Study 1 and Study 2 are not interpretable as reported.
Where: Section 5.1, 5.3. What:
  1. Study 1: 159/302 is a raw proportion over pairs that are not independent (same benchmark, same reviewer run, same item feeding several pairs), with no chance correction and no interval. "Open" versus "Open" counts as agreement (equal verdicts), which means two "not decidable" answers agree. The rate depends on the strict conjunction rule chosen by the authors (a framework with many items fails a concern when any item fails), which the paper itself says produces 50 of the 143 disagreements, so the disagreement is partly an artifact of MESA's own aggregation. The ceiling set by run to run noise is 81% to 90% (Study 1 repeats), so the gap between 53% and the ceiling is the quantity to explain, and the paper does not do that.
  2. Study 2 nominal alpha 0.80 with 81% raw agreement (26/32) implies an expected chance agreement of only about 6%. That is possible only with many roughly evenly used categories. But Part A criteria A01 to A08 have different category sets (scoring method, reference type, containedness, progression, task variation), and pooling them into one alpha is not valid; per criterion alpha is needed. With 32 units, alpha has a wide interval, and none is given ("no intervals computed").
  3. Ordinal alpha 0.70 on an order Contradicted < Undocumented < Claimed < Documented < Verified. This is not a scale: "Undocumented" means "sources do not allow a level to be chosen" and is not lower than "Claimed"; placing Contradicted below Undocumented is an assumption. Alpha ordinal uses squared distances over this ordering, so the number depends on it. Krippendorff himself treats 0.667 to 0.80 as tentative; the paper gives no interpretation.
  4. The 124 Part B pairs include 17 trivially agreeing N/A pairs (4 of them are B14b, which was N/A by design in every session) and a scope field that matches 124/124, which indicates a constant default rather than a measured property. The raw 80% therefore overstates agreement on judged content (the paper's own 82/106 = 77% is the better number).
  5. Two runs of one model are a test retest estimate, not inter rater reliability; the term "independent runs" invites the wrong reading. The reliability statistic should not be named "alpha" in the abstract without the qualifier "same model, two runs".
  Fix: per criterion statistics with bootstrap intervals clustered by benchmark; drop B14b and scope from agreement; report distributions of levels; justify or drop the ordinal ordering (use nominal alpha, Gwet AC1 or Cohen kappa); chance correct Study 1.

W7 (decision). The measurement theory is used as vocabulary; the argument structure of Kane is not used, and some mappings and references are doubtful.
Where: Section 2.1, 2.2, Eq. 1, intro ("representation theory [32]"), Table 3. What:
  - Kane's approach builds an interpretation and use argument and then evaluates each inference with evidence, with an explicit view of which assumptions are weakest. Here the four stages are used as a filing scheme for criteria. No claim, warrant or backing is stated, no stage level result is reported (for example, which inference is best or worst supported on the four benchmarks), and Eq. (1) `W, E, O_bench(M,B) |-ind G_AI` has no defined semantics ("inductive assurance argument" is not defined; AMLAS [17] has argument patterns, not this relation).
  - The assignment of criteria to stages is unmotivated and in places wrong by measurement standards. Contamination and exposure (B13 to B16) and shortcuts are filed under Extrapolation, but contamination is a threat of construct irrelevant variance to the score interpretation (Messick) and in Kane's terms would be argued under generalization or scoring. "Decision" collects replication, licensing and maintenance, which are about use and governance, not about the inference from performance on a target domain to a decision. Kane's fourth inference is usually called implication or decision, but the stage's content here has little to do with it.
  - The 2014 Standards [4] name five sources of validity evidence (content, response processes, internal structure, relations to other variables, consequences). The rubric covers reporting of content and internal consistency, but has no relations to other variables (does a benchmark score predict the deployment outcome, the requirement), which is the evidence a requirement engineer needs most.
  - "Representation theory [32]": Wand and Weber (1993) is the representation model for information systems grammars based on Bunge's ontology, not representational measurement theory (Stevens, Krantz and Suppes). It is cited in the introduction as grounding and never used again. Either remove it or state what is taken from it.
  - The rubric rates what is reported and available (Claimed, Documented, Verified-as-reported). A benchmark can be fully Documented and be invalid; a benchmark can be valid and poorly documented. The paper says the rubric records "evidence", which is fair, but the title, keywords ("Construct Validity") and Section 2.2 suggest it measures validity. Say what the rubric does not measure.
  Fix: either use Kane's structure (state the claims and the evidence per inference, and report which link is weakest for each benchmark) or present the stages as a convenience grouping; add a criterion or section on relation to external criteria; correct or drop [32].

W8 (decision). The RTM gate (Section 6.2, Eq. 2 to 4, Table 5) is unevaluated, internally loose, and its running example overreaches.
Where: Section 6.2, Table 5, Section 3.3. What:
  - Not evaluated, and its implementation is deferred to a companion paper [5] "under review". The abstract lists it as a contribution (3). The contribution cannot be counted for soundness, and relying on a companion submission weakens verifiability and raises an overlap question (the call has no policy, but the reviewer cannot see [5]).
  - Eq. (2): Def(c) is "level = Contradicted OR outcome = failed", so the level "Contradicted" is redundant with outcome "failed", and the very example shows the level is unstable (B28a was Contradicted in run 1 and Documented in run 2). The gate works only because of the OR; this undermines the paper's argument that levels separate located defects from absences. A "Documented" rating with outcome "failed" is also semantically odd. The sufficiency rule uses `level(c) >= Documented` with an order that is never defined for Contradicted, Undocumented and N/A (the order is defined only in Section 5.3 for alpha). `Active(c)`, `tau_active` and `Loc(c)` are not defined in the text; B14b appears in the profile of R1 as N/A "applies to R1 without rating", whereas Eq. (2) would make N/A mean "not applicable for r", the opposite.
  - Severity is absent. In the example, an unisolated `exec()` in the released harness makes the evidence Inadmissible for R1 (pass@1 >= 80% for IDE Python synthesis). But the effect of in process execution on the score validity depends on whether candidate code is adversarial; for a non adversarial model the pass@1 is not changed. It is a safety and hygiene defect, and the paper's own S1 says the README warns about it. Also, the HumanEval paper's gVisor statement describes the authors' evaluation infrastructure; the released harness is a different artifact, so calling it a contradiction of "a claim of the benchmark" confuses two artifacts. A gate that blocks on any located defect without threat model or effect size would mark nearly every released harness Inadmissible and nearly every benchmark Inquiry Required (because Admissible needs Verified, passed, with detection limits for five criteria, which almost no paper reports). The gate then has no discriminating power, and no calibration shows otherwise.
  - Removal of tasks with located defects before scoring (`T'_r = T_r \ D(c)`) is selection on the outcome side: defects are usually found by inspecting tasks that models fail, which biases the score upward and breaks comparability with the published number. The confidence interval method in Eq. (4) is unspecified (for n = 164 and theta = 0.80 the half width alone is about six points), and `n_min` is not given a value.
  - Table 5 is an instantiation of one cell from two sessions, not a test.
  Fix: either move the RTM to the companion paper or evaluate it (even a small study with practitioners or a worked comparison on several benchmarks); define all symbols; add severity and threat model; remove the OR redundancy or justify it; handle post hoc task removal explicitly.

W9 (decision). Benchmark selection and the claim of relevance to RE.
Where: Section 4.1, title, abstract, Section 7. What: HumanEval (2021, saturated, 164 tasks), TruthfulQA, HLE and tau-bench are four famous benchmarks that were certainly seen by the reviewer model in pretraining; its ratings may reflect recall of known critiques more than inspection. This is a threat to the claim that the sessions measure what is in the repository. The selection has no rationale, includes no RE benchmark, no repository level software engineering benchmark and no less known benchmark (where recall cannot help). The title says "for AI in Requirements Engineering", but the RE content is the Jackson and Zave framing and the unevaluated RTM. Claims to generality ("published review frameworks frequently reach opposite conclusions", Section 6.1 "our findings show why this is fragile") are written about frameworks and checklists, while Section 7 says the finding shows "how frameworks differ when one model applies them, not how human reviewers would apply them". The abstract and Section 6.1 should carry that qualification. Fix: add benchmarks outside the model's likely memory (new or private style ones) and at least one RE related benchmark; state the recall risk and test it (for example, ask the model to rate without the repository and compare).

W10 (minor). Missing related work on benchmark quality, validity and contamination.
The related work (Section 2.3) lists mostly review frameworks and assurance models. For a paper that proposes a benchmark meta evaluation, the following lines are missing (I list works I am confident exist; the authors should check details):
  - Validity and measurement of AI evaluations: Raji et al., "AI and the everything in the whole wide world benchmark" (NeurIPS D&B 2021); Jacobs and Wallach, "Measurement and fairness" (FAccT 2021); Blodgett et al., "Stereotyping Norwegian salmon" (ACL 2021); Wallach et al., "Evaluating generative AI systems is a social science measurement challenge" (2024); Eriksson et al., "Can we trust AI benchmarks? An interdisciplinary review of current issues in AI evaluation" (2025); Xiao et al., an NLG metric evaluation under measurement theory (EMNLP 2023); Bowman and Dahl, "What will it take to fix benchmarking in natural language understanding?" (NAACL 2021); McIntosh et al., "Inadequacies of large language model benchmarks in the era of generative artificial intelligence".
  - Contamination: Magar and Schwartz (ACL 2022); Sainz et al., "NLP evaluation in trouble: on the need to measure LLM data contamination for each benchmark" (2023); Oren et al., "Proving test set contamination in black box language models" (ICLR 2024); Xu et al., survey of benchmark data contamination (2024); LiveCodeBench (Jain et al. 2024) as a design response.
  - Benchmark defects and score reliability: EvalPlus (Liu et al., NeurIPS 2023) for HumanEval's weak tests (this is the standard evidence that HumanEval's harness validity concerns are about tests, not isolation); Northcutt et al., "Pervasive label errors in test sets" (2021); Gema et al., "Are we done with MMLU?" (2024); Dehghani et al., "The benchmark lottery" (2021); Madaan et al., "Quantifying variance in evaluation benchmarks" (2024); Miller, "Adding error bars to evals" (2024); Biderman et al., "Lessons from the trenches on reproducible evaluation of language models" (2024); Burnell et al., "Rethink reporting of evaluation results in AI" (Science 2023).
  - Models as raters of artifacts: Zheng et al. (MT-Bench and Chatbot Arena, 2023) and Panickssery et al. on self preference of LLM evaluators; work on LLMs as annotators compared with humans (for example the JUDGE-BENCH study). These are directly relevant to W2.
  - Measurement foundations: Messick (1995) on validity as a unified concept, Cronbach and Meehl (1955), and the Standards [4] sources of evidence (W7).
  - Compared work already cited but not compared: Bean et al. [6] is a 445 benchmark review with recommendations on construct validity; the paper uses it only for the definition of a benchmark. BQAI [14], BenchFrame [22] and NIST AI 800-2 [27] are one sentence each; the difference from MESA is asserted ("MESA instead reconciles...") not shown.

W11 (minor, but affects verifiability under the call). Reproducibility of the model based procedure.
Where: Section 4.1, 4.2, Data Availability. What: "Claude Sonnet 5.5 through Claude Code at medium effort" and "Claude Fable 5.1 subagent" give no model identifiers or dates, sampling settings, prompt text, or tool definitions in the paper; models are retired and Claude Code's behavior changes. The call recommends the LLM Guidelines Initiative; the paper does not mention it, nor does it state how LLMs were used in preparing the paper (Springer policy). The package is "provided with this submission" with no link or warning, and I could not check it. The total cost (2.23 USD for 8 sessions) is reported but not the cost or tokens of the 20 Study 1 sessions. Fix: give identifiers, dates, prompts (appendix), settings and a statement against the LLM guidelines checklist.

W12 (minor). Some benchmark and framework descriptions are only partly right or cannot be confirmed.
  - HumanEval line 50: confirmed (S1). But the paper says README states the call "is commented out" and that the comment "states that the guard is not a security sandbox"; in the file I saw, the comment above the call asks the user to uncomment it after reading the disclaimer, and the sandbox disclaimer is in the reliability guard. Quote the comment exactly.
  - ABC: the paper says "44 released items, 42 in the paper". The arXiv v5 text lists 42 items (10 task validity, 19 outcome validity, 13 reporting). The extra 2 may come from the repository, but 280 is built on 44; the discrepancy should be sourced.
  - Benchmark Caliper [2]: the repository describes six validity dimensions (input and output, each across ontology, content, form), scored 1 to 5, applied to a benchmark paper plus a target deployment. "28 items on cultural and regional transfer" could not be confirmed from the repository front page; if the 28 items are sub checks, say so. It is a software repository without a publication, which is a different kind of evidence than the other six.
  - BetterBench [30]: 46 criteria and 24 benchmarks in the paper (confirmed); "47 template items" is the authors' own count and should be explained.
  - Scorecard [20]: the proceedings entry and authors exist (EvalEval 2026, pp. 128 to 160); I could not confirm "22 principles and 46 sub-bullets, 68 items".
  - "Frameworks ... reach opposite conclusions" (intro): the intro compares BetterBench's partial score of 10/15 with Scorecard "four of eight scoring items unsatisfied". A score of 10/15 is not a verdict, so it is not the opposite of an unsatisfied item; the recoding maps it to Satisfied (partial), a choice by the authors.

W13 (minor). Relevance claims in the introduction rest on weak citations. "The engineering bottleneck shifts upstream to validating whether candidate models satisfy system requirements [16]": [16] is a 2024 mapping study of RE for AI based systems; it does not support a claim about AI velocity. "A leaderboard score does not establish that a model satisfies a system requirement [31,3]": [31] (Leaderboard Illusion) is about Chatbot Arena's sampling and private testing practices; [3] I could not confirm (W-check below).

##### 5. Questions for the authors

Q1. How does a "Contradicted" instance arise on a framework item in Study 1 (Section 5.2), given that BetterBench, Scorecard, How2Bench and ABC have no such answer value and prompts were "not altered"? Who assigned it, and by which rule?
Q2. What do the four frozen snapshots contain? Does the HLE snapshot hold the questions or only code and the paper? Does the reviewer have web or memory access to anything beyond the two read tools?
Q3. Did the reviewer model rate criteria from the files, or from prior knowledge? Did you run any sessions on the same benchmark with the repository removed, or on a benchmark released after the model's cutoff?
Q4. Which known published defects of the four benchmarks (for example HumanEval's weak tests, HLE label errors, TruthfulQA's format issues) did MESA find or miss?
Q5. Was the rubric (including the splits B14a/b, B28a/b and the task defect field) developed while looking at these same four benchmarks, especially HumanEval? If so, "frozen before the eight sessions" does not give an out of sample test.
Q6. Why order the levels as Contradicted < Undocumented < Claimed < Documented < Verified for ordinal alpha? What are alpha values with nominal alpha, and per criterion? What are intervals?
Q7. Nominal alpha 0.80 at 81% raw agreement implies about 6% chance agreement. What are the category sets and marginals of A01 to A08, and is alpha pooled across them?
Q8. What happens to the 29 disagreements with an Open verdict, and what is the agreement if Open versus Open pairs are removed? What if aggregation is "any item unsatisfied" versus "majority" versus "mean score", per benchmark?
Q9. In the 143 disagreements, how many would remain if the same framework were run twice (the repeat sessions imply about 10% flips)? Can part of the 64% be attributed to run noise rather than to framework design?
Q10. The audit finds 6 absences contradicted by the sources (2%) and 29 weaker support ratings (including 11 of 46 Verified). How were these 35 found, given 54 other "plausible absences" were accepted? What is the false negative rate of the checker?
Q11. Why is the gate Inadmissible for R1 when the exec() call does not change pass@1 for a non adversarial model? How would a threat model or effect size enter the decision?
Q12. How does the overlap with the companion paper [5] divide the contribution: which equations, tables or results are in [5] and not here?
Q13. 286 quotes are checked against 312 judgments: what supports the 26 judgments without a quote (N/A ratings, absences)?

##### 6. Checks I made

Arithmetic that adds up:
- Table 3: every row and column total is correct (56+29+88+69+67+45+32 = 386; 10+46+58+173+99 = 386). The 29 B criteria in stage lists: 2 + 6 + 10 + 11 = 29, plus two splits gives 31; 8 + 31 = 39.
- Item counts: 47+20+68+55+44+28+18 = 280 (Table 1 uses the released counts; using paper counts 46 and 42 gives 277).
- Study 1: 159 + 143 = 302; 159/302 = 52.6%; 148/302 = 49.0%; 143/302 = 47.4% ("47%" in Section 6.1). 50 + 42 + 42 + 8 + 1 = 143; 92/143 = 64.3%. 199 = 41+123+23+12; 13 = 9+2+2; 210/711 = 29.5% ("30%"); 210/559 = 37.6% ("38%"); 13/711 = 1.8%.
- 711 answers = BB 4x47 (188) + SC 4x68 (272) + ECBD 4x20 (80) + OECD 4x18 (72) + H2B 55 + ABC 44. So the 711 excludes the two repeat sessions; "18 sessions" and "28 sessions" (18 + 2 + 8) are consistent. It also includes the 9 answers from the six items excluded from aggregation (BB-45, BB-46 x4, H2B-45), which is not said.
- Study 2: 8 x 8 = 64 and 8 x 31 = 248, total 312. 159 + 54 + 29 + 6 = 248 and 55 + 9 = 64. 32 Part A pairs = 4 x 8 and 124 Part B pairs = 4 x 31. 82 + 17 = 99; 124 - 18 = 106; 35 N/A ratings = 17 x 2 + 1. 21 + 5 + 2 = 28. 94/124 = 75.8%, 101/124 = 81.5%, 83/124 = 66.9%.
- Percentages in the audit (64%, 22%, 12%, 2%) round correctly.

Arithmetic or text that does not add up or is unclear:
- Section 3.2: the reconciliation counts (kept the draft 56, author 28, combined 4, third reading 12) sum to the 100 differences, but "the final mapping equals the draft on 234 of 280 items" does not follow: items that matched (180) plus items where the draft was kept (56) give 236, not 234. The same 234 is repeated in Section 7. Either the count of kept items or the 234 is wrong.
- Caliper: "All 28 items map to cultural transfer (C23/B23), with 13 carrying secondary links" gives 28 + at least 13 = 41 minimum links, and Table 3 has 45 Caliper links, so 17 secondary links are spread over 13 items; plausible, but not shown.
- Section 5.3 says "Part B evidence levels and fields matched on 99 of 124 pairs"; 99 is levels only (the fields are listed afterwards with their own counts: scope 124, kind 101, outcome 94). The abstract says "levels". Use one wording.
- 286 quotes versus 312 judgments (Q13); 246 + 40 = 286 is correct.
- Section 3.2 "Under strict conjunction ... Satisfied if all are Satisfied", but Satisfied (partial) is a separate value in the recoding rules and is not defined in the Tier 2 term (Table 2 lists only Satisfied, Unsatisfied, Open).
- Intro: Scorecard "four of its eight scoring items"; Section 3.2 says SC-65 to SC-68, four items for C07; Table 3 gives Scorecard 12 links in the scoring stage. "Eight" is not explained.
- The binomial in Section 3.2 appears as "42 = 6" in the text extraction; in the PDF it is (4 choose 2) = 6, so this is only an extraction artifact. Of the six pairs in the C07 example, two agree (BB and ECBD, H2B and SC) and four disagree: correct.
- Table 1 gives the MESA missing documentation rule as "Open" with "Recorded as Undocumented"; Section 3.2 recodes framework answers as Unsatisfied with -r. The MESA rubric itself is therefore never used to produce a Tier 2 verdict.
- Table 5: B14b "N/A ... applies to R1 without rating" conflicts with Eq. (2), where N/A is only for criteria that are not applicable to r.

Terms used inconsistently:
- "levels" versus "levels and fields" (above); "Verdict" has three values in Table 2 but "(partial)" in the text; "Part A classifications" versus "descriptive criteria"; "concern" and "criterion" are one to one for 29 of 30 concerns but are described as different units; "independent" runs for two runs of one model; "Decision" is used for both the Tier 3 status and the Accept/Reject/Inconclusive result in Eq. (4); the abstract lists six record fields, Section 3.3 lists seven (level, outcome plus five fields).

Claims without support:
- "Teams use public benchmark scores and automated reviews as acceptance evidence" (abstract, intro): no data or citation.
- "Our findings show why this is fragile" (Section 6.1): see W9.
- "Agreement was high on documentation and licensing (B18, B19: 17 of 19 pairs, 89%) but dropped on B01 to B16 (117 of 221 pairs, 53%)": 17/19 is a very small base; 117/221 includes B14a and B12, and 29 + 19 + 221 = 269 pairs leaves 33 pairs out (B17 to B29 other than B18/B19) without a figure.
- "0 fabricated quotes" is a weak claim, since string presence can be tested deterministically; the paper does not say what the model checker added beyond a string search.

References:
- Checked and found as cited: Zhu et al. [35] (NeurIPS 2025 D&B, the arXiv text lists 42 checklist items); Reuel et al. [30] (46 criteria, 24 benchmarks); Cao et al. [8] (arXiv 2501.10711 exists, with many versions; an ICML 2026 position paper page also exists under the title "Position: Code Benchmarks Should Prioritize Rigor, Reliability, and Reproducibility"; the earlier arXiv titles were different ("How Should I Build A Benchmark?"), so the reference points to the latest title; give the venue); San Joaquin et al. [20] (the ACL Anthology entry 2026.evaleval-1.25 exists, pp. 128 to 160; the first author is "San Joaquin", while the reference lists "Joaquin, A.S."); Ghosh et al. [13] (arXiv 2606.09809 exists with that title); Cohn and Hernandez-Orallo [10] and [11] exist; Berry [7] and Zave and Jackson [34] are real and correctly cited.
- Could not confirm: Alonso and Church [3] "Evaluating the evaluations: A perspective on benchmarks", ACM SIGIR Forum 58(2) with DOI 10.1145/3720330.3720332. Searches turned up no matching record, and the DOI did not resolve for me. Because the call allows desk rejection for many hallucinated references, the authors should check it. If it is a hallucinated or mis-cited reference, it supports claim 2 of the introduction.
- [2] Benchmark Caliper is a software repository, not a paper (see W12); [5] is cited as "Author(s), A." where the call suggests "A. Anonymous"; it is a paper "under review" that the reviewers cannot see.
- [32] Wand and Weber: real paper, wrong use (W7). [31] Leaderboard Illusion: real, but weak support for the sentence it is attached to (W13). [16]: real, weak support for the bottleneck claim.
- I did not check [12], [13] beyond existence, [14], [17], [19], [22], [23], [27] in detail.

Rule checks (call for papers):
- Page limit: 15 pages including references; fits technical design and scientific evaluation papers. LNCS layout: appears to be LNCS.
- Abstract: exactly four paragraphs, with the required labels; keywords present. The abstract is long and number heavy (about 20 numbers).
- Anonymity: no names, affiliations or acknowledgments; "contact@example.org" is a placeholder. The text says "the author" and "one author" (Section 3.2, Section 7), which is not a leak. Companion paper [5] is cited as "Author(s), A." under review; acceptable, but the contribution overlap should be stated (Q12).
- Data Availability Statement: present at the end, but it points to "an anonymized repository provided with this submission" with no link and no warning about non anonymized artifacts. I could not inspect it. The statement does describe the contents (mapping, recoding rules, rubric, four snapshots, logs of the 28 sessions, verification scripts). It does not say whether the prompts and the full 39 criterion rubric text are included, or whether the licenses of the four benchmark snapshots allow redistribution.
- Generative AI: the paper does not say how generative AI was used in writing (Springer policy) and does not refer to the LLM Guidelines Initiative, although the research involves LLMs as the measuring instrument.
- Hallucinated references: one reference I could not confirm (Alonso and Church [3]); not "many", so no desk rejection ground on this check alone.

##### 7. Score

Weak reject.

##### 8. Reviewer confidence

Medium: I am sure of the evaluation and measurement issues (W1 to W7, W9, W10), but I am less sure of RE community norms for a design paper with a preliminary evaluation, and I could not open the replication package.

##### 9. Recommendation

I would not accept the paper as submitted. The problem is real and the paper is candid about its limits, but what it demonstrates is that one model gives similar ratings when run twice (about 80%, with an alpha whose scale and pooling are questionable), and that frameworks disagree when the same model applies them under aggregation rules the authors chose. It does not show that the ratings are right, that the mapping is reliable, that the qualifier -r tracks absent reporting, or that the RTM gate improves any decision; and read only access cannot reach the criteria (exploit tests, contamination checks, task quality) that the gate depends on. The smallest set of changes that would move my score up one step, to borderline: (1) add a human validation: two human raters on a random sample of mapping decisions, disagreement codes and rubric ratings (or a seeded defect study with known flaws), with kappa and intervals; (2) restate the claims to the static, read only subset of criteria and mark which of the 31 criteria this covers, remove the headline reading of 210 versus 13 as a finding, and say how a Contradicted instance is produced; (3) fix the statistics (per criterion alpha with intervals, drop trivial N/A and constant fields, justify or drop the ordinal order, chance correct Study 1) and the 234 versus 236 inconsistency; (4) either evaluate the RTM or cut it to a short design sketch with defined symbols and a severity notion, and avoid presenting it as a contribution; (5) fix or confirm reference [3], correct the use of [32], and add the benchmark quality, validity and contamination literature in W10.

---

### Paper 2: reviewer for requirements engineering

#### REFSQ 2027 research track: review of submission "Applying Meta-Evaluation Benchmark Reviews to Requirement Decisions: An Executable Method"

Reviewer perspective: requirements engineering researcher. Files read: the call, paper2.pdf (15 pages), paper2.txt. Web search used only on references.

##### 1. Summary of the paper

The paper takes a single operational requirement for SymPy ("Working alone on a bug report ... the tests the maintainers later wrote for that bug pass, for at least 70% of bug reports, within 15 minutes each") and asks whether a coding agent meets it. Instead of testing the agent directly, a team would use public benchmark evidence (SWE-bench Verified). The authors build a three level decision engine on top of "MESA", a benchmark review rubric defined in a companion submission [3]. Level 1 checks input integrity (hashes, identities). Level 2 assigns an evidence status (Admissible, Inquiry Required, Inadmissible) from signed rating forms for seven criteria (B05, B07, B12, B14a, B14b, B28a, B28b). Level 3 computes a 95% Wilson interval on resolved tasks and returns Accept, Reject, Inconclusive, or No decision. The paper compares six outputs (raw rate, audit only, ABA, MESA strict, MESA lenient, ABC) on 20 source tasks and plans to compare them with a direct test on 20 post-cutoff target tasks.

What is shown: (a) a method description; (b) an executed B07 exploit check (17 of 20 tasks have a patch that passes hidden tests but fails an independent check; 6 are classed as task defects); (c) one B05 case (sympy-18199); (d) a B28a check in which 9 of 9 test runner hijack patches are scored as resolved; (e) nine forms signed by one author; (f) exact binomial power calculations (Table 4); (g) a Monte Carlo simulation under assumed review accuracy (Table 5). No agent session has run. The abstract says RQ2 is not answered and RQ1 is answered only for the evidence gate.

##### 2. Paper category under the call

The paper declares itself a technical design paper (Sect. 1.2), 15 pages. Criteria in the call's order:

- Novelty. The combination (signed rating forms, evidence status, Wilson bound, abstention) is a reasonable engineering of known parts. The abstention and Wilson ideas are standard (refs [8], [37]). The novel element is mapping benchmark review evidence into an acceptance gate. Its RE novelty is thin (see W2, W3).
- Potential impact and relevance. Relevance to the theme "Aligning RE and AI Velocity" is plausible but indirect. The paper is about validating agents with benchmark evidence. It is not about requirements elicitation, refinement or validation as the call frames the upstream bottleneck. See W2.
- Soundness. Not met in the current state. The decision for the SymPy case is fixed before any session (Sect. 4.5), the rule for removing tasks has a flaw (W4), and the requirement and acceptance rule have problems (W1).
- Verifiability. Partly met. A replication package is announced, which I could not inspect, and the engine depends on a companion paper that reviewers cannot read.
- Presentation. Dense, heavy with identifiers (B05, B14a, M3_strict, CONFIG_01...), and hard for an RE audience to follow without the companion paper.

Other categories:

- Scientific evaluation paper: not met. The main sessions (90 sessions, RQ1 and RQ2 comparisons) have not run, so the paper reports no empirical result for either research question. It would be rejected under soundness.
- Experience report: not met. There is no use in a project and no lessons from practice.
- Vision paper (8 pages): the paper does not give a roadmap and exceeds 8 pages.
- Research preview (8 pages): the content is closest to this category (well defined idea, protocol fixed, execution pending). It is 15 pages, so it would have to be cut by nearly half, and the call asks for a sound plan with limitations and risks, which the paper partly gives in Sect. 7.

Conclusion: the work fits a research preview better than a technical design paper. As submitted at 15 pages as a technical design paper, the "preliminary evaluation" consists of checks whose outcome is determined by construction, a power table, and a simulation with assumed parameters.

##### 3. Strengths

S1. The paper is candid about its status. Table 1 separates what is adopted, implemented, executed and pending. The abstract states that no agent session has run and that RQ2 is not answered. Sect. 7 lists the use of Claude models for drafts and code, one signer, and a shared scratch overlap. This is better reporting than most.

S2. The pre-commitment design (frozen manifest, hashed task order, signed forms before sessions, target tasks after training cutoffs) is a sound way to limit analysis flexibility. The target pool is described with counts and a contamination check (5 of 20 issues opened before the cutoffs, reported as a separate 15 task analysis).

S3. Separating "No decision" from "Inconclusive" (Sect. 3.2 and 6.2) is a useful idea for acceptance decisions: a missing or flawed evidence base is not the same as a statistical tie. The point that flawed tests "do not prove that the candidate agent fails" is correct.

S4. Table 4 is correct. I recomputed the Wilson bounds and the exact probabilities: 9/9 gives LB 0.7009, 8/8 gives 0.6756, 14/20 gives LB 0.481, and all rows of Table 4 match. The paper's own message that N = 14 to 20 almost never gives a definitive decision at 95% confidence is honest and useful.

S5. The executed checks (B07, B28a) are concrete and the 6 task defects are listed by identifier, so they can be examined.

##### 4. Weaknesses

**W1 (decision). The requirement and its acceptance rule are not well formed, and the paper itself shows the rule cannot be satisfied with the evidence it plans to collect.** Where: Sect. 1 (the requirement sentence), Sect. 3.2 Eq. 1, 4.2, Table 4, Sect. 5.1.
- The requirement has no stated stakeholder, source or rationale for 70% or 15 minutes. Nothing says why 70% and not 60% or 85%.
- "at least 70% of bug reports" has no defined population. Is it all future SymPy bug reports, those of a period, or those resolvable by a test? The sample is "the first 20 in hash order" from SWE-bench Verified, a filtered set that is not a sample of SymPy bug reports.
- "Working alone" and "within 15 minutes" give no resource conditions (hardware, token budget, tools, retries, random seeds). One run per task per agent hides run to run variation, and the Wilson interval treats tasks as the only source of variance.
- The oracle is "the tests the maintainers later wrote". These tests are the object of B05 and B07 criticism by the paper itself. So the requirement uses as its fit criterion exactly the thing the method calls unreliable. The target tasks use the same kind of oracle (PR tests) and are never audited for B05/B07, yet they are the "direct test" of ground truth for RQ2.
- The acceptance rule (Accept if the lower bound is at least 0.70 at 95%) means 14 of 14 at N = 14 and 19 of 20 at N = 20. Table 4 shows that an agent with true rate 0.85 is accepted in only 17.6% of cases at N = 20 and needs about N = 60 for 80% power. A requirement whose acceptance criterion needs 3 times the planned evidence is not verifiable as designed. The paper reports this (Sect. 6.2) but treats it as a finding about subsets rather than as a defect of the requirement. An RE reader would ask for the threshold and confidence to be set from stakeholder risk, and for the sample size to be derived from them before the study.
- Fix: write the requirement with a fit criterion in the usual form (scale, meter, population, conditions, minimum/target levels, stakeholder), justify θ and α, derive N from a power requirement, and state how tasks are drawn from the bug report population.

**W2 (decision). The link to RE theory and to prior RE work is weak, and the RE contribution is shallow.** Where: Sect. 1, 2.2, 6.
- The related work is about AI benchmarks, assurance cases and statistics. RE work is limited to Berry [5], a mapping study on RE for AI [11], and a quality model [17]. There is nothing on requirement quality and fit criteria (for example Volere, Planguage, ISO/IEC/IEEE 29148 verifiability), on requirements validation and acceptance testing, on traceability research, on NFR specification for ML, or on RE for ML performance requirements (thresholds on metrics). The claim "for an AI, such measures and their thresholds are in effect its requirements specification [5]" is used as a premise but not developed.
- The paper never says what RE activity it supports. Is it requirements validation (is the requirement met), acceptance, or verification of a requirement against evidence? The method takes a finished requirement as given. It does not help someone write, refine or negotiate it.
- Much of the contribution is benchmark meta-evaluation (B05, B07, B28a checks on SWE-bench), which belongs to ML/SE evaluation venues. The RE parts (the requirement sentence, the transfer justification, signing) are thin. The "transfer justification" is the one place where RE judgment enters, and it is an author signed record that the engine checks only for existence and scope match (Sect. 3.2 and 7). So the human RE decision is the part that is not supported.
- Fix: position the work in RE literature on verifiability, fit criteria, evidence and traceability. State which requirement validation problem is solved and how the engineer's decisions are supported or recorded.

**W3 (decision). A requirements engineer could not use the method as described, and the paper rests on an unavailable companion paper.** Where: Sect. 2.1, 3, Table 2, Sect. 4.3.
- The method needs the MESA rubric (39 criteria, six levels, rating fields), defined only in the companion submission [3]. Within this paper the criteria are named by codes (B05, B14a ...) with one line each in Table 2. A reader cannot tell what "Documented" versus "Verified" requires in practice, how a form is filled, or what a "detection limit" is.
- Producing the forms needs executable work (exploit patches, runner hijack patches, container inspection) beyond the usual skills of a requirements engineer, and the forms were drafted by an LLM and then edited (34 field edits). No cost, time, or effort figure is given. No guidance says how to choose the criteria profile or the policy (strict versus lenient) for a different requirement.
- The method is shown on one repository, one benchmark, one author, for a case where the result (No decision) is predetermined. There is no evidence that a practitioner can apply it or that it changes a decision.
- Fix: make the paper self contained for the needed criteria, give a worked procedure for an engineer (inputs, steps, effort), and show it with at least one user other than the author.

**W4 (decision). The task removal rule changes the requirement being tested and introduces selection bias; the B07 rating is internally inconsistent.** Where: Sect. 3.2 Level 3, 4.3 (B07 check), Table 3.
- Tasks with a located B05/B07 defect are removed before scoring. The requirement is about 70% of bug reports. Removing 6 of 20 tasks leaves a different population (tasks whose tests are well specified), and the paper does not say the removal is neutral. Target tasks are not filtered in the same way, so the source decision and the target direct test measure different things. This undermines RQ2 even if sessions run.
- The B07 check found a passing exploit on 17 of 20 tasks. Only 6 are counted as defects because the behavior is stated in the issue text; the other 11 are "set aside". The signed B07 form then rates B07 "Verified, passed" on the remaining 14 tasks, but 11 of those 14 have a demonstrated cheating patch. A rating of "passed" on tasks where the exploit was shown is hard to defend. The reason given ("inferred solely from the reference fix") is a judgment about the issue text that the paper does not validate, for example by a second rater. Runs A and B "identify the same 6", but both runs are by the same model.
- The abstract says "executed checks found cheating patches passing hidden tests on 17/20 source tasks" and then reports 6 as defects. A reader can take 17 as the rate of defective tasks. The wording should separate "exploit exists" (17) from "task defect by the paper's rule" (6).
- Fix: justify the removal rule against the requirement's population, apply the same audit to target tasks, and rate B07 so that the form does not say "passed" where exploits were shown. Add a second human rater and report agreement.

**W5 (decision). The evidence gate returns "No decision" by construction on any SWE-bench Verified evidence, so the main empirical result is not informative about the method.** Where: Abstract, Sect. 3.2, 4.5, Table 3, Sect. 7.
- B28a is a release wide property (the grading harness) and B14a is a property of the public benchmark. Both are "failed" before any session. So both MESA policies withhold whatever the agents do (the abstract admits "withholds on this benchmark whatever the agents do"). A gate that rejects every public benchmark cannot be said to be validated by one application where it does so.
- The gate treats the harness vulnerability as blocking, while the study itself defines a session validity rule (Sect. 4.4) that would mark a hijacking session invalid, and Sect. 7 says the gate "does not credit" that rule. For a requirement that says "working alone ... changes the code so that the tests pass", a hijack of the runner is a violation the requirement can exclude. So the blocking reason is a mismatch between the requirement and the criterion, not a defect of the evidence. A requirements engineer would say the criterion should follow from the requirement. The paper leaves this to an "amendment".
- The comparison across six outputs is therefore one sided: five methods give a number, MESA gives nothing. Without sessions, nobody can say whether withholding was right.
- Fix: run the sessions or reframe the paper as a research preview; show a second case where the gate returns Admissible and a decision, to show that the engine can discriminate.

**W6 (decision). The evaluation does not support the claims of the abstract and contribution list.** Where: Abstract, Sect. 4, 5, 8.
- Contribution (3) is a protocol, not a result. RQ1 and RQ2 are not answered. The paper's stated research questions therefore have no answer, and the preliminary evaluation (executed checks, power table, simulation) does not test the method's usefulness.
- Table 5 is a simulation under assumed review accuracy (85% detection, 5% false alarm, 10% missing documentation) that the paper itself says is "not evidence about real reviews". Most of the false acceptance reduction comes from abstaining. The advantage over random abstention at equal coverage is "about one percentage point", and false rejection for a compliant agent rises from 0.44% to 1.42%. So the simulation shows no clear benefit over a trivial baseline.
- The abstract's headline numbers (17/20, 9/9) come from patches written by an LLM that was told to omit parts of the fix, or to modify test runner scripts. That the official harness accepts a patch editing the test runner is a security finding about the harness, not a measure of agent behavior. The count "9 of 9" is 3 tasks times 3 patches, written by one model; it is not 9 independent trials.
- Fix: align the claims with what was done; present the paper as a design plus protocol; drop the headline numbers from the abstract's results or explain what they measure.

**W7 (minor). Fit with the special theme is argued only in the title of Sect. 6.** The paper does not show how the method speeds RE or keeps alignment under AI velocity. Cost per review, time to produce forms, and how a team would use "No decision" to move on are not discussed. Sect. 6 repeats results and two short points.

**W8 (minor). Reliance on LLMs for preparation and a single human signer.** All forms were drafted by Claude Sonnet 5.5, the engine and the requirement and transfer justification were drafted by Claude Opus 5.5, and one author signed everything. Sect. 7 admits this. Raters and exploit generator are the same model family, which limits independence. The same model also assisted in writing the manuscript. This is handled openly but weakens "signed review records" as evidence. A second human reviewer is needed.

**W9 (minor). Terminology.** "Requirement decisions" (title), "score decision", "source decision", "target requirement decision" D_req, "evidence status" and "admissibility" are used in overlapping ways. "Inquiry Required" is an evidence status, while "Inconclusive" and "No decision" are score decisions; the reader must hold four sets of labels. "Review" (MESA review) and "audit" are separated in RQ1 without a definition. "Nine forms" includes the ABC form, which is not a MESA form, while the abstract says "all nine forms".

**W10 (minor). Presentation for the REFSQ audience.** Identifiers such as B14a, M3_withheld, CONFIG_02_SOL_MED, and file names fill Tables 1 to 3. The paper would be easier to read with a running example of one form and one engine output. The task illustration (sympy-18199) is the only worked example.

**W11 (minor). Unsupported or loosely supported statements.** (a) "teams frequently substitute public benchmark scores ... as fast acceptance evidence [13,29]": [13] is a literature review of LLMs for SE and [29] is about leaderboard bias; neither shows teams use them as acceptance evidence. (b) "Among existing methods, none has evaluated ..." (Gaps 1 and 2) is a universal negative claim from a short search; the paper does not describe the search. (c) "the 2026 audit's 59.4% flaw rate on 138 tasks" is cited via [25], a company blog page; I could not check it. (d) The comparison with ABA says MESA "removes 5 additional tasks that ABA did not flag", but ABA also flags sympy-13031, which MESA keeps; this difference is not discussed.

##### 5. Questions for the authors

Q1. Who is the stakeholder for the requirement, and where do 70%, 95% and 15 minutes come from? If a different θ or α were chosen, would the conclusion on admissibility change?

Q2. Why is the requirement's population "SymPy bug reports" when source tasks are a hash ordered sample of a filtered benchmark? What would make removal of the 6 defective tasks neutral for the 70% claim?

Q3. For the 11 tasks with a demonstrated passing exploit that you "set aside", why is the B07 form "Verified, passed"? What would a "failed" B07 rating look like, and would the policy outcome differ?

Q4. Are the target tasks audited for B05 and B07? If not, how can their PR tests serve as ground truth for RQ2?

Q5. If the session validity rule (Sect. 4.4) excludes hijacking sessions, why should B28a still block the decision for this requirement? Can the requirement be rewritten so the criterion follows from it?

Q6. Can you show one case (another repository or benchmark) where the engine returns Admissible and an Accept or Reject decision? Without it, what shows the engine does not simply reject all public benchmarks?

Q7. What effort did a review take (hours, tokens, human edits), and could a practitioner without the companion paper fill the forms?

Q8. What do you expect from the planned sessions that would change the paper's conclusion? If every plausible result still ends in "No decision", what is the research question?

Q9. Which parts of the contribution are in this paper and which in the companion paper [3]? Could a reader judge this paper without [3]?

##### 6. Checks I made

Arithmetic and counts (recomputed with Python):
- Wilson bounds: 9/9 gives LB 0.7009 (paper: 0.701), 8/8 gives 0.6756 (paper: 0.676), 14/20 gives LB 0.4810 (paper: 0.481). Correct. So n_min = 9 follows.
- Table 4: all cut points (14/6, 14/7, 17/8, 19/9, 26/16, 38/25, 49/35, 72/54, 94/74) and all Accept, Reject and Inconclusive percentages match my exact binomial calculation. The "Inconclusive" column equals 100% minus Accept minus Reject, where the Reject share at p = 0.75 (for example 1.0% at N = 14) is small and not shown; the column heads show only Accept for p = 0.75 and Reject for p = 0.65, 0.85 is dropped (0.0%). Fine. N = 62 gives 78.8% at p = 0.85 (paper: 78.8%), and N = 60 gives 81.9%. Correct.
- The abstract says "Accept 14/14; Reject at most 6/14" for N = 14 and "Accept at least 19/20; Reject at most 9/20; 97.2% Inconclusive at p = 0.75". The 97.2% value is the same for N = 14 and N = 20 in Table 4, so the abstract's placement next to N = 20 is correct but ambiguous.
- ABC counts: 8 met + 9 not met + 10 not applicable + 6 unknown = 33 items; 9 + 6 = 15 caveats; part scores 5/8 + 2/11 + 1/4 = 8 met out of 23 applicable items. All consistent with the text.
- Forms: eight MESA forms are 6 single forms (B05, B07, B12, B14a, B28a, B28b) plus 2 B14b forms (one per agent) = 8; plus ABC = 9. Consistent, but "nine forms" mixes MESA and ABC (W9).
- Sessions: 2 + 40 + 40 + up to 8 = 90. Consistent.
- 17 of 20 exploit passes, 6 defects, 11 set aside, 14 retained: 6 + 14 = 20, and 17 − 6 = 11. Consistent. But 11 of the 14 retained tasks carry a shown exploit (W4).
- ABA: 20 − 2 = 18; MESA removes 6, of which 1 overlaps with ABA, so 5 are additional (consistent), and ABA flags 13031 which MESA keeps (not discussed).
- Target pool: 322 merged pull requests, 108 pass the filter, first 20 checked all pass; 5 of 20 have older issues, so 15 remain. Consistent. Intro says tasks merged "between 13 June and 5 November 2026", Sect. 4.2 says pool window starts 1 May; the intro gives the range of the selected tasks, which is consistent.
- The text says the 2026 audit flagged a "59.4% flaw rate on 138 tasks"; not checked (blog source).

Terms used inconsistently: see W9. "Requirement decision", "source decision", "score decision" and "withheld" overlap. "Review" and "audit" are used for different things without a definition. "Cheating patch" (abstract) versus "exploit patch" (text) versus "mechanical pass".

Claims without support: W11 items (a) to (d). The statement that "none provides an executable gate" is a universal claim from an undescribed search.

Simulation (Sect. 5.2, Table 5): I could not rerun it (no scripts). The text mentions Δ = 0 and "d = 0.30, Δ = 0" results (0.44% and 1.42%) that are not in Table 5, which lists only Δ of −0.15 and −0.05, though the text sets Δ ∈ {−0.15, −0.05, 0}. The "mean reduction across 100 seeds" figures (0.88 and 1.14 points) are consistent with the table differences at d = 0.30, Δ = −0.15 (6.4 − 5.4 = 1.0, 6.5 − 5.4 = 1.1), within the stated spread.

References:
- Spot checked by search: Zhu et al. (ABC, NeurIPS 2025) exists with the title "Establishing Best Practices in Building Rigorous Agentic Benchmarks" (matches). Hou et al. (TOSEM 2024) exists; the DOI given (10.1145/3689498) did not appear in my search and I believe the published DOI is different (10.1145/3695988); please check. The paper's references to Kane 2013, Wilson 1927, Brown et al. 2001, Newcombe 1998, El-Yaniv and Wiener 2010, Berry 2022 look correct to me.
- Many references are 2026 arXiv preprints (for example [2], [7], [9], [10], [20], [21], [32], [33], [34]), and two are company web pages ([24], [25]) plus one METR note [36]. I could not confirm these, and the paper depends on them for the gaps and for the key premise on B05 (sympy-18199 and the 59.4% rate). Reference [2] has no URL or DOI. Reference [3] is given as "Author(s), A." rather than the call's "A. Anonymous" placeholder (minor).
- I did not find signs of many hallucinated references, but the ones I could not check carry the paper's gap claims.

Rule violations:
- Page limit: 15 pages including references; fits the technical design limit. It would exceed a research preview limit of 8.
- Abstract: four paragraphs with the required headings (Context and motivation; Question/problem; Principal ideas/results; Contribution). It is very dense with numbers and identifiers.
- Keywords present.
- Anonymity: no author names or affiliations; own companion work is cited in third person form. Text says "the author" and "one author" (fine). The placeholder contact line is allowed.
- Data Availability Statement: present, at the end. It describes the package but gives no link or warning text; sharing is not mandatory.
- Companion submission: the call states no policy; the paper's central rubric is defined in [3], which reviewers cannot see (W3).
- Use of generative AI is disclosed in Sect. 7 (Claude models for forms, code, drafting requirement and editing the manuscript); the call asks authors to follow Springer's policy and recommends LLM guidelines. The paper does not say whether it follows them.

##### 7. Score

**Reject**

##### 8. Reviewer confidence

Medium: I am confident about the RE issues (requirement form, acceptance rule, theory link) and the arithmetic, which I recomputed, but I could not inspect the replication package, the companion paper, or most 2026 references.

##### 9. Recommendation

I would not accept the paper exactly as submitted. As a technical design paper it lacks a sound evaluation: the two research questions are not answered, the one decision it reports (No decision) is fixed by two benchmark wide failures before any session, the simulation uses assumed parameters and shows little gain over random abstention, and the requirement at the center is not well formed (undefined population, unjustified threshold, oracle that the method itself doubts, and an acceptance rule that needs about three times the planned evidence). The link to RE theory is weak and an engineer could not apply the method without the companion paper. The smallest set of changes to move me up one step (to weak reject): (1) re-categorize as a research preview or cut the paper to fit that frame, and remove claims of results that the evidence does not support (W6); (2) rewrite the requirement with a stakeholder, a justified θ and α, a defined population and conditions, and derive the sample size from the acceptance rule (W1); (3) fix the B07 rating and the removal rule, and audit the target tasks the same way (W4). To reach borderline or higher, the sessions would also need to run, with at least one case where the gate returns a decision, and the paper would need to ground itself in RE literature on verifiability, fit criteria and validation (W2, W5).

---

### Paper 2: reviewer for empirical methods

#### Review of REFSQ 2027 submission: "Applying Meta-Evaluation Benchmark Reviews to Requirement Decisions: An Executable Method"

Reviewer role: researcher in empirical methods for software engineering. Files read: the call summary, paper2.pdf (all 15 pages) and paper2.txt. Web search was used only to check a few references.

##### 1. Summary of the paper

The paper takes a rubric for reviewing benchmarks (MESA, described in a companion submission) and turns part of it into a decision engine for one requirement: a coding agent resolves at least 70% of SymPy bug reports within 15 minutes, judged with a 95% Wilson interval. The engine has three levels. Level 1 checks input integrity (hashes, scopes). Level 2 sets an evidence status (Admissible, Inquiry Required, Inadmissible) from rating forms for seven MESA criteria. Level 3 removes tasks found defective by B05 (overbroad tests) and B07 (exploitable tests), computes the Wilson interval on the rest, and returns Accept, Reject or Inconclusive. If evidence is not Admissible, or no transfer justification is signed, the output is "No decision".

The planned study has two agents, 20 SWE-bench Verified SymPy source tasks and 20 SymPy pull requests merged after the model cutoffs as target tasks (at most 90 sessions). Five method families give six outputs: raw resolve rate (M2), an executed B05/B07 task audit (audit_only), the published ABA audit, MESA strict, MESA lenient, and the ABC checklist. RQ1 asks how reviewing with MESA or ABC, beyond an automated audit, changes the decision. RQ2 asks whether decisions from reviewed source tasks agree with a direct test on the target tasks.

What the paper shows is limited to work done before any agent session:
- Claude Sonnet 5.5 wrote patches that passed the hidden tests but failed an independent check on 17 of 20 source tasks. Six of these are counted as task defects.
- 9 of 9 patches that edited only the test runner were scored as resolved.
- Nine forms were signed by one author. Both MESA policies are Inadmissible, so the output is "No decision".
- An exact power table and a Monte Carlo simulation with assumed review accuracy.

No agent session has run. The authors say RQ2 is not answered and RQ1 is answered only for the evidence gate.

##### 2. Paper category under the call

The paper labels itself a technical design paper (Section 1.2). I take the categories in the order the call gives them.

**Technical design (15 pages).** Criteria in order: novelty, potential impact and relevance, soundness, verifiability, presentation.
- Novelty is modest. The pieces are a rubric (from the companion paper), hash checks, a Wilson interval and an abstain rule. The combination for benchmark evidence is new, but the engine is small and the transfer step is a formal check that a signed record exists (Eq. 2).
- Relevance to the theme is acceptable (benchmarks and evaluation for RE at AI speed). The RE content is thin: the requirement is one sentence, and no requirements engineering practice or practitioner is studied.
- Soundness is the problem. A "preliminary evaluation" for a design paper should show the artifact working. Here the only executed result is that the gate withholds, and that result does not depend on any agent data (W1). The simulation is built on assumed parameters.
- Verifiability is partly met. There is a Data Availability Statement and many checks are scripted. Core judgments come from a language model and one signer (W5).
- Presentation is dense. Output codes, B numbers and the companion paper are needed to follow it.

**Scientific evaluation (15 pages).** Soundness comes first and the call points to the SIGSOFT Empirical Standards. Both research questions are unanswered because the main sessions have not run. A study whose data collection has not happened cannot meet this category. As submitted it would be rejected here.

**Experience report (12 pages) and vision (8 pages).** Neither fits. There are no lessons from practice and no roadmap argument.

**Research preview (8 pages).** This fits best: an early stage, well defined study plan with some executed groundwork. The criteria are novelty, soundness of the research plan including limitations and risks, potential for discussion, and presentation. The plan as written has serious design flaws (W1 to W4), so it would need a revised plan. It would also need to be cut by about half. This is the only category where I could see acceptance, and only after revision.

##### 3. Strengths

- S1. The paper states plainly that no session has run, that RQ2 is unanswered and that RQ1 is answered only for the gate (abstract, Section 7). This is rare and I credit it.
- S2. The exact binomial calculations are correct. I recomputed every Wilson cut point and every cell of Table 4 (Section 6 below). The paper also reports that power is not monotone in N (78.8% at N=62).
- S3. The separation of "No decision" (evidence defect) from "Inconclusive" (statistical) is a clear idea. The reason given (Section 3.2, "flawed tests or missing checks do not prove that the candidate agent fails") is sound.
- S4. Source and target tasks are drawn by a fixed hash order (Section 4.2). The counts for the target pool (322, 108, 20) are given. The paper reports that 5 of the 20 target issues were opened before the training cutoffs and plans a separate N=15 analysis.
- S5. Task removal by B05/B07 is defined to happen before any model score is inspected (Section 3.2, Level 3). This avoids choosing tasks after seeing results.
- S6. The roles of the language models are disclosed in detail (Section 7): who generated exploit patches, forms and ABC answers, who wrote the engine, who signed. The shared scratch overlap and the 34 edits are also reported.
- S7. The B28a finding (a patch that edits only test runner scripts is scored as resolved) is concrete and checkable.
- S8. A Data Availability Statement is present and lists specific contents.

##### 4. Weaknesses

**W1 (decision). RQ1 is answered by construction, and RQ2 cannot be answered with this design.** Where: abstract, Sections 1.1, 4.5, 7, Table 3.
- The gate depends on forms, not on agent data. B28a is rated "failed" for the whole SWE-bench release and B14a is "failed" from published audits. Both MESA policies therefore return "No decision" for any agent result on this benchmark. The paper admits this ("withholds on this benchmark whatever the agents do"). A gate that cannot return Admissible on the benchmark under test has no demonstrated discrimination. There is no positive control (a benchmark or case where the engine is expected to return Accept or Reject) and no test of whether the engine ever ends a case as Admissible.
- Several outputs are not distinct. M2 and ABC use the same 20 tasks and the same cut points, so they give identical decisions. audit_only and M3_withheld are identical by definition. M3_strict and M3_lenient are both fixed at "No decision". Of six outputs, three differ in practice: M2/ABC, audit_only, ABA.
- RQ2 reduces to at most 2 agents times 3 or 4 comparisons, with no agreement measure, no success criterion and no rule for agreement when both sides are "Inconclusive". With N=15 to 20 on both sides, both decisions will almost always be Inconclusive (Table 4: 90 to 97% at p=0.75), so "agreement" will be uninformative.
- Fix: state an agreement measure and what result would count for or against MESA before the sessions run. Add a case where the gate can pass. Or reduce the claim to "a protocol and a demonstration that the gate withholds".

**W2 (decision). The study is underpowered by the paper's own Table 4, and the design choices that cause this are not justified.** Where: Sections 4.1, 4.2, 5.1, Table 4.
- At N=14 an Accept needs 14 of 14 (power 1.8% at p=0.75 and 10.3% at p=0.85). At N=20 it needs 19 of 20 (2.4% and 17.6%). The paper reaches more than 80% power only at N=60 and p=0.85, a 15 point margin.
- For p=0.75 power never gets high: about 15 to 16% at N=75 or 90, 23% at N=120, and under 61% even at N near 390. This follows from using the Wilson lower bound against a threshold only 5 points below the true rate. The requirement as a rule therefore cannot certify an agent that is modestly compliant, on any benchmark of realistic size.
- Only 20 of the 75 SymPy tasks are used (Section 4.2). Running all 75 costs 150 source sessions instead of 40. After removing about 30% defective tasks (6 of 20 in this sample), N would be about 52 and power at p=0.85 about 75%, still short of 80%. The budget and the use of 20 tasks are what make the study uninformative. No reason is given.
- The 95% two sided Wilson interval is used as a one sided test in both directions. Accept at LB at or above 0.70 corresponds to one sided 97.5% confidence, not 95%. The requirement text says "95% confidence".
- Fix: compute N from a stated smallest effect of interest and target power before choosing 20 tasks. Use all 75 source tasks or justify the cap. State the one sided or two sided choice. Consider an estimation goal (interval width) instead of a three way decision.

**W3 (decision). The comparison confounds the review content with the decision rule, and the comparators are weak or not independent.** Where: Section 3.4, Table 3, Section 4.5.
- MESA is run with a gate that withholds, while ABC is run without any gate ("without withholding the score decision"). Any difference in RQ1 between MESA and ABC then comes from the gate, not from the review framework. An ABC arm with the same gate rule (for example, withhold when any applicable item fails) and a MESA arm without the gate are needed.
- "audit_only" is the authors' own executed B05/B07 check, written by Claude. It is not an automated audit such as BenchGuard, ABA or BenchJack, yet RQ1 asks about change "beyond an automated audit". Only the published ABA result is an independent audit. BenchGuard and BenchJack are not run.
- The ABC session "read the MESA rating rules before answering" (Section 7). This gives ABC knowledge of the competing method and breaks independence.
- There is no ground truth for which tasks are defective. The paper says MESA "removes 5 additional tasks that ABA did not flag" (Section 4.3), which is a count and not evidence that the extra removals are right. ABA flags -13031 as major and the MESA check does not remove it. The disagreement is not examined.
- Fix: add the missing arms, run at least one independent automated audit, and explain the ABA disagreement.

**W4 (decision). The "clean task" claim contradicts the paper's own B07 result, and the removal rule differs from the stated requirement.** Where: Sections 1, 4.3, Table 3, abstract.
- The B07 check found a patch that passes the hidden tests while failing the independent check on 17 of 20 tasks. Only 6 are removed, because their omitted behaviour is stated in the issue. The other 11 tasks are "set aside". The 14 retained tasks include those 11, so 11 of 14 retained tasks accept a wrong patch by the authors' own test. Only 3 of 20 had no exploit. Yet the signed B07 form is "Verified, passed on the remaining 14 tasks", and Section 3.2 calls them "clean tasks". By the question in Table 2 ("Does scoring accept wrong solutions?") B07 did not pass. The resolve rate on the 14 is still inflated.
- The requirement is "the tests the maintainers later wrote for that bug pass". Under that wording the hidden tests define success, so an overbroad test (B05) is not a defect of the task relative to the requirement. Removing such tasks changes the population the requirement refers to, and the target test keeps them. This construct problem is not discussed.
- The B05 check was executed on one task (18199) only. For the other 19 the check ran the reference fix, which cannot detect an overbroad test. "Verified, passed" is overstated. The cited rate (59.4% on 138 tasks) comes from an audit of problems that o3 did not consistently solve (I checked the OpenAI page), so it is a hard subset rate, not an estimate for SymPy.
- The target tasks are not audited for B05 or B07 at all. If the source defect rate (6 of 20, or 17 of 20 exploitable) holds for the target tasks, the "direct test" is as unreliable as the source evidence.
- Fix: relabel the retained set, rerun or report B07 consequences for the 11 tasks, state which definition of success the requirement uses, and run B05/B07 on the target tasks.

**W5 (decision). The review records come from one language model and one human signer, with no reliability evidence, and the contaminated run was the one signed.** Where: Sections 4.3, 7.
- Claude Sonnet 5.5 wrote the exploit patches, the independent tests that decide "failed", the form drafts and the ABC answers. It saw the reference fix. The independent tests were not shown to be valid by any other means.
- "Both rating runs A and B identify the same 6 tasks" is agreement of the same model with the same prompt. It is not inter rater reliability. No agreement statistic or second human rater is reported.
- Five form sessions in run A shared a scratch folder, so run A may be contaminated. The signed forms come from run A, with 34 edits, while run B was clean. The paper gives no reason for signing run A and does not say what the 34 edits changed or whether any changed a rating or a removed task.
- The model family overlap is stated: Claude Opus 5.5 built the engine, drafted the requirement and the transfer justification and helped edit the manuscript. One author signed all records, so the signer is also the designer. The Level 2 rule asks that "author and model roles are recorded" but nothing checks them.
- The call recommends the LLM Guidelines Initiative. The prompts, model versions, sampling settings and number of repeats are not in the paper.
- Fix: put the prompts and the diff of the 34 edits in the paper or its package, report agreement with a second human rater on at least the B07 task defect labels, and explain why run A was signed.

**W6 (decision). Pre commitment is claimed but has not happened, and the analysis plan is incomplete.** Where: abstract (contribution 3), Sections 4.1, 4.5, Table 1.
- Table 1 lists the frozen manifest, phase authorizations and sessions as "pending after protocol freeze". The freeze has not been made. "Fixed before any agent session" is a promise, with no public timestamp or registration cited.
- The expected results of the main analysis are already written ("Known Pre Session Outcomes"), based on checks that were run before the plan was fixed. The lenient policy, which keeps B28a, was therefore chosen with the B28a result known. The Limitations (Section 7) mention a "protocol amendment" to credit the session validity rule. That amendment would be made after the withheld results are known, which is the situation pre commitment is meant to prevent.
- Missing from the plan: the agreement metric (W1), how two agents are combined, what is done when sessions are invalid beyond counting them unresolved, and the stopping rule for the reserve slots.
- Fix: deposit the manifest with a time stamp (for example a registered report or an archived commit) before submission, and complete the analysis plan.

**W7 (decision). The simulation does not support the claim and does not match the study.** Where: Section 5.2, Table 5.
- The metric is "false acceptance per case", counted over all trials. Always withholding gives 0%, so the metric rewards abstaining. The paper concedes "most of the reduction comes from abstaining". Dividing by coverage shows the problem: among issued decisions, 20.8/22.4 = 93% are false accepts under M2, 5.4/6.8 = 79% under M3, 94% under Random and 96% under Proximity. Four of five definitive decisions under M3 are still wrong.
- Every row of Table 5 has a target agent below the threshold (Δ of −0.15 or −0.05 from a base of 0.72). There is no row with a compliant agent, no sensitivity (probability of Accept when the agent is compliant) and no risk coverage curve. The text mentions Δ=0 results (false rejection 0.44% against 1.42%), but the table has no Δ=0 rows and no false rejection column, although Section 5.2 lists Δ=0 among the scenarios. A simple check shows a compliant agent with p=0.72 at N=30 gets an Accept 5% of the time.
- The gain over Random is "about one percentage point" (0.88 and 1.14), and it depends on assumed 85% detection, 5% false alarm and 10% missing documentation. These are not varied, and nothing in the executed work estimates them. The inflation to 0.86 is also assumed.
- The simulation uses N=30 and a benchmark wide defect indicator. The engine, as described, removes individual tasks and the case has N=14 to 20. The simulation does not model task removal, so it does not test the Level 3 rule.
- As a rough check, I computed the M2 false acceptance rate in a simple model (defective benchmark with p=0.86 else 0.72, Accept needs 26 of 30). I got 10.3%, 15.7% and 21.1% for d=0.10, 0.20, 0.30, close to the reported values for d=0.10 and 0.30. At d=0.20 the paper reports 16.9% and 15.5% for the two Δ rows, which my model puts at the same value, so part of that gap may be simulation noise or an unstated detail. The simulation setup is not described well enough to reproduce.
- Fix: model task level removal at the empirical N, vary the review accuracy parameters, report both error types and a risk coverage curve, and compare with the trivial rule "require N of at least X and the full Wilson bound".

**W8 (minor, borderline decision). The selection of agents and the session design limit what can be said.** Where: Sections 4.1, 4.4.
- Two closed models are each paired with a different vendor tool (Antigravity, Codex), so model and harness effects are confounded. Reasoning effort is fixed at "medium". There is one run per agent and task, with no repeats, so run to run variation is not estimated. For a threshold at 70%, the variation at N=20 matters.
- Isolation is checked in scratch runs only, and for real sessions "from the recorded transcripts" after the fact. Network and test file access during the sessions rests on tool flags. Invalid sessions count as unresolved, which biases results down.
- Model cutoffs are the vendors' stated dates. Five target issues predate them (S4 mitigates this); more subtle exposure (similar earlier fixes in the repository history, discussions of the fix before the pull request) is not addressed.
- The target pool uses "the first 20 checked in deterministic order" without naming the order. The pilot task and the "rehearsal task" (21930) are described in different places and it is unclear whether they are the same.
- Fix: say why these two agents, pin tool versions, add repeats for at least a subset, and name the ordering and labels.

**W9 (minor). The 9 of 9 and 17 of 20 figures are presented as rates but are existence demonstrations.** Where: abstract, Sections 4.3, 6.1, 8.
- Patches were written by a model that was told what to attack, and for B07 had the reference fix. "Succeeding in 9/9 attempts" says the weakness exists (three layouts, nine patches built to succeed). It is not a success rate that real agents would reach. The wording "hijacks succeeding in 9/9 attempts" in the abstract should say this.

**W10 (minor). Evidence status rules are not fully consistent.** Where: Sections 3.2, 4.3.
- Level 2 sets Inadmissible when the outcome is failed, "the defect cites a verified location, and a counterexample patch, where the defect rests on one, was executed". B14a is rated "Verified, failed" from published audits and not from an executed check. The paper does not say whether this meets the rule, or what "Verified" means when the check kind is "reported". B14b is "Documented, not performed" although the target tasks (RQ2) are an executed contamination test of exactly that kind.
- The six rating levels are listed but not defined in this paper, and the criteria are only named in Table 2. The reader must trust the companion paper, which is under review and not available.

**W11 (minor). Claims about practice and about the literature are not supported.** Where: Section 1.
- "Teams frequently substitute public benchmark scores ... as fast acceptance evidence" cites a literature review [13] and a leaderboard paper [29], neither of which studies team behaviour. The "none provides" statements for Gap 1 and Gap 2 rest on a short related work section and are stated as facts.

##### 5. Questions for the authors

- Q1. What result in the planned sessions would count as evidence against MESA? If the answer is "none, since the gate withholds", what does RQ1 test?
- Q2. Why 20 of 75 SymPy source tasks, given Table 4? What N and effect size did you aim for?
- Q3. In the B07 check, what do the 11 set aside tasks mean for the claim that 14 tasks are clean? What would the resolve rate look like if they were also removed?
- Q4. Which of the 34 edits to run A changed a rating, a verdict or a task list? Why was run A signed rather than the clean run B?
- Q5. How were the independent tests used in B07 validated? Did a human check them for at least a sample of tasks?
- Q6. Under the requirement as worded ("tests the maintainers wrote"), why is an overbroad test a defect?
- Q7. Can the manifest be made public before the sessions run, with a verifiable time stamp?
- Q8. What does the ABC arm give if it is also gated? Why was ABC given the MESA rules to read?
- Q9. Can the Table 5 simulation be rerun with N=14 to 20, task level removal, varied review accuracy, and with a compliant agent and the true acceptance rate?
- Q10. How is the "first 20 in deterministic order" defined for the target pool, and are the pilot task and the rehearsal task the same?
- Q11. Is the statistical decision meant as a one sided test at 95% or at 97.5%?

##### 6. Checks made

**Wilson cut points (Eq. 1, z=1.95996, theta=0.70), recomputed in Python:**

| N | Accept at or above | Reject at or below | Paper | Result |
|---|---|---|---|---|
| 9 | 9 (LB 0.701) | 3 | LB 0.701 for 9/9 | matches |
| 8 | none (8/8 gives 0.676) | 3 | LB 0.676 for 8/8 | matches |
| 14 | 14 | 6 | 14; 6 | matches |
| 15 | 14 | 7 | 14; 7 | matches |
| 18 | 17 | 8 | 17; 8 | matches |
| 20 | 19 | 9 | 19; 9 | matches |
| 30 | 26 | 16 | 26; 16 | matches |
| 45 | 38 | 25 | 38; 25 | matches |
| 60 | 49 | 35 | 49; 35 | matches |
| 90 | 72 | 54 | 72; 54 | matches |
| 120 | 94 | 74 | 94; 74 | matches |

Also: 14/20 gives LB 0.481 (paper 0.481). The abstract's "97.2% Inconclusive at p=0.75" for N=20 is correct.

**Power table (Table 4), exact binomial.** I recomputed all rows, not only four. Examples:
- N=14, p=0.75: Accept 1.8%, Inconclusive 97.2% (the remaining 1.0% is Reject, not shown). Matches.
- N=20, p=0.65: Reject 5.3%, Inconclusive 94.5%. Matches.
- N=30, p=0.85: Accept 52.4%, Inconclusive 47.5%. Matches.
- N=60, p=0.85: Accept 81.9%, Inconclusive 18.1%. Matches.
- N=120, p=0.75: Accept 23.3%, Inconclusive 76.6%. Matches.
- N=62, p=0.85: 78.8% (text). Matches. First N above 80% is 60, but power falls to 78.8% at N=62 and 77.1% at N=63 (and below 80% again at 68), so the claim is true for N=60 and the threshold is not crossed stably.

Notes on Table 4: the "Inconclusive" column includes the opposite tail (a small Reject or Accept mass), which is not shown, and the table shows Accept for p=0.75 and 0.85 but Reject for 0.65. This is a presentation point. Only three true rates are used, and none near the threshold other than 0.75 and 0.65.

**Counts across abstract, text and tables.**
- 17 of 20 exploitable, 6 task defects, 11 set aside, 14 retained: 17−6=11 and 20−6=14. Consistent. 3 tasks had no exploit.
- 18199 is a B05 and a B07 defect, so "6 B05/B07 defective tasks" is 6. ABA flags 13031 and 18199, so MESA removes 5 more than ABA. Union of the two lists would be 7. Consistent.
- Sessions: 2 pilot + 40 source + 40 target + 8 reserve = 90. Consistent.
- Forms: 8 MESA (B05, B07, B12, B14a, B28a, B28b, plus B14b twice) + 1 ABC = 9. Consistent.
- ABC: 8 met + 9 not met + 10 not applicable + 6 unknown = 33. The 15 caveats are 9 + 6. The part scores 5/8, 2/11 and 1/4 sum to 8 met of 23 applicable items (33−10). Consistent.
- Target pool: 322 merged, 108 pass the filter, first 20 taken. Window "1 May to 5 November" in 4.2 and "13 June to 5 November" in the introduction describe the pool and the 20 chosen. Consistent. Five issues predate the cutoffs, so 15 remain. Consistent.
- Table 3 and Section 4.5 agree on blocking criteria (strict: B14a and B28a failed, B12 and B14b inquiry; lenient: B28a failed).

**Terms used inconsistently.** "Pilot task" and "rehearsal task" (Section 4.2, Table 1). "Clean tasks" versus the B07 outcome (W4). "Audit" for an author run check versus automated audit (W3). "Method 1" is mentioned and then dropped. "Table 3" in the abstract ("five method families") counts MESA as one family with two policies; fine.

**Claims without support.** Team practice (W11); "none provides" statements; the lenient and strict policies "to show the decision when uncertainty reporting and exposure are set aside" without an executed case where the lenient policy passes; the transfer justification is not checked for content (acknowledged).

**References.**
- Checked and consistent: SWE-bench, SWE-bench+, SWE-rebench, SWE-Bench Illusion, BetterBench, Leaderboard Illusion, UTBoost, Kane 2013, Newcombe 1998, Wilson 1927, Brown et al. 2001, El-Yaniv and Wiener 2010, ECBD, the two OpenAI posts and the METR note exist and fit their use. The OpenAI audit covers 138 problems that o3 did not consistently solve, with 59.4% flagged. ABC [40] exists as an arXiv paper; I could not confirm the item count from the abstract.
- Not confirmed: [7] (Ding, arXiv:2610.30635). Searches found papers on the same theme but not this identifier. [13] Hou et al. DOI 10.1145/3689498: I could not confirm it, and my recollection is a different TOSEM DOI; the authors should check. The 2026 arXiv items [2], [9], [10], [17], [20], [21], [32], [33], [34] and the 2026 articles [27], [30] I could not verify. I do not claim any is invented. A check by the program committee is advisable because the call mentions hallucinated references.
- [3] is cited as "Author(s), A." with a note "companion paper under review"; the call asks for a placeholder like "A. Anonymous". Minor.

**Rule checks.**
- Pages: 15 including references. Within the limit for the category chosen.
- Abstract: four labelled paragraphs, as required. It is long and carries many numbers.
- Keywords: present.
- Anonymity: no names or affiliations. "contact@example.org" is a placeholder. The reference to a companion submission tells the reader a related paper exists but does not identify authors. The call states no policy on companion papers.
- Data Availability Statement: present and specific. I could not inspect the package.

##### 7. Score

**Reject.** (Under the research preview category with a revised plan, I would move to borderline.)

##### 8. Reviewer confidence

**High**, because I recomputed the statistics and traced every count to the tables, and the main problems follow from the paper's own numbers and statements. Medium on the reference checks, which I could only do in part.

##### 9. Recommendation

I would not accept the paper as submitted. As a technical design paper its evaluation shows only that a gate withholds for a reason known before any data, and as an evaluation paper it has no results for either research question. The power table, which is correct, shows that the planned N=14 to 20 cannot produce a decision for a modestly compliant agent in more than a few percent of cases. The retained tasks are called clean although the authors' own check found 11 of the 14 accept a wrong patch. The review records were produced by one model and one signer with no reliability evidence, and the freeze that would make the study pre committed has not been made. The smallest set of changes that would move my score up one step, to borderline: (1) reframe the paper as a research preview or cut the claims to match what was done; (2) fix the analysis plan, including an agreement measure and a statement of what outcome would count against MESA, and deposit the frozen manifest with a time stamp; (3) justify or change the sample size using the paper's own power calculation, using all 75 source tasks or stating why not; (4) add an ABC arm with the same gate and run at least one independent automated audit; (5) report agreement with a second human rater for the B07 labels, explain the choice of run A and the 34 edits, and relabel the 14 tasks; and (6) redo the simulation at the real N, with a compliant agent, both error types and varied review accuracy.

---

### Paper 2: reviewer for AI evaluation

#### REFSQ 2027 research track: review of submission "Applying Meta-Evaluation Benchmark Reviews to Requirement Decisions: An Executable Method"

Reviewer perspective: AI evaluation (coding agent benchmarks, measurement validity, contamination, harnesses).
Files read: the call, paper2.pdf (all 15 pages), paper2.txt. Web search was used only to check that cited references exist and say what the paper claims.

##### 1. Summary of the paper

The paper takes a rubric from a companion submission (MESA: 39 criteria, from which seven are used here) and turns it into a three level decision engine. Level 1 checks input integrity with hashes. Level 2 assigns an evidence status (Admissible, Inquiry Required, Inadmissible) per criterion. Level 3 computes a 95% Wilson interval on resolve rate over retained tasks and returns Accept, Reject, Inconclusive, or No decision. The case is the requirement "at least 70% of SymPy bug reports resolved within 15 minutes" for two coding agents (Gemini 3.8 Flash in the Antigravity CLI, GPT-6.1 Sol in the Codex CLI). Source evidence is 20 of the 75 SymPy tasks in SWE-bench Verified. The planned direct test is 20 SymPy pull requests merged after the models' stated training cutoffs.

The paper reports four things.
- Checks run before any agent session. A Claude model wrote partial patches that pass the hidden tests while failing a self written independent test on 17 of 20 source tasks. By the paper's own rule only 6 of those are task defects. One task (sympy-18199) was also confirmed as an overbroad test. Nine patches that edit only test runner scripts were all scored as resolved by the official harness.
- Signed rating forms (one signer, forms drafted by an LLM) that make both a strict and a lenient MESA policy return Inadmissible, hence No decision.
- An exact binomial table (Table 4) and a Monte Carlo simulation (Table 5) under assumed review accuracy.
- A protocol of at most 90 agent sessions, which have not run.

The abstract says RQ2 is unanswered and RQ1 is answered only for the evidence gate, "which withholds on this benchmark whatever the agents do".

##### 2. Paper category under the call

The paper declares itself a technical design paper (Sect. 1.2, 15 pages). That category fits better than scientific evaluation, because the main sessions have not run. Criteria in the call's order:

- **Novelty.** An evidence admissibility gate in front of a confidence bound is a modest idea. Its parts (Wilson intervals, selective abstention, audit flags) are all known. The related work does not show that the combination is new relative to evaluation practice outside RE, and it omits the benchmark validity literature that already argues for error bars and for abstaining on flawed tasks (W9). The contribution is conveyed clearly in the abstract, but the abstract mixes results and cut points (W10).
- **Potential impact and relevance.** The topic fits the special theme (benchmarks and evaluation for AI speed RE). Impact is limited by the fact that the gate returns No decision on SWE-bench Verified by construction (W1) and has no positive case where it returns Admissible.
- **Soundness.** Weak. The central evidence is one model's exploit patches rated by the same model and signed by one author (W3, W4, W5). The only comparison with direct testing is unrun and underpowered (W2).
- **Verifiability.** Partly met. A Data Availability Statement exists and lists the artifacts, but it gives no link, and the paper cannot be understood without the companion paper's rubric (W8).
- **Presentation.** Dense and heavy with codes (B05, B28a, M3_withheld, CONFIG_02_SOL_MED). The abstract does not define MESA or ABC.

The call has no rule for a study whose main sessions have not run. My reading for each category it could be submitted under:
- *Technical design:* acceptable in principle, since the preliminary evaluation is allowed to be small, but the preliminary evaluation must show that the artifact can work. Here it shows only that the artifact withholds.
- *Scientific evaluation:* would not meet the first criterion (soundness). RQ2 is unanswered, RQ1 is predetermined, and the Empirical Standards for experiments or case studies are not met without results.
- *Research preview (8 pages):* the best fit for the present state. It asks for "a well defined research idea with a sound plan, limitations and risks". The plan here is well defined, the limitations are honest, but the paper is 15 pages and its checks are presented as findings.
- *Experience report, vision paper:* not fitting.

##### 3. Strengths

- **S1.** The paper states its limitations unusually plainly. The abstract says that no agent session has run, that RQ2 is unanswered, and that the gate withholds whatever the agents do. Sect. 7 also states that the session validity rule is not credited by the gate. I did not see overclaiming about agent results.
- **S2.** The statistics check out. I recomputed the Wilson bounds and every row of Table 4 (see Sect. 6). The values 0.701 for 9 of 9 and 0.676 for 8 of 8 are correct. The point in Sect. 5.1 and 6.2 that N between 14 and 20 gives more than 90% Inconclusive at p = 0.75 is correct and a useful warning for anyone who gates on a 20 task subset.
- **S3.** The paper separates "No decision" (evidence defect) from "Inconclusive" (statistics). The argument that flawed evidence does not prove the agent fails (Sect. 3.2) is sound and worth keeping.
- **S4.** The design of the pre session record is good practice: frozen manifest, SHA-256 digests of patches and logs, a replay test with provenance removed. Preregistering which outputs each method must produce before any session is a step ahead of most coding agent evaluations.
- **S5.** The B07 check follows a reasonable principle: a mechanical pass counts as a defect only if the omitted behavior is stated in the issue. The authors apply it conservatively (17 passes, 6 defects) rather than reporting 17/20 as defects in the body text.
- **S6.** Honest disclosure of LLM use (Claude Sonnet 5.5 for patches and drafts, Claude Opus 5.5 for engine code) and of the shared scratch overlap in run A.
- **S7.** The simulation text (Sect. 5.2) admits that most of the benefit comes from abstaining and that the gain over random abstention at equal coverage is about one percentage point.

##### 4. Weaknesses

**W1 (decision). The answer to RQ1 is fixed by the rules, so the gate is not informative on this benchmark.**
Where: abstract, Sect. 3.2 Level 2, Sect. 4.3 B28a and B14a forms, Sect. 4.5, Table 3, Sect. 7.
What is wrong: Level 2 makes the aggregate status Inadmissible if any criterion has outcome "failed". The B28a form is "Verified, failed" because the official harness can be fooled by a patch that edits test runner scripts. This is "a release-wide property of the grading harness" (Sect. 4.3), so it holds for every agent and every task set drawn from SWE-bench Verified. B14a is also "Verified, failed" from published contamination audits, again for every agent. The strict policy is therefore blocked before any session runs, and the lenient policy is blocked by B28a alone. The paper says this itself ("whatever the agents do"), but it still lists the withheld output as an RQ1 result and as a method comparison (Table 3). A gate that cannot return Admissible on this benchmark gives no information about the agents and no evidence that it would ever return Admissible. No positive control (a benchmark or harness where the gate passes) was run, and no negative control that separates a real defect from a rule artifact. Withholding on SWE-bench Verified is also already the position of its own cited source [25], which states that the benchmark no longer measures frontier coding capability, so the finding is not new.
Why it matters: the paper's main contribution (an executable gate that changes decisions) has no demonstrated case in which it changes a decision for a reason that depends on the agents or the tasks.
Fix: either show a case where the gate returns Admissible and then changes the outcome (for example SWE-bench Verified with a patched harness that rejects edits to runner and config files, or another benchmark), or reframe the paper as a research preview whose finding is "SWE-bench Verified fails two criteria".

**W2 (decision). RQ2 cannot be answered even if the sessions run, because the design has too little power and the "direct test" is not a reference standard.**
Where: Sect. 4.2, 4.5, Table 4, Sect. 6.2.
What is wrong:
(a) Table 4 shows 97.2% Inconclusive at p = 0.75 for N = 14 and N = 20, and 82.4% Inconclusive at p = 0.85 for N = 20. Most likely outcome: source decision Inconclusive, target decision Inconclusive. "Agreement" between two Inconclusive results is trivially high and says nothing about transfer. The paper acknowledges the N = 14 to 20 problem but does not change the design (20 of 75 tasks, 20 target tasks, pass@1, 2 agents).
(b) The sample is 20 of 75 SymPy tasks because of the session budget. All 75 are available and eligible (Sect. 4.2). Using all 75 sources would lift power (Table 4 gives only 14 to 120 as examples, and N = 60 gives 81.9% at p = 0.85).
(c) The target tasks only had the eligibility check (FAIL_TO_PASS fails pre fix, passes post fix). They did not receive the human validation that SWE-bench Verified tasks received, and they did not receive the B05 or B07 filtering that the source tasks receive. The same defect types (narrow tests, wide tests, partial patches that pass) will be in the target tasks. The target result is therefore no more a ground truth for "meets the requirement" than the source result. The comparison confounds task defects, task difficulty, year, repository state and training exposure (Sect. 7 admits "training exposure and issue difficulty" differ).
(d) One session per task and agent: no repeated runs, so run to run variance is mixed with task variance. The binomial model in Eq. 1 assumes independent tasks drawn at random from the population, but 20 tasks were selected by hash order from 75 (source) and by "first 20 checked in deterministic order" from 108 (target). The ordering used for the target selection is not stated.
Why it matters: RQ2 is the paper's second reason to exist, and the design cannot produce an answer that separates MESA from raw resolve rate.
Fix: use all 75 source tasks, state the required N for a meaningful agreement analysis, validate the target tasks with the same B05 and B07 procedure, run repeated sessions, or drop RQ2 from this paper.

**W3 (decision). The headline "cheating patches passing hidden tests on 17/20" is mislabeled and rests on one unvalidated model run.**
Where: abstract, Sect. 4.3 "Executed B07 exploit check", Sect. 6.1, Sect. 8.
What is wrong:
(a) The patches are partial fixes that omit part of the reference fix. They are not cheating or exploit patches in the sense used by the benchmark gaming literature (BenchJack, [33]), where an agent games the grader. Calling them "cheating" in the abstract and conclusion blurs two failure types (weak tests versus grader exploitation) that the paper itself separates later (B07 versus B28a).
(b) By the paper's own rule, 11 of the 17 are not defects. The abstract and conclusion give "17/20" first and "6 are task defects" second, which makes the weakness of the benchmark look larger than the paper's rule supports. It is also unsurprising: for any non trivial fix, a model that sees the reference fix can usually write a smaller patch that satisfies a given test file.
(c) The independent verification test was written by the same model that wrote the partial patches and that had the reference fix. It was not validated by a human or by a second tool against the issue text. An independent test that encodes implementation details of the reference fix would make partial patches "fail" spuriously. The check that defines the 6 defects therefore depends on this test being faithful to the issue.
(d) The task defect judgement ("the broken behavior is stated in the issue") was made by the same model in runs A and B, and then signed by the author with 34 edits. Agreement between two runs of the same model is not inter rater reliability, and run A had a shared scratch folder overlap (Sect. 7), so A and B are not independent. The nature of the 34 edits is not reported.
(e) 6 of 20 (30%) is near the proportion reported by other audits of SWE-bench patches [35, 38] and by [25], but the paper does not compare. The comparison would be the one place where the executed check could be tested against outside evidence.
Why it matters: the 6 removed tasks drive N = 14, audit_only, and the claim that MESA's executed check "removes 5 additional tasks that ABA did not flag".
Fix: rename to "incomplete patches that pass the hidden tests"; report 6 of 20 as the finding; have a human or a different model validate each independent test and each of the 6 issue-scope judgements; report agreement statistics for two independent raters; compare with the SWE-bench Verified annotation data and with [35, 38].

**W4 (decision). B05 and B07 are marked "Verified, passed" for tasks that were not checked.**
Where: Sect. 4.3, Table 2, Level 2 rule in Sect. 3.2.
What is wrong: B05 (do tests reject valid fixes) was run on one task (sympy-18199, plus the pilot task). For the other 19 tasks "were run only with the reference fix" (Sect. 4.3), which tests nothing about rejecting valid alternative fixes. The form is still "Verified, passed" with a "detection limit" note. That is, the engine would accept this form as admissible evidence for 19 unchecked tasks. The 2026 audit [25] reports a 59.4% flaw rate on 138 tasks, which the paper records as a detection limit. That rate was measured on 138 problems that a frontier model (o3) did not consistently solve over 64 runs, so it is not a random sample of SWE-bench Verified and says little about SymPy tasks (the cited post does mention sympy-18199 as an example of wide tests). It is not used as a prior for the remaining 19 tasks either. The same applies to B07 on the retained 14 tasks: "Verified, passed" means only that up to three partial patches from one model were unsuccessful in producing a counterexample. Absence of a found counterexample is not "Verified passed".
Why it matters: the gate's logic depends on the difference between "performed and passed" and "not performed". The paper's own forms blur it for the two criteria that drive task removal.
Fix: record B05 as "not performed" for 19 tasks (or run it: generate alternative valid fixes), and grade B07 on the retained tasks as "Documented" or "Inquiry Required". Report how the aggregate status changes.

**W5 (decision). The B28a check shows feasibility of an attack on three tasks, not a property of the harness, and the gate gives the attack more weight than the paper's own mitigation.**
Where: Sect. 4.3 "Executed B28a", Sect. 4.4, Sect. 7.
What is wrong:
(a) Nine patches on three tasks (three layouts) are not nine independent samples. "9/9" in the abstract and conclusion reads like a rate. It shows that an attacker prompted to edit runner scripts can do so for the three layouts tested. It does not show that any evaluated agent does so.
(b) Whether the runner script can be edited and still scored as resolved depends on the harness version and configuration (which files the test patch overwrites, how logs are parsed). The paper gives no harness commit or version. Without it the result is hard to reproduce. I could not confirm from the cited source [33] that BenchJack audited SWE-bench Verified (the abstract names WebArena and OSWorld), so the B28a result is the authors' own, and [33] supports only the general class of flaw.
(c) The session validity rule (Sect. 4.4) marks a session invalid if it modifies test runner scripts or test configuration files, and the study counts that session as unresolved. This is the standard mitigation (reject patches that touch runner and config files) and it removes the attack for the study's own sessions. Sect. 7 says the gate "does not credit" it. So the gate declares the benchmark Inadmissible for a risk that the study protocol itself has closed. The "amendment" that would credit it is left unevaluated, yet it is the only change that would let the gate return anything other than No decision on this study.
Why it matters: it is the sole blocker under the lenient policy and one of two blockers that are checkable at all (B14a being literature based). A reader can reasonably conclude that the gate is too strict, or that the paper chose the criterion that guarantees the result.
Fix: evaluate the amendment (credit a verified per session control as a mitigation, with the scanner's detection rate measured), or show the gate's behavior with and without it, and report the harness version.

**W6 (decision). The contamination argument and the choice of post cutoff target tasks are not enough to support "evidential transfer".**
Where: Sect. 4.2, 4.3 (B14b), Sect. 1 (Gap 2).
What is wrong:
(a) The cutoffs are vendor stated dates (March 2026; 30 April 2026). Stated cutoffs are known to be imprecise (the effective knowledge is thinner for the last months, and later post training data can include newer content). A merge date after the cutoff is not proof that the fix, the issue, or near duplicate fixes were not available to the model.
(b) The target filter looks at pull request merge dates, but five of 20 close issues opened before the cutoff (the paper handles this by reporting 15). SymPy bug fixes often follow earlier reports, earlier similar fixes, or discussion that predates the cutoff, and the paper does not check for linked earlier issues or duplicate fixes beyond the opening date of the one linked issue.
(c) The agents run through commercial CLI tools. If the CLI includes web search, browsing, or fetch tools, the agent could find the merged pull request, which is public for target tasks. The paper relies on "tool flags and hook settings" and "network commands" detection in transcripts, and says "runtime isolation during the actual study sessions is verified from the recorded session transcripts" after they run. Scratch checks v1 to v8 were run in a scratch workspace, not in the actual task environment (Sect. 4.4). For target tasks the repository clone may contain the future fix commit unless the git history is trimmed; the paper checked git history only for the source task containers (B28b form) and never says how the target repositories are prepared. Known reports of agents reading future commits from SWE-bench containers show why this matters.
(d) B14b is "Documented, not performed" for both agents. No contamination test (for example a memorization probe on source tasks, or a performance comparison on pre and post cutoff tasks with the same preparation) is run. The paper therefore cannot say whether contamination affects the source resolve rate, which is what the gate is meant to guard against.
(e) The source and target tasks differ in more than cutoff: Verified tasks were human screened for solvability, target tasks were not (W2c). A drop from source to target can come from that alone, and the paper would read it as contamination.
Why it matters: RQ2 is about transfer from contaminated, audited source tasks to clean target tasks. The clean side is not shown to be clean, and the contamination side is not measured.
Fix: add a contamination probe for B14b, prepare target repositories with history cut at the base commit and verify it, run sessions in a container or VM with network blocked by the OS or the network layer (not by CLI flags), log the tool inventory per CLI, and use a decontaminated comparison set only after human validation of tasks.

**W7 (decision). Fairness of the two agent setups and of the sandbox.**
Where: Sect. 4.1, 4.4, 7.
What is wrong: the two agents use different CLIs (Antigravity, Codex) with different system prompts, tool sets, hooks, and "medium" reasoning settings that are not comparable across vendors. Each run is limited to 900 seconds wall clock, so the resolve rate depends on API latency, rate limits, and time of day, not only on the model. Resolve rates are pass@1 with one run per task. Per agent requirements do not need a comparison between agents, so this does not break the method, but it limits any statement about what the requirement says about the models. The sandbox checks were run only in a scratch workspace; the study sessions run on the author's machine (the data statement says raw logs "contain local host paths"), so the agent shares a file system with the study folders, signed forms, and target task records. The invalidity rule relies on scanning transcripts for access to "study folders" and "git history beyond the base commit". A session that reads the data without leaving a transcript trace would not be caught, and an invalid session counts as unresolved, which biases resolve rates down differently for each CLI depending on how often it triggers a scanner rule. Whether the installed SymPy in the environment (rather than the repository checkout) is the pre fix version is not stated, and the package manager is an obvious route to a newer SymPy if network access exists.
Why it matters: the direct test is the reference for RQ2, so any leak or tool difference moves the reference.
Fix: run each session in a container with no network and with only the pre fix repository mounted, publish tool inventories and prompts for both CLIs, set a token budget as well as a time limit, and report test only resolution next to the scanner adjusted rate for every session (the paper plans the latter for control only).

**W8 (decision). The paper depends on a companion submission and on LLM generated review records that the reader cannot judge.**
Where: Sect. 1 (MESA), Sect. 2.1, 3.3, Table 2, Sect. 4.3, 7.
What is wrong:
(a) The MESA rubric (39 criteria, 30 concerns) and the criterion ids (B05, B12, B14a, B14b, B28a, B28b) are defined only by one line each in Table 2. The reader cannot check whether "Verified", "Documented", and "Undocumented" are applied as intended, or why B12 (uncertainty reporting) is "Undocumented, not performed" when the paper itself computes Wilson intervals for the same benchmark. The companion paper [3] is under review and cannot be assumed read.
(b) All forms are drafted by Claude Sonnet 5.5, the engine and the requirement and transfer justifications by Claude Opus 5.5 (same family), and the one human signer made 34 edits that are not analyzed. The ABC checklist was completed by the same model after it "read the MESA rating rules" (Sect. 7), so the comparison "MESA versus ABC" is not independent, and ABC was applied through a mapping to MESA's seven criteria (33 items), which is not how ABC [40] is meant to be used. ABC is a design checklist for benchmark builders and does not claim to make accept or reject decisions, so "ABC issues a score decision with 15 caveats" is a strawman comparison. ABA [34] and UTBoost [38] are likewise not decision methods.
(c) For ABA, the paper compares against "the 2 source tasks flagged with a major finding (sympy-13031, -18199)". From the ABA paper I could confirm only that it names sympy-18199 as a major issue; I could not find sympy-13031 in the part of the text I could read, and its SWE-bench Verified review is described as a sample of 25 major issues. If ABA did not audit all 20 source tasks, "not flagged" does not mean "audited and clean", and the statement that MESA removes "5 additional tasks that ABA did not flag" is not a like for like comparison. ABA also flags specification gaps, environment issues, and wrong ground truth, which differ from B07.
Why it matters: the comparisons in Table 3 are the paper's RQ1 content.
Fix: summarize the criteria and levels used in an appendix; report human inter rater agreement on at least a sample of forms; have a person who did not see MESA fill ABC; and clarify which tasks ABA actually audited.

**W9 (decision). Description of SWE-bench Verified and missing related work.**
Where: Sect. 1, Sect. 2.2, reference list.
What is wrong:
(a) "SWE-bench Verified [14]" cites the original SWE-bench paper (Jimenez et al.). Verified is the human validated 500 task subset released by OpenAI with annotators (Chowdhury et al., 2024); it is not described here. The reader is not told that Verified tasks were filtered for underspecification and test validity by annotators, which matters directly for W3 and W4 (the 6 defects are tasks that passed that annotation). The sources of tasks (SymPy 75 tasks from 2016 to 2023), the harness (patch applied in a fresh container, test patch applied on top, log parsing), and the meaning of FAIL_TO_PASS and PASS_TO_PASS are only partly given.
(b) The introduction states that "teams frequently substitute public benchmark scores ... as fast acceptance evidence [13,29]". [13] is a literature review of LLMs for software engineering and [29] is about Chatbot Arena leaderboards; neither shows that teams use SWE-bench scores as acceptance tests. "For an AI, such measures ... are in effect its requirements specification [5]" is an interpretation of Berry, not a finding. [11,17] are about RE for ML systems and do not support "the bottleneck shifts upstream" for coding agents.
(c) Missing related work (to my knowledge): the OpenAI SWE-bench Verified release and annotation; SWE-bench Pro, SWE-bench Multilingual, SWE-Lancer and similar benchmarks designed for harder or less contaminated evaluation; LiveCodeBench for time windowed decontamination; reports of agents reading future commits from repository history in SWE-bench containers and the later fix to the harness; Kapoor et al., "AI Agents That Matter" (holdout sets, cost); work on uncertainty in evals ("Adding Error Bars to Evals", Miller 2024) and on the unreliability of normal approximations at small n (Bowyer et al. 2025), which bears directly on the paper's small N argument; the broader contamination literature (surveys and time based probes); and prior work on SWE-bench patch correctness (for example PatchDiff in [35], used here only as a motivation). The paper's own list of audits [32, 33, 34, 20, 38, 35, 7, 24] is good, but none is used to test the paper's numbers (for example 6 of 20 versus the rates in [35, 38]).
(d) Related work on selective prediction and abstention is limited to [8]; the simulation baseline (random and proximity withholding) is reasonable but the gain is only about one percentage point (Sect. 5.2).
Fix: describe Verified correctly and cite its release; replace or remove the unsupported motivation citations; add the benchmark and contamination related work above and position the Wilson gate against error bar practice.

**W10 (minor). The abstract reports plan outputs as if they were results.**
Where: abstract, "Principal ideas/results".
What is wrong: "Accept 14/14; Reject <= 6/14 ... versus N = 20 for raw and ABC (Accept >= 19/20; Reject <= 9/20; 97.2% Inconclusive at p = 0.75)" are cut points and power numbers, not outcomes. MESA, ABC, B05, B07, B28a are used in the abstract without definition. The sentence on "17/20" precedes the qualification (W3).
Fix: define the terms, say that the numbers are decision rules, and lead with the finding that both policies withhold.

**W11 (minor). The simulation does not test the study's case.**
Where: Sect. 5.2, Table 5.
What is wrong: the simulation uses N = 30, while the study uses 14 to 20. The review accuracy parameters (85% detection, 5% false alarm) are assumed, and the evidence gate in the simulation never behaves as in the real case (always blocked by B28a). The text discusses a scenario (d = 0.30, delta = 0, false rejection 0.44% versus 1.42%) that is not in Table 5, and Table 5 omits delta = 0 rows. "False acceptance per case" is not defined (denominator all trials, which is why M3's value is low mostly because it abstains). As the text says, most of the reduction is abstention.
Fix: add the delta = 0 rows, simulate N = 14 to 20, report accuracy among decided cases, and vary the review accuracy.

**W12 (minor). Requirement and threshold.**
Where: Sect. 1, Sect. 3.4.
What is wrong: the requirement "the tests the maintainers later wrote for that bug pass" is the same quantity the benchmark scores. There is no gap between the metric and the requirement except the sample, so the example does not exercise the validity problems (construct, B01 to B04, are omitted). The threshold of 70% is not justified, and the statement "at least 70% of bug reports" is a population claim tested with 14 to 20 hash selected tasks. Finite population effects (20 of 75 without replacement) are ignored in Eq. 1.
Fix: justify theta, discuss the sampling frame, and use a requirement whose acceptance test differs from the benchmark metric.

**W13 (minor). Smaller issues.**
- Sect. 4.3 and Table 1 say "20 B07 exploit attempts" but Sect. 4.3 says up to three candidate patches per task; clarify attempts versus tasks.
- Sect. 4.2 target window "1 May and 5 November" versus Sect. 1 "13 June and 5 November" (the second is the range of the selected sample; say so). The order in which the "first 20 checked" were chosen is not given.
- "Gemini 3.8 Flash" and "GPT-6.1 Sol" cutoffs are cited without a source.
- The title says "Requirement Decisions" and the abstract "Meta-Evaluation Benchmark Reviews"; the terms "audit", "review", "check", "form" and "record" are used for overlapping things (Sect. 6.1 uses "automated checks" for forms signed by a human).

##### 5. Questions for the authors

- **Q1.** Is there any benchmark, harness version, or task set on which the gate returns Admissible today? If not, what is the evidence that the gate is not simply a rule that always withholds on public benchmarks?
- **Q2.** The session validity rule closes the test runner attack in your own sessions. What measured detection rate does the scanner have for runner or config edits, and why is that control not credited by Level 2 (W5)?
- **Q3.** Who validated the independent verification tests written by the model? How many of the 17 passes survive if each independent test is checked by a person against the issue text only?
- **Q4.** Which harness version produced the 9 of 9 result, and do patches that edit files overwritten by the test patch still pass? Did you try the same patches against a harness that rejects edits to runner and config files?
- **Q5.** Why 20 of 75 source tasks when all 75 are eligible and Table 4 shows that N = 14 to 20 gives more than 90% Inconclusive? What is the expected agreement outcome for RQ2 under your own power calculation?
- **Q6.** How are target repositories prepared (history cut at base commit? installed SymPy version?), and which tools, including web search and fetch, are enabled in each CLI? Is network access blocked at the operating system level?
- **Q7.** Which ABA outputs cover which of your 20 source tasks, and where does "major finding" for sympy-13031 come from?
- **Q8.** What were the 34 edits between draft and signed forms? How many changed a level or an outcome?
- **Q9.** Why is B12 "Undocumented, not performed" when SWE-bench resolve rates here are reported with intervals by your own method? Is the criterion about the benchmark's reporting or about the user's?
- **Q10.** If the sessions produce a pass rate above 0.7 on both source and target, what would count as evidence against your method?

##### 6. Checks I made

Arithmetic (recomputed in Python, Wilson interval with z = 1.95996):
- 9/9 gives LB 0.701 and 8/8 gives LB 0.676, so n_min = 9 is correct (Sect. 4.2).
- 14/20 gives LB 0.481 and UB 0.855 (Sect. 6.2: "only 0.481" is correct).
- Cut points match Table 3 and Table 4: N = 14: Accept only at 14/14 (13/14 gives LB 0.685), Reject at 6 or fewer (UB 0.674 at 6/14, 0.732 at 7/14); N = 15: Accept at 14 or more, Reject at 7 or fewer; N = 18: Accept 17 or more, Reject 8 or fewer; N = 20: Accept 19 or more, Reject 9 or fewer; N = 30: 26 and 16; N = 45: 38 and 25; N = 60: 49 and 35; N = 90: 72 and 54; N = 120: 94 and 74.
- Every Accept, Reject and Inconclusive percentage in Table 4 matches my exact binomial computation to one decimal. Examples: N = 14, p = 0.75 gives 1.8% Accept and 97.2% Inconclusive (my Reject value 1.0% is omitted from the table, so the columns do not sum to 100%, which is not explained); N = 15, p = 0.85 gives 31.9% Accept; N = 120, p = 0.65 gives 25.0% Reject.
- Sect. 5.1: power for Accept at p = 0.85 first exceeds 80% at N = 60 (81.9%) and falls to 78.8% at N = 62; true. It rises again to 80.4% at N = 61 (the text says N = 60 is the first N that reaches 80%, which is correct, but the statement "requires N = 60" is only a statement about the first N).
- Session budget: 2 + 40 + 40 + 8 = 90, consistent. Forms: B05, B07, B12, B14a, B28a, B28b (6) plus B14b for two agents (2) gives 8 MESA forms; plus the ABC record gives nine records, consistent with the abstract.
- ABC counts: 8 + 9 + 10 + 6 = 33 mapped items, and T 5/8 + O 2/11 + R 1/4 gives 8 met of 23 applicable (33 minus 10 not applicable); caveats 9 + 6 = 15. These agree. The paper does not say how the 10 "not applicable" items were decided.
- B07: 17 passes; 6 named defects; 11 set aside; 14 retained; 20 - 6 = 14. B05 adds sympy-18199, which is already one of the 6, so no further removal; ABA flags 2 of which one overlaps, so the claim "5 additional tasks" (6 minus 1 overlap) is arithmetically right.
- Table 5 versus text: M2 20.8% (22.4% coverage), M3 5.4% (6.8%), Random 6.4%, Proximity 6.5% match the text. The differences 1.0 and 1.1 points are consistent with the reported 0.88 and 1.14 (paired means). The Delta = 0 scenario cited in the text is not in the table.
- Targets: 322 merged, 108 matched, first 20 chosen, 5 with older issues, 15 left. Consistent.

Claims without support or with weak support:
- "teams frequently substitute public benchmark scores ... [13,29]": not supported by those references (W9b).
- "17/20 cheating patches": mislabeled (W3).
- "Verified, passed" for B05 on 19 untested tasks (W4).
- "59.4% flaw rate on 138 tasks" is from a non random subset of problems that a model did not solve consistently (checked at the cited OpenAI post). The post does name sympy-18199 as a wide test example, which matches the paper.
- "BenchJack flags unisolated runners (B28a)": [33] exists and is about auditing agent benchmarks by red teaming; I could not confirm it covers SWE-bench Verified.

Reference checks (existence only; web search):
- Found and consistent with the use made of them: [25] (OpenAI, Feb 2026), [32] BenchGuard (arXiv 2604.24955), [33] BenchJack (arXiv 2605.12673), [34] ABA (arXiv 2605.26079), [20] (arXiv 2607.27518), [10] (arXiv 2609.16302).
- [7] (arXiv 2610.30635): a search for the exact title did not return the paper; related titles on specification gaps exist. I could not confirm it. [2], [21], [9], [17] could not be checked in the time I used. I did not find fabricated looking references among those I checked.
- [14] cites the original SWE-bench paper for "SWE-bench Verified" (W9a). [3] is cited as "Author(s), A." instead of the form the call asks for ("A. Anonymous").

Terms used inconsistently: "audit", "review", "check", "form" and "record" overlap; "resolved" is defined differently from SWE-bench (adds the 15 minute limit and session validity); "post-cutoff tasks" means merged after the cutoff for 20 tasks and issue opened after the cutoff for 15; "Inadmissible" is used both for a criterion and the aggregate; "attempt" and "task" are mixed for B07 (W13).

Rule checks:
- Page limit: 15 pages including references, matches the technical design limit.
- Abstract: four paragraphs with the required labels and a limitations statement; keywords given. Dense, with undefined terms (W10).
- Anonymity: no names or affiliations. The paper refers to "the author" (singular) in several places and to model names in the Disclosure, which is fine. The companion paper is cited as "Author(s), A." (not the call's placeholder). The contact line is a placeholder address. No link is given for the replication package, so I could not check its anonymization.
- Data Availability Statement: present and mandatory item met; it lists the content but gives no access information for reviewers.
- Overlap: the call states no policy on companion submissions; the paper relies on the companion for the rubric (W8).
- AI use is disclosed (S6).

##### 7. Score

**Reject** (one step below weak reject).

##### 8. Reviewer confidence

**Medium.** I know SWE-bench, its harness and the audit literature well and recomputed all statistics, but I could not see the replication package or the companion paper, and several 2026 references could not be verified.

##### 9. Recommendation

I would not accept the paper as submitted. The statistics and the honesty about limits are good, but the paper contains no result that depends on the agents or on the clean versus contaminated comparison it is built around. The one finding is that SWE-bench Verified fails B28a and B14a, which follows from the gate's rules plus published audits and which [25] already supports. The executed checks that lead the abstract are weaker than they look: the 17 of 20 figure is mislabeled as cheating, the independent tests and the 6 defect judgements come from one model and one signer, B05 is graded "passed" on tasks never tested, and 9 of 9 comes from three tasks. The smallest set of changes that would move my score up one step (to weak reject) is: (1) relabel the 17 of 20 result and report only the 6 issue scope defects as findings, with a human validation of the independent tests and defect judgements; (2) correct B05 and B07 outcomes for unchecked tasks and show the effect on the aggregate status; (3) evaluate the session validity amendment so the gate's behavior on B28a is shown with and without it, or else state that the gate is only a check on harness readiness; (4) use all 75 source tasks and state a power analysis for RQ2, or drop RQ2 and submit as a research preview; (5) describe SWE-bench Verified and its annotation correctly, fix the unsupported motivation citations, and add the missing benchmark validity and error bar literature. To reach weak accept the sessions would need to have run, with sandboxing at the operating system level and a case where the gate returns Admissible.
