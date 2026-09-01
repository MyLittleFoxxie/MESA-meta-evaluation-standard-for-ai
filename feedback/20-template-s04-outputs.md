# Feedback — `20-template-s04-outputs` (`MESA EFPA template official.md:767-922`)

Unit reviewed: Section 4 preamble (:769), 4.1 Output Availability (:771-789), 4.2 Output Name
or Description (:791-797), 4.3 Design/Presentation (:799-812), 4.4 Output Structure
(:814-833), 4.5 Sensitivity to Context (:836-847), 4.6 Development of Outputs (:849-862), 4.7
Modifiability (:864-873), 4.8 Linkage Status (:875-885), 4.9 Output Content (:887-904), 4.10
Intended Recipients (:906-919). EFPA counterpart: Section 4 "Digitally-generated reports"
(`EFPA_Test_Review_Model_2025_Markdown.md:450-567`), 1:1 subsection mapping preserved.

What holds up: the leaderboard/dashboard/trace reading of EFPA's "digitally generated reports"
is a natural fit, and the preamble does it in one clean sentence (:769) with the
descriptive/evaluative fence intact. 4.8's retitle ("Documented Linkage Status Between Tasks,
Scoring, and Report Labels") is clearer than EFPA's "Transparency". 4.5 and 4.7 add "Not
documented" options EFPA lacks — the right AI-context move. Machine-contract check: "List
available contexts:" (:845) and "Describe origin of report content:" (:862) parse as intended
free-text prompts; all lists and the 4.2 fill-in table parse; no violations.

---

### F-20-template-s04-1 — [Major] EFPA's per-report iteration rule was dropped, making the select-one items unanswerable for multi-output benchmarks
- **Axis:** EFPA traceability (dropped function)
- **Where:** `MESA EFPA template official.md:771-789` (4.1) and `:793-795` (4.2, single placeholder row); contrast `EFPA_Test_Review_Model_2025_Markdown.md:454`
- **Quote:** > If there is more than one report, please complete 4.2 to 4.10 for each report. *(EFPA:454 — no MESA equivalent anywhere in Section 4)*
- **Why it fails a user:** AI benchmarks in scope almost always have multiple outputs — a paper results table, a public leaderboard, sometimes a dashboard and an API. MESA 4.1 catalogs availability well, but 4.2's table has one placeholder row and nothing tells the reviewer to answer 4.3-4.10 per output. The "Select one" items then break: for a benchmark with a static paper table and a modifiable interactive leaderboard, 4.7 Modifiability has two true answers and one checkbox; same for 4.5 and 4.8. Reviewers will silently anchor on different outputs and their reviews will disagree while both being "correct".
- **Fix:** Restore the EFPA rule as one sentence at the top of 4.2: "If more than one output exists, complete 4.2-4.10 for each output, or state in 4.2 which single output the following answers describe." Give 4.2 three placeholder rows (same fix as F-20-template-s02b-5). Parser impact: none — added rows are fill-in cells; the sentence is a paragraph.
- **EFPA link:** EFPA 4.1 (`:452-456`) — dropped; restoring is pure retention.

### F-20-template-s04-2 — [Major] 4.10 restates 2.4 — EFPA's two distinct questions collapsed into one, asked twice
- **Axis:** repetition
- **Where:** `MESA EFPA template official.md:906-919` (4.10) vs `:236-249` (2.4)
- **Quote:** > - [ ] Benchmark maintainers
> - [ ] Model developers
> - [ ] AI researchers
> - [ ] Safety evaluators *(4.10, :910-913 — all eight 4.10 options appear in 2.4's nine)*
- **Why it fails a user:** EFPA 2.4 asks who *uses the test* (psychologists, HR professionals — `EFPA:179-188`); EFPA 4.10 asks who *receives reports*, classified by interpretive competence — qualified users who can read technical output vs. test takers and third parties who need plain language (`EFPA:554-565`). In MESA both collapse to "who consumes benchmark outputs", so the reviewer answers the same audience question twice with near-identical checklists (8 of 4.10's 8 options are in 2.4's list). The one EFPA dimension that mattered for Part B §12 — can this recipient class interpret technical output, or must caveats be pre-digested for them? — survives nowhere.
- **Fix:** Two options. (a) Cheapest: delete 4.10, add "Public audience" to 2.4, and have Section 4's preamble note that intended recipients are recorded in 2.4. (b) Truer to EFPA: keep 4.10 but re-ask it as the competence question — "For each recipient class in 2.4, is the output interpretable without benchmark-specific expertise? Which outputs assume technical knowledge of the metric?" — one fill-in table, two columns. Either way, one home for the audience list. Parser impact: deleting a subsection or converting to a small fill-in table are both parser-safe.
- **EFPA link:** EFPA 2.4 (`:179`) and 4.10 (`:554-565`) — drifted: two functions merged, then duplicated; fix (b) restores the lost function.

### F-20-template-s04-3 — [Minor] One 4.1 option is a strict subset of another
- **Axis:** repetition
- **Where:** `MESA EFPA template official.md:777-778`
- **Quote:** > - [ ] Public model responses, traces, logs, judge rationales, or per-item data available
> - [ ] Public traces or logs available
- **Why it fails a user:** :778 is entirely contained in :777. Whatever a reviewer means by ticking :778, :777 already says it; ticking one but not the other creates a contradiction a reader cannot resolve.
- **Fix:** Delete :778, or narrow :777 to "Public model responses, judge rationales, or per-item data available" so the two options partition (responses/judgments vs. execution traces/logs). The partition version is more informative.
- **EFPA link:** MESA-original list (EFPA 4.1 is Yes/No); internal defect only.

### F-20-template-s04-4 — [Minor] 4.4's fifteen structure labels have no definitions — EFPA's were dropped
- **Axis:** vagueness
- **Where:** `MESA EFPA template official.md:818-832`
- **Quote:** > - [ ] Capability-domain based
> - [ ] Capability-domain profile based
- **Why it fails a user:** EFPA 4.4 defines each structure option in the label itself ("Criterion-based: where the report focuses on links to empirical outcomes" — `EFPA:490-494`). MESA offers fifteen bare labels including pairs with no discernible boundary ("Capability-domain based" vs "Capability-domain profile based"; "Aggregate-score based" vs "Suite-aggregate based"). Fifteen undefined options in a select-all is noise: ticks become unfalsifiable and unreliable.
- **Fix:** Cut to ~8 options and give each a one-line definition in the label, EFPA-style: e.g. "- [ ] Capability-domain profile (scores broken out per domain, no single total)", "- [ ] Suite aggregate (one score combining multiple component benchmarks)". Parser impact: none — longer checkbox labels parse unchanged.
- **EFPA link:** EFPA 4.4 (`:487-495`) — drifted: option set adapted, definitions dropped.

### F-20-template-s04-5 — [Minor] 4.8's five options include two indistinguishable middle grades in a select-one
- **Axis:** vagueness
- **Where:** `MESA EFPA template official.md:879-883`
- **Quote:** > - [ ] Partial linkage between benchmark tasks, scores, reported score interpretations, and capability-domain labels
> ...
> - [ ] Mixture of clear and concealed linkage
- **Why it fails a user:** EFPA 4.8 has three disjoint grades: clear / black box / mixture (`EFPA:534-536`). MESA added "Partial linkage" while keeping "Mixture of clear and concealed linkage" — no reviewer can say which of the two a half-documented leaderboard belongs to, and "Not documented" vs "Linkage is not obvious from available documentation" blur the same way. A select-one with overlapping anchors fails the two-reviewers test outright.
- **Fix:** Return to three disjoint grades plus absence: "Clear linkage / Mixed (some scores clearly linked, others not) / No discernible linkage (black box) / No documentation to judge from." Delete "Partial linkage".
- **EFPA link:** EFPA 4.8 Transparency (`:531-536`) — drifted: a fourth overlapping grade was inserted into a clean three-grade scale.

### F-20-template-s04-6 — [Nit] "actuarial" survives translation into an audience that won't know it
- **Axis:** terminology
- **Where:** `MESA EFPA template official.md:854`
- **Quote:** > - [ ] Based on empirical or actuarial relationships
- **Why it fails a user:** "Actuarial" is psychometric-tradition jargon (statistical prediction tables); benchmark authors read it as insurance vocabulary.
- **Fix:** **Substitute:** "- [ ] Based on documented statistical relationships with outcomes". No loss — "empirical or actuarial" was already one concept.
- **EFPA link:** EFPA 4.6 (`:513`) — retained verbatim where translation was needed.

---

## Verdict
- **Disposition:** Trim (delete or repurpose 4.10; restore per-output iteration; define or cut 4.4's labels)
- **Items:** 10 subsections, ~70 options + 1 fill-in table → 9 subsections, ~52 options + expanded 4.2 table
- **Rationale:** The adaptation concept is sound and several subsections improve on EFPA, but the section inherits every systemic Part A defect at once — dropped iteration rule, duplicated audience list, undefined labels, subset options — and they compound in the same ten pages.
