# Recoding answers into three outcomes

Status: declared before any agent session, 31 October 2026; reviewed and finalized by the author on 31 October 2026. These rules turn any framework's answer to an item into one of three outcomes per shared concern, so that frameworks with different scales can be compared. The original answer is always kept next to the outcome.

## The three outcomes

- **Favorable.** The framework's answer says the concern is met to that framework's own standard.
- **Unfavorable.** The framework records a defect, or records an absence as a negative finding.
- **Unresolved.** The framework records missing information, uncertainty, inapplicability or insufficient evidence, or its answer gives no verdict.

There are three outcomes and no fourth. Markers travel beside an outcome: **partial** on a favorable outcome that rests on a middle score or a Stated or Shown anchor, **not applicable** on an unresolved outcome, and **unresolved by rule**, which is set when a framework's own rule turns an absence into a negative answer. The outcome is still recorded as the framework gives it (unfavorable), and the marker says that the same absence would be unresolved under a framework that keeps missing information apart. RQ3 counts these markers.

## Per framework

| Framework | Answer | Outcome | Marker |
|---|---|---|---|
| BetterBench | 15 | favorable | |
| BetterBench | 10 | favorable | partial |
| BetterBench | 5 | unfavorable | unresolved by rule: acknowledged but not addressed is a score, not a finding of a defect |
| BetterBench | 0 with an explanation that says the item is absent or not documented | unfavorable | unresolved by rule |
| BetterBench | 0 with an explanation that names a defect | unfavorable | |
| BetterBench | n/a | unresolved | not applicable |
| ECBD | describe question with content | favorable for the describe part of the concern | |
| ECBD | describe question answered "not stated" or equivalent | unresolved | |
| ECBD | justify question with a reason given by the creators | favorable | |
| ECBD | justify question answered that no reason is given | unresolved | ECBD records the absence, it does not score it |
| ECBD | support question with evidence named | favorable | |
| ECBD | support question answered that no evidence is offered | unresolved | |
| ECBD | any question whose answer reports a contradiction or a problem found | unfavorable | |
| Scorecard | satisfied | favorable | |
| Scorecard | unsatisfied with a justification that names a defect | unfavorable | |
| Scorecard | unsatisfied with a justification that says the documentation is vague or absent | unfavorable | unresolved by rule |
| Scorecard | not applicable with a reason | unresolved | not applicable |
| How2Bench | present | favorable | |
| How2Bench | not mentioned | unfavorable | unresolved by rule: the authors group not mentioned with not done |
| How2Bench | a reviewer's note that the practice was done wrongly | unfavorable | |
| Agentic Benchmark Checklist | 1 | favorable | |
| Agentic Benchmark Checklist | 0 with a reason that names a defect | unfavorable | |
| Agentic Benchmark Checklist | 0 with a reason that says the benchmark does not document or address the item | unfavorable | unresolved by rule |
| Benchmark Caliper | 4 or 5 | favorable | |
| Benchmark Caliper | 3 | favorable | partial |
| Benchmark Caliper | 1 or 2 | unfavorable | unresolved by rule when the rubric text says the low score comes from silence in the documentation |
| Benchmark Caliper | Unknown | unresolved | |
| OECD facets, facet with a preferred value | preferred value | favorable | |
| OECD facets, facet with a preferred value | other value | unfavorable | |
| OECD facets, Reliability | N/A | unresolved | the chapter allows N/A when the methodology is unclear |
| OECD facets, descriptive facet | any value | not recoded | reported as a description under C30 |
| New rubric | rated at the top anchor | favorable | |
| New rubric | rated at Stated or Shown | favorable | partial |
| New rubric | rated at the lowest anchor because a defect was found | unfavorable | |
| New rubric | insufficient evidence | unresolved | |
| New rubric | not applicable with a reason from the description part | unresolved | not applicable |

## Aggregating items to a concern

A concern usually has several items from one framework. The concern outcome for that framework on that benchmark is:

- unfavorable if any mapped item is unfavorable;
- otherwise favorable, without a marker, if every mapped item is favorable and none carries the partial marker;
- otherwise favorable with the partial marker if at least one mapped item is favorable;
- otherwise unresolved.

Agreement between frameworks is counted on the three outcomes; a stricter count that also requires the partial marker to match is reported beside it. Items whose answerability column in `questions.json` begins with "no" (three items among the applied frameworks, `BB-45`, `BB-46`, and `H2B-45`, plus three porting action items in unapplied Benchmark Caliper, `CAL-IC-4`, `CAL-OO-4`, and `CAL-OC-4`) are recorded but left out of concern outcomes and agreement counts. Because item counts per concern differ between frameworks, a framework with many items on a concern reaches unfavorable more easily than one with a single item; this is a structural source of disagreement and is coded as scope or threshold in the disagreement log.

The marker "unresolved by rule" carries up to the concern if the unfavorable outcome came only from marked items.

## What the rules do not do

- They do not say whether a framework's answer is correct.
- They do not convert a framework's score into another framework's score.
- They do not treat not applicable as favorable or as unfavorable.
- They are frozen before the sessions; a gap found when recoding the existing framework applications (step 3 of the checks) is fixed and logged before the freeze, not after.
