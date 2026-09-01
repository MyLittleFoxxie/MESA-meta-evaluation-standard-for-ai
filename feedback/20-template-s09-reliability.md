# Feedback — `20-template-s09-reliability` (`MESA EFPA template official.md:1624-1815`)

Unit reviewed: Section 9 — preamble (:1626-1632), Figure 3 (:1636-1700), stakes paragraph
(:1702), guidance table (:1704-1712), sub-sections 9.1 (1 item), 9.2 (2), 9.3 (3), 9.4 (3),
9.5 (1), 9.6 overall. 11 rated items.

Much here is right: the EFPA-mapping sentence is present (:1626); the no-single-coefficient
paragraph (:1632) is honest measurement thinking ("Exact-match deterministic scoring does not
remove uncertainty when item counts are small" — exactly the DesignQA finding); 9.3's framing
sentence (:1747 — scorers "treated as measurement components requiring evidence, not as
neutral implementation details") is one of the template's best; and Figure 3, unlike Figure 2,
maps accurately onto the real items. The :1729 run-conditions formula occurrence is covered by
F-20-template-s08-1. Parser check: all conventional; no form loss.

---

### F-20-template-s09-1 — [Major] The sources of score variation are enumerated three times — and 9.1.1's rating collides with 9.6's
- **Axis:** repetition (with structural consequences)
- **Where:** `MESA EFPA template official.md:1630` (preamble, 17 elements), `:1722` (9.1.1 anchor, 22 elements), `:1727-1802` (the same sources distributed across 9.2-9.5)
- **Quote:** > Excellent: The benchmark reports reliability, precision, or stability evidence across the major sources of score variation relevant to the benchmark, including repeated runs, prompt wording, small item changes, claimed capability domains or capability-domain profiles where applicable, scorers, judges, parsers, scorer or judge versions, external APIs and services, search indexes, tools, simulators, user models, tokenizers, context bins, versions, forms, public/private splits, temporal cohorts, environments, leaderboard reruns, and model settings. *(9.1.1 — 22 elements)*
- **Why it fails a user:** The reviewer meets the variation-source inventory in the preamble (:1630), again as 9.1.1's 22-element anchor — the longest in the template — and then a third time as the actual rated items 9.2.1-9.5.1. Worse, 9.1.1 asks for a single rating of "coverage across the major sources", which is indistinguishable from the overall judgment 9.6 asks for after the per-source items: two reviewers will either duplicate 9.6 into 9.1.1 or invent a distinction the template never states.
- **Fix:** Three moves, preserving EFPA §9.1's "data provided about reliability" function: (1) preamble :1630 shrinks to "sources of variation include decoding stochasticity, scoring mechanisms, prompt and version changes, and execution environment — itemized in 9.2-9.5"; (2) 9.1.1 becomes the *inventory*, not a judgment: keep the rating but anchor it in one line — "Excellent: Evidence exists for each source of variation material to this benchmark's design (see 9.2-9.5); which sources lack evidence is explicitly stated" — matching the 9.1 bullet (:1717) that already describes exactly this selective-noting job; (3) 9.2-9.5 carry the per-source judgments and 9.6 the overall, unchanged. Saves ~120 words and the template's most daunting anchor.
- **EFPA link:** EFPA §9.1 data-provided item — retained in function; the 22-element inflation and the 9.6 collision are MESA-original.

### F-20-template-s09-2 — [Minor] Single-item sub-sections 9.1 and 9.5 add heading depth without grouping anything
- **Axis:** complexity and cognitive load
- **Where:** `MESA EFPA template official.md:1714-1723` (9.1 → 9.1.1) and `:1795-1802` (9.5 → 9.5.1)
- **Quote:** > ### 9.5 Statistical Comparison Quality [...] #### 9.5.1 Meaningfulness of score differences
- **Why it fails a user:** A sub-section wrapping exactly one item forces the reviewer through two headings and two preambles to reach one rating, and inflates the apparent size of the section (six sub-sections for eleven items). The 9.5 preamble's useful sentence ("distinguish statistical significance, practical significance, and leaderboard convenience") belongs in the item itself.
- **Fix:** Flatten: renumber 9.1.1→9.1 and 9.5.1→9.5, folding each sub-section preamble into the item's lead bullet. Parser note: heading-derived item IDs change (9.1.1→9.1, 9.5.1→9.5), so stored form answers keyed to the old IDs need the same migration treatment as the 5.1 retitle (F-20-template-s05-1) — do them in one migration.
- **EFPA link:** EFPA §9's flatter item list — returning to EFPA's economy.

### F-20-template-s09-3 — [Nit] The stakes paragraph is the fourth corpus statement of stakes-dependent adequacy
- **Axis:** repetition
- **Where:** `MESA EFPA template official.md:1702` (previously :1139 factors, :1141 critical attributes, :1158 General Guidance)
- **Quote:** > A small amount of instability may be acceptable for exploratory research but unacceptable when leaderboards rank systems by narrow margins, when procurement or policy decisions rely on the scores, or when public score interpretations imply meaningful superiority.
- **Why it fails a user:** The principle is already established three times; only the leaderboard-margins example is new here.
- **Fix:** Keep the sentence quoted above (it earns its place with section-specific examples); delete the framing sentence before it ("When ratings depend on numerical evidence, reviewers should consider the benchmark's stakes and score use." — that is :1158 verbatim in spirit). −16 words.
- **EFPA link:** n/a — guidance economy.

---

## Verdict
- **Disposition:** Trim (demote the mega-anchor, flatten two sub-sections)
- **Items:** 11 rated → 11 (2 renumbered; ≈ −140 words)
- **Rationale:** The right per-source decomposition with honest measurement guidance, wrapped in a redundant coverage layer: the section says its source list three times and rates its overall judgment twice.
