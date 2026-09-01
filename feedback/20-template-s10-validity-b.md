# Feedback — `20-template-s10-validity-b` (`MESA EFPA template official.md:1944-2077`)

Unit reviewed: Section 10 items — 10.1 Content (2 items), 10.2 Internal Structure (3), 10.3
Metrics and Scoring (2), 10.4 Relations to Other Variables (3), 10.5 Contamination/Gameability
(2), 10.6 Claim Proportionality (2), 10.7 Overall (1). 15 rated items.

The sub-section architecture is the AERA/EFPA validity-evidence taxonomy faithfully extended
with two MESA-original sub-sections (10.5, 10.6) that the AI-benchmark literature demands —
both well grounded (BetterBench for 10.5, Measuring what Matters / A Definition of AGI for
10.6). One item deserves explicit protection as a pattern: **10.5.1's two-tier conditional
anchor** (base evidence, then "For benchmarks with high risk of unintended disclosure...
stronger evidence may include...") is exactly the core/supporting structure the bloat-family
fixes (F-20-template-s06-1) prescribe — it should be the template's model anchor. 10.2.2's
overlap with 6.1.7 (difficulty spread, discrimination, redundancy) is EFPA-inherited
role-splitting (reported evidence vs. structural support) and is acceptable. Parser check:
all 15 items conventional.

---

### F-20-template-s10b-1 — [Major] 10.3.1 hard-codes benchmark-specific residue into a generic anchor
- **Axis:** vagueness (over-specificity)
- **Where:** `MESA EFPA template official.md:1995`
- **Quote:** > Excellent: Scoring rules, scorers, rubrics, parsers, equality-checker LLMs, models used as judges, hash-prefix or strict output rules, coordinate formats, bank-balance or accumulated-return rewards, simulator-based rewards, and score-combination rules are justified and validated as measuring the intended capability rather than irrelevant behavior, output format compliance, parser strictness, verbosity, prior exposure to items or answers, or benchmark-specific tactics; strict formats are tested, relaxed, retried, or justified when they are not part of the target capability.
- **Why it fails a user:** ~70 words, and the mechanism list is the source inventory's fingerprints: "coordinate formats" (ARC-AGI), "bank-balance or accumulated-return rewards" (Vending-Bench), "hash-prefix...rules" — three of the fifteen source benchmarks hard-coded into an anchor every reviewer must parse. A reviewer of a QA benchmark wades through reward-signal clauses that can never apply, and the item's real rule (scoring must reward the target capability, not artifacts) is buried mid-sentence. This is the template's worst single anchor.
- **Fix:** Generalize and tier: "Excellent: The scoring pathway — rules, scorers, parsers, model-based judges, and score combination — is justified and validated as rewarding the intended capability rather than formatting compliance, verbosity, parser strictness, prior exposure, or benchmark-specific tactics. Strict output formats are tested, relaxed, retried, or justified when format is not part of the target capability. (Task-appropriate reward signals — e.g., simulator returns or accumulated-reward metrics — are held to the same standard.)" (−25 words, mechanism examples demoted to one parenthetical.)
- **EFPA link:** EFPA §10 scoring-validity concern — retained; the residue is MESA-original.

### F-20-template-s10b-2 — [Minor] 10.1.1 carries the 12-element bloat pattern at the section's first item
- **Axis:** verbosity
- **Where:** `MESA EFPA template official.md:1952`
- **Quote:** > Excellent: The task sample comprehensively represents the intended capability domain or use context, with explicit coverage analysis across relevant language families, scripts, cultures, modalities, application domains, environment states, context-length bins, difficulty bands, task horizons, expert review where relevant, documented exclusions, and clear limits on generalization.
- **Why it fails a user:** Same discrimination failure as F-20-template-s06-1, positioned as the reviewer's first contact with Section 10; "language families, scripts, cultures" fires only for multilingual benchmarks yet reads as universally required.
- **Fix:** Core/supporting split: core — coverage analysis matching the claimed capability space, documented exclusions, limits on generalization, expert review where relevant; supporting (rate only where the construct claims them) — language/script/culture spread, context-length bins, task horizons, environment states.
- **EFPA link:** EFPA §10.1 content validity — retained; inflation MESA-original.

### F-20-template-s10b-3 — [Minor] 10.6.1 and 10.6.2 rate the same broad-claim evidence twice
- **Axis:** repetition
- **Where:** `MESA EFPA template official.md:2054-2064`
- **Quote:** > Excellent: Score interpretations are explicitly bounded... and public language avoids unsupported extrapolation from scores to broad capability, expert-level competence, long-horizon agency, real-world readiness, AGI, autonomy, or general intelligence. *(10.6.1)* — > Excellent: If broad score interpretations are made, the benchmark provides evidence across relevant capability domains... otherwise it explicitly rejects or limits such interpretations. *(10.6.2)*
- **Why it fails a user:** Both items trigger on the same claims with the same evidence (the benchmark's public framing plus the 2.1/2.5 domain mapping); 10.6.2 is the conditional-evidence test and 10.6.1 the boundedness test, but for any benchmark that either makes or disclaims broad claims, the two ratings are determined together. In the case studies both benchmarks with AGI framing would receive coupled scores — one item's worth of information for two items' work.
- **Fix:** Merge into one item "10.6.1 Proportionality of score interpretations" with the conditional inside the anchor: "Excellent: Score interpretations are explicitly bounded by the task sample, scoring rule, and validation evidence. Where broad interpretations (AGI, general intelligence, agency, autonomy) are made, evidence spans the relevant capability domains (2.1/2.5); otherwise such interpretations are explicitly rejected or limited." 15 → 14 rated items. Parser note: removing item 10.6.2 orphans stored answers under that ID — same migration bucket as the 9.x renumbering (F-20-template-s09-2).
- **EFPA link:** MESA-original sub-section (no EFPA counterpart); the merge preserves both functions in one anchor.

---

## Verdict
- **Disposition:** Trim (one anchor rewritten, one split, one merge)
- **Items:** 15 rated → 14 (≈ −100 words)
- **Rationale:** The template's most important section has the right taxonomy and two strong MESA-original additions; its defects are concentrated in anchors — one hard-codes source-benchmark residue, one over-enumerates, and the proportionality pair double-charges the reviewer for one judgment.
