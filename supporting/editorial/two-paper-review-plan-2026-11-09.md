# Review synthesis and plan for both papers

Date: 9 November 2026. Requested scope: three agent reviews and a plan before Paper 2 experiments. This document proposes changes; it does not amend the protocol or authorize a session. The reviews are model generated judgments, not conference decisions or evidence from human readers.

## Review records

- [REFSQ reviewer](refsq-reviewer-review-2026-11-09.md): acceptance, contribution, RE relevance, gaps, and evidence.
- [Novice reader](novice-reader-review-2026-11-09.md): explanations, terms, prose, and sequence.
- [Comparison with prior REFSQ papers](refsq-paper-comparison-2026-11-09.md): published examples and transfers to these manuscripts.

Reviewed working copies:

| File | SHA256 |
|---|---|
| `mesa_paper.tex` | `4a491d889cec3ad8e0a2bf24a89fbb996757a3e257696eb2bb3a31ba6ecc9095` |
| `paper2.tex` | `8d275bfb5e682095977565f2661b099bd8605452e67c39a5b1257674bde16f9e` |

## Assessment

The reviewer recommends **weak reject for MESA** and **reject for Paper 2 as a completed submission**, in their present states. These are assessments of the manuscripts, not acceptance forecasts. REFSQ's [technical design category](https://2027.refsq.org/track/refsq-2027-research-papers) expects a requirements problem, an artifact, and evaluation; a human study is not a universal condition for this category.

MESA has a contribution in making benchmark reviews comparable and exposing how their questions and reporting rules differ. Its evidence supports findings about model generated reviews under the chosen mapping. It does not establish how engineers behave or whether their decisions improve. The mapping procedure needs more explanation, and the headline findings need the qualifications already present later in the paper.

Paper 2 has a contribution in implementing the step from a requirement and review evidence to an explained decision. The current case can demonstrate the consequences of those rules, including abstention. It cannot establish improved decision accuracy: both signed policies already withhold MESA decisions, and two coding agents provide two cases. More sessions on the same case do not remove that limitation.

The novice reader can recover both ideas but must reread to distinguish a rating level, a check outcome, an evidence status, and a score decision. The proposed sequence is one example, the problem it reveals, the method, the study, the findings, and their limits.

## State checked during this review

The working tree already contained changes to both manuscripts, the runbook, and readiness, plus untracked signed records. They were preserved.

- The requirement and nine completed form records already contain signatures dated 9 November 2026. This review created none of them.
- The signed B28a form records Verified with a failed outcome. It blocks both policies. B14a also fails under the strict policy; B12 and B14b lack performed checks.
- No `frozen_manifest.json` exists and the study ledger has no JSON entries.
- Statements that all signatures are pending are stale. Do not rerun signing to make those statements true, and do not overwrite signed records.
- Existing checks and rehearsals are not the main coding sessions. No new study session was launched for these reviews.

## Plan, in order

### 1. Set the claim that Paper 2 will test before the freeze

**Recommendation:** retain the current case and present it as an evaluation of the method's outputs and limits. Keep the known abstention result.

For RQ1, compare what each approach reports, which evidence changes the output, which tasks it removes, and why it withholds a decision. For RQ2, compare issued source decisions with the direct test where a decision exists. Report MESA's withheld decision as not comparable to an issued decision. A score decision before the evidence gate is a counterfactual output, not an issued MESA decision. Keep Inconclusive separate from no decision, and do not treat agreement as correctness.

The direct test is another measurement using maintainer tests, not ground truth for deployment suitability. A transfer record with a matching scope and signature establishes the presence of an argument, not its truth. Describe the selected seven criteria as a restricted profile; specifying the target ability does not establish task coverage.

If the intended claim remains improved decision accuracy, design a separate study with justified variation in evidence states and a basis for judging decisions. That would need a new plan before collection. Do not relax known blockers, replace this case, or choose policies to produce decisions.

**Completion condition:** paper, protocol, analysis plan, and runbook agree on the claim, outputs, comparison denominators, and handling of abstention. Any change to rules or signed inputs follows the record preservation procedure before a freeze.

### 2. Correct claims and record inconsistencies

| Paper | Change |
|---|---|
| MESA | Describe the 210 answers as a pool of unmet reporting requirements and unobserved practices. Describe the 13 as answer instances recording contradictions, not 13 independently confirmed software defects. Attribute disagreement causes to the coding interpretation. |
| MESA | Present the source audit categories together, including weaker support and contradicted absence claims. Report level plus outcome repeatability alongside level repeatability. Do not make none unsupported sound like every rating was correct. |
| Both | Distinguish model observations from human behavior and proposed use from established benefit. Bound novelty claims to the approaches actually compared. |
| Paper 2 | Report 17 mechanical exploit results separately from the six task defects admitted under the issue scope rule. Explain the nine grading checks and their limits. |
| Paper 2 | Correct the status of rating runs and signatures. Remove unsupported independence and ground truth wording; retain disclosure of shared scratch interaction, the replacement run, and the ABC prompt access. |
| Paper 2 | Define resolved once using tests, time, and session validity. Distinguish five method families from six outputs when the two MESA policies are separate; explain the coincident M1 and M2 once. |
| Both | Restore the existing repository link specified by project instructions. Do not claim an anonymous package exists when it does not. |

**Completion condition:** every headline number and claim has the same meaning in the abstract, results, discussion, and conclusion, and agrees with saved records.

### 3. Explain MESA's method and separate the papers' contributions

MESA should explain framework selection, concern construction, the author's changes to the assistant mapping, item splitting, recoding, and aggregation. Trace one source item through a concern, answer, and comparison verdict. Explain why seven frameworks are mapped but six are applied in 18 sessions. The mapping's 386 links are correct; do not change that count.

Give MESA ownership of the mapping, review representation, rubric, and model study. Present its requirements application as a proposal. Give Paper 2 ownership of the executable records, checks, requirement profile, and case evaluation. Keep enough rules in each paper for it to stand alone, but avoid presenting the same formalism as two separate contributions. Do not rewrite frozen study materials to match prose.

**Completion condition:** each introduction identifies its problem, artifact, evaluation, and contribution without depending on an unseen companion paper.

### 4. Revise explanation and flow

Use an example near the beginning of each paper. In MESA, contrast a missing scoring check with a check that finds a defect. In Paper 2, bring the SymPy task and requirement together with the distinction between source and target tasks. Reuse those examples when explaining outputs.

Add a compact terminology table. Explain that Verified records a check and its findings; its outcome can still be failed. Distinguish eight description fields, 31 evaluation questions, and 30 comparison concerns. Explain evidence status before score decision, and prose before equations.

Shorten both abstracts to the problem, method, main finding or study status, contribution, and boundary. Move launch mechanics to the replication guide while retaining sampling, exclusions, failure handling, and analysis rules in the paper. Begin each results subsection with an answer to its research question. Remove repeated claims and prescriptive practitioner boxes where the evidence supports only a proposal. RQ boxes may remain where useful.

**Completion condition:** a reader can explain the problem, contribution, study, and limits from the abstract and introduction, then follow the example without consulting repository guides.

### 5. Check the design at its actual sample sizes

Use the existing calculation method to report decision probabilities for 14, 18, and 20 tasks, not only 15 and 30 or larger samples. Label assumptions and keep these calculations separate from observations. Do not increase the sample merely to force a desired result; any change needs a scientific rationale and a recorded amendment before collection.

Check that the transfer justification, profile exclusions, target test limits, and planned treatment of invalid sessions match the claim selected in step 1. Keep fixture tests and replay as implementation checks, not validation of decision usefulness.

**Completion condition:** the plan states what each planned result could establish, including an all abstention outcome, and what it could not establish.

### 6. Recheck, freeze, then run the authorized phases

After edits, rerun manuscript and mapping checks and the tests affected by any code change. Check citations against the source claims, not just the existence of bibliography keys. Update the runbook with any procedure, code, record, or state change. Preserve signed inputs; if they need correction, use the supersession procedure and author review.

Only after the design issues are settled should the readiness and freeze steps proceed. Follow the runbook for commits, freeze, author authorization of each phase, pilot, source sessions, target sessions, and analysis. This plan does not authorize any of those actions. Preserve failures and deviations and do not change the rules after results arrive.

Replace planned text with findings from saved outputs, then reassess both papers for submission. Completing sessions alone does not establish acceptance readiness.

## Verification for this review

- `python3 verify_manuscripts.py`: no reported missing citation keys, references, or unbalanced braces in either current manuscript.
- `python3 v4/mapping/check.py`: 280 items, 30 concerns, no errors.
- `python3 -m unittest discover -s paper2/tests -p 'test_*.py'`: 181 tests passed.
- No LaTeX compilation or manuscript PDF preview. Layout and page length remain unchecked.

These checks support record and implementation consistency. They do not establish research validity, readability for people, or an acceptance outcome.
