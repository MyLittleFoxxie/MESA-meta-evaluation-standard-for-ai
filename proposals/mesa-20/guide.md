# How to use MESA-20

Draft 0.1, 2026-09-29. Read alongside the [20 questions](questionnaire.md).

## Start with a decision

Choose the exact benchmark, version and use. “Does this result support choosing model A over B for these tasks?” is more useful than “Is this a good benchmark?” A review may support a narrow use and reject a broader one.

Answer Q1-Q4 with facts first. For later questions, record any additional facts in the evidence part of the note before making a judgment. Reuse source IDs. Check papers against the actual materials where available. Label a documentation-only inspection as such; do not imply that you ran the benchmark.

Identify which findings would change the decision in Q2. These are critical findings. Declare likely critical areas before rating, then record reasons for any later change. This avoids selecting them merely to obtain a preferred conclusion.

## Choose an answer

| Answer | Meaning | Link to the EFPA/MESA scale |
| --- | --- | --- |
| Supported | Relevant evidence is enough for this aspect of the stated use, with the limits you name. | Combines 2, 3 and 4. It does not retain their differences. |
| Weakness | Available evidence shows a problem that makes this aspect inadequate for the stated use. | 1 |
| Unknown | Available evidence is absent, inaccessible, conflicting or insufficient to decide. | 0 |
| Not applicable | This issue does not arise for the stated use; explain why. | n/a |

This is a proposed scale, not a validated conversion of past ratings. EFPA permits collapsing categories if inadequate and adequate remain distinguishable and the mapping is given (EFPA PDF p. 18, PDF page 23; [source notes](sources.md)). Do not reconstruct a 2, 3 or 4 from Supported.

**Supported requires a reason about the evidence, not just the existence of a document.** For example, software tests need to cover consequential scoring cases; repeated runs need to address variation that matters to the claimed use. There is no universal number of runs or agreement threshold in this draft. State why the evidence is enough for the decision. If you cannot judge a critical technical issue, record Unknown and seek the relevant expertise.

For mixed evidence, name the supported part and the unresolved or weak part. Give Weakness if a demonstrated problem defeats the question's purpose for the stated use. Otherwise give Unknown if necessary evidence is missing. Use Supported only when the remaining limits do not defeat that purpose. Never hide a critical gap behind strengths elsewhere. Separate findings within a note when a benchmark has multiple scoring routes or task groups.

Examples:

- A judge is named, but no relevant checks are available: Q9 **Unknown**. This does not prove the judge is inaccurate.
- Testing finds frequent scoring errors that reverse the intended comparison: Q9 **Weakness** for that comparison.
- Representative expert checks support the scorer for the specified task, with remaining limits that do not defeat that use: Q9 **Supported**.
- A test has no AI judge: the AI-judge part of Q9 is inapplicable, but Q9 still applies to its actual scorer.
- No human baseline is available: this is an unresolved gap in Q10 if the claim is human-level performance. It need not block reporting a bounded task score with another suitable reference.

Q5-Q9 and Q17-Q19 normally apply to any benchmark review. An absent mechanism only makes the relevant portion inapplicable: no leaderboard still leaves paper reporting in Q19; no updates still leaves fixed version identity in Q18. Q10-Q16 depend on the intended interpretation, but absence of a study is not a reason to mark a relevant question Not applicable.

## Keep the note short but checkable

Use one note per judgment: **what was found and where; why it supports the answer; what remains missing or limited; what this changes for use**. “S3, scorer tests: only well-formed outputs tested; malformed responses occur in the intended task; scorer behavior on them is unknown; comparison remains provisional.”

Q8 examines the scoring rule's meaning. Q9 examines whether the scorer applies it correctly. Q13 examines alternative ways to obtain a score. Q11 concerns repeated results; Q12 concerns the precision needed for a decision. Related evidence can be cited once and reused, but these are different judgments.

A missing study and a missing instruction are not identical. No repeat-run study leaves actual stability unknown. An inspected instruction sheet that gives contradictory attempt limits demonstrates a documentation problem, even if its effect on scores remains unknown. Record both facts.

## Finish without a total score

In Q20, weigh findings against the use in Q2. A critical Weakness or Unknown prevents recommending that use as established. Explain whether limited research or expert-supervised exploration remains reasonable. An Unknown blocks confidence in a use without proving that the instrument fails in reality. A critical weakness cannot be cancelled by several Supported answers.

The evidence gaps already recorded under Q5-Q19 serve as the gap record. In Q20, name the gaps that change the recommendation and the evidence needed to resolve them. A separate gap table is optional; it adds workload and is not part of the 20-question count.

## When the short answer is not enough

Use fuller analysis when the question combines materially different findings or a decision depends on a specialized method. Record the trigger and the added work. The short form is not a promise of the same workload for every benchmark.

| Trigger | Expand using the current full MESA template |
| --- | --- |
| Multiple scorers or an AI judge | Q9: 9.3.1-9.3.3; inspect each consequential route and judge change. |
| A combined ability score or claimed sub-abilities | Q8: 10.2.1; Q7: 10.1.2; examine the proposed structure and weighting. |
| Small ranking differences or a pass/fail decision | Q10-Q12: 8.1.5, 9.2, 9.5.1; examine the uncertainty method and decision threshold. |
| Live tasks, new versions, translations or derived tests | Q6/Q11/Q18: 6.1.8, 9.4.2-9.4.3, 11.3.3; check comparability instead of inheriting evidence. |
| Broad intelligence, deployment or safety claims | Q7/Q15/Q20: 10.1, 10.4, 10.6.1; require evidence across the claim's scope. |
| Different languages, systems or affected user groups | Q16: Section 11; check group-specific evidence and human impacts where relevant. |
| Restricted data, sensitive content or consequential reuse limits | Q17: 7.1.7, 11.5.2; inspect the relevant access, privacy and use safeguards. |
| Conflicting reports or complex leaderboard rules | Q19: Section 12; identify each consequential reporting surface separately. |

These are referrals, not automatic additional ratings. If expanded, describe the result as “MESA-20 with additional analysis.” If the full item-level profile is required, use the full template.

## Turn the answers into a readable review

For a standalone narrative, reuse the answers under five headings: **Description** (Q1-Q4), **Development** (Q5-Q7), **Technical evidence** (Q8-Q18), **Commentary** (consequences and Q19), and **Summary** (Q20). This adapts Buros's organization; it is optional and should replace repetitive answer prose, not add a second compulsory report. Preserve question/source references for audit.

The two supplied Buros examples show how an account can retain strengths, gaps and use limits in connected prose. They do not establish the accuracy or completeness of this new checklist. This is an independent MESA proposal, not a Buros review or endorsed instrument. See [sources](sources.md) for attribution and scope.
