# Manuscript findings and source records

| Manuscript statement | Saved evidence | Boundary |
| --- | --- | --- |
| Accessibility is a design goal; questions and choices are unchanged | [Revised guidance](../materials/revised-guidance.json), [source/freeze checks](verification.json), [static prototype](../prototype.html) | No human ease or effort measured |
| 40 conversations completed, 31 usable, nine structural exclusions | [Run accounting](runs.csv), [attempts](attempts.csv), [exclusion list](exclusions.md) | No invalid response repaired or replaced |
| 160/160 expected answers per method; 640 total | [Claims](claims.csv), [per-conversation counts](case-runs.csv), [family counts](families.csv) | Same 32 claims repeated; same-assistant key |
| 320 paired-claim comparisons match expectations | [Related cases](paired-cases.csv) | Dependent within and across conversations |
| 0/120 unjustified endorsements of selected negative claims | [Claims](claims.csv), negative_conclusion and unjustified_negative_support columns | Not an error rate for complete review prose |
| 640 quoted excerpts found in passages | [Claims](claims.csv), quote_found column | Location is not semantic correctness |
| Original MESA 200 usable choices, 10 variable pairs, 270/300 matching comparisons | [Distributions](mesa-distributions.csv), [agreement](mesa-agreement.csv) | Four usable conversations, dependent answer pairs |
| Revised MESA 100 usable choices, three variable pairs, 47/50 matching comparisons | [Distributions](mesa-distributions.csv), [agreement](mesa-agreement.csv) | Two usable conversations; not proof of improved consistency or correctness |
| Eight selected reviews show remaining interpretation problems | [Illustration](illustrative-reviews.md), [exact quotations/source hashes](illustrative-reviews.json) | Assistant interpretation; selected invalid responses labeled; not general rates |
| Prototype works with keyboard, narrow viewport and enlarged text | [Browser checks](prototype-verification.json) | Mechanical checks, not human usability or accessibility compliance |
| Earlier study, live survey, bibliography and other manuscripts unchanged | [Protection/freeze verification](verification.json) | Compared with committed baseline |

The earlier experiment's manuscript traceability remains unchanged in its original study directory. These new results are not pooled with the earlier Sol or Astra series. The paper's abstract Background and original first-experiment results were preserved; the abstract Method, Results and Conclusion now identify both experiments. No LaTeX compilation or PDF preview was performed.
