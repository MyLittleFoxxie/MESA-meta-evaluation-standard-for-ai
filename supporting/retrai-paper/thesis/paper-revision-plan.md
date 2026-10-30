# Plan for paper.tex

## Focus

Present MESA as a completed conference contribution: **an adaptation of EFPA for reviewing AI benchmarks, illustrated through three case studies**.

Explain the framework, its basis, what the applications show, and the limits of those findings. Omit template history, editing decisions, and accounts of wording changes. The broader thesis research plan stays outside this paper.

## Research questions

1. How can EFPA's review model be adapted to AI benchmarks?
2. What does applying MESA reveal about the claims supported by HLE, ARC-AGI-2, and DesignQA?
3. What do these applications show about MESA's usefulness and limits?

The third question concerns what the cases demonstrate, not measured time savings or independent validation.

## Section plan

| Section | What to present |
| --- | --- |
| Title | **MESA: Adapting the EFPA Test Review Model for AI Benchmarks.** |
| Abstract | The problem, the adaptation, the three applications, the main finding, and the validation limit. |
| Introduction | Who needs benchmark review and what decision MESA helps them make. State the contribution and research questions. |
| Related work | EFPA supplies the review structure; BetterBench supplies engineering concerns; AGI/CHC and construct-validity literature help assess capability claims. Explain how MESA combines these. |
| Methodology | How the adaptation was derived, why the cases were selected, what sources were used, and how the AI-assisted reviews were produced and checked. Describe only work actually performed. |
| MESA framework | Part A, Part B, the rating meanings, and one short worked example. Add a small table explaining representative EFPA-to-AI adaptations. |
| Case studies | For each benchmark: what it measures, the main supporting evidence, the important gaps, and what its scores support. Keep detailed reviews in the supporting materials. |
| Discussion | Explain what MESA makes visible in the cases and where reviewer judgment remains necessary. Answer the research questions without treating completed reviews as proof of validity. |
| Limitations | Three cases, overlap with the benchmarks used during construction, AI-assisted judgments, and no independent human validation or measured reviewer workload. |
| Future work | Briefly propose expert review, studies of reviewer agreement, and measurement of review effort. |
| Conclusion | State the contribution and what the cases demonstrate. Avoid claims of certification readiness or universal benchmark quality measurement. |

## Material to remove from the current paper

- The “Artifact Evolution” subsection and discussion of template versions, file hashes, retired item IDs, and historical wording.
- The account of instruction edits and the step-by-step revision process.
- The new fictional examples and partial HumanEval/TruthfulQA checks as research results. Keep them in research notes rather than adding another study to this conference paper.
- References to local working folders, unfinished repository work, and the author's next editing tasks.

Rating disagreements may illustrate the need for reviewer judgment, but should not become a separate agreement study unless the paper provides a suitable method and analysis.

## Two useful tables

- **Adaptation:** EFPA concept → AI counterpart → reason for the change.
- **Case findings:** benchmark → supported use → missing support → limit on interpretation.

Keep the rating table only if it adds information beyond the case findings. Explain that the ratings are contextual judgments, not a ranking of benchmarks.

## Final checks

Use brief, plain prose. Ensure every conclusion has support, describe AI involvement accurately, and cite only supporting materials available to readers. Any difference between the framework described and the reviews must be resolved before presenting them as one study; the paper does not need a history of that work.

**Order:** settle the research questions, organize methods and case findings around them, then write the abstract and conclusion. This plan does not make further edits to `paper.tex`.
