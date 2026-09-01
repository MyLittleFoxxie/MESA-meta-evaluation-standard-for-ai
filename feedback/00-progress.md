# MESA Self-Review — Progress Ledger

**REVIEW COMPLETE (2026-08-09).** All 27 content units and 4 cross-cutting units are done.
Totals: 122 findings — 0 Blockers / 31 Majors / 72 Minors / 19 Nits. Entry point for
consumers: `feedback/90-synthesis.md`. `/mesa-core-plan` is now unblocked.

Maintained by the `mesa-self-review` skill. One unit per invocation: read this ledger, review
the first `pending` unit, write `feedback/<unit-id>.md`, update this file, stop.
Done format: `done (B/M/m/N)` = Blocker/Major/Minor/Nit finding counts.

## Paper units — `paper.tex`

| id | span | section | status |
|---|---|---|---|
| `10-paper-00-title-abstract` | 20-50 | Title, abstract | done (0/2/4/1) |
| `10-paper-01-introduction` | 51-71 | Introduction | done (0/0/6/1) |
| `10-paper-02-related-work` | 72-91 | Related Work (+2 subsections) | done (0/1/3/0) |
| `10-paper-03-methodology` | 92-139 | Methodology (+3 subsections; figures at 99, 106) | done (0/2/1/1) |
| `10-paper-04-mesa-model` | 140-189 | The MESA Test Review Model (5 `\paragraph` pseudo-headings) | done (0/1/3/1) |
| `10-paper-05-case-study-design` | 190-209 | Case Study Design (worked example inlined at 204) | done (0/0/2/1) |
| `10-paper-06-case-study-results` | 210-265 | Case Study Results (HLE, ARC-AGI-2, DesignQA, overall) | done (0/0/1/1) |
| `10-paper-07-discussion` | 266-279 | Discussion | done (0/0/2/1) |
| `10-paper-08-limitations` | 280-301 | Limitations and Threats to Validity | done (0/1/1/0) |
| `10-paper-09-future-conclusion` | 302-321 | Future Work, Conclusion | done (0/0/2/0) |

## Template units — `MESA EFPA template official.md`

| id | span | section | status |
|---|---|---|---|
| `20-template-00-frontmatter` | 1-97 | Introduction, How the Model Should Be Used, Figure 1 | done (0/0/7/0) |
| `20-template-s01-factual` | 101-148 | 1. Factual Description | done (0/1/1/1) |
| `20-template-s02-classification-a` | 149-397 | 2. Classification: preamble + 2.1-2.9 | done (0/3/2/1) |
| `20-template-s02-classification-b` | 398-591 | 2. Classification: 2.10-2.18 | done (0/1/4/1) |
| `20-template-s03-measurement` | 592-766 | 3. Measurement and Scoring | done (0/2/4/1) |
| `20-template-s04-outputs` | 767-922 | 4. Benchmark Outputs and Reports | done (0/2/3/1) |
| `20-template-s05-access` | 923-1122 | 5. Access, Materials, Lifecycle + Appendix A | done (0/3/3/0) |
| `20-template-partb-preamble` | 1123-1165 | Information Sources, Explanation of Ratings, General Guidance | done (0/1/2/2) |
| `20-template-s06-rationale` | 1166-1382 | 6. Rationale, Development, Documentation, Task/Item Quality | done (0/1/2/1) |
| `20-template-s07-materials` | 1383-1468 | 7. Quality and Usability of Benchmark Materials | done (0/1/3/0) |
| `20-template-s08-baselines` | 1469-1623 | 8. Baselines, Comparators, Reference Interpretation | done (0/1/3/1) |
| `20-template-s09-reliability` | 1624-1815 | 9. Reliability, Precision, Score Stability | done (0/1/1/1) |
| `20-template-s10-validity-a` | 1816-1943 | 10. Validity Evidence: preamble, Figure 4, guidance table | done (0/0/2/0) |
| `20-template-s10-validity-b` | 1944-2077 | 10. Validity Evidence: items 10.1-10.7 | done (0/1/2/0) |
| `20-template-s11-fair-use` | 2078-2313 | 11. Fair Use, Comparability, Appropriate Use | done (0/2/2/0) |
| `20-template-s12-reports` | 2314-2432 | 12. Quality of Reports, Leaderboards, Public Claims | done (0/1/2/1) |
| `20-template-99-final` | 2433-2479 | Final Evaluation, Bibliography | done (0/2/1/1) |

## Cross-cutting units — run last, only after every unit above is `done`

| id | scope | status |
|---|---|---|
| `80-xcut-paper-template-consistency` | paper.tex:140-189 vs actual template; drift vs `.codex/memory/template-structure.md` and README phase lists | done (0/1/3/0) |
| `80-xcut-terminology` | Consolidate Cross-cutting log into term table (Substitute / Keep+define / Split) | done (table: 20 terms → 10-entry glossary) |
| `80-xcut-length-budget` | Rateable items per section, estimated reviewer hours, burden concentration | done (analysis: 28-45h full review; −14% via filed fixes) |
| `90-synthesis` | Findings by severity; top-ten usability changes; "is the template too long, and by how much?" | done (122 findings: 0B/31M/72m/19N; 10 change-packages; two-tier answer) |

Line numbers are a starting map — if a file has shifted, locate the section by heading and
record the corrected span here.

## Cross-cutting log

- `claim proportionality` first use `paper.tex:44` (abstract), undefined; verdict candidate: Substitute → "claims that outrun what the scores support" (F-10-paper-00-5). Watch for body first-use and senses.
- `construct validity` first use `paper.tex:44` (abstract), no inline definition; Keep+define candidate — definition belongs at first Introduction/body use, not abstract.
- Verdict formula "best characterized as X, rather than a standalone Y" ×3 in abstract (`paper.tex:44`); expect recurrence in Case Study Results (210-265) — flag as repetition if abstract keeps the long form.
- Use-case triple "model selection / safety / procurement" appears twice in abstract (`paper.tex:44` opening and closing); watch Introduction and Discussion for third+ occurrences.
- Part A/Part B naming: paper glosses "Descriptive"/"Evaluative"; EFPA originals are "Part A. Description of the instrument" (`EFPA_Test_Review_Model_2025_Markdown.md:97`), "Part B. Evaluation of the Instrument" (`:613`) — retained, link visible.
- RE orientation is paper-framing only: template audience list (`MESA EFPA template official.md:9`) contains no RE role; recheck at `80-xcut-paper-template-consistency` (F-10-paper-00-6).
- "unrevised benchmarks" (`paper.tex:44`) = wrong word for "unaudited"; check body for recurrence of "revise/revision" in the review sense.
- Entity taxonomy: three variant lists at template `:13` (11 items), `:21` (7 items, renamed), `:1259` (6 items); "rolling version"↔"rolling cohort", "evaluation slice"↔"slice" — check Section 1 entity-type options against these (F-20-template-00-2).
- Phrase "the specific meaning users are supposed to draw from a score" verbatim at template `:11`, `:19`; canonicalize as "the intended score meaning" (F-20-template-00-3). Track further occurrences.
- `calibration` (model-capability sense) first use template `:7`; known Split vs scorer-tuning sense at `:1135`.
- "irrelevant score effects" (template `:11`) — garbled rendering of construct-irrelevant variance; track how Part B names this concept.
- Source-preference guidance (prefer official materials) at template `:25`; expect repeat in Part B preamble `:1123+` — check for triple-statement at section level.
- Template Figure 1 ShortDesc node (`:36`) has no implementing section; Appendix A (`:1115`) is the likely implementer (F-20-template-00-7). Recheck at `20-template-99-final`.
- Template has `## Bibliography` at `:2473` but frontmatter `:11` says "two main review parts plus supporting appendices" (EFPA has explicit Part C) — bookkeeping only; note at `20-template-99-final`.
- Entity taxonomy fourth variant at `:119` (Entity Type placeholder: "derived variant", "harness", "etc.") — escalated to Major in F-20-template-s01-1; canonical-list fix proposed there.
- "review base" coinage at `:103`, single use — Substitute (F-20-template-s01-2).
- "judge" (LLM-judge sense) first use `:122` (1.2 Implementation/Scorer Version), undefined but standard usage; watch for sense drift vs human judges in Part B.
- Parser fact (verified `assets/mesa-form.js:199-216`): colon-terminated line + following checkbox/table = grouplabel (safe); + plain `- ` list = paragraph; otherwise = free-text prompt. Only truly standalone colon lines become fields.
- "Other (describe)" escape option systematically dropped from all Section 2 checklists vs EFPA (F-20-template-s02a-2); check Sections 3-5 and Part B lists for the same pattern.
- 2.6 vs 2.9 near-duplicate response-type checklists (F-20-template-s02a-1); check whether Section 3 scoring lists overlap 2.9's evidence group too.
- EFPA's "up to 3 keywords" prioritization cap on content domains dropped in MESA 2.1 (F-20-template-s02a-3).
- Claimed-construct free-text rows live in 2.5 (:259-262), not 2.1 — Section 10 validity units should check where they point reviewers back to (F-20-template-s02a-5).
- CHC ten-domain descriptions (:157-166) verified faithful to `A_Definition_of_AGI.md:18-38`.
- 2.9 evidence group (:381-394) vs 2.17 scoring-evidence list (:551-567): ~10 shared options; generated-vs-consumed boundary sentence proposed (F-20-template-s02b-2). Check Section 3 scoring tables for a third statement of the same options.
- "Human judge" / "Model judge" first checkbox use at `:563-564`.
- 2.18 broad-claim screen trigger list (:573) includes "reasoning" — fires on nearly every modern benchmark; feed into `80-xcut-length-budget`.
- EFPA 2.12.2 supervision-spectrum definitions dropped in MESA 2.12 identity-controls group (F-20-template-s02b-1).
- Single-placeholder-row fill-in tables under-serve multi-entry cases in the live form (2.15, :522); watch for the same pattern in later sections (F-20-template-s02b-5).
- 2.14 drift is deliberate and good: EFPA reviewer-estimates → MESA documented-estimates-only (:500); cite as a positive pattern in synthesis.
- Score-inventory duplication cluster: 2.5 (:268-272) / 3.2 (:630-633) / 3.7 (:759-760) / 2.18 (:583) — single-home consolidation proposed (F-20-template-s03-1). Check Part B Sections 8-10 for fourth/fifth statements.
- Construct-irrelevant-variance concept now has 2+ names: "irrelevant score effects" (:11) and "non-target rewarded behavior" (:753); track Part B naming.
- 3.6 descriptive uncertainty screen mirrors Part B Section 9; 3.7 mirrors Sections 6/10; check those units for prompts that re-collect the same facts instead of referencing 3.6/3.7.
- 3.5 (baselines/comparators, descriptive) mirrors Part B Section 8; same check.
- LLM-judge method boundary unstated: "LLM equality-checker" (:602) vs "scoring by another model" (:613) (F-20-template-s03-2).
- Escape-option gap continues in 3.1/3.3/3.4/3.5 (F-20-template-s03-6); 3.3 also lacks "Not explicitly stated".
- Audience list duplicated: 2.4 (:240-249) vs 4.10 (:910-917), 8/8 overlap; EFPA's recipient-competence dimension lost (F-20-template-s04-2). Watch Part B §12 for a third audience list.
- EFPA per-report iteration rule (EFPA:454) dropped from Section 4; select-one items break for multi-output benchmarks (F-20-template-s04-1).
- Bare-label pattern (definitions dropped from EFPA options): 2.12 identity controls, 4.4 structure labels, 4.8 linkage grades — same fix family (one-line definitions in the label).
- Single-placeholder-row tables again at 4.2 (:795); same as 2.15 (F-20-template-s02b-5).
- Part A totals: Sections 1-5 done — systemic patterns: (1) duplicated checklists/rows (2.6×2.9, 2.4×4.10, 2.5×3.2×3.7, 5.6×5.8), (2) dropped EFPA escape options, (3) dropped EFPA definitions (2.12, 3.4, 4.4, 4.8), (4) dropped EFPA iteration/prioritization/completion rules (2.1 cap, 4.x per-report, 5.4 none-vs-unclear, Appendix A spec), (5) single-row tables (2.15, 4.2).
- 5.1 heading is a copy-paste duplicate of 5.2's title over documentation-list content (F-20-template-s05-1); retitle changes the live form's derived ID → stored-answers migration note.
- Appendix A spec restored per F-20-template-s05-3 would close the Figure-1 ShortDesc gap (F-20-template-00-7) — link the two in synthesis.
- 5.6/5.8 row inventory deduped in F-20-template-s05-2 (46 → ~36 rows); retirement stated 4× in 5.8 alone.
- Trace/output availability recorded in both 4.1 (:777-778) and 5.5 (:1015-1016) — minor, log-only; revisit at `80-xcut-length-budget`.
- Positive pattern for synthesis: Section 5's escape-hatch discipline (5.2 :961, 5.5 "Not available", 5.6 "Not documented") is the model the rest of the template should copy; BetterBench grounding made explicit at :927.
- "traceability" coined as "the core operational requirement" at `paper.tex:59`; template uses the concept but not the term prominently — check Methodology/MESA-model units and `80-xcut-paper-template-consistency` for whether the term survives past the intro.
- "capability-area" one-off variant of canonical "capability domain" at `paper.tex:61` (F-10-paper-01-4); "execution bias" undefined coinage same line.
- "construct validity" first body use `paper.tex:55` — inline definition proposed there (F-10-paper-01-2); resolves the abstract-review log entry.
- ¶53 (`paper.tex:53`) motivating claims still uncited — the one Reviewer-1 intro comment not yet closed (F-10-paper-01-5).
- RQ1 (`paper.tex:65`) repeats the "RE-oriented" artifact-vs-framing gap (F-10-paper-00-6, F-10-paper-01-6) — third occurrence; consolidate at synthesis.
- Phenomenon→task→metric→claim chain stated 3× (`paper.tex:61, :78, :88`); one-home fix proposed (F-10-paper-02-2). Watch Methodology/MESA-model/Discussion for fourth statements.
- Penn Treebank drift example uncredited to Alonso & Church at `paper.tex:76` (F-10-paper-02-1, Major) — verified against `Evaluating_the_Evaluations.md:57, :226`.
- Verified-accurate attributions (do not re-check): EFPA averaging caution (EFPA:1838 etc.), Leaderboard Illusion summary, lineUP saturation/shortcuts, Hendrycks jagged profile + Canivez caveat.
- Framework naming variants: "MESA" / "the MESA Test Review Model" (`paper.tex:82`, section IV title) / "MESA Review Model" (template Figure 1 `:33`) — inventory at `80-xcut-paper-template-consistency`.
- Paper's EFPA Part B list at `paper.tex:86` omits §12 and uses MESA's §6 name (F-10-paper-02-3).
- Four adaptation rules + 8-item added-fields list duplicated verbatim `paper.tex:128` vs `:132` (F-10-paper-03-1, Major) — largest verbatim redundancy in paper; III-A/III-B merge proposed.
- Chain 4th occurrence at `paper.tex:134` is name-only ("phenomenon-task-metric-claim chain") — acceptable pointer form, no new finding.
- 15-benchmark→requirements procedure unstated (`paper.tex:128`, F-10-paper-03-2, Major); mapping examples norms→reference-points and reports→leaderboards verified against template Sections 8, 4/12.
- ":94 verify/comprehensive/useful" vs ":138 does not yet validate" internal tension (F-10-paper-03-3); Discussion/Limitations units should check which claim-strength wins elsewhere.
- Paper Table II (`paper.tex:153-166`) verified faithful to template architecture incl. Appendix A position; one drift: S12 row adds "Dashboards" not in template heading (F-10-paper-04-5).
- ":180 template-coherence defense ("not redundant as long as each section preserves its role") contradicted by same-role duplicates found in Part A review — quote as acceptance criterion in mesa-core-plan (F-10-paper-04-1, Major).
- Rating meanings 2/3/4 never defined in paper (F-10-paper-04-2); n/a-0-1 semantics at `paper.tex:177` match EFPA.
- ":175 gloss after "claim proportionality" defines gameability instead (F-10-paper-04-3); proposed fix finally defines the term — resolves the log's claim-proportionality watch if applied.
- ":177 "replaces mechanical averaging" misattributes EFPA's own prohibition as MESA-original (F-10-paper-04-4); contradicts accurate :86.
- "requirements object" one-off coinage `paper.tex:142`.
- "four-element anchoring model" first/only use `paper.tex:204` with definite article (F-10-paper-05-2); check Case Study Results and reviews for reuse of the term.
- Feasibility-not-validation stated at `paper.tex:138, :202` (consistent) vs ":94 "verify" (conflict, F-10-paper-03-3) — twice is acceptable, no further statements needed.
- Positive exemplar for synthesis: worked example `paper.tex:204` shows n/a-0-1 discipline operating; cite in 90-synthesis as the pattern Part B anchors should follow.
- Positive exemplars for synthesis (Case Study Results): footnote-definition discipline (:214-232), quantified thresholds (:224 1%≈1 task, :232 6.25pp, :234 10-15pp caution rule) — the decision-rule pattern template Part B anchors lack.
- "calibration" THIRD sense at `paper.tex:222` ("calibration campaign" = human difficulty calibration) — now: model-confidence (:214, template :7), scorer-tuning (template :1135), task-difficulty (:222). Split verdict must cover all three at 80-xcut-terminology.
- Part B section names now have 3 in-paper variants: template headings, Table II rows (faithful), Table III rows (paraphrased, F-10-paper-06-1).
- "claim proportionality" gets serviceable contextual gloss at `paper.tex:262`; formal definition still lands via F-10-paper-04-3 fix at :175.
- AGI first expanded `paper.tex:218`, first used `:90` (F-10-paper-06-2, Nit).
- "traceability" survives to Discussion (`paper.tex:268` "requirements traceability problem") — intro coinage cashes out; log watch closed.
- Hold-fixed conditions list enumerated twice with drift: `paper.tex:177` vs `:270` (F-10-paper-07-3, Nit).
- Only RQ2 answered explicitly (`paper.tex:274`); RQ1/RQ3 markers proposed for Sections IV and VI (F-10-paper-07-1) — verify Conclusion doesn't already do this when reviewing unit 09.
- Pillar-integration statement (EFPA+BetterBench+Alonso) now at `paper.tex:76-78, :134, :286` — 3rd occurrence acceptable (mitigation argument in threats); no further.
- External Validity ¶ (`paper.tex:294`) is unedited draft prose — "based of", "very big span", "the MESA's" (F-10-paper-08-1, Major); rewrite supplied restores critique_plan Task 5's named out-of-scope paradigms.
- ":300 promotional close inside limitations section → move to Conclusion (F-10-paper-08-2); unit 09 confirmed Conclusion :315 already says it → fix simplifies to DELETE :300.
- KEY for mesa-core-plan: `paper.tex:307` pre-authorizes compact MESA ("many RE workflows need a compact scorecard that preserves evidence without hiding caveats") — the invariant for trimming.
- Validation measurands duplicated `paper.tex:138` vs `:305` (F-10-paper-09-1); reframing sentence duplicated `:268` vs `:315` with reframes/re-frames spelling wobble (F-10-paper-09-2).
- Chain 5th enumeration at `paper.tex:313` (Conclusion echo — acceptable if :78 fix applied); RE-oriented framing 4th occurrence `:313`.
- Conclusion answers no RQ explicitly — F-10-paper-07-1 confirmed.
- PAPER UNITS COMPLETE. Totals: 10 units, 39 findings (0 Blocker / 7 Major / 25 Minor / 7 Nit).
- HIGHEST-LEVERAGE Part B fix: Excellent-only anchoring (:1139) leaves 1-3 unguided for all 89 items (F-20-template-partb-1, Major); interpolation-rule fix proposed in preamble — s06-s12 units should flag items where even the Excellent anchor is vague, not re-flag the 1-3 gap.
- EFPA :633 minimum-standard verdict rule + :631 bold-critical convention dropped at :1141 (F-20-template-partb-2) — feeds 20-template-99-final.
- Calibration Split fix filed in situ at :1135 → "tuning data for model-based scorers" (F-20-template-partb-3).
- Source-precedence rule stated 2× (:25, :1133) — acceptable; flag any 3rd statement in s06-s12 preambles.
- Anti-averaging now at :19 (frontmatter) and :1143 (preamble); EFPA repeats per overall item — count per-section repeats in s06-s12 for length budget. S06: 4× (:1250, :1313, :1368, :1375).
- Section 6 has a section-level 0-4 guidance table (:1178-1184) — the partb-1 interpolation aid at section grain; CHECK whether s07-s12 have equivalents; absence there = inconsistency finding at those units.
- S06 positive patterns: explicit EFPA-mapping sentence :1168 ("EFPA Section 6 asks... MESA asks..."); consolidation of EFPA's ~14 doc items into 7+overall. Check s07-s12 preambles for same mapping sentence.
- Anchor element-bloat family: 6.1.3 (14 elts), 6.2.7 (14), 6.3.1 (15) (F-20-template-s06-1, Major); core/supporting split fix — reuse for other sections' worst anchors.
- Revisit-instruction (:1172) fix = Final Evaluation checkpoint (F-20-template-s06-2) — feeds 20-template-99-final.
- MESA-added sub-overalls 6.2.8/6.3.7 (EFPA has none there) — optional cut; count in length budget.
- Section 6 rated items: 25. Section 7 rated items: 8.
- S07 has guidance table ✓ but NO EFPA-mapping sentence (S06 has one) — inconsistent traceability pattern (F-20-template-s07-3); check s08-s12 for both devices.
- Preamble↔anchor duplication instance: :1391 18-item list vs 7.1.2 anchor 13-item list (F-20-template-s07-1, Major) — the skill's "common case"; also :1389≈:1393 access-rule duplicate.
- Five-verb formula "inspect, run, score, reproduce, or audit" at :5, :1385, :1393, 7.1.8 — consistent canonical reuse, fine; do not flag.
- Anchor-bloat family grows: 7.1.2 (13 elts), 7.1.4 (12) join 6.1.3/6.2.7/6.3.1.
- Mixed-evaluand accessibility item 7.1.6 (F-20-template-s07-4) — human-accessibility concept half-ported; check §11 fairness items for the same pattern.
- RUN-CONDITIONS FORMULA: "prompts, settings, tools, time limits, access rules, hardware, or human-intervention rules" verbatim 10× (:151, :324, :1321, :1347, :1588, :1729, :2249, :2316, :2356, :2360) — define-once fix in F-20-template-s08-1 (Major); s09/s11/s12 units need not re-flag, occurrences there are covered.
- S08 has EFPA-mapping sentence ✓ and guidance table ✓; Figure 2 mermaid duplicates 8.2 node + phantom "Final checks" tier (F-20-template-s08-2); only section with a figure.
- ":1545 = 3rd statement of anchor-in-intended-meaning rule (:1139, :1158) — watch s09-s12 preambles for 4th+.
- "Repeat or qualify ratings" (:1562) impossible in single-field live form (F-20-template-s08-4) — joins single-row-table family; check s09-s12 for same instruction.
- S08 positive: reference-kind typology :1547 — best decision aid in Part B; preserve through trims.
- Section 8 rated items: 8. Section 9 rated items: 11.
- S09: 9.1.1 is the template's longest anchor (22 elements) and triple-enumerates the preamble list + items 9.2-9.5; rating collides with 9.6 (F-20-template-s09-1, Major).
- Single-item sub-section pattern (9.1→9.1.1, 9.5→9.5.1) — flatten fix with ID-migration note (F-20-template-s09-2); check s10-s12 for same pattern.
- Figure 3 (S09) is accurate, unlike Figure 2 (S08); figures exist only in S08/S09.
- S09 positive: :1632 no-single-coefficient paragraph, :1747 scorers-as-measurement-components sentence — protect through trims.
- Stakes-dependence now stated 4× (:1139, :1141, :1158, :1702) — 5th+ statements in s10-s12 should be flagged as Nits.
- "specific meaning users are supposed to draw" 3rd occurrence :1824; canonical replacement = "intended score meaning" (already at :1158, :1545) — F-20-template-s10a-1; adopt at 80-xcut-terminology.
- 10.3.1 (:1995) = template's worst anchor: source-benchmark residue hard-coded (coordinate formats/ARC, bank-balance rewards/Vending-Bench) — F-20-template-s10b-1, Major.
- 10.5.1 two-tier conditional anchor (:2038) = the MODEL anchor pattern for all bloat fixes; cite in synthesis.
- 10.6.1+10.6.2 merge proposed (15→14 items) — joins ID-migration bucket with 9.x renumbering.
- Section 10 rated items: 15 (14 after merge). Figure 4 accurate.
- S10 positives: :1932 anti-difficulty rating prohibition; visible Bean/BetterBench grounding; 10.2.2-vs-6.1.7 overlap is EFPA-inherited role-splitting, acceptable.
- Section 11 rated items: 12 (11 after 11.3.1+11.3.2 merge, F-20-template-s11-2 Major — same-role duplicate pair).
- Figure 5 (S11) = 24 bare-number cross-lookups + forward refs to 12.3.1/12.4.1-3 + visually annexes 12.4 into S11 (F-20-template-s11-1, Major); verify "12.4 Fairness, Acceptability, and Public Communication" title exists in s12.
- 6.2.6 ↔ 11.1.2 cross-section documentation duplicate — boundary bullet proposed (F-20-template-s11-3).
- CLAIMS CLUSTER: 2.18 (screen), 10.6 (proportionality), 11.5.1 (use guidance), 12.x (public claims) — four sections touch claims; map the division at 90-synthesis.
- S11 positives: :2082 "broader than demographic fairness" reframing; 11.3.3 temporal comparability item — protect.
- Section 12 rated items: 10. Dropped-iteration problem 3rd appearance (:2324 per-surface vs single fields; F-20-template-s12-1 Major; family: s04-1, s08-4).
- S12 comments-field pattern breaks mid-section (per-item from 12.3.1 only) + missing --- after :2421 (F-20-template-s12-2).
- 12.4.3 anchor self-duplicates (eligibility/updates/claims ×2 within one sentence, F-20-template-s12-3); 12.2 preamble+anchor = worst run-conditions adjacency (F-20-template-s12-4, covered by s08-1).
- VERIFY AT 99-final: does template bibliography include The Leaderboard Illusion? 12.4.3 governance content clearly derives from it; only BetterBench cited in S12 preamble (:2318).
- Figure 5 forward refs verified accurate against S12 (12.4 title, 12.3.1, 12.4.1-3 exist).
- S12 positive: :2322 inference-level principle ("whether reports support the level of inference they invite") — protect.
- Part B section titles in template confirmed: S12 heading has "Dashboards" (:2314) — paper Table II row matches template after all? NO: ledger row said "12. Quality of Reports, Leaderboards, Public Claims" but actual heading (:2314) = "Quality of Reports, Leaderboards, Dashboards, and Public Claims" → F-10-paper-04-5's premise inverted: paper Table II matches template; the LEDGER title was the stale one. F-10-paper-04-5 CORRECTED in place (withdrawal note added).
- Template bibliography = 3 entries only; EFPA itself UNCITED (F-20-template-99-1, Major); Leaderboard Illusion uncited (resolves s12 deferred check — governance content source-invisible).
- Final Evaluation lacks the hold-fixed-conditions prompt paper :177 promises (F-20-template-99-2, Major) — landing site for partb-2 minimum-standard rule + s06-2 revisit checkpoint.
- Summary of Ratings rows (:2457-2463) = origin of the 3-way section-name drift; paper Table III copied them (amends F-10-paper-06-1: align template heading + summary + Table II + Table III to one name).
- Gap Register = best MESA-original device; single-placeholder-row family (F-20-template-99-4).
- ALL PAPER + TEMPLATE UNITS DONE. Only cross-cutting units remain.
- Consistency verdicts: paper §IV accurate; mirror accurate & declares numbering load-bearing (hardens all ID migrations); Figure-1 ShortDesc = house-convention section missing from template (F-80-xcut-consistency-1, Major — closes F-20-template-00-7 root cause); 5.1/5.2 "by design" note lives in wrong artifact; framework has 4 names; 4 sync surfaces for section names ("Supply & Materials" README drift).

## Already-addressed criticism (critique_plan.md, verified against paper.tex 2026-08-09)

All six remediation tasks from the RETRAI 2026 reviews appear **closed**. Do not re-report these:

- **Task 1 (structural reorganization)** — CLOSED. `\section{The MESA Test Review Model}` exists at `paper.tex:140`; `\subsection{Intended Empirical Validation Strategy}` at `paper.tex:136`.
- **Task 2 (RE/SE context)** — CLOSED, via a stronger route than planned: DesignQA added as RE-native third case study (abstract `paper.tex:44`, intro `:67`, dedicated subsection `:228`); SWE-Bench referenced at `:116`. Residual framing gap tracked as F-10-paper-00-6, not as an open task.
- **Task 3 (BetterBench + Alonso & Church integration)** — CLOSED. Alonso & Church cited at `paper.tex:76`, Reuel/BetterBench at `:78` (both in Related Work II-A), Reuel again at `:134`, both again in Construct Validity at `:286`.
- **Task 4 (LLM-as-assistive-tool + instrument-evaluand interface)** — CLOSED. "assistive" and "human expert" language at `paper.tex:188`; Model Cards / evaluand contextualization at `:186`.
- **Task 5 (threats to validity)** — CLOSED. `\section{Limitations and Threats to Validity}` at `paper.tex:280` with Construct (`:284`), Internal (`:288`), External (`:292`) subsections.
- **Task 6 (minor polish)** — CLOSED. `,rather` and `reveals revealed` no longer present in the abstract (`paper.tex:44` reads ", rather than" and "Our analysis revealed"); "it (1)" fix present at `:61`. New grammar defects found in the abstract are tracked as F-10-paper-00-4 and F-10-paper-00-7 (distinct from the reviewer-reported ones).
