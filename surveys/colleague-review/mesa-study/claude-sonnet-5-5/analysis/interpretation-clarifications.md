# Clarifications added after reviewing the completed study

This note supplements the original analysis. It changes no questionnaire text, expected label, raw response, exclusion, historical checklist code, or original calculation. OpenAI Codex prepared this clarification and the post hoc sensitivity calculation. This is interpretation by the assistant revising the manuscript, not independent validation. The study remains thirty conversations with one reviewer model, Claude Sonnet 5.5, and one MESA questionnaire.

## Testing occurred versus testing was thorough enough

The [MESA instructions](../materials/mesa.txt) say: “For whether something was tested, Yes means testing occurred, not that results were favourable.” The same instrument's completed HLE question-8 example says: “Partly. Expert review and later checks were conducted, but experts still disagreed about some questions or answers. This gives some support for the checks without establishing that every answer is correct.”

The instruction records the occurrence of testing, while the example also evaluates its outcome. They provide mixed guidance about whether answers concern testing that occurred or testing that was thorough enough. This tension is in the supplied materials, not evidence that the model alone failed to follow a single clear rule. The questions, explanations and teaching example were evaluated together; their individual effects were not isolated.

In the [MESA response labeled repetition 1](../outputs/real-mesa-neutral-1/response.txt), DesignQA questions 8 and 12 both receive Partly. The exact comments remain “Additional reviewers checked written questions with exceptions; errors remaining unknown.” and “Small marking-test files and scoring discussion, but no full study.” These are recorded comments, not correct answers or evidence of the model's internal reasons. The original instrument remains unchanged. Reconciling the instruction and example belongs to future work, followed by suitable evaluation of changed materials.

## P6B concerns sufficiency of evidence

P5A asks whether testing against independently established correct marks took place. The description only says no comparison is reported, so an absent report does not establish that testing never occurred.

P6B claim 1 instead asks: “The findings are sufficient for the report's stated use.” The use is identifying greater general intelligence across subjects and real-world settings, but the case supplies only grid results. Contradicted can reasonably express that the described evidence is insufficient for that use. The frozen Not established label is debatable; disagreement with it is not automatically a demonstrated reasoning error or unjustified negative finding.

All fifteen observed disagreements are mechanically Contradicted versus the frozen Not established label. Seven concern P6B claim 1, five concern P5A claim 1, and three concern C6, C7 and C8 in one EFPA-TRM conversation. The [post hoc sensitivity report](p6b-sensitivity.md) retains the original key and varies only the P6B assumption. Under that assumption MESA and EFPA-TRM both match 240/245; general instructions remain at 191/196. This illustrates key dependence, not a corrected key or a new correctness standard.

## Selected reviews are repetition 1, not the first launched

The [frozen protocol](../protocol.md) selected neutral repetition 1 for each method, both benchmarks: six reviews. Selection was fixed before execution, independent of launch order or response validity. The [launch manifest](../launches/20261017T053319.json) orders jobs for scheduling; it does not select the qualitative sample.

For example, the first launched benchmark conversation for MESA was repetition 5, and for EFPA-TRM and general instructions it was repetition 4. EFPA-TRM repetition 4 is the excluded format-invalid response, but it was never the selected qualitative response. The selected repetition-1 responses all met the required format. The manuscript now uses the response identifiers rather than the ambiguous phrase “first conversation.” No response is replaced.

## Shortcut opportunity versus observed use

The selected MESA DesignQA response states: “Drawings with scale bars all comply, so always answering yes would earn credit on that portion.” The conditional “would” already describes a possible strategy, not an observed AI behavior. A shortcut opportunity can be a benchmark-design concern even if no tested AI is shown to exploit it. The general-instruction response adds an explicit statement that no AI is shown to do this; that extra disclaimer does not establish a better conclusion.

The [original checklist coding](selected-review-observations.json) remains unchanged: MESA ten addressed and two partly addressed, EFPA-TRM and general instructions twelve addressed. The partial code for MESA's shortcut point is open to interpretation. Those historical codes should not be treated as accuracy scores or evidence of full instrument coverage. The manuscript presents concrete differences in wording and detail rather than an aggregate checklist comparison. An absent extra disclaimer is distinguished from an assertion that a tested AI actually used the shortcut.
