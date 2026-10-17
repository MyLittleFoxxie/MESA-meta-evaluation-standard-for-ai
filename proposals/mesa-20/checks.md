# Checks of draft 0.1

2026-09-29. AI-assisted checks by the same assistant that drafted the questions. These are not independent ratings, human trials or fresh benchmark audits. No benchmark code was run. No new numerical Part B ratings were assigned.

## Item coverage

The [mapping](coverage-map.md) gives a primary destination for all 44 active descriptive units and 87 rated items in the current MESA template. It also accounts for unnumbered opening/closing sections and four retired IDs. This is a structural check, not a finding that the grouped questions retain equal detail or elicit the same judgments.

The existing 40-item scorecard omits direct scorer checks (§9.3). MESA-20 restores that topic explicitly in Q9. The current proposal also retains score structure (Q8) and public reporting (Q19), which need attention beyond counting the low ratings in three historical pilots.

## Every recorded pilot gap has a destination

The tables below cover the complete gap registers: 7 entries for HLE, 10 for ARC-AGI-2 and 8 for DesignQA. Names are shortened. Each row is a topic recovered from the old review, not an endorsement of its wording or current factual accuracy. The question explanations explicitly invite the corresponding investigation; this does not establish that an unaided reviewer would perform it.

### Humanity's Last Exam

Source: [reconciled HLE review](../../reviews/gemini_supervising_editor/Humanitys-Last-Exam.md), Gap Register and cited item sections.

| Existing gap | MESA-20 destination | Finding of this reading |
| --- | --- | --- |
| Judge validation | Q9 | Explicit expert checks; naming the judge alone cannot establish support. |
| Confidence intervals | Q12, Q19 | Separates having precision evidence from communicating it. |
| Repeated runs | Q11 | Requires observed variation rather than settings alone. |
| Matched human reference | Q10 | Applies to human-level claims; no universal human-baseline requirement. |
| Answer-key corrections | Q6, Q9, Q18 | Separates task checking, scoring and correction/version history. |
| Public caveats | Q19, Q20 | Separates the benchmark's reporting from the reviewer's recommendation. |
| Changes to task sets | Q11, Q18 | Requires evidence or limits on comparison across changed versions. |

Positive finding retained: the review describes expert-authored academic tasks and accessible evaluation materials. Q6 and Q17 can recognize these strengths without supporting an AGI interpretation in Q20.

Correction retained: the historical review's missing judge study becomes an unresolved support question under Q9, not automatic proof of bad judging. Its claims about small differences being statistically meaningless are not copied. The first draft also mentions a confidence-interval calculation in scorer code (§9.2.2), so Q12 and Q19 must distinguish computation from display and investigate the actual source before drawing a present-day conclusion.

### ARC-AGI-2

Source: [reconciled ARC review](../../reviews/gemini_supervising_editor/ARC-AGI-2.md), Gap Register and cited item sections.

| Existing gap | MESA-20 destination | Finding of this reading |
| --- | --- | --- |
| Confidence intervals | Q12 | Keeps small-comparison precision visible. |
| Conflicting attempt limits | Q3-Q4, Q19 | Records the contradiction; does not choose one rule without evidence. |
| Different evaluation cohorts | Q16, Q19 | Requires condition labels and interpretation limits. |
| Relations with other measures | Q15 | Needed for claims beyond the recorded grid tasks. |
| Task-category information | Q7-Q8, Q13 | Retains coverage, score structure and error-analysis questions; detailed labels need an expanded note. |
| Prompt/grid format | Q3, Q11, Q13, Q17 | Separates reproduction from sensitivity and unrelated format effects. |
| Repeated runs and seeds | Q11 | Attempt allowance is not repeated-run stability. |
| Test-time training policy | Q14, Q16 | Distinguishes permitted adaptation from unfair exposure or unmatched conditions. |
| Item outputs and audit traces | Q17, Q19 | Accepts justified controlled audit access rather than demanding public hidden answers. |
| Simple-strategy references | Q10 | Distinguishes meaningful task difficulty from doing better than an unspecified floor. |

Positive finding retained: the review describes task curation, human references and grid exact-match scoring. Q6, Q10 and Q8 keep these separate strengths visible.

Correction retained: the historical statement that exact matching is “perfectly reliable” does not establish implementation correctness. Q9 still requires scorer checks. The gap-register claim that one task out of 120 equals 1% is also inexact: it is about 0.83 percentage points. No statistical conclusion follows merely from that increment or from the absence of intervals.

### DesignQA

Source: [reconciled DesignQA review](../../reviews/gemini_supervising_editor/DesignQA.md), Gap Register and cited item sections.

| Existing gap | MESA-20 destination | Finding of this reading |
| --- | --- | --- |
| Score uncertainty | Q12 | No inference that unmeasured small differences are necessarily noise. |
| Repeated runs | Q11 | A narrow repeated experiment does not cover all model/condition combinations. |
| Human reference scores | Q10, Q15 | Relevant to human/engineering-performance claims; judge the actual intended use. |
| Exposure controls | Q14 | Public rules are intended task context in some conditions; distinguish that from access to test answers. |
| Metric validation and formats | Q8-Q9, Q13 | Separates what the metric rewards from scoring errors and format effects. |
| License and documentation | Q17 | Records access/reuse terms without issuing a legal opinion. |
| Versions and reproduction | Q17-Q18 | Separates usable replication assets from change comparability. |
| Leaderboard rules | Q19 | Missing or inaccessible reporting is documented, not silently passed. |

Positive finding retained: expert-written, real engineering-document tasks can support a bounded diagnostic use through Q6-Q7. Q15/Q20 do not require general engineering coverage to recognize that strength.

Correction retained: the old conclusion's recommendation to treat small differences as noise is too strong without the relevant analysis. Nor is a large gap automatically reliable. Q12 requires evidence matched to the actual comparison. Historical license observations are not presented as current legal conclusions.

## Eight contrasting reading checks

These small fictional evidence packets were written and judged during development. The result is an observed reading of the draft, not a measured success rate. Sources for the expected distinctions are the current MESA rating guidance and the guide in this folder.

| Packet and intended use | Expected distinction | Observed reading |
| --- | --- | --- |
| A judge prompt is available but no study; claim is accurate grading. | Unknown, not demonstrated error. | Q9: Unknown; Q20 cannot endorse grading accuracy as established. |
| Same task, with representative expert comparisons supporting accuracy for the stated use. | Added evidence should improve the judgment. | Q9 can be Supported for that route; unrelated broad claims receive no extra support. |
| A deterministic grid scorer has no tests. | Determinism does not establish correctness. | Q9: Unknown; AI-judge checks are inapplicable, not the whole question. |
| Repeat studies show reversals larger than the difference used to choose a winner. | Demonstrated inadequacy differs from no study. | Q11/Q12: Weakness for a stable-winner claim. |
| Only settings are published for that same claim. | Unknown differs from observed instability. | Q11: Unknown; Q20 leaves the winner claim unsupported. |
| A checked 200-question science test is used only to describe its recorded responses; alternatively it is advertised as general intelligence. | Broader use requires more evidence. | Q7/Q15/Q20 expand for the broad claim. Narrow scope is not itself a defect. |
| Old and new live cohorts use different tasks with no comparison study. | Dates and labels alone do not establish equivalence. | Q18: Unknown for cross-cohort comparison, even if version documentation is supported. |
| A fixed task has no alternate form and no live service. | Relevant absence can justify Not applicable only for that portion. | No alternate-form check is needed; scorer correctness and relevant repeated-run questions remain. |

## Wording/workload check

There are exactly 20 numbered question headings and fifteen judgment slots. None is a separately numbered checklist of hidden ratings. Nevertheless, several questions are compound at the evidence level. Q9 combines scorer types; Q10 combines references; Q11 combines variation sources; Q16 combines access and group evidence; Q17 combines availability, usability, reproduction and terms. Their notes must retain consequential differences, and the guide provides expansion routes.

No reading formula or heading count can establish ease of use. The draft uses some unavoidable technical words, such as scorer, uncertainty and version, with examples in the surrounding text. Human comprehension and workload must be measured using [validation-plan.md](validation-plan.md).

## Mechanical checks

Run `python3 proposals/mesa-20/verify.py` from the repository root. It checks question/answer counts, current item-map completeness, mapping destinations, the 25 pilot gap entries, local Markdown links, and preservation of the 106 inventoried source files. It reports word counts as whitespace-separated tokens; these are not page counts or completion times. It does not assess scientific validity or factual correctness of every source.

Completed 2026-09-30: all listed mechanical checks passed. The questionnaire contains 1,220 words and the guide 1,215, for 2,435 combined. The full template has 21,488 and the existing scorecard 14,222 by the same counting rule. All 106 source hashes still matched, including the current template and nine original reviews. The repository already had unrelated working-tree changes before this task; this proposal did not overwrite them.
