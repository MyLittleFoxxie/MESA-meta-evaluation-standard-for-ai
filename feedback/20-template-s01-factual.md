# Feedback — `20-template-s01-factual` (`MESA EFPA template official.md:101-148`)

Unit reviewed: Section 1 preamble (:103), 1.1 Review Administration (:105-111), 1.2 Benchmark
Identity & Provenance (:113-127), 1.3 Materials, Sources, & Access Tracking (:129-145). EFPA
counterpart: Section 1 "Factual description" (`EFPA_Test_Review_Model_2025_Markdown.md:105-124`)
plus the Part A "Information Sources" rule (`:99-101`).

What holds up: this is the template's leanest section and a model for the others. 1.1 and 1.2
retain EFPA's General Information table with sensible AI substitutions (version/split, scorer
version, license, DOI). 1.3 is a MESA-original materials inventory whose purpose — making every
later judgment traceable to an inspected source with an access date — is exactly the
auditability the AI setting needs, and the preamble (:103) states the EFPA relocation
explicitly, which is the visible-traceability practice the rest of the template should copy.
EFPA's Part A source rule (:99-101, "select from those descriptions that the publisher
provides... indicate this fact") survives adequately in the front matter (:17, :25).
Machine-contract check: fill-in tables use `_(placeholder)_` cells and "Reviewer comments:"
(:145) is a colon-terminated standalone line — all three subsections parse into the live form
as intended; no violations.

---

### F-20-template-s01-1 — [Major] The Entity Type field has no controlled vocabulary — and introduces a fourth variant of the taxonomy
- **Axis:** vagueness (with terminology drift)
- **Where:** `MESA EFPA template official.md:119`
- **Quote:** > | Entity Type | _(Original benchmark, derived variant, hosted leaderboard, harness, etc.)_ |
- **Why it fails a user:** This is the operative field where the reviewer commits to what they are reviewing — the decision the front matter (:13, :21) says must precede Part A. But the placeholder offers a free-text "etc." with a third naming scheme: "derived variant" (vs. "derived benchmark" at :13 and "variant" at :21) and "harness" (vs. "evaluator-specific implementation" at :13/:21) — and `:1259` later uses yet another subset. Two reviewers auditing the same leaderboard slice will record different entity types in different vocabulary, which breaks exactly the cross-review comparability MESA exists to provide, and makes the "do not inherit from the parent benchmark" rule (:21) unenforceable because entity type is not machine-comparable.
- **Fix:** Give the field the canonical closed vocabulary from :13 plus "Other (describe)". Parser-safe cheap version: keep the table row and make the placeholder the full list verbatim — `_(one of: original benchmark | derived benchmark | subset | evaluation slice | hosted leaderboard | private form | rolling cohort | suite component | task environment | evaluator-specific implementation | other)_`. Better version: pull Entity Type out of the table as a `- [ ] Label` checkbox group under a `#### Entity Type` heading — this parses as first-class checkboxes in the live form (`assets/mesa-form.js:8`) and does not break the remaining fill-in table.
- **EFPA link:** MESA-original — EFPA's unit of review is simply "the test" (`EFPA_Test_Review_Model_2025_Markdown.md:105`); the entity taxonomy is MESA's most important structural addition, which is why it must be a controlled list, not a placeholder suggestion.

### F-20-template-s01-2 — [Minor] "the review base" — an undefined coinage in the section preamble
- **Axis:** terminology
- **Where:** `MESA EFPA template official.md:103`
- **Quote:** > ...moves the inventory of reviewed materials into this section so later descriptive and evaluative judgments can be traced to the review base.
- **Why it fails a user:** "Review base" is a MESA coinage appearing here for the first (and possibly only) time; a reader must guess it means "the set of materials inspected". The sentence's point — traceability — is carried by plainer words.
- **Fix:** **Substitute:** "...so later descriptive and evaluative judgments can be traced to the specific materials that were actually inspected." If "review base" is used again later in the template, standardize on one term and define it here instead.
- **EFPA link:** MESA-original preamble; no EFPA dependency.

### F-20-template-s01-3 — [Nit] Response columns are headed "Description"
- **Axis:** vagueness
- **Where:** `MESA EFPA template official.md:107` and `:115`
- **Quote:** > | Prompt | Description |
- **Why it fails a user:** The second column is where the reviewer writes their answer, but its header says "Description" (the placeholder text is guidance, the cell content is a response). EFPA heads the same column "Response" (`EFPA_Test_Review_Model_2025_Markdown.md:109`). Print/markdown users may read the column as pre-filled documentation. In the live form this is invisible (placeholders become input hints), so Nit.
- **Fix:** Rename the column header to "Response" in 1.1 and 1.2. No parser impact — headers are not parsed for field extraction.
- **EFPA link:** EFPA Section 1 table header (`EFPA_Test_Review_Model_2025_Markdown.md:109`) — drifted (trivially).

---

## Verdict
- **Disposition:** Keep as-is (apply F-1's controlled vocabulary)
- **Items:** 3 subsections, 25 fill-in prompts → unchanged
- **Rationale:** The leanest, best-adapted section in Part A; its one real defect is that the template's central entity-taxonomy decision point is a free-text placeholder with drifting vocabulary.
