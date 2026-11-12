# Overview of the method and the two studies

The image `mesa_study_overview.pdf` (and `mesa_study_overview.png`) is produced by `mesa_study_overview.tex` (compile with pdflatex); the Mermaid block below is a text version with the same boxes and arrows.

```mermaid
flowchart LR
    F["Review frameworks<br/>7 frameworks<br/>280 questions"]
    C["Shared concerns<br/>30 concerns<br/>Sorted by one author<br/>Compared with an AI draft"]
    R["MESA rubric<br/>39 criteria<br/>Part A: 8 properties<br/>Part B: 31 criteria<br/>Level and outcome separate"]
    B["AI benchmarks<br/>4 benchmark snapshots<br/>HumanEval, TruthfulQA, HLE, τ-bench"]
    S1["Study 1 (RQ1, RQ2)<br/>Six frameworks, one model<br/>18 sessions<br/>Answers as three verdicts<br/>Agreement and its causes<br/>Missing information against located defects"]
    S2["Study 2 (RQ2, RQ3)<br/>Two model families<br/>Two runs per benchmark<br/>Checks: planted defects, known defects, confirmation scripts"]

    F --> C
    C --> R
    F --> S1
    R --> S2
    B --> S1
    B --> S2
```
