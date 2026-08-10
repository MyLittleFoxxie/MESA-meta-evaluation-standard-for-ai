# Feedback — `20-template-s11-fair-use` (`MESA EFPA template official.md:2078-2313`)

Unit reviewed: Section 11 — preamble (:2080-2086), Figure 5 cross-reference map (:2088-2193),
groups paragraph (:2195), guidance table (:2197-2205), 11.1 (2 items), 11.2 (2), 11.3 (3),
11.4 (2), 11.5 (2), 11.6 overall. 12 rated items.

The adaptation honesty here is exemplary: the mapping sentence is present (:2080), and :2082's
"Responsible use in AI benchmark review includes, but is broader than, demographic fairness"
is exactly the right reframing of EFPA's human-fairness section. 11.3.3 (temporal comparability
for rolling/live benchmarks) is a first-class MESA-original item no psychometric source could
have supplied. The run-conditions formula at :2249 is covered by F-20-template-s08-1. The
11.2.2-vs-10.1.1 coverage overlap is the fairness-vs-validity lens split EFPA itself maintains
— acceptable. Parser check: items conventional; Figure 5 is a legal mermaid block.

---

### F-20-template-s11-1 — [Major] Figure 5 demands 24 bare-number cross-lookups, forward-references Section 12, and visually annexes 12.4 into Section 11
- **Axis:** complexity and cognitive load
- **Where:** `MESA EFPA template official.md:2088-2193`
- **Quote:** > S116("12.4 Fairness, Acceptability,<br/>and Public Communication") [...] D116a("12.3.1") D116b("12.4.1") D116c("12.4.2") D116d("12.4.3")
- **Why it fails a user:** The figure's nodes are bare item numbers (6.1.1, 7.1.5, 9.4.3...) — the reviewer must page back across five sections to decode 24 of them. Worse, one of its six columns is headed by a *Section 12* sub-section (12.4) whose four items the reviewer has not yet reached, so the map both breaks the linear workflow and makes 12.4 look like part of Section 11. One node ("10.5") is a sub-section while the rest are items — inconsistent granularity. This renders in the live form exactly as authored.
- **Fix:** Replace the figure with a compact table: | Related rating | Title | Bears on |, with the Section 12 rows marked "revisit after Section 12" — or move the whole map into the Final Evaluation's revisit checkpoint (F-20-template-s06-2), where cross-section reconciliation belongs. If a figure is kept, one column per *this* section's sub-sections only.
- **EFPA link:** EFPA §11 also cross-references other sections, but by named concept in prose — the bare-number diagram is MESA-original.

### F-20-template-s11-2 — [Major] 11.3.1 and 11.3.2 are the same item written twice
- **Axis:** repetition
- **Where:** `MESA EFPA template official.md:2249` (11.3.1) and `:2256` (11.3.2)
- **Quote:** > Excellent: Prompts, settings, tools, time limits, access rules, hardware, and human-intervention rules support fair comparison across intended AI systems, including model versions, API or local access modes, tool availability, context limits, compute budget, multimodal inputs, safety or refusal policies, latency constraints, and system-specific affordances. *(11.3.1)* — vs — > Excellent: Access routes, compute requirements, hardware assumptions, API limitations, local execution constraints, tool-use differences, context windows, external service access, and hosted/private evaluation routes are documented and managed so that score comparisons are not distorted without warning. *(11.3.2)*
- **Why it fails a user:** Both anchors enumerate API/local access, tools, compute, hardware, and context; the nominal distinction (conditions *support* comparison vs. constraints *are documented and managed*) cannot be rated separately — any evidence satisfying one satisfies the other. Two reviewers will produce coupled ratings and wonder what the second item added. Same-role duplication, the kind the paper's coherence defense (`paper.tex:180`) says the template avoids.
- **Fix:** Merge into one item "11.3.1 Cross-system and access-condition comparability": "Excellent: Run conditions (see glossary) and access constraints — API or local mode, tool availability, compute and hardware, context limits, safety/refusal policies — are documented and managed so intended systems can be compared without undisclosed distortion; condition labels or separate cohorts are used where differences affect interpretation." 12 → 11 rated items; ID migration joins the 9.x/10.6 bucket.
- **EFPA link:** EFPA §11 comparability concern — retained; the split into two items is MESA-original and unearned.

### F-20-template-s11-3 — [Minor] 11.1.2 re-rates 6.2.6 without a stated boundary
- **Axis:** repetition (cross-section)
- **Where:** `MESA EFPA template official.md:2220` (11.1.2) vs `:1299` (6.2.6)
- **Quote:** > Excellent: Documentation gives clear details of fairness, accessibility, bias, language, domain, modality, sensitive-content, and comparability issues considered during benchmark design, evaluation, and interpretation. *(11.1.2; 6.2.6 rates "fairness, accessibility, language or domain coverage, cross-system comparability, evaluation-condition comparability, and any restrictions")*
- **Why it fails a user:** Both items rate the adequacy of fair-use documentation; Figure 5 itself lists 6.2.6 as feeding 11.1. Without a boundary sentence, the second rating is a re-rating — and divergent scores for 6.2.6 and 11.1.2 will look like reviewer error.
- **Fix:** Add one boundary bullet to 11.1.2: "6.2.6 rates whether fair-use documentation *exists and is usable*; this item rates whether the fairness consideration it documents was *substantively adequate* for the intended contexts. Divergent ratings should be explained in comments." (EFPA carries a similar dual structure; making the division explicit is the MESA improvement.)
- **EFPA link:** EFPA §6 documentation vs §11 fairness items — retained duplication, needs the boundary EFPA also leaves implicit.

### F-20-template-s11-4 — [Minor] The preamble enumerates the relevant-differences list twice
- **Axis:** verbosity
- **Where:** `MESA EFPA template official.md:2084` and `:2195`
- **Quote:** > ...review language-family and script coverage, local cultural authorship, translation or adaptation method, community consent or participation where relevant, model access mode, API/local comparability, tool availability, context length, safety or refusal policy, and compute budget. *(:2084)* — vs — > Relevant differences may include model family, language, modality, API versus local deployment, context window, tool access, refusal behavior, safety policy, compute budget, domain expertise... *(:2195)*
- **Why it fails a user:** Two 10-14-element lists with ~8 shared members, separated only by the figure; the reviewer reads the same inventory twice before the first item, which then enumerates it a third time (11.3.1).
- **Fix:** Keep :2195 (it defines groups/contexts, the section's scoping move); cut :2084's list to its two non-overlapping ideas — cultural authorship/community participation, and the cohort-labeling rule ("Leaderboards comparing API-hosted, open-weight, tool-using, and local systems need condition labels or separate cohorts"). −35 words.
- **EFPA link:** n/a — guidance economy.

---

## Verdict
- **Disposition:** Trim (merge one item pair, fix or relocate the map, one boundary bullet)
- **Items:** 12 rated → 11 (≈ −120 words)
- **Rationale:** The section's reframing of fairness for AI benchmarks is genuinely strong and 11.3.3 is a model MESA-original item, but its middle is padded by a duplicated comparability item and a cross-reference figure that costs more navigation than it saves.
