# Possible changes to the research direction

29 October 2026. Assistant analysis for author consideration. This is a targeted follow-up to the existing review, not a new systematic review or a completed novelty assessment. No manuscript, questionnaire, study protocol or participant record was changed. The earlier review counts remain unchanged. New sources require eligibility and full-text assessment before inclusion in that review.

## What should not be claimed as a new gap

The seven starting sources already supply substantial conceptual and practical support. The Standards and EFPA address interpretations, uses, documentation and review. OECD characterises evaluation instruments. Measuring what Matters audits the relation among capabilities, tasks, metrics and claims. The Leaderboard Illusion examines the process producing public rankings. BetterBench covers development, documentation and maintenance. A Definition of AGI addresses a particular account of the breadth of intelligence claims. These are different contributions, not seven failed attempts at the same task.

Additional work narrows the available space further:

- [ECBD](https://aclanthology.org/2024.acl-long.861/) provides a worksheet and asks designers to describe, justify and support decisions. Local full text, discussion and limitations, checked.
- [Scorecard of AI Benchmark Quality](https://aclanthology.org/2026.evaleval-1.25/) provides review criteria and suitability classifications. Its local full text reports disagreement about scope and evidential weight. Merely attaching intended uses to a review is not new.
- [Evaluation Cards](https://arxiv.org/abs/2606.09809) and its [official documentation](https://evalcards.evalevalai.com/about) cover reporting, missing information, provenance and interpretation for readers. Merely making a readable card is not new.
- [Automated Transcript Analysis for Detecting Flaws in Agentic Benchmarks](https://arxiv.org/html/2607.27518v1) evaluates scanners against human labels and uses synthetic violations during development. Sections 3.6.1 and 5.1 were checked. Limitations include transcript observability and disagreements in human grading. Merely testing an automated auditor on introduced flaws is not new.
- [When benchmark inferences do not compose](https://arxiv.org/abs/2607.26159) proposes an audit of connections across studies. Abstract and version record inspected; full assessment pending. A chain from score to deployment is not an unoccupied topic.
- [Benchmark Caliper](https://github.com/aims-foundations/benchmark-caliper) assesses contextual applicability, including cultural transfer. Its paper, *Uplifting Human Decision Making in AI Evaluation by Automating Benchmark Validity Analysis*, is listed by [an author](https://cs.stanford.edu/~nntruong/publications/). OpenReview PDF retrieval encountered browser verification; repository and author record were available. Do not treat this as a completed paper review or infer missing methods from access failure.

## Direction 1: Test the review methods themselves

Question: under controlled changes, which review procedures detect a specified problem, avoid inventing a problem, and preserve conclusions when only wording changes?

MESA could become a method and case collection for evaluating benchmark review procedures. The current questionnaire would be one comparator, not the required solution. Existing criteria would define the problems to investigate. Differences among frameworks' purposes must be respected: OECD classification values cannot be treated as quality ratings, and failure to cover a criterion outside a framework's scope is a coverage limit rather than a detection error.

Possible study: construct paired benchmark dossiers with declared changes. Include a relevant change in procedure, an omission in documentation, a meaning-preserving rewrite, and a contradiction between documentation and executable scoring. Use small runnable artifacts for implementation claims. Hide construction notes from reviewers, check transformations independently where feasible, and keep development cases separate from final cases. Do not automatically repurpose the existing 24 examples or assume 24 is an adequate sample.

Report detected problems, false alarms, appropriate uncertainty and conclusions changed by wording alone. Show outcomes by problem type and source availability. With model reviewers the result concerns each model, prompt and procedure combination, not human performance or an intrinsic score for a framework. Map outputs to shared findings with a declared coding method; do not force every method into MESA's five choices.

Candidate contribution: an empirical comparison of how review procedures respond to controlled changes, including differences between absent information and demonstrable faults. This is narrower than inventing benchmark auditing. Strong overlap with automated auditing and adjacent peer-review evaluation remains; novelty needs further checking. This is the most feasible direction for work that does not depend on new human recruitment.

## Direction 2: Decide what to check next

Question: when a review cannot support a conclusion, which next check resolves the uncertainty with the least declared cost?

MESA could become an investigation procedure. Its output would be a claim, a missing or conflicting fact, a proposed check, and the possible consequences of that check. For example, a repeatability claim may require run logs, while a scoring claim may require running a scorer against verified examples. Requesting another benchmark description would not resolve either by itself.

Possible study: use cases with several possible document requests or executable checks and a declared action budget. Compare a proposed selection rule with a fixed checklist order and a model asked to choose a check without that rule. Measure verified issues resolved, checks used, unresolved issues and unsupported stopping decisions. A claim about an optimal next action requires defined costs and available actions; do not equate fewer requests with less human effort.

Candidate contribution: tested selection and stopping rules for benchmark investigation. ECBD already calls for collecting missing validity evidence; audit and decision research already considers prioritisation. A workflow diagram or a list of recommendations would not establish novelty. Search cost-sensitive diagnosis, active information gathering and assurance-case literature before choosing this direction. This option requires more new design work than Direction 1.

## Direction 3: Explain disagreements without forcing agreement

Question: do reviewers differ because they read different sources, interpret a criterion differently, consider different intended uses, or require different amounts of support?

MESA could become a comparison procedure that records each review's claim, source, criterion interpretation and unresolved objection. Its output is the cause and status of disagreement, rather than a majority vote or merged answer key.

Possible study: start with verified examples of disagreements, classify their causes, and test whether the procedure identifies the distinction and requests relevant clarification. The Scorecard and scanner papers already report disagreements. Adjacent scientific peer-review work also studies contradictions, so this is not a first account of reviewer disagreement. Proposed classifications must be compared with that work.

Candidate contribution: a tested method for identifying causes of disagreement in benchmark reviews while preserving defensible alternatives. A collaboration claim would require people actually using it. The current survey's optional reasons and shared source packet may not provide enough material. Model disagreements can support an initial study but cannot establish improved human collaboration.

## Decision

Do not select a new direction solely because it sounds suitable for a conference. Direction 1 currently provides the clearest route to results without new participants. Direction 2 most changes the output from a completed form to an investigation plan, but has the least settled novelty. Direction 3 has a direct collaboration question but conflicts most with the constraint on new human data.

Changing the project does not require deleting the earlier questionnaire. Preserve it as a version, use it as a comparator if relevant, and label any later survey separately. Responses to the old survey cannot validate a different procedure. Approachability may remain a design aim without being the paper's central empirical claim.

## Search record and limits

Sources: existing seven-source summaries, synthesis and gap ledger; targeted web discovery supplemented by primary publication records, author pages and project documentation. Searches conducted 29 October 2026. Search-engine ranking and result limits apply. Results were selected for direct overlap and counterexamples, not exhaustively screened. No claim that an unsuccessful query demonstrates an empty field.

Exact discovery queries:

1. `AI benchmark review framework evidence provenance updates benchmark validity review disagreement`
2. `AI benchmark selection intended use requirements evidence framework Evaluation Cards BetterBench ECBD`
3. `AI benchmark evaluation validity assurance case evidence gaps uncertainty claims`
4. `"benchmark" "review" "disagreement" "Scorecard" AI`
5. `"Evaluation Cards" AI evaluation reporting provenance`
6. `AI benchmark review prioritization missing evidence next test audit framework`
7. `benchmark version changes review validity impact analysis AI evaluation`
8. `"AI benchmark" "review" "metamorphic"`
9. `"benchmark quality" "checklist" "sensitivity"`
10. `"AI benchmark" "repair" "prioritization"`
11. `"Scorecard of AI Benchmark Quality"`
12. `"AI benchmark" "audit" "injected" flaws`
13. `"benchmark review" "reliability" framework`
14. `"benchmark" "audit" "next" "evidence" framework AI`
15. `"Automated Transcript Analysis for Detecting Flaws in Agentic Benchmarks"`
16. `benchmark review framework sensitivity specificity validation checklists quality AI review methods`
17. `"AI evaluation" "value of information" audit`
18. `"benchmark" "reviewer disagreement" framework`
19. `"benchmark review" "paraphrase"`
20. `"Uplifting Human Decision Making in AI Evaluation"`

Broader search hits in medicine, financial auditing, alignment auditing and scientific peer review were discovery leads, not assessed as evidence of benchmark-review effectiveness. Specific follow-up is needed for each direction. No new experiments were conducted.
