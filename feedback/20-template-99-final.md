# Feedback — `20-template-99-final` (`MESA EFPA template official.md:2433-2479`)

Unit reviewed: Final Evaluation — Evaluative Report (:2435-2439), Conclusions (:2441-2445),
Recommendations (:2447-2451), Summary of Ratings table (:2453-2465), Gap Register
(:2467-2471), Bibliography (:2473-2479).

The three free-text blocks faithfully mirror EFPA's Evaluative Report / Conclusions /
Recommendations structure, and the **Gap Register is the template's single best MESA-original
device** — a six-column register that operationalizes the evidence-gap discipline the paper
advertises (`paper.tex:172`). The deferred check from `20-template-s12-reports` resolves here:
the bibliography has exactly three entries. Parser check: "Free Text:" prompts and both tables
parse; the Gap Register is a single-placeholder-row fill-in (family F-20-template-s02b-5),
which matters more here than anywhere — a register is multi-row by definition.

This unit is also the landing site for two earlier restorations: the below-minimum-standard
verdict rule (F-20-template-partb-2) and the Section 6 revisit checkpoint (F-20-template-s06-2)
both belong in the Evaluative Report's instructions.

---

### F-20-template-99-1 — [Major] The template's bibliography does not cite the EFPA Test Review Model
- **Axis:** EFPA traceability
- **Where:** `MESA EFPA template official.md:2473-2479`
- **Quote:** > [1] D. Hendrycks et al., "A Definition of AGI"... [2] A. M. Bean et al., "Measuring what Matters"... [3] A. Reuel et al., "BetterBench"...
- **Why it fails a user:** The document that declares itself an adaptation of the EFPA Test Review Model 2025 (:5) and opens seven Part B sections with "EFPA Section N asks..." never cites EFPA in its bibliography. A reviewer who wants to check any adaptation against the source has no pointer; MESA's authority claim rests on a reference that isn't there. Secondarily: Section 12's leaderboard-governance content (12.4.3 — private-set governance, retraction, eligibility) is plainly informed by The Leaderboard Illusion, which is also uncited, leaving that section's most AI-specific guidance source-invisible.
- **Fix:** Add: EFPA, "EFPA Test Review Model 2025" (with edition/URL as used in `references.bib`'s `efpa_test_review_model_2025`); Singh et al., "The Leaderboard Illusion" (cited from Section 12's preamble alongside BetterBench); optionally AERA/APA/NCME Standards, which the paper cites as EFPA's own foundation.
- **EFPA link:** The link itself is the finding — currently invisible at the document level.

### F-20-template-99-2 — [Major] The Final Evaluation never asks for the hold-fixed-conditions statement the paper promises
- **Axis:** claim support (template side)
- **Where:** `MESA EFPA template official.md:2437-2443`
- **Quote:** > It should describe its strengths and limitations, give general recommendations about how and when it may be used, and include warnings where necessary about when it should not be used.
- **Why it fails a user:** The paper's description of the final evaluation (`paper.tex:177`) promises three outputs: what the score can support, what it cannot, and "what conditions must be held fixed for comparisons to be meaningful, such as benchmark version, split, prompt, harness, scorer, comparator cohort, uncertainty, and run conditions" — and the worked example (`paper.tex:204`) delivers exactly that four-element profile. The template's Final Evaluation prompts cover the first two (supported use, warnings) but never require the conditions statement; a reviewer following only the template will omit the element the paper calls out as MESA's distinctive product. This is the inverse of the axis-7 rule: the artifact lacks what the paper describes.
- **Fix:** Add to the Evaluative Report instruction (:2437): "State explicitly: (1) the interpretations the scores support; (2) the interpretations they do not support; (3) the run conditions that must be held fixed for comparisons to be meaningful (version, split, prompts, scorer, comparator cohort, uncertainty basis)." In the same edit, land the two earlier restorations: the below-minimum-standard trigger ("If any critical attribute is rated 0 or 1, state that the benchmark falls below the minimum standard for its stated use") and the revisit checkpoint ("Before concluding, re-check ratings 6.1.1, 6.1.3, and 6.2.5 against Sections 8-10 findings").
- **EFPA link:** EFPA Final Evaluation (Evaluative Report/Conclusions/Recommendations) — retained structurally; the conditions statement is the MESA-original element that went missing between paper and template.

### F-20-template-99-3 — [Minor] The Summary of Ratings table renames the sections it summarizes — and the paper inherited the drift
- **Axis:** repetition (naming consistency)
- **Where:** `MESA EFPA template official.md:2457-2463`
- **Quote:** > Section 8. Reference points and documented comparison groups [...] Section 10. Validity support [...] Section 12. Reports, leaderboards, and public score claims
- **Why it fails a user:** The summary rows match neither the template's own section headings ("Baselines, Comparators, and Reference Interpretation"; "Validity Evidence"; "...Dashboards, and Public Claims") nor the paper's Table II. Paper Table III (`paper.tex:247-253`) copies *these* rows, which is how the three-way naming divergence flagged in F-10-paper-06-1 arose — the drift originates here, inside the template.
- **Fix:** Make the Summary rows verbatim copies of the section headings (shortened identically everywhere if width demands). One authoritative name per section, used by the heading, this table, paper Table II, and paper Table III.
- **EFPA link:** EFPA's summary table reuses its section names exactly — retained in form, drifted in content.

### F-20-template-99-4 — [Nit] The Gap Register ships with one placeholder row
- **Axis:** complexity and cognitive load (form contract)
- **Where:** `MESA EFPA template official.md:2470-2471`
- **Quote:** > | _(Specific missing or inaccessible evidence)_ | _(Benchmark, slice, implementation, report, or leaderboard)_ | ...
- **Why it fails a user:** Every real review produces multiple gaps (the HLE case study alone lists four in one section), but the live form renders exactly one fillable row — the F-20-template-s02b-5 pattern at the table where multi-row entry is the entire point.
- **Fix:** Whatever multi-row mechanism `/mesa-core-plan` adopts for 2.15/4.2 applies here first; until then, add an instruction line: "Duplicate this row per gap."
- **EFPA link:** MESA-original device — protect it; fix only the row mechanics.

---

## Verdict
- **Disposition:** Trim + strengthen (two added citations, one three-part prompt, aligned names)
- **Items:** 3 free-text prompts + 2 tables → unchanged (+~60 words of instructions, +2 bibliography entries)
- **Rationale:** The right closing structure with the template's best original device, undermined by two absences — the parent framework missing from its own bibliography, and the paper's signature deliverable (the hold-fixed-conditions statement) missing from the prompts that produce it.
