# Feedback — `20-template-partb-preamble` (`MESA EFPA template official.md:1123-1165`)

Unit reviewed: Part B header (:1123-1125), Information Sources (:1127-1135), Explanation of
Ratings (:1137-1154, incl. Rating Scale table), General Guidance on Assigning Ratings
(:1156-1164).

EFPA comparison (`EFPA_Test_Review_Model_2025_Markdown.md:613-656`): the adaptation is
substantively faithful. The five source tiers map onto EFPA's four with a sensible AI-specific
addition (public benchmark materials, :1132); EFPA's starred-rating and NDA machinery is
simplified into reviewer-note disclosure (:1134-1135) without losing the function; the
General Guidance section (:1158-1162) is genuinely better than its EFPA counterpart — the
"first ask what evidence would be needed" rule (:1160) and the broad-claims escalation (:1162)
are concrete where EFPA offers a cooking metaphor. The rating-scale table (:1147-1154) improves
on EFPA by giving 1-3 one-line meanings. Parser check: headings, bullets, and a plain table —
no rating items or placeholders; nothing at risk in the live form.

---

### F-20-template-partb-1 — [Major] Excellent-only anchoring leaves ratings 1-3 to unguided interpolation — the template's central inter-rater risk
- **Axis:** vagueness
- **Where:** `MESA EFPA template official.md:1139`
- **Quote:** > Detailed "Excellent" anchors identify what a rating of `4` would require for that item. Lower ratings should be assigned by reviewer judgment, considering the benchmark's intended use, scope of score interpretation, decision stakes, technical complexity, evidence quality, and consequences of misinterpretation.
- **Why it fails a user:** EFPA supplements its scale with per-item guidance values across levels ("Notes provide some guidance on the sorts of values to associate with inadequate, adequate, good, and excellent ratings for many items", EFPA `:654`). MESA anchors only the top of the scale, then hands the reviewer a six-factor judgment list. Two competent reviewers who agree an item falls short of Excellent have no shared rule for 1 vs 2 vs 3 — precisely the subjectivity the paper's Internal Validity section concedes (`paper.tex:290`). The 89 rated items inherit this gap wholesale; fixing it here fixes it everywhere.
- **Fix:** Add one sentence making the generic scale definitions operational per item: "To assign 1-3, apply the Rating Scale meanings to the item's Excellent anchor: `2` means the anchor's core function is met with stated limitations; `1` means the function is not met for the stated purpose; `3` means met with only minor gaps." For the critical sections (9, 10), add explicit per-item "Adequate:" anchors in a later revision — EFPA does this for its psychometric sections.
- **EFPA link:** EFPA Explanation of Ratings (`:629`) and General Guidance (`:654`) — drifted: EFPA's multi-level guidance narrowed to top-anchor-only.

### F-20-template-partb-2 — [Minor] EFPA's below-minimum-standard rule and bold-critical convention are dropped
- **Axis:** EFPA traceability
- **Where:** `MESA EFPA template official.md:1141`
- **Quote:** > Where a `0` or `1` rating is assigned to an attribute that is critical for the benchmark's stated purpose, the review should caution that the benchmark is suitable only for limited exploratory, research, or expert-qualified use unless stronger evidence is supplied.
- **Why it fails a user:** The caution function survives, but EFPA pairs it with two harder devices MESA dropped: a verdict rule — "Any instrument rated with one or more [0] or [1] ratings in attributes that are regarded as critical...should be considered as falling below the minimum standard for the purpose it is intended to fulfil" (EFPA `:633`) — and the convention of bolding critical-quality ratings for visibility (`:631`). Without the verdict rule, MESA's Final Evaluation has no crisp trigger for a "not suitable" outcome; without the marking convention, a reader scanning a completed review cannot see which ratings were load-bearing. (EFPA's related follow-through — recommending the publisher publish valuable non-public reports, `:621` — is likewise dropped from :1134.)
- **Fix:** Append to :1141: "A benchmark with one or more `0`/`1` ratings on attributes critical to its stated use falls below the minimum standard for that use; the Final Evaluation must say so explicitly. Mark critical-attribute ratings in **bold** in the completed review." (Bold marking is reviewer-authored output, not template markup — no parser impact.)
- **EFPA link:** EFPA `:631-633` — dropped; restoration proposed.

### F-20-template-partb-3 — [Minor] "Calibration data for scoring by another model" — the known calibration Split, in situ
- **Axis:** terminology
- **Where:** `MESA EFPA template official.md:1135`
- **Quote:** > ...hidden test splits, item provenance, audits for prior exposure to benchmark items or answers, scorer validation reports, calibration data for scoring by another model, or security details.
- **Why it fails a user:** "Calibration" now carries three senses across the corpus: model-confidence calibration (template `:7`, `paper.tex:214`), this scorer-tuning sense, and human difficulty calibration (`paper.tex:222`). A reviewer meeting "calibration data" here may read it as confidence-calibration logs — a materially different artifact.
- **Fix:** **Split** (per the standing known case): "...scorer validation reports, tuning data for model-based scorers, or security details."
- **EFPA link:** MESA-original bullet (EFPA `:622` lists scoring-algorithm development reports); renaming preserves the function.

### F-20-template-partb-4 — [Nit] :1164 restates what :1139 and :1143 already said
- **Axis:** verbosity
- **Where:** `MESA EFPA template official.md:1164`
- **Quote:** > Ratings should be based on the information available, with comments explaining consequential evidence, limitations, and rating rationale where needed.
- **Why it fails a user:** Every element (evidence-based ratings, explanatory comments) is already required by :1139 (judgment factors) and :1143 (judgment over averaging). A closing platitude dilutes the two real rules above it.
- **Fix:** Delete the line. (It is prose, not a parsed field — no form impact.)
- **EFPA link:** No EFPA counterpart — MESA-original filler.

### F-20-template-partb-5 — [Nit] Official-sources precedence stated here and in the frontmatter
- **Axis:** repetition
- **Where:** `MESA EFPA template official.md:1133` (first statement at `:25`)
- **Quote:** > Use these sources to contextualize or challenge score interpretations, not to replace official facts.
- **Why it fails a user:** Second statement of the source-precedence rule (Cross-cutting log). Mild — the phrasing here is role-specific (third-party literature) — but section preambles in 6-12 should not add a third.
- **Fix:** Keep both (the :1133 wording earns its place); enforce no further restatements downstream.
- **EFPA link:** EFPA `:620` ("reviewers may source and make use of this information") — retained with a MESA-added precedence rule.

---

## Verdict
- **Disposition:** Trim + strengthen (delete :1164; add the interpolation rule and minimum-standard sentence)
- **Items:** 3 subsections → 3 (net +2 sentences, −1 line)
- **Rationale:** A faithful and in places superior adaptation whose one structural choice — anchoring only Excellent — exports unguided 1-3 judgment to all 89 rated items; the two-sentence fix here is the highest-leverage change available to the whole of Part B.
