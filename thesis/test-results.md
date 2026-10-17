# First check results

Performed by the AI assistant on 2026-09-25 using [the written instructions](test-instructions.md) and [recorded template version](test-version.json). These are reading checks of selected questions, not six independent experiments or complete benchmark reviews. The same assistant helped revise the wording, wrote the examples, and judged the results.

## Fictional examples

| Check | Observed judgment | Result and limit |
| --- | --- | --- |
| F1 | Part A still records 200 science questions. Under 10.6.1, accuracy on those questions is a narrower claim than general reasoning. Nothing in the packet supports the latter across other domains. | Met in this reading. No numeric quality rating is needed to distinguish the claims. |
| F2 | 9.3.3 recognizes the held-out human comparison, response coverage and prompt checks as support absent from the prompt-only packet. There is still no study of future judge versions. 10.6.1 gains no support for broad intelligence from this scorer study. | Met in the full template. The scorecard lacks 9.3.3 and cannot perform that check by itself; the guide sends the reviewer to the full template. |
| F3 | Under the clarified 9.2.1, A receives 0: settings alone cannot establish stability. B receives 1 for the stated stable-ranking use: observed reversals contradict it. A's actual stability remains unknown. | Met for these examples. This does not prove that the new instruction resolves disagreements in harder cases. |
| F4 | The verified answer key and tested scorer support reporting the fraction correct on the specified quiz. 10.6.1 does not require a general-intelligence claim. Predicting future runs or performance elsewhere would need more information. | Met for the bounded description. No full benchmark endorsement follows. |

## Real examples: facts first

Sources below were accessed on 2026-09-25. Only the named sections were used. Repository pages were read at their current URLs, not pinned source commits; later changes may affect reproducibility. No evaluation code was executed.

**HumanEval.** The original paper describes evaluating code generated from docstrings. The repository runs generated completions against tests, reports pass@k and individual outcomes, and requires enough samples for the requested k. It also documents execution-environment issues. Sources: [paper abstract, v2](https://arxiv.org/abs/2107.03374v2), [official README, Usage and Known Issues](https://github.com/openai/human-eval).

**TruthfulQA.** The original paper concerns answers to questions designed around common misconceptions. The README separates answer generation from multiple-choice tasks, and truthfulness from informativeness. Generation can use fine-tuned model graders or similarity metrics. It describes validation against human judgments, warns about generalizing the graders to new questions, and records a January 2025 multiple-choice update. Sources: [paper abstract, v2](https://arxiv.org/abs/2109.07958v2), [official README, Tasks, Fine-tuning and Updates](https://github.com/sylinrl/TruthfulQA).

## Applying the selected questions

| Check | MESA application | Result and missing information |
| --- | --- | --- |
| R1: HumanEval | 3.2 records pass@k with k and the sample count. 9.2.1 keeps sampling settings separate from repeated-evaluation stability. 9.3.1 concerns the executable scorer; 9.3.3 is n/a for this scoring route. 10.6.1 keeps conclusions within the tested coding tasks. | Met as a routing and interpretation check. Passing the supplied tests is not proof of general software engineering competence. This source packet is insufficient for a full reliability rating or a review of test completeness. |
| R2: TruthfulQA | 1.2 and 3.2 require identifying the task/version and metric. 9.3.3 applies to the model-graded generation route, but not to a multiple-choice route with no model grader. 10.3.1 asks whether a truthfulness-only score rewards uninformative answers. | Met in the full template. The 2025 update makes an unspecified “TruthfulQA score” ambiguous. The claimed grader validation was not independently reproduced; numerical results and present-day API usability were not audited. |

The scorecard alone did not cover the scorer question in F2/R2. This is a concrete limit of the short form, not a defect in TruthfulQA. The guide's referral to the full template helps, but whether unfamiliar reviewers notice and follow it remains untested.

## What this adds to the thesis

The checks show how selected MESA questions can distinguish claim breadth, scorer support, and unknown versus observed instability. They do not establish overall accuracy, human agreement, or adequate coverage of either real benchmark. New case selection was outside the construction list, but the assessment was neither blind nor independent of the revisions.

No human effort measurements were collected. Full applications and a human reading check remain needed before claiming the whole procedure is usable. The tested framework was not changed after these checks.
