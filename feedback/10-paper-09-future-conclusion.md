# Feedback — `10-paper-09-future-conclusion` (`paper.tex:302-321`)

Unit reviewed: Future Work (:302-309, three paragraphs) and Conclusion (:311-315, two
paragraphs).

Two observations that matter beyond this unit:

1. **The paper pre-authorizes a compact MESA.** ":307 — "A full MESA review is intentionally
   detailed, but many RE workflows need a compact scorecard that preserves evidence without
   hiding caveats." This is the paper's own admission that the full template exceeds many
   workflows, and it names the required invariant (preserve evidence and caveats). Quote it in
   `/mesa-core-plan` as in-paper authorization for the trimmed template.
2. **RQ1/RQ3 confirmation.** The Conclusion does not answer RQ1 or RQ3 explicitly either —
   F-10-paper-07-1 stands as filed.
3. Also: Conclusion :315 already contains the content of the Limitations section's promotional
   close (:300 "open-source, replicable... apply today" ≈ :315 "open-source, and replicable...
   equips requirements engineers") — so F-10-paper-08-2's "move :300 to the Conclusion"
   simplifies to "delete :300"; nothing is lost.

---

### F-10-paper-09-1 — [Minor] The validation measurands are enumerated twice — III-C and Future Work
- **Axis:** repetition
- **Where:** `paper.tex:305` (first enumeration at `:138`)
- **Quote:** > Future work will validate MESA as a review instrument through multi-reviewer studies, inter-rater agreement analysis, structured reviewer training, and refinement of ambiguous rating anchors. [...] comparing reconciled LLM outputs against expert human reviewer panels, measuring LLM-reviewer agreement... *(:305)* — vs — > ...allowing us to estimate inter-rater agreement on Part B ratings, quantify the effect of reviewer training, and compare reconciled human panels against the multi-LLM pipeline. *(:138)*
- **Why it fails a user:** :138 promises "This planned study is detailed as the primary thread of future work" and then pre-details it — inter-rater agreement, reviewer training, and panel-vs-pipeline comparison appear in both places. The Future Work section, whose job this is, arrives half-spent. :305's genuinely new content (model-choice sensitivity, prompt-perturbation stability, anchor refinement) gets diluted.
- **Fix:** Shorten :138 to the design commitment only: "The intended validation strategy centers on human-in-the-loop consensus panels applying MESA to a shared benchmark cohort; the planned study is detailed in Section~\ref{sec:future}." (−25 words; the measurands live once, here.)
- **EFPA link:** n/a — paper structure.

### F-10-paper-09-2 — [Minor] The Conclusion repeats the Discussion's signature sentence nearly verbatim — with different spelling
- **Axis:** repetition
- **Where:** `paper.tex:315` (original at `:268`)
- **Quote:** > ...it re-frames benchmark use as a requirements traceability problem. *(:315)* — vs — > MESA reframes benchmark use as a requirements traceability problem. *(:268)*
- **Why it fails a user:** The paper's central reframing claim appears twice in three pages, once as "reframes" and once as "re-frames" — verbatim self-quotation with an inconsistent hyphen is the worst of both: it reads as repetition, not reinforcement, and the spelling wobble suggests neither instance was edited against the other.
- **Fix:** Keep :268 as the definition. At :315, advance rather than repeat: "...it treats benchmark evidence as a requirements-traceability obligation: a trustworthiness claim backed by a benchmark score is only as strong as the measurement evidence behind that score." (The following sentence already says this — so the simplest fix is deleting the "re-frames" clause and letting :315's second sentence carry the close.) Standardize on "reframes" wherever it survives.
- **EFPA link:** n/a — paper prose.

---

## Verdict
- **Disposition:** Keep as-is (two deduplications, both cutting the *earlier* occurrence or the echo)
- **Items:** 5 paragraphs → unchanged (≈ −40 words across :138, :300, :315)
- **Rationale:** Future Work is concrete and the Conclusion lands the right claims; both are weakened only by echoing sentences that already exist elsewhere — and :307's compact-scorecard admission is the strategic sentence the template-trimming plan should cite.
