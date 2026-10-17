# MESA's purpose

## Who uses it and why

MESA is for researchers who need to decide whether a benchmark score supports a particular claim. A requirements engineer might ask whether a coding benchmark supports a requirement for solving software maintenance tasks. The review should identify what the benchmark tests, how it is scored, and what the available research supports.

A finished review contains a description, a source list, justified ratings, missing information, and a short explanation of supported and unsupported uses. The same benchmark may support a narrow claim without supporting a broader one.

## Thesis questions

1. How should EFPA's questions be adapted to AI benchmarks, and why?
2. What works, what is unclear, and what takes too much effort when applying MESA?
3. Does the revised MESA work as expected on new benchmarks and small examples designed to test specific questions?

The main contribution is explaining and checking the adaptation. Applying MESA is a way to learn about the framework, as well as about the benchmark.

## What to examine

| Question | Work needed | Signs of a problem |
| --- | --- | --- |
| 1 | Link MESA questions to sources and explain the changes. | No reason for a question; a human-testing assumption copied without explanation. |
| 2 | Compare the existing drafts and final reviews; record effort during later human use. | Unclear ratings, repeated work, unsupported conclusions, or missing information treated as a proven defect. |
| 3 | Keep the tested version fixed and apply it to specified examples. | A broader claim receives no extra scrutiny; stronger relevant research makes no difference; a supported narrow claim is rejected without reason. |

AI-assisted checks are labeled as such. They are not the author's measured experience or an independent expert assessment. Human completion time, agreement between reviewers, and superiority over other methods remain untested.

MESA cannot by itself certify a benchmark, prove the absence of contamination, or establish a model's capabilities. Model training, tools, and intended use also matter.

This scope implements the requested plan. It has not been approved by a thesis supervisor.
