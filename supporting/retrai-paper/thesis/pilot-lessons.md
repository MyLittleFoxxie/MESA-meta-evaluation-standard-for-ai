# Lessons from the existing reviews

This is an AI-assisted analysis of past drafts, not a fresh audit of the benchmarks' current websites. The [rating table](pilot-ratings.md) preserves all 21 section comparisons. The drafts differ in seven. No agreement statistic or correctness claim follows from that count.

## Findings and changes

| Observation | What it reveals about MESA | Change |
| --- | --- | --- |
| HLE 9.6 is 2 in the first draft and 1 in the second and final review. The first draft discusses broad directional use; the final review stresses small ranking differences. | The judgment may concern different uses. This is a plausible explanation from the text, not a known cause of the reviewers' behavior. | State the exact use beside each disputed rating before resolving it. |
| ARC-AGI-2 9.2.1 is 2 in the first draft, which cites configurable settings, and 1 in the second. The editor notes that pass@2 is not a stability measurement. | Settings and allowed attempts can be confused with measured stability. | Clarify 9.2.1: settings alone do not show how much scores vary. |
| Several pilot items rate missing run evidence as 1. The template distinguishes insufficient information (0) from demonstrated inadequacy (1). | The boundary needs a concrete example. | Require an explanation of what is actually known to be inadequate when assigning 1. |
| The HLE final review says small differences are statistically meaningless; the DesignQA final review says to treat small gaps as noise. | Missing uncertainty estimates do not establish that a particular difference is noise. | Describe the comparison as unresolved; remove unsupported numerical or categorical conclusions from the paper. |
| ARC-AGI-2's final 9.6 rationale calls its exact-match scorer “perfectly reliable.” | Deterministic rules alone do not establish error-free implementation. | Separate deterministic scoring, parser correctness, and variation in model outputs. |
| DesignQA's final review gives 3 to content validity (10.1.1) and supports bounded diagnostic use. | MESA can record positive support as well as limitations in this example. | Preserve the positive finding and avoid requiring broad intelligence coverage for a narrow claim. |
| Original ratings and reconciled ratings coexist in separate files. | Reconciliation resolves a review; it does not erase initial disagreement. | Keep the drafts and identify the basis for each change. |

Sources: items 9.2.1 and 9.6 in the [HLE drafts](../reviews/chatgpt_reviewer1/Humanitys-Last-Exam.md), [Claude HLE draft](../reviews/claude_reviewer2/Humanitys-Last-Exam.md), and [final HLE review](../reviews/gemini_supervising_editor/Humanitys-Last-Exam.md); the same items in the [ARC first draft](../reviews/chatgpt_reviewer1/ARC-AGI-2.md), [second draft](../reviews/claude_reviewer2/ARC-AGI-2.md), and [final review](../reviews/gemini_supervising_editor/ARC-AGI-2.md); items 9.2.2, 9.6, 10.1.1 and the final evaluation in [DesignQA](../reviews/gemini_supervising_editor/DesignQA.md).

## What remains unknown

No comparable human completion-time records were found in the materials inspected. The earlier hour estimates in `feedback/80-xcut-length-budget.md` are estimates, not observations. This analysis checks the reasoning visible in the drafts; it does not independently verify every benchmark fact. The original reviews are preserved, including statements now flagged for caution.
