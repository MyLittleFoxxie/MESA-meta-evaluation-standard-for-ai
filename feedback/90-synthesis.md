# MESA Self-Review — Synthesis (`90-synthesis`)

All 27 content units reviewed (10 paper, 17 template including splits), plus three
cross-cutting analyses. **122 findings: 0 Blockers, 31 Majors, 72 Minors, 19 Nits.**

The zero-Blocker result is itself a finding: the template's markup honors the
`assets/mesa-form.js` parser contract everywhere — no rated item is currently being dropped
from the live form — and no unit contained an instruction a reviewer would confidently
misapply. MESA's problems are cost problems (duplication, anchor overload, navigation), not
correctness problems.

## 1. Findings by severity — the Majors, grouped

**Template-wide diseases (fix once, benefit everywhere):**
1. **Excellent-only anchoring** leaves ratings 1-3 unguided across all 89 items
   (F-20-template-partb-1) — the root of the inter-rater risk the paper itself concedes.
2. **Anchor element-bloat family** — 10-22 co-equal elements per anchor at 6.1.3, 6.2.7,
   6.3.1, 7.1.2, 7.1.4, 8.1.2, 8.1.3, 9.1.1, 10.1.1, 10.3.1, 12.2.1, 12.4.3
   (F-20-template-s06-1 and kin); 10.3.1 additionally hard-codes source-benchmark residue
   (F-20-template-s10b-1). The in-house cure exists: 10.5.1's two-tier core/supporting anchor.
3. **The run-conditions formula** pasted verbatim at ten sites (F-20-template-s08-1).
4. **Same-role duplicate items**: 2.6×2.9, 2.4×4.10, 2.5/3.2/3.7, 5.6/5.8 rows, 9.1.1×9.6,
   10.6.1×10.6.2, 11.3.1×11.3.2, 6.2.6×11.1.2 — collectively contradicting the paper's own
   coherence defense (`paper.tex:180`, F-10-paper-04-1), which should become the acceptance
   criterion for the dedup work.
5. **Dropped EFPA machinery**: per-report/per-surface iteration (F-s04-1, F-s12-1), the
   below-minimum-standard verdict rule (F-partb-2), escape options and option definitions
   across Part A checklists (F-s02a-2 and kin).
6. **Missing homes**: the hold-fixed-conditions statement the paper promises is absent from
   the Final Evaluation (F-20-template-99-2); EFPA itself is absent from the template
   bibliography (F-20-template-99-1); the Short Description and Source Inventory exist only
   as an undocumented house convention while Figure 1 depicts them
   (F-80-xcut-consistency-1).

**Paper camera-ready Majors:** uncredited Alonso & Church PTB example (F-10-paper-02-1);
duplicated adaptation rules in III-A/III-B (F-10-paper-03-1); unstated 15-benchmark procedure
(F-10-paper-03-2); draft-grade External Validity paragraph (F-10-paper-08-1); "unrevised
benchmarks" and the 74-word results sentence in the abstract (F-10-paper-00-1/2); the
coherence-defense contradiction (F-10-paper-04-1).

## 2. The ten changes with the highest usability payoff

| # | Change | Findings | Payoff |
|---|---|---|---|
| 1 | Add the 1-3 interpolation rule to the Part B preamble; per-item "Adequate" anchors for Sections 9-10 later | partb-1 | Every one of 89 ratings becomes decidable by two reviewers alike |
| 2 | Anchor surgery: two-tier core/supporting rewrite of the 12 bloat anchors, using 10.5.1 as the pattern | s06-1, s07-1, s08-3, s09-1, s10b-1/2, s12-3 | The highest-traffic items become discriminating instead of unreachable |
| 3 | Define "run conditions" once; substitute at all ten sites | s08-1 | −110 words, one concept, reusable in the Final Evaluation prompt |
| 4 | One migration batch: merge 10.6, 11.3, 2.6/2.9, 2.4/4.10; dedup 5.6/5.8 rows; flatten 9.1/9.5; retitle 5.1 | s10b-3, s11-2, s02a-1, s04-2, s05-1/2, s09-2 | −5 rated items, −~800 words, one coordinated ID/answer migration |
| 5 | Final Evaluation upgrade: hold-fixed-conditions prompt + minimum-standard trigger + Section 6 revisit checkpoint + multi-row Gap Register | 99-2, partb-2, s06-2, 99-4 | The review's output becomes the deliverable the paper advertises |
| 6 | Promote Short Description + Source Inventory into the template | consistency-1 | Figure 1 becomes true; the evidentiary backbone gets a form home |
| 7 | Add EFPA + Leaderboard Illusion to the template bibliography; EFPA-mapping sentence for Section 7 | 99-1, s07-3 | The authority chain becomes visible end-to-end |
| 8 | Canonical names: one framework name, one section-name list regenerated across template heading / Summary of Ratings / paper Tables II-III / README / mirror | consistency-3/4, 99-3, 06-1 | Traceability of labels in a framework about traceability |
| 9 | Ten-line glossary + the ~20 term substitutions from the decision table | 80-xcut-terminology | Non-psychometricians stop guessing; `calibration`'s three senses get three names |
| 10 | Paper camera-ready pass: PTB citation, III-B dedup, External Validity rewrite, abstract fixes, procedure statement, RQ1/RQ3 markers | 02-1, 03-1/2, 08-1, 00-1/2, 07-1 | Removes every publication-risk finding in one editing session |

## 3. Is the template too long — and by how much?

**Yes, in two distinct senses.**

*As prose:* about 14% of the template is removable duplication — the filed fixes take
~20,600 words to ~17,800 and 89 rated items to 84 with zero loss of EFPA function (every cut
names where the function survives). That pass is mandatory and cheap.

*As an instrument:* even after that pass, a competent non-psychometrician needs **roughly a
working week (22-35 h)** for one full review (`80-xcut-length-budget`). For its
certification-grade use case — the audits the paper envisions for procurement, safety cases,
and policy — that is defensible; EFPA reviews of psychological tests cost comparable effort.
For the paper's *stated primary audience* — requirements engineers making routine benchmark
selections — it is roughly 3× too long, and the paper knows it: "many RE workflows need a
compact scorecard that preserves evidence without hiding caveats" (`paper.tex:307`).

**The answer is therefore two-tier, and the paper has already authorized it:** trim the full
template per this review (the certification tier), and derive **MESA-Core** — approximately
30-35 rated items centered on the sections where the case-study ratings actually turned
(8-10 and 12), a compressed Part A, the Gap Register, and the supported-use/non-use statement
— targeting 8-12 hours. The invariant `paper.tex:307` imposes: evidence and caveats survive
compression. That derivation is `/mesa-core-plan`'s job, with F-10-paper-04-1's role-purity
criterion as its acceptance test.

## 4. What must survive any trimming — the protect list

- Section 5's escape-hatch discipline ("Not available"/"Not documented" options) — extend it, never cut it.
- 2.14's documented-estimates-only rule (deliberate, good EFPA drift).
- 10.5.1's two-tier anchor (the pattern for fix #2).
- The reference-kind typology (:1547) and the anti-difficulty rating rule (:1932).
- "Scorers are measurement components, not implementation details" (:1747) and the inference-level principle (:2322).
- The Gap Register; the n/a-vs-0-vs-1 semantics; the worked example's four-element profile (`paper.tex:204`).
- The paper's footnote-definition discipline and quantified interpretation thresholds (Case Study Results) — the model for template anchor examples.
- The claims-cluster division of labor as clarified: 2.18 *collects* claims → 10.6 rates *evidence proportionality* → 11.5 rates the benchmark's *own use guidance* → 12.3/12.4 rate *how claims are communicated*. One boundary paragraph in the Part B preamble should state this pipeline once.

## Verdict
- **Disposition:** Trim (template, −14% now) + Derive (MESA-Core, per `/mesa-core-plan`) + one paper editing pass
- **Items:** 122 findings → 10 change-packages above
- **Rationale:** A faithful, zero-Blocker adaptation whose costs concentrate in duplication and anchor overload; the fixes are mechanical, the compact tier is already authorized by the paper, and nothing found challenges MESA's core design.
