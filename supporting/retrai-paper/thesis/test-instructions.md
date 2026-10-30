# Instructions for the first checks

Written on 2026-09-25 after the pilot analysis and framework edits, before recording the test results. The tested template, scorecard and guide are identified by [hashes](test-version.json). Do not change them during the checks.

## Scope and limits

The AI assistant will perform focused reading checks, not full benchmark reviews or human usability tests. No model inference, benchmark execution, or human timing study is involved. Sources for HumanEval and TruthfulQA were initially inspected to choose the cases before these instructions were written. This is not blind testing or external preregistration. The assistant has prior general knowledge of both; the author's familiarity is unknown.

HumanEval and TruthfulQA are absent from the paper's 15-benchmark list. They contrast code scored by tests with natural-language answers that may be graded by people or models. The aim is to exercise specific MESA questions, not rate either benchmark overall.

## Checks and expected behavior

| Check | Material | Expected behavior and reason |
| --- | --- | --- |
| F1: broader claim | Fictional 200-question science quiz; change only “accuracy on these questions” to “general reasoning.” | 10.6.1 should distinguish the claims. The broader one lacks evidence outside this task set. The factual description should remain the same. |
| F2: scorer study | Fictional answer grader, first with only its prompt, then with a held-out study against qualified human graders using the same rubric. The study covers the intended response types, reports disagreement and tests prompt variants. | 9.3.3 should recognize stronger support, while retaining questions about future model changes. A study of the grader should not establish broad intelligence. |
| F3: absent versus adverse study | Fictional stochastic benchmark: A publishes settings only; B also reports repeated runs whose ranking frequently reverses under the same settings, while claiming stable rankings. | 9.2.1 should use 0 for A and justify 1 for B. Both restrict a stable-ranking claim for different reasons. |
| F4: supported narrow claim | Fictional fixed quiz with a verified answer key and tested exact-match scorer. Claim only the fraction correct on that set under recorded conditions. | Accept the bounded description; do not require evidence of general intelligence or real-world transfer. Do not infer that future runs will have the same score. |
| R1: HumanEval | Official repository README and original paper abstract. Inspect score definitions, sample count, scorer pathway and run conditions. | Record what pass@k measures and the need to specify k and sampling. Distinguish executable scoring from model-output stability; do not infer general software engineering competence. |
| R2: TruthfulQA | Official repository README and original paper abstract. Inspect task scope, grading routes and claims. | Keep generation and multiple-choice scoring distinct. Route model-based grading to 9.3.3; mark it n/a for a route without model-based grading. Look for how truthfulness is distinguished from informativeness. |

## Reporting

Use “met,” “not met,” or “unclear” for each expected behavior, with a reason and missing information. Record any difficulty applying the framework. These labels assess the reading checks, not benchmark quality. Numeric ratings are used only for the fictional 0-versus-1 example; no overall rating is assigned to the real benchmarks.

Report results on the same limited source packet for each case. Absence from this packet does not establish absence from all benchmark materials. Keep source URLs, access date, and inspected sections. Do not invent human effort measurements or treat the assistant's elapsed time as reviewer workload.

## Further work

The two real cases here are partial applications. Full reviews, detailed source verification, human completion-time observations, and independent reviewers remain needed to test the whole workflow. A failed check stays in the report; any subsequent template fix requires another version and another test record.
