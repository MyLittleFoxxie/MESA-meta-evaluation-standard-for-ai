# MESA-20: a short benchmark review

Historical draft 0.1. The revised [MESA-25 form](../mesa-25/questionnaire.md) supersedes this form as of 2026-10-01.

Draft 0.1, 2026-09-29. An unvalidated proposal. Use it to review one benchmark version for one stated use. It does not certify the benchmark or the AI system.

There are **20 questions: four factual questions, fifteen evidence judgments, and one final recommendation**. The short explanations belong to their question; they are not separately scored. A source list and reviewer details are additional records, not included in the question count. Complex cases can still require substantial investigation.

**Reviewer / date / relevant interests or conflicts / assistance used:**

**Sources:** Give each source an ID, title or URL/path, version or page/section, access date, and access limits. Cite these IDs in answers. Record missing information rather than guessing. Do not inherit evidence from another version without checking it.

## Part A: describe it

### Q1. Exactly which benchmark are you reviewing?

Name its version, task split and scoring implementation, creators or maintainers, and any parent benchmark. Identify the published results being examined. Say when an identifier is unavailable.

Answer and sources:

### Q2. What is it meant to measure?

Record the authors' definition, intended systems and users, claimed uses, and stated limits. Then name the particular claim or decision this review will examine. Keep the authors' claim separate from your choice of review scope.

Answer and sources:

### Q3. What does a system have to do?

Describe the task types, number of tasks, inputs and required responses. Record the run conditions needed to understand the result: prompts, tools, attempts, time or compute limits, and human help where relevant.

Answer and sources:

### Q4. How are responses turned into results?

Describe the scorer, score calculation, combination of task scores, and handling of failed or missing responses. Name the reported scores and reference comparisons. Record reported uncertainty; leave judgment to Part B.

Answer and sources:

## Part B: judge the evidence

For Q5-Q19, choose **Supported / Weakness / Unknown / Not applicable** using the [guide](guide.md). Add a brief note in this order: **evidence and source → reason → missing evidence or limitation → effect on the intended use**. Record material differences between tasks, scorers or groups instead of hiding them in one label. Mark a finding **critical** if it could change the decision in Q2, and explain why.

### Q5. Why should these tasks measure the stated ability?

Check the explanation linking the defined ability to the task demands and score meaning. A convincing explanation is a starting point; evidence that it works is examined below. Difficulty or popularity alone is not support.

Judgment and note:

### Q6. Were the tasks checked for errors during development?

Look for documented sourcing, selection, expert review, piloting, item-level results and correction of faulty tasks or answers. For reused, translated or AI-generated material, check what was changed and how it was reviewed.

Judgment and note:

### Q7. Do the tasks cover the ability being claimed?

Compare the sampled tasks and their balance with the intended domain. Identify important omissions. Broad intelligence claims need evidence across relevant abilities; a narrowly defined test need not measure everything.

Judgment and note:

### Q8. Does the scoring rule reward the intended performance?

Examine whether the metric and any combined score reflect success at the intended task. Check evidence for claimed subscores and whether averages hide important failures. A standard metric is not automatically suitable.

Judgment and note:

### Q9. Can the scorer be trusted to apply that rule?

Check the actual scoring route: software/parser tests, human agreement, or AI-judge checks against expert judgments. Examine relevant errors, bias and changes in the scorer. A fixed algorithm or named judge is not evidence of correctness.

Judgment and note:

### Q10. Do the reference comparisons give the score a defensible meaning?

Use the references the claim requires: chance, simple strategies, humans, other models, or justified pass/fail boundaries. Check who or what was compared, under which conditions, and whether the reference still applies. Consider whether scores bunch at the top or bottom.

Judgment and note:

### Q11. Would the result hold up if the evaluation were repeated?

Look for measurements of variation across runs and relevant changes in prompts, task forms or environments. Published settings alone do not show stability. State which sources of variation were studied and which remain unknown.

Judgment and note:

### Q12. Are score differences precise enough for the intended decision?

Check uncertainty around scores and comparisons, the amount and dependence of data, and whether the difference matters in practice. Missing uncertainty leaves a comparison unresolved; it does not prove the difference is noise.

Judgment and note:

### Q13. Are shortcuts that bypass the intended skill addressed?

Look for tests of shortcuts such as superficial cues, answer style, formatting tricks or exploiting the scoring rule. Use error analysis to distinguish failure at the target task from failure at an unrelated demand.

Judgment and note:

### Q14. Are prior exposure and test-specific tuning addressed?

Check item origins, exposure to tasks or answers, held-out evaluation and repeated-submission rules where relevant. Separate intended access to task documents from answer leakage. Public release is a risk factor, not proof of contamination; secrecy alone is not proof of protection.

Judgment and note:

### Q15. What supports claims beyond these particular tasks?

Look for evidence linking scores to related abilities, distinguishing them from different abilities, or predicting the claimed real use. Realistic-looking tasks alone do not establish transfer. This question can be not applicable when the claim is strictly limited to the recorded tasks and runs.

Judgment and note:

### Q16. Are comparisons fair across the intended systems and contexts?

Check relevant differences in tools, compute, access, language, modality and task groups. Look for unnecessary barriers and evidence about measurement quality across those groups. A performance gap alone does not establish bias.

Judgment and note:

### Q17. Can another qualified person inspect and repeat the evaluation?

Check usable materials, instructions, code or an audit route, recorded settings and outputs, and access and reuse terms. Record relevant privacy safeguards, sensitive-content warnings and restrictions. Distinguish materials being available from a successful independent reproduction.

Judgment and note:

### Q18. Can users tell when changes make old and new scores incomparable?

Look for version records, error correction, responsible maintainers and rules for changed tasks, scorers or services. For live tests, check evaluation dates and task cohorts. A frozen test needs identifiable materials, not constant new releases.

Judgment and note:

### Q19. Do the published results tell users what the evidence supports?

Inspect the important paper tables, reports or leaderboard. Check score traceability, conditions, uncertainty and use limits. Note conflicting headlines, selective reporting or submission rules that could mislead readers. A paper's caveat does not automatically fix its leaderboard.

Judgment and note:

## Final recommendation

### Q20. What should someone use these results for?

Give the strongest supported use and its main strength; the uses not supported; the conditions needed for comparison; and the most important missing evidence or correction. Refer to earlier answers rather than repeating them. Explain any critical Unknown or Weakness that blocks the proposed use. Include required reviewer/user expertise where it affects the recommendation. Do not add or average the judgments.

Recommendation and question references:

---

The [guide](guide.md) explains answers and when to expand the review. The [proposal](README.md), [mapping](coverage-map.md), [source notes](sources.md), and [checks](checks.md) document the design. These are development records, not additional forms to complete.
