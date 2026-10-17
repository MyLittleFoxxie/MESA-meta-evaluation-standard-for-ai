# MESA accessibility guidance: separate model experiment

This version examines proposed help for MESA's unchanged 25 questions. Accessibility means making the review easier to approach through short questions and explanations available when needed. It is a design goal, not an observed human benefit.

The pre-change baseline is local `master` commit `031437277cb0860aedc3a6bf8a353d8ac54e18f2`. New work is on `codex/mesa-accessibility`. Neither branch has been pushed. The baseline merge preserves the existing project work and a newer user-edited abstract. The earlier survey and model-study files are protected by hashes.

## Read the proposed materials

- [Static prototype](prototype.html): 25 unchanged questions with expandable revised help, optional comment prompts, closing reminders, and unchanged benchmark passages and completed HLE example. No fields, scripts, saving, tracking or submission.
- [Revised guidance](materials/revised-guidance.json): question-by-question proposed help.
- [Method reporting](analyst/standards-note.md): relevant empirical standards and remaining limits.
- [Protocol](protocol.md): conditions, comparisons, failure handling, analysis and limits fixed before runs.
- [Guidance freeze](guidance-freeze.json) and [final input freeze](freeze-manifest.json): dates and fingerprints. Guidance was frozen before assessment cases were written.
- [Execution manifest](jobs.json) and [exact inputs](inputs/): four methods, five repetitions, two batches, 40 planned conversations.
- [Expected answers](analyst/expected.json): analyst-only labels, reasons and paired comparisons, withheld from reviewer conversations.
- [Illustration checklist](analyst/real-comparison-checklist.json): twelve points for examining eight selected reviews, fixed before execution.

## What changes and what stays the same

The original and revised MESA methods share exact questions, choices, definitions, benchmark passages and HLE examples. Only question help, optional comment prompts and closing reminders differ. Comments remain optional, including in model output. No additional evidence field or second review pass is required. The live participant survey is unchanged.

The revised package adds explanation rather than reducing the original MESA word count. The model receives all help as text. This experiment does not test whether people open expandable help, how long they take, or whether the HTML is easier for them to use. Keyboard and responsive-layout checks are separate interface checks.

The other methods use the original complete EFPA-TRM and general review instructions. All four methods receive the same benchmark information and intended uses. Neutral instructions assign no reviewer identity. The requested model is `gpt-6.1-sol`, medium reasoning effort; backend revision, temperature and generation seed are unavailable. The scheduling seed controls order only.

Twenty conversations review ARC-AGI-2 followed by DesignQA. Twenty separate conversations each answer 32 claims across 16 constructed cases. The 640 planned answers repeat the same claims and are not independent test cases. The cases were prepared by the same assistant as the guidance; freezing the key is not independent validation. The earlier Sol and incomplete Astra series are preserved and are not pooled with this study.

## Saved results and verification

- [Results summary](analysis/summary.md) and [structured summary](analysis/summary.json).
- [Completed format exclusions](analysis/exclusions.md) and [manuscript traceability](analysis/manuscript-traceability.md).
- [All planned executions](analysis/runs.csv), [retained attempts](analysis/attempts.csv), and [original outputs](outputs/).
- [Answers to claims](analysis/claims.csv), [per-conversation counts](analysis/case-runs.csv), [case-family counts](analysis/families.csv), and [paired cases](analysis/paired-cases.csv).
- [MESA choices](analysis/mesa-answers.csv), [choice distributions](analysis/mesa-distributions.csv), and [repeated-choice matches](analysis/mesa-agreement.csv).
- [Illustrative review examination](analysis/illustrative-reviews.md): the assistant's interpretation of the eight fixed reviews; not a correctness reference set.
- [Input and preservation checks](analysis/verification.json) and [prototype checks](analysis/prototype-verification.json).

A completed response failing the predefined structure is retained, excluded from the structured counts, and not replaced. The selected first reviews are not replaced if invalid; any separately inspected invalid response is explicitly labeled. No independent human validation or human ease-of-use result is claimed. Execution durations and token use do not measure human effort.

## Reproduce calculations

From this directory:

```sh
python3 test_analysis.py
python3 analyze.py
python3 verify.py
python3 verify_results.py
python3 verify_manuscript.py
```

These commands inspect saved files and regenerate derived summaries; they do not launch model reviews. Browser checks use `check_prototype.cjs`, Playwright, and local Chrome, without opening the participant survey. Archived builders document how materials were generated and refuse to overwrite the frozen version.

The runner uses the existing Codex authentication, empty working directories, ephemeral conversations, disabled project documentation, memories, web search and shell tools, and at most three processes. `run_series.py --root <this-directory> --resume` schedules only unattempted jobs. `retry_failed_once.py --root <this-directory> --job <id>` allows one separately retained infrastructure retry only when no completed response exists. Do not change frozen prompts to respond to results or service failures.

No LaTeX compilation or PDF preview is part of this study. Manuscript layout and page length remain unchecked.
