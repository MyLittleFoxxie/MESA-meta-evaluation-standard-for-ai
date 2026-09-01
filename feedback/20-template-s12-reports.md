# Feedback — `20-template-s12-reports` (`MESA EFPA template official.md:2314-2432`)

Unit reviewed: Section 12 — preamble (:2316-2324), guidance table (:2326-2334), 12.1 (2 items),
12.2 (2), 12.3 (2), 12.4 (3), 12.5 overall. 10 rated items.

Verification notes: Figure 5's forward references from Section 11 are accurate — "12.4
Fairness, Acceptability, and Public Communication" (:2394) and items 12.3.1/12.4.1-12.4.3 all
exist as referenced. The EFPA-mapping sentence is present (:2316), and the inference-level
principle (:2322 — "whether reports support the level of inference they invite") is the
section's best sentence. The 12.3.1-vs-10.6.1 adjacency is a defensible communication-vs-
evidence role split (logged to the claims-cluster map for synthesis). One source-visibility
question is deferred: 12.4.3's governance content (private-set governance, retraction,
eligibility, refresh labels) is plainly informed by The Leaderboard Illusion, but only
BetterBench is cited in the preamble (:2318) — whether the template's bibliography covers it
is checked at `20-template-99-final`.

---

### F-20-template-s12-1 — [Major] "Judge reporting quality for each major output surface" — with one rating field per item
- **Axis:** vagueness (form contract)
- **Where:** `MESA EFPA template official.md:2324`
- **Quote:** > Judge reporting quality for each major output surface that shapes use: paper tables, dataset cards, hosted leaderboards, downloadable results, public announcements, scorecards, badges, dashboards, and model-result pages.
- **Why it fails a user:** EFPA §12 is explicitly iterated — "This overall rating is provided for each report" (`EFPA_Test_Review_Model_2025_Markdown.md:2570`) — because a paper table and a public leaderboard can deserve opposite ratings (exactly the HLE case: careful paper, caveat-dropping leaderboard). MESA keeps the per-surface instruction but the form provides one rating per item, so the reviewer must either average surfaces (which :2425 forbids in spirit) or silently pick one. This is the third appearance of the dropped-iteration problem (F-20-template-s04-1, F-20-template-s08-4).
- **Fix:** Add a decision rule to :2324: "Rate each item against the most consequential public surface (normally the primary leaderboard or headline report); where another surface would rate materially differently, name it and its divergent rating in the item's Reviewer comments." Longer term, a per-surface fill-in table (surface | rating | note) before 12.1 would restore EFPA's iteration within the parser's table convention.
- **EFPA link:** EFPA §12 per-report rule (`:2570`) — dropped mechanism, retained instruction; fix restores the function.

### F-20-template-s12-2 — [Minor] Per-item "Reviewer comments:" fields start mid-section, and 12.4.3's block is missing its separator
- **Axis:** complexity and cognitive load (form consistency)
- **Where:** `MESA EFPA template official.md:2381, :2390, :2403, :2412, :2421` (present) vs 12.1.1-12.2.2 (absent); missing `---` between `:2421` and `:2423`
- **Quote:** > Rating: [n/a | 0 | 1 | 2 | 3 | 4] ⏎ ⏎ Reviewer comments: *(from 12.3.1 onward only)*
- **Why it fails a user:** Sections 6-11 place one comments field at section end; Section 12 switches mid-stream to per-item comments at 12.3.1 — the live form therefore renders six comment boxes in the back half of Section 12 and none in the front half, which reads as (and probably is) an editing artifact rather than a design decision. The missing `---` after :2421 also breaks the item-separator rhythm the rest of the template maintains.
- **Fix:** Choose one policy: per-item comments only where divergence is expected (12.2.1, 12.4.3 — consistent with F-s12-1's divergent-surface rule), or a single section-end field like Sections 6-11. Add the missing `---` after :2421. Parser note: each standalone "Reviewer comments:" line is a free-text prompt; removing some deletes stored answers under those prompts — same migration bucket as the ID renumberings.
- **EFPA link:** EFPA per-item comment convention varies by section — MESA should pick one and say so.

### F-20-template-s12-3 — [Minor] 12.4.3's anchor duplicates its own elements
- **Axis:** verbosity
- **Where:** `MESA EFPA template official.md:2418`
- **Quote:** > Excellent: Public score interpretations, rankings, badges, headlines, and rules for leaderboard submissions, eligibility, updates, versions, ranking, audits, and public score claims are transparent, cautious, versioned, resistant to overinterpretation, and clear about update rules, eligibility, cohort or refresh labels, deprecation or archival rules, ranking uncertainty, raw output or trace audit route, private-set governance, public claim rules, capability-domain claim limits where applicable, and known limitations.
- **Why it fails a user:** ~60 words in which "eligibility", "updates/update rules", "ranking", and "public score claims/public claim rules" each appear twice — the subject list and the predicate list were drafted separately and never reconciled. Combined with the bloat family (12.2.1 carries 15 elements), the section's two most decision-relevant anchors are its least readable.
- **Fix:** One pass de-duplicating subject and predicate: "Excellent: Public rankings, badges, and headlines are transparent, cautious, and versioned; leaderboard governance states submission and eligibility rules, update and refresh labels, deprecation rules, ranking uncertainty, audit routes for raw outputs, private-set governance, and claim limits (capability-domain limits where applicable)." (−20 words, zero repeats.) Apply the 10.5.1 two-tier pattern if a supporting tier is wanted.
- **EFPA link:** EFPA §12 governance concerns — retained; duplication is drafting residue.

### F-20-template-s12-4 — [Nit] 12.2's preamble and 12.2.1's anchor state the run-conditions formula back to back
- **Axis:** repetition
- **Where:** `MESA EFPA template official.md:2356` and `:2360` (family: F-20-template-s08-1)
- **Quote:** > ...traced to the prompts, settings, tools, time limits, access rules, hardware, and human-intervention rules that produced it... *(:2356, followed four lines later by the same list inside 12.2.1's anchor)*
- **Why it fails a user:** The template's worst adjacency of the ten-site formula — the reviewer reads the 13-word list twice within one sub-section.
- **Fix:** Resolved automatically by the run-conditions substitution (F-20-template-s08-1); recorded here so the s12 pass is traceable.
- **EFPA link:** covered by F-20-template-s08-1.

---

## Verdict
- **Disposition:** Trim (restore the per-surface mechanism, normalize comments, de-duplicate two anchors)
- **Items:** 10 rated → 10 (≈ −80 words)
- **Rationale:** The section MESA most needed to add beyond EFPA's scope, with the right inference-level principle at its head; its failures are mechanical — a dropped iteration rule inherited from Section 4's same mistake, a comments pattern that changes mid-section, and anchors that repeat themselves.
