# Feedback — `80-xcut-length-budget`

Scope: rateable items per section, estimated reviewer hours, burden concentration, and a
realistic completion time. Numbers from the per-unit reviews (item counts recorded in the
Cross-cutting log) and the corpus statistics (template: 2,479 lines, ~20,600 words,
194 headings, 89 rated items).

## Item inventory

**Part A (descriptive — no ratings, but every field must be filled or marked as a gap):**

| Section | Fields/subsections | Lines | Notes |
|---|---|---|---|
| 1. Factual Description | 3 subsections (multi-row tables) | 48 | fast |
| 2. Classification | 18 subsections, dozens of checklists | 443 | **18% of the whole template** |
| 3. Measurement and Scoring | 7 subsections | 175 | overlaps 2.9/2.17 inventories |
| 4. Outputs and Reports | 10 subsections | 156 | audience list duplicates 2.4 |
| 5. Access, Materials, Lifecycle | 8 subsections + Appendix A | 200 | 5.6/5.8 = 46 fill-in rows |

**Part B (evaluative — each item: read anchor, gather evidence, rate, comment):**

| Section | Rated items | Of which roll-ups |
|---|---|---|
| 6. Rationale, Documentation, Task Quality | 25 | 4 |
| 7. Materials | 8 | 1 |
| 8. Baselines | 8 | 1 |
| 9. Reliability | 11 | 1 |
| 10. Validity | 15 | 1 |
| 11. Fair Use | 12 | 1 |
| 12. Reports | 10 | 1 |
| **Total Part B** | **89** | **10** |

Plus the Final Evaluation: 3 free-text essays, ratings summary, Gap Register.

## Time estimate

Assumptions: competent reviewer, not a psychometrician, benchmark with typical documentation
(paper + repo + leaderboard), evidence must be located and cited per the anchoring discipline
the worked example (`paper.tex:204`) demonstrates.

- Part A: Section 2 alone ≈ 3-4 h (18 subsections against scattered documentation); Sections
  1, 3-5 ≈ 5-8 h combined. **Part A ≈ 8-12 h.**
- Part B: consequential items (Sections 9-10, where evidence is scarce and judgment heavy)
  ≈ 15-20 min each; checklist-like items ≈ 5-10 min; roll-ups ≈ 10 min. At 89 items:
  **≈ 19-33 h**, concentrated in Sections 6 (25 items) and 10 (15 items, hardest evidence).
- Final Evaluation: **1-2 h.**

**Realistic total: 28-45 hours — a full working week for one reviewer.** The multi-LLM
pipeline masks this; a human panelist in the planned validation study (`paper.tex:305`) will
not. For comparison, BetterBench assesses a benchmark against 46 criteria; MESA Part B alone
carries 89 rated items plus ~46 Part A subsections.

## Where the burden concentrates

1. **Section 2 (Classification): 443 lines, 18 subsections — the single heaviest unit** and
   it produces no ratings. Its checklist duplications (2.6×2.9, 2.9×2.17×3.x) are pure re-read
   cost. The 2.18 broad-claim screen triggers on "reasoning", i.e., on essentially every
   modern benchmark — its conditional structure saves no one any work in practice.
2. **Section 6: 25 of 89 ratings (28%)** — partly justified (EFPA's §6 is also large), but
   4 of the 25 are roll-ups, and the three worst bloat anchors (6.1.3, 6.2.7, 6.3.1) sit here.
3. **Anchor re-parsing:** the ten run-conditions formula sites, the triple-stated variation
   sources in Section 9, and the preamble↔anchor duplicate lists in Section 7 tax every pass
   through the document, not just the first.
4. **Cross-section duplicate ratings:** 6.2.6↔11.1.2, 11.3.1↔11.3.2, 10.6.1↔10.6.2 — each
   pair costs a second judgment for one item of information.

## Effect of the already-filed fixes

Applying only this review's consolidation verdicts (no new cuts): rated items 89 → 84
(−6.1.9/6.2.8/6.3.7 optional −2, 9.1.1 demoted in weight, 10.6 merge −1, 11.3 merge −1);
template words ≈ 20,600 → ≈ 17,800 (−14%): run-conditions substitution −110, preamble trims
−500, anchor surgeries −400, Part A dedups (5.6/5.8 rows 46→36, 2.6/2.9, 2.4/4.10) −800,
formula and repetition removals −900. **Reviewer time ≈ 28-45 h → ≈ 22-35 h.** Real, but not
transformative — which is the honest headline: **the template's length problem is structural
(item count and duplication), not prose-level, and the full instrument will remain a
multi-day commitment.** The paper already concedes this and points at the answer: "many RE
workflows need a compact scorecard" (`paper.tex:307`). A MESA-Core of roughly 30-35 rated
items (the non-roll-up items whose ratings actually moved in the three case studies, chiefly
from Sections 8-10 and 12, plus a compressed Part A) would serve routine RE use at ≈ 8-12 h,
with the full template reserved for certification-grade audits.

## Verdict
- **Disposition:** Trim (full template) + derive (MESA-Core) — per the split above
- **Items:** 89 rated + ~46 descriptive → 84 + ~40 after filed fixes; MESA-Core target ≈ 30-35 rated
- **Rationale:** A week-long instrument survives fixes worth ~25% of its time cost; the paper's own compact-scorecard admission is the mandate for the two-tier answer.
