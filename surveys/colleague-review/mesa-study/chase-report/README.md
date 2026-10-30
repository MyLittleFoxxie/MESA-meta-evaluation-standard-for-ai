# CHASE reporting records

This directory defines the reporting selection used by `paper_chase.tex`: all ten MESA conversations from `../claude-sonnet-5-5-guidance-v2/` and all twenty EFPA-TRM/general-instruction conversations from `../claude-sonnet-5-5/`. Names of source directories are provenance identifiers. No earlier MESA development responses enter this selection.

The reporting selection was assembled after execution at the author's request. It combines sequential method batches, not a jointly randomized experiment. The source protocols and their historical reporting decisions remain untouched. [selection.json](selection.json) specifies each conversation, chosen attempt, exact input and response hashes. It includes completed invalid responses in the accounting; neither exclusions nor responses were changed.

The selected thirty conversations completed through thirty-two attempts, with twenty-eight eligible responses. See [summary.json](summary.json), [selected reviews](selected-reviews.md), and [manuscript traceability](manuscript-traceability.md).

## Reproduce

```sh
python3 surveys/colleague-review/mesa-study/chase-report/analyze.py
python3 surveys/colleague-review/mesa-study/chase-report/verify.py
```

The analyzer reads source records and writes exports only in this directory. It validates response structure and isolation, uses the retained retry decision for synthetic authentication failures, and computes descriptive counts and the P6B sensitivity calculation. No models or submission services are called. `qualitative-audit.json` and `selected-reviews.md` contain assistant interpretations with exact response excerpts; those judgments are not produced by the numerical analyzer.

The earlier author check covers the four comparison-method reviews here as part of a six-review set. The author reviewed the two MESA responses against the supplied passages, checked their interpretation, and reviewed the expected answers, including the disputed P6B label. These author checks do not constitute independent validation or separate coding. Historical source files, the live survey, and the other manuscripts remain preserved. No LaTeX compilation or PDF preview is used.
