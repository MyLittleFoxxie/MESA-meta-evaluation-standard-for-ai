# Feedback — `20-template-s02-classification-b` (`MESA EFPA template official.md:398-591`)

Unit reviewed: 2.10 Input Stimulus Type (:398-421), 2.11 Number of Items (:423-443), 2.12 Mode
of Evaluation (:445-473), 2.13 Technological Arrangements (:475-496), 2.14 Time and Resource
Requirements (:498-514), 2.15 Forms, Versions, and Variants (:516-524), 2.16 Static or Dynamic
Task Determination (:526-545), 2.17 Evidence Sources Used in Scoring (:547-569), 2.18
Broad-Claim Flags (:571-588). EFPA counterparts: 2.10-2.17
(`EFPA_Test_Review_Model_2025_Markdown.md:277-385`); 2.18 is MESA-original.

What holds up: 2.17 is the most elegant adaptation in Part A — EFPA's "Informant in the test"
(who provides information: self-report, parents, teachers — `EFPA:367-382`) becomes "evidence
sources used in scoring" (final answer, traces, judges, verifiers), a translation that
preserves the EFPA function exactly while being natively meaningful for AI. 2.18 is MESA's
signature original addition, and its discipline line ("Record only interpretations made or
clearly implied from benchmark scores; put evaluation and reviewer caution in Part B", :573)
is exactly right. 2.14's shift from EFPA's "reviewer estimates timing" to "record documented
estimates; mark missing if not stated" (:500) is deliberate, correct drift that enforces
MESA's source-grounding rule. 2.15's "Stated score-comparability interpretation" column (:520)
plants the seed Section 11 needs. Machine-contract check: the A/R matrix (:479-494), the
"Identity and condition controls:" group label (:465), and the trailing prompt "Describe task
selection method:" (:545) all parse correctly (`assets/mesa-form.js:199-216`); no violations.

---

### F-20-template-s02b-1 — [Major] 2.12's identity-control levels lost EFPA's definitions, leaving unanchored labels
- **Axis:** vagueness
- **Where:** `MESA EFPA template official.md:465-471`
- **Quote:** > - [ ] No control over submitted systems
> - [ ] Some control over submitted systems
> - [ ] Controlled model access or audit
> - [ ] Controlled evaluation center or private harness
- **Why it fails a user:** This group is EFPA 2.12.2's four-level administration-security spectrum — but EFPA defines each level in the option text itself ("Controlled but unsupervised administration. Control over conditions (timing etc.) and some control over the identity of the test taker (e.g., ... password restricted access)", `EFPA:312-315`). MESA kept the spectrum and stripped every definition. "Some control over submitted systems" has no anchor at all: for the same public leaderboard with account-gated submission and self-reported model identity, one reviewer ticks "Some control", another "Controlled model access or audit". Identity control is precisely the dimension that leaderboard-gaming critiques turn on, so an unreliable tick here propagates into Sections 8, 11, and 12. The surrounding "Mode of Evaluation" list (:449-461) compounds the noise by mixing venue (local batch, hosted platform), openness (public, private), cadence (rolling), and event type (competition) in one flat 12-option list.
- **Fix:** Give each control level a one-line definition with an AI example, mirroring EFPA's pattern: e.g. "- [ ] No control over submitted systems (open submission; identity and run conditions self-reported)"; "- [ ] Some control over submitted systems (gated submission, e.g. account or API key, but model identity and conditions not verified)"; "- [ ] Controlled model access or audit (organizers run or verify the model, or audit submitted outputs)"; "- [ ] Controlled evaluation center or private harness (organizers administer the full evaluation on their own infrastructure)". Parser impact: none — longer checkbox labels are still `- [ ] Label` lines. For the first list, add group labels ("Venue:", "Openness:", "Cadence:") as colon-terminated lines before checkbox runs — these parse as group labels, not fields.
- **EFPA link:** EFPA 2.12.2 (`EFPA_Test_Review_Model_2025_Markdown.md:309-315`) — drifted: spectrum retained, level definitions dropped.

### F-20-template-s02b-2 — [Minor] 2.17 never says how it differs from 2.9's evidence group
- **Axis:** vagueness (boundary with repetition)
- **Where:** `MESA EFPA template official.md:549` (instruction) vs `:381-394` (2.9, "Observable evidence or process data")
- **Quote:** > Select all that apply. *(the entire 2.17 instruction)*
- **Why it fails a user:** Roughly ten of 2.17's options (tool traces, search/retrieval transcript, execution result, environment state, leaderboard submission metadata...) also appear in 2.9's observable-evidence group. The distinction is real and valuable — 2.9 records what the evaluation *generates*, 2.17 what the scorer *consumes* (a benchmark may log traces but score only final answers) — but no sentence states it, and 2.17's only instruction is "Select all that apply." Reviewers will either mirror their 2.9 ticks (making 2.17 redundant) or wonder which section was supposed to hold what.
- **Fix:** Replace 2.17's instruction with: "List only evidence the scoring procedure actually consumes to produce scores. 2.9 records everything the evaluation generates; a source belongs here only if it affects the score." (Two sentences; no format change.)
- **EFPA link:** EFPA 2.17 Informant (`EFPA_Test_Review_Model_2025_Markdown.md:367-382`) — retained via an excellent translation; the missing boundary sentence is the only gap.

### F-20-template-s02b-3 — [Minor] Missing escape options continue through 2.10-2.17 (extends F-20-template-s02a-2)
- **Axis:** EFPA traceability (dropped function)
- **Where:** `MESA EFPA template official.md:402-419` (2.10), `:449-471` (2.12, both groups), `:479-494` (2.13), `:530-541` (2.16), `:551-567` (2.17)
- **Quote:** > - [ ] External search results
>
> Reviewer comments: *(end of 2.10 options — no "Other"; EFPA 2.10 closes with "Other (describe)", `EFPA:286`)*
- **Why it fails a user:** Same failure mode as F-20-template-s02a-2, inventoried here for the second half of Section 2: EFPA closes 2.10 and 2.13 with "Other (describe)" (`EFPA:286, 328`); MESA's 2.10, 2.12, 2.13, 2.16, and 2.17 all lack it. 2.17 additionally lacks "Not explicitly stated" — yet scoring-evidence documentation is among the most commonly incomplete areas in real benchmarks (an LLM-judged benchmark that never specifies what the judge sees leaves the reviewer with no honest box to tick).
- **Fix:** As in F-20-template-s02a-2: append `- [ ] Other (describe in Reviewer comments)` to each list, an "Other" row to the 2.13 matrix, and `- [ ] Not explicitly stated` as 2.17's first option. Parser-safe throughout.
- **EFPA link:** EFPA 2.10 (`:286`), 2.13 (`:328`) — dropped; restoring is pure retention.

### F-20-template-s02b-4 — [Minor] 2.11 expands one EFPA free-text prompt into thirteen undifferentiated rows
- **Axis:** verbosity (completion burden)
- **Where:** `MESA EFPA template official.md:427-441`
- **Quote:** > | Counts by language, culture, or locale | ... | Counts by context-length bin | ... | Counts by difficulty band | ...
- **Why it fails a user:** EFPA 2.11 is one prompt (`EFPA:290-293`). MESA's table has thirteen rows presented as equally mandatory, but for the majority case — a static, single-language QA benchmark — at least five rows (locale, context-length, difficulty, episodes, dynamic counts) are n/a. Nothing marks which rows are core and which apply only when the documentation provides that breakdown, so a conscientious reviewer writes "n/a" repeatedly and a fatigued one starts skipping rows — the exact instrument-abandonment pattern over-long templates produce.
- **Fix:** Split the table: five core rows (public items, private/hidden items, test items, dev/example items, item count uncertainty) always completed; the remaining breakdown rows under a lead-in sentence "Complete only the breakdowns the documentation provides:". Parser impact: none — same fill-in rows, one added paragraph line.
- **EFPA link:** EFPA 2.11 (`EFPA_Test_Review_Model_2025_Markdown.md:290-293`) — retained and expanded; the split preserves all added content while restoring EFPA's proportionality.

### F-20-template-s02b-5 — [Minor] 2.15's single template row cannot hold a multi-form benchmark in the live form
- **Axis:** complexity and cognitive load (form usability)
- **Where:** `MESA EFPA template official.md:520-522`
- **Quote:** > | _(Name, split, version, cohort, or slice)_ | _(Why this form exists)_ | _(Comparable, non-comparable, or undocumented)_ | _(Active, retired, hidden, draft, etc.)_ |
- **Why it fails a user:** The table has exactly one placeholder row. Markdown users can add rows, but the live form renders exactly the fields the template declares (`assets/mesa-form.js:11`), so a form user reviewing a benchmark with a public set, a private set, and two language variants gets one row for four forms and must cram the rest into Reviewer comments — for the subsection whose whole point is enumerating forms.
- **Fix:** Provide three or four placeholder rows (parser-safe: each `_(placeholder)_` cell becomes a field), and add a line "Add rows as needed; note additional forms in Reviewer comments if the form limits entries."
- **EFPA link:** EFPA 2.15 Different forms (`EFPA_Test_Review_Model_2025_Markdown.md:347-350`) — retained; this is an implementation-capacity gap, not a content gap.

### F-20-template-s02b-6 — [Nit] 2.18 placeholders that echo their row labels
- **Axis:** verbosity
- **Where:** `MESA EFPA template official.md:582` and `:584`
- **Quote:** > | Coverage across modalities, tools, memory, planning, or speed | _(Modalities, tools, memory, planning, speed, etc.)_ | ... | Stated AGI, autonomy, or agency caveats | _(Author caveats about AGI, autonomy, or agency)_ |
- **Why it fails a user:** The placeholder repeats the label instead of guiding the answer; wasted hint space in the two rows where an example would help most.
- **Fix:** Replace with example-bearing hints, e.g. "_(e.g., text-only, no tool use, no persistent memory tested)_" and "_(quote the caveat, e.g. 'not a test of AGI')_".
- **EFPA link:** n/a — 2.18 is MESA-original.

---

## Verdict
- **Disposition:** Trim (restore EFPA level definitions in 2.12; split 2.11 into core/conditional; keep 2.17 and 2.18 intact)
- **Items:** 9 subsections, ~60 checkboxes + 28 A/R cells + 23 fill-in rows → same subsection count; 2.11 restructured, ~8 escape options added, 2.12 labels lengthened
- **Rationale:** The second half of Section 2 contains Part A's two best adaptations (2.17, 2.18); its defects are one de-anchored EFPA spectrum (2.12) and completion burden that concentrates in 2.11's undifferentiated table.
