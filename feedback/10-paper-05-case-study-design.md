# Feedback — `10-paper-05-case-study-design` (`paper.tex:190-209`)

Unit reviewed: Case Study Design — benchmark selection (:193), pipeline figure (:195-200),
pipeline description (:202), worked example (:204), Replication Package (:206-208).

This is the paper's tightest section. The three benchmark thumbnails (:193) are accurate and
appropriately hedged; the pipeline description names concrete models and steps; the worked
example (:204) is the single most persuasive paragraph in the paper — it shows the
n/a-vs-0-vs-1 discipline of :177 actually operating, and its "The anchor is this four-element
profile, not the number" close is exactly the right claim. "This is a feasibility demonstration
of the workflow, not a validation study" (:202) is consistent with :138 (and both contradict
:94's "verify" — already filed as F-10-paper-03-3). Two wording findings and one nit.

---

### F-10-paper-05-1 — [Minor] The figure caption garbles the reconciliation step the body describes correctly
- **Axis:** vagueness (grammar)
- **Where:** `paper.tex:198`
- **Quote:** > A supervising editor model reconciled the resulting MESA by removing discrepancies to produce final MESA evaluations.
- **Why it fails a user:** "The resulting MESA" is missing its noun (drafts/reviews), and "removing discrepancies" says the editor deleted disagreements — the body (:202) says it "reconciled each discrepancy...against the sources", which is a materially different (and better) procedure. Captions are read independently of body text; a skimming reviewer takes away "discrepancies were dropped".
- **Fix:** "A supervising editor model reconciled the two resulting MESA drafts, resolving each discrepancy against the sources, to produce the final MESA evaluations."
- **EFPA link:** n/a — pipeline description (MESA-original workflow).

### F-10-paper-05-2 — [Minor] "The four-element anchoring model" arrives with a definite article but no introduction
- **Axis:** terminology
- **Where:** `paper.tex:204`
- **Quote:** > ...the editor set the final rating to 1 using the four-element anchoring model.
- **Why it fails a user:** The phrase implies an established method the reader should already know, but this is its first and only occurrence in the paper, and the template has no such term. The four elements are in fact defined by the bold labels that follow (evidence, missing evidence, editor rationale, supported-use/non-use statement) — the paragraph defines the thing after invoking it as known.
- **Fix:** Invert the introduction: "...the editor set the final rating to 1, anchoring it in a four-element profile: \textbf{evidence}, \textbf{missing evidence}, \textbf{editor rationale}, and a \textbf{supported-use and non-use statement}." Then the existing element sentences follow. If the anchoring procedure is specified in the editor role definition (`GEMINI.md`), cite that as its home.
- **EFPA link:** MESA-original (the profile operationalizes EFPA's evidence-based-rating principle; no EFPA item names it).

### F-10-paper-05-3 — [Nit] "Utility files" says nothing
- **Axis:** vagueness (polish)
- **Where:** `paper.tex:208`
- **Quote:** > It contains the manuscript source and bibliography, the MESA template, the reviews for HLE, ARC-AGI-2, and DesignQA, and utility files.
- **Why it fails a user:** A replication-package sentence should let a reader predict what they will find; "utility files" is a shrug.
- **Fix:** "...and the form-rendering and dataset-export utilities." (Matches `assets/mesa-form.js` and `dist/hf_mesa_dataset/`.)
- **EFPA link:** n/a.

---

## Verdict
- **Disposition:** Keep as-is (two wording fixes, one nit)
- **Items:** 4 paragraphs + 1 figure → unchanged
- **Rationale:** The strongest section in the paper — concrete, calibrated, and honest about feasibility vs. validation; only the caption and the worked example's opening phrase need repair.
