# Feedback — `80-xcut-paper-template-consistency`

Scope: does `paper.tex:140-189` describe the template that exists? Drift against
`.codex/memory/template-structure.md` (281-line self-declared mirror) and the README phase
lists. Sources: full template read (Part A units + this run), paper §IV (unit 04), mirror
(read in full), README :14-38.

## Verification results

**Paper §IV vs. template — substantially accurate.** Table II's thirteen rows match the
template's architecture including Appendix A's position; the S12 "Dashboards" discrepancy
flagged in F-10-paper-04-5 was this review's own error (stale ledger title) and was corrected
in place — the paper matches the template heading (`:2314`) exactly. Rating-scale semantics
match (paper explains only n/a-0-1: F-10-paper-04-2). The two real paper↔template gaps are
already filed: the :180 coherence defense contradicted by same-role duplicates
(F-10-paper-04-1) and the :177 hold-fixed-conditions statement missing from the template's
Final Evaluation (F-20-template-99-2) — the latter is the single most consequential drift,
because it is the paper's signature deliverable.

**Mirror vs. template — accurate.** Every heading, item list, rating-scale row, and the
three-entry bibliography in `template-structure.md` matches the template as read. The mirror
also correctly warns that numbering is load-bearing ("the site's PDF export, the
review-heading-consistency checks depend on numbered headings matching the template verbatim")
— which hardens every ID-renumbering proposal in this review (9.x flatten, 10.6 merge, 11.3
merge, 5.1 retitle): each must update template + mirror + stored form answers + tooling in one
change.

**README vs. template — consistent** in structure and boundary language; one naming variant
noted below.

---

### F-80-xcut-consistency-1 — [Major] Template Figure 1 depicts a section that exists only as a house convention in reviews
- **Axis:** EFPA traceability (artifact consistency)
- **Where:** `MESA EFPA template official.md:36` (ShortDesc node) vs `.codex/memory/template-structure.md:27-36`
- **Quote:** > Every review in `reviews/` also carries two sections that are **not** part of `MESA EFPA template official.md` itself — they are a house convention layered on top of the template. [...] **Short Stand-Alone Non-Evaluative Benchmark Description** [...] **Source Inventory**
- **Why it fails a user:** This resolves the Figure-1 orphan node (F-20-template-00-7) with a worse diagnosis than "decorative": the template's own overview figure depicts a deliverable the template never collects, which real reviews then supply via an undocumented convention a new reviewer cannot know about. The Source Inventory — arguably the review's evidentiary backbone (the paper's own worked example depends on source-grounding) — likewise has no home in the template or the live form. Meanwhile Appendix A ("General Description") half-overlaps the Short Description's function, so the corpus has two description devices, one homeless.
- **Fix:** Promote both house sections into the template: a "Short Stand-Alone Benchmark Description" free-text prompt and a Source Inventory fill-in table (ID | source | access date | use), placed before Section 1 — both parser-compatible conventions. Then either merge Appendix A into the Short Description or state their division (one-paragraph reader summary vs. fuller non-evaluative account). Figure 1 becomes accurate without edits.
- **EFPA link:** EFPA's General Description section — the house convention is the de-facto adaptation; it belongs in the instrument, not in agent memory.

### F-80-xcut-consistency-2 — [Minor] The 5.1/5.2 duplicate heading is defended as "by design" — in a memory file the reviewer never sees
- **Axis:** complexity and cognitive load
- **Where:** `.codex/memory/template-structure.md:108` vs `MESA EFPA template official.md:941/:957` (F-20-template-s05-1)
- **Quote:** > *(Note: 5.1 and 5.2 share the same heading text in the canonical template by design — 5.1 covers documentation artifacts, 5.2 covers the access/distribution route.)*
- **Why it fails a user:** The Part A review read the identical headings as a copy-paste defect; the mirror asserts intent. Either way the template user faces two sections with the same name and no in-template disambiguation, and heading-derived item IDs collide in the live form. A design decision that must be explained in an agent-memory aside is a design decision the artifact failed to communicate.
- **Fix:** F-20-template-s05-1's retitle stands ("5.1 Documentation Artifacts Provided"), now with the mirror's note as evidence of intended scope; update the mirror in the same change per its own sync rule.
- **EFPA link:** EFPA §5 separates supply and documentation items under distinct names — the retitle restores EFPA's clarity.

### F-80-xcut-consistency-3 — [Minor] The framework has four names across three artifacts
- **Axis:** terminology
- **Where:** `paper.tex:140` ("The MESA Test Review Model"), `paper.tex:61` ("MESA (Meta-Evaluation Standard for AI Benchmarks)"), `MESA EFPA template official.md:1` ("MESA EFPA Template"), template Figure 1 (`:33`, "MESA Review Model")
- **Quote:** > \section{The MESA Test Review Model} — vs — # MESA EFPA Template — vs — MESA Review Model *(Figure 1 root node)*
- **Why it fails a user:** A reader moving from paper to repository must infer that "MESA Test Review Model", "MESA Review Model", and "MESA EFPA Template" are one artifact; a citation or search on any one name misses the others.
- **Fix:** One canonical name — "the MESA Test Review Model" for the framework, "the MESA template" for the markdown artifact implementing it — applied to the template H1 ("MESA Test Review Model — Review Template"), Figure 1's root node, and README. The paper already conforms.
- **EFPA link:** EFPA maintains one name ("EFPA Test Review Model") across all its artifacts — retained in spirit, drifted in execution.

### F-80-xcut-consistency-4 — [Minor] Four surfaces must now be edited in lockstep — and the README already drifted once
- **Axis:** complexity and cognitive load (maintenance)
- **Where:** `README.md:24` ("Supply & Materials") vs template Section 5 ("Benchmark Access, Materials, and Lifecycle"); sync rule at `.codex/memory/template-structure.md:8-10`
- **Quote:** > 5. **Supply & Materials:** Technical documentation, changelogs, and usage requirements.
- **Why it fails a user:** Section names live in four places — template headings, template Summary of Ratings (`:2457`, already drifted: F-20-template-99-3), paper Tables II/III (Table III drifted: F-10-paper-06-1), and README/mirror ("Supply & Materials" is EFPA's old vocabulary, not the template's). Every rename in the `/mesa-core-plan` work multiplies by four.
- **Fix:** Make the mirror the declared name authority (it already claims numbering authority); add to `/mesa-core-plan` a closing task: regenerate the Summary of Ratings rows, paper table rows, and README list from the mirror's headings, and fix "Supply & Materials" → "Access, Materials, and Lifecycle" now.
- **EFPA link:** n/a — repository hygiene.

---

## Verdict
- **Disposition:** Keep as-is (the consistency machinery exists and mostly works; fix the four filed drifts)
- **Items:** 4 artifacts compared → 2 already-filed cross-references + 4 new findings
- **Rationale:** The paper describes the template honestly and the mirror is genuinely in sync; the residual drift concentrates in names (four for the framework, three for some sections) and in the house-convention sections that Figure 1 promises but only `reviews/` delivers.
