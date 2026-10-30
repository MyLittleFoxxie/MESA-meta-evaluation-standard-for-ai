# Review of repository discrepancies reported by the Claude batch

Prepared on 30 October 2026 by the assistant that ran the Claude batch (Claude Fable 5.1, the same model as the reviewer), in response to external feedback asking that each reported discrepancy be checked for version, scope and consequence. The check reads the frozen snapshots offline. No benchmark code was executed, no later repository version was fetched, and no human author has confirmed these readings. Each entry records what the code does, what the documentation says, the assessed scope, and what remains unverified.

Snapshots are those in [sources.json](../../sources.json), retrieved on 30 October 2026: HumanEval at commit `b9453e8f1865`, TruthfulQA at `d71c110897f5`, DesignQA at `dd909455afb9`. Line numbers refer to the files under `v3/study/sources/<benchmark>/repository/`.

## 1. HumanEval: execution line described as commented out is active

- Reported in: `humaneval-repository-1` and `humaneval-repository-2`, criterion A1 (both rated 10), and A5 in repetition 1.
- Code: `human_eval/execution.py` line 50 reads `exec(check_program, exec_globals)` with no comment marker. Lines 40 to 49 contain the warning text that asks users to uncomment the line.
- Documentation: `README.md` lines 28 to 31 state that the execution call "is deliberately commented out to ensure users read this disclaimer", and line 33 says to enable execution before generating samples. README line 40 names `data/example_solutions.jsonl`; the snapshot's `data/` folder contains `example_samples.jsonl`, which the README's own command at line 78 uses.
- Assessed scope and consequence: the shipped harness in this snapshot runs model generated code without the manual edit the README describes. Scores are not affected; the mismatch concerns the safety notice and the setup instructions. The README banner also marks the repository as unmaintained, so the documentation may describe an earlier state. Whether the line was commented out in an earlier commit was not checked.
- Reviewer reasoning: both repository responses used the mismatch to withhold anchor 15 for A1 because no execution for this edition is documented, and repetition 1 recorded the file name error as an A5 limit without lowering the rating. That reading is consistent with the anchors.
- Unverified: execution behaviour, the commit history of the line, and whether the README has since been corrected.

## 2. TruthfulQA: a fixed reference answer is appended during generative scoring

- Reported in: `truthfulqa-repository-1`, criterion A2 (rated 10), described as undocumented.
- Code: `truthfulqa/metrics.py` lines 222 to 223, inside `run_bleu_and_rouge`, append the string "I have no comment." to the list of true reference answers when it is not already present. The comment at line 220 says this is for generative metrics only. The same three lines appear in `run_finetuned_GPT3` (lines 115 to 116) and `run_BLEURT` (lines 308 to 309), so the appended reference is used by every reference comparison metric for generated answers (GPT-sim, BLEU, ROUGE and BLEURT). The end to end judge in `run_end2end_GPT3` scores the answer without reference lists and is unaffected.
- Documentation: the paper (Section 2.1, extracted text lines 262 to 268) defines non-committal answers such as "No comment" as true, and the README objective paragraph (line 47) says a model answering "I have no comment" to every question would be perfectly truthful and therefore uses informativeness as a secondary objective. Neither the README nor the paper describes the implementation step of adding the string to the reference list.
- Assessed scope and consequence: the behaviour implements the paper's stated definition for the similarity based generative metrics; a non-committal model output can match the appended reference and score as true on BLEU, ROUGE and BLEURT difference metrics. This is not a scoring rule violation. It is an undocumented implementation detail that a reader comparing code with the README's metric description would not expect, and it does not affect the multiple choice metrics, which are computed in `models.py`.
- Reviewer reasoning: the response called the step undocumented and still rated A2 at 10 because the main rules match. The present reading agrees that it is undocumented and adds that it is consistent with the construct definition, which the response did not say.
- Unverified: effect sizes on reported scores; whether later versions document the step.

## 3. DesignQA: the similarity metric is commented out

- Reported in: `designqa-repository-1`, criteria A1 and A2 (both rated 10).
- Code: `eval/metrics/metrics.py` lines 412 to 415 contain the sentence transformer similarity computation as comments. `eval/full_evaluation.py` writes no similarity value.
- Documentation: the paper describes a Similarity metric based on `sentence-transformers/all-MiniLM-L6-v2` (Section 3.2.3) and reports it in Table 2. Older per subset result files in `eval/rule_compliance/` contain a "Macro similarities" line, which indicates that the metric was computed by an earlier version of the code.
- Assessed scope and consequence: the Similarity column of Table 2 cannot be regenerated from the shipped evaluation entry point in this snapshot. The other metrics are unaffected. This is a reproducibility gap for one reported metric, not evidence that reported values are wrong.
- Reviewer reasoning: the response treated this as a reproducibility limit rather than an anchor 0 violation. Anchor 0 requires an inspected discrepancy that violates the documented rule; a missing metric is a different kind of defect, and the rubric does not name it. The present reading agrees that the rubric wording leaves the choice open.
- Unverified: whether a separate script in the repository or supplement computes similarity; whether later commits restore it.

## 4. DesignQA: the overall score divides by a fixed six

- Reported in: `designqa-repository-1`, criterion A2 (rated 10).
- Code: `eval/full_evaluation.py` lines 8 to 19 make every subset path optional with default `None`; lines 40 to 64 append a subset average to `all_subsets` only when its path is given; line 71 writes `sum(all_subsets) / 6`; lines 74 to 79 print `N/A` for subsets that were not supplied.
- Documentation: `README.md` lines 48 and 53 define the overall score as the simple unweighted average across all six segments.
- Assessed scope and consequence: with all six subsets supplied the code matches the README. With fewer subsets the overall line reports a value divided by six rather than by the number of subsets, which understates the average of the supplied subsets while the per subset lines correctly show `N/A`. The consequence is limited to partial invocations, which the README does not describe as a supported use. This is not a bug for the documented use and not evidence about reported results.
- Reviewer reasoning: the response listed it among four findings and did not claim it affected the paper's results. That is consistent with this reading.
- Unverified: whether the authors intend partial runs to be meaningful.

## 5. HumanEval and DesignQA: smaller observations

- `designqa-repository-1` reported that `eval_definition_qa` in `metrics.py` normalizes the prediction but not a ground truth that contains no semicolon (line 242). The line appends the unnormalized ground truth characters. Scope: Definition QA items with a single synonym and characters affected by normalization. Consequence not assessed; it would require running the metric on the data.
- `designqa-repository-1` and `designqa-repository-2` reported that imports in the per subset inference scripts (for example `eval/rule_compliance/dimension_evaluation.py` lines 1 to 2) name packages absent from `requirements.txt`, and that API token fields are blank. This concerns regenerating model predictions, not scoring, and the README does not claim to cover inference.

## What this record does and does not establish

The readings above confirm that the cited lines exist as described in the frozen snapshots and assess scope from the code and documentation. They do not establish effects on any reported benchmark score, because nothing was executed, and they do not establish the state of any later repository version. A discrepancy between code and documentation is evidence for A1, A2 or A5 judgments about this edition; it is not by itself a judgment about the benchmark's results or about the ratings the reviewer assigned. Independent author checking of this record has not occurred.
