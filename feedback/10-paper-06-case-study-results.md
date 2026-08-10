# Feedback — `10-paper-06-case-study-results` (`paper.tex:210-265`)

Unit reviewed: Case Study Results — HLE (:212-218), ARC-AGI-2 (:220-226), DesignQA (:228-234),
Overall ratings (:236-264, Table III).

This section is the paper's evidentiary core and it largely works. Three patterns deserve
explicit praise because the synthesis should protect them through any trimming:

1. **Footnote-definition discipline.** Calibration error (:214), confidence interval (:216),
   fluid intelligence (:224), scaffolding (:224), pass@2 (:224), long-horizon planning (:218),
   BLEU/ROUGE (:232) are each defined in one plain-language footnote at first use — exactly the
   Substitute-first terminology policy this review applies to the template.
2. **Quantified interpretation thresholds.** "A 1\% difference is about one task" (:224, checks
   out: 120 tasks), "one item changes accuracy by 6.25 percentage points" (:232, checks out:
   16 items), "differences roughly below 10--15 percentage points should be treated cautiously"
   (:234). These are the decision rules the template's Part B anchors mostly lack.
3. **The tripartite per-case structure** (materials reviewed → gaps found → supported-use /
   non-use statement) is disciplined repetition in the good sense — same role, parallel form.

The overall-ratings interpretation (:260-262) correctly applies the paper's own 0-vs-1
semantics ("missing measurement evidence", not "poor construction"), and :262 finally uses
"claim proportionality" with a serviceable contextual gloss. Findings are labeling-level.

---

### F-10-paper-06-1 — [Minor] Table III renames the Part B sections a third way
- **Axis:** repetition (naming consistency)
- **Where:** `paper.tex:247-253`
- **Quote:** > 6. Rationale, documentation, and task/item quality [...] 8. Reference points and comparison groups [...] 10. Validity support
- **Why it fails a user:** The same sections now have three names in one paper: the template's headings, Table II's row titles (`:159-165`, faithful), and Table III's shortened paraphrases — "Reference points and comparison groups" for "Baselines, Comparators, and Reference Interpretation", "Validity support" for "Validity Evidence". A reader tracing a rating from Table III back to Table II or the template must fuzzy-match titles; in a paper about traceability, labels should trace.
- **Fix:** Reuse Table II's row titles verbatim in Table III (they fit — Table III is `\footnotesize` single-column; abbreviate identically in both tables if width forces it, e.g. "8. Baselines and reference interpretation" in *both*).
- **EFPA link:** Part B section identities (EFPA §6-§12) — retained in substance; drifted in presentation.

### F-10-paper-06-2 — [Nit] AGI is expanded on its ~fourth use rather than its first
- **Axis:** terminology (polish)
- **Where:** `paper.tex:218` (first use at `:90`)
- **Quote:** > ...nor as evidence of Artificial General Intelligence (AGI), autonomous research...
- **Why it fails a user:** "AGI" appears unexpanded at :90 (Related Work heading and body) and in the benchmark name ARC-AGI-2 throughout; the expansion then lands mid-way through the results. Harmless but backwards.
- **Fix:** Move the expansion to :90 ("...the strongest benchmark claims --- those equating performance with Artificial General Intelligence (AGI)..."); use bare "AGI" at :218.
- **EFPA link:** n/a.

---

## Verdict
- **Disposition:** Keep as-is
- **Items:** 10 paragraphs + 1 table → unchanged
- **Rationale:** The section demonstrates the method it describes — quantified, hedged, source-grounded, with explicit supported/non-use boundaries; only the Part B section labels need aligning with Table II.
