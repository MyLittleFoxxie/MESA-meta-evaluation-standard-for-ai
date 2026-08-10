# Feedback — `20-template-s03-measurement` (`MESA EFPA template official.md:592-766`)

Unit reviewed: Section 3 preamble (:594), 3.1 Scoring Procedure (:596-622), 3.2 Scores and
Metrics (:624-641), 3.3 Scale or Metric Types (:643-670), 3.4 Score Transformation (:672-688),
3.5 Reference Groups, Baselines, Comparators (:690-722), 3.6 Score Uncertainty and Stability
(:724-743), 3.7 Documented Metric Rationale (:745-763). EFPA counterpart: Section 3
(`EFPA_Test_Review_Model_2025_Markdown.md:386-449`).

What holds up: 3.5 is the hardest translation in Part A — EFPA's norming procedures (:441-447)
have no direct AI analog, and recasting norms as "documented reference groups, baselines, and
comparators" (chance floors, human/expert panels, model cohorts, tool/no-tool contrasts) is
the right move and covers the space well. The three failure-handling prompts (:635-639 —
format failures, run failures, retry/repair policy) are excellent AI-native additions with no
EFPA precedent needed. The "This remains descriptive in Part A" discipline lines (:726, :747)
correctly fence 3.6/3.7 off from Part B's Sections 9-10. Machine-contract check: the three
colon-terminated failure prompts parse as free-text fields, both fill-in tables and all
checkbox lists parse; no violations.

---

### F-20-template-s03-1 — [Major] The score inventory and its interpretation are recorded in three places (2.5, 3.2, 3.7 — plus 2.18)
- **Axis:** repetition
- **Where:** `MESA EFPA template official.md:628-633` (3.2 table) vs `:268-272` (2.5 rows) vs `:759-760` (3.7 rows) vs `:583` (2.18 row)
- **Quote:** > | Primary score | _(Main outcome and scale)_ | ... *(3.2, :630)* — vs — > | Primary score | _(Main reported score and unit)_ | *(2.5, :268)* — and — > | Whether aggregate score interpretations preserve capability-domain caveats | *(3.7, :760)* — vs — > | Whether aggregate scores preserve capability-domain caveats | *(2.18, :583)*
- **Why it fails a user:** Three clusters of duplication. (1) 2.5's last five rows (Primary score, Subscores, Derived scores, Qualitative score ranges, interpretation boundaries, :268-272) and 3.2's four table rows (:630-633) ask for the same score inventory with slightly different placeholders — the reviewer describes every score twice and a reader cannot tell which description is authoritative when they diverge. (2) 3.2's columns 4-5 ("Capability-domain linkage stated by authors", "Interpretation stated by authors") reappear as 3.7 rows ("Whether score or subscore interpretations are linked to capability domains from 2.1", :759). (3) "Whether aggregate scores preserve capability-domain caveats" appears near-verbatim at 2.18:583 and 3.7:760. Across Part A the reviewer documents score meaning four times; in a 20,600-word template this is where completion time goes to die.
- **Fix:** One home per fact: (a) delete the five score rows from 2.5, leaving a single "Primary score name" orientation row pointing to Section 3; (b) keep 3.2 as the sole score-definition table including domain linkage and stated interpretation; (c) delete 3.7 rows :759-760 (linkage and aggregate-caveat rows), leaving 3.7 to its unique content — metric rationale, floor/ceiling, non-target behavior, scorer validation, sensitivity, non-use statements; (d) in 2.18, keep the aggregate-caveat row (it serves the broad-claim screen) but add "see 3.2 for score definitions". Parser impact: deleting fill-in rows removes fields by design; no orphaned markup.
- **EFPA link:** EFPA 3.2 Scores (`EFPA_Test_Review_Model_2025_Markdown.md:402-406`) is a single free-text prompt — the duplication is entirely MESA-original; consolidation restores EFPA's one-place economy while keeping MESA's added structure.

### F-20-template-s03-2 — [Major] 3.1's option list violates its own "methods only" instruction and contains unstated near-duplicates
- **Axis:** vagueness
- **Where:** `MESA EFPA template official.md:598-620`
- **Quote:** > Select scoring methods only. Do not describe the scoring pipeline in this subsection.
> ...
> - [ ] Output parser or extractor that turns model responses into scoreable values
> - [ ] Multi-run or pass@k sampling policy
- **Why it fails a user:** Two options are pipeline components (:614 parser/extractor, :615 fuzzy parsing) and one is a sampling policy (:619) — the exact things the instruction says not to record here. Meanwhile "LLM equality-checker scoring" (:602) and "Scoring by another model that evaluates outputs" (:613) name overlapping method classes with no stated boundary (an equality-checker *is* a model evaluating outputs; the intended distinction — narrow answer-equivalence checking vs. open-ended quality judging — is never stated). For the growing class of LLM-judged benchmarks this is the load-bearing distinction, and two reviewers will tick different subsets of {602, 613, 617} for the same benchmark.
- **Fix:** (a) Move :614-615 into 3.2's pipeline prompts and :619 into 2.8's sampling-settings row (or a "Runs policy" row there). (b) Group the remaining options under colon-terminated group labels — "Answer matching:", "Execution or environment verification:", "Judge-based scoring:", "Preference or ranking:" — which parse as group labels, not fields. (c) Reword :602 and :613 to state the boundary: "LLM equality-checker (model decides only whether the answer matches the reference)" vs. "LLM judge (model rates open-ended output quality against a rubric)". Parser impact: group labels safe (`assets/mesa-form.js:210-211`); moved options remain checkbox/prompt items.
- **EFPA link:** EFPA 3.1 Scoring procedure (`EFPA_Test_Review_Model_2025_Markdown.md:388-398`) — retained in function; EFPA's six options are disjoint, and the MESA expansion lost that disjointness.

### F-20-template-s03-3 — [Minor] 3.5's checkbox list duplicates its own fill-in table
- **Axis:** verbosity
- **Where:** `MESA EFPA template official.md:694-707` (checkboxes) vs `:711-720` (table)
- **Quote:** > - [ ] Expected performance from random guessing or trivial selection *(:695)* — vs — > | Random guessing or trivial-selection reference point | *(:713)*
- **Why it fails a user:** The 14 checkboxes mark which reference points exist; the 8-row table then names the same types again with construction-method and interpretation columns. Every tick is re-stated as a row; the reviewer handles ~22 items where 8 would carry all the information (an unused row left "n/a" marks nonexistence as clearly as an unticked box).
- **Fix:** Delete the checkbox list; keep the table, adding its two missing types as rows ("Commercial or open-weight comparison system", "Domain-specific reference group") and a first row "No reference point documented — [ ]". Net: 22 items → 10. Parser impact: none — table rows with `_(placeholder)_` and one `[ ]` cell all parse.
- **EFPA link:** EFPA 3.5 Norming procedures (`EFPA_Test_Review_Model_2025_Markdown.md:441-447`) — the translation itself is retained (and good); the double-entry is MESA-original overhead.

### F-20-template-s03-4 — [Minor] 3.6's governing sentence is garbled
- **Axis:** vagueness
- **Where:** `MESA EFPA template official.md:726`
- **Quote:** > Record whether uncertainty or similar scores across repeated evaluations under documented conditions are reported.
- **Why it fails a user:** "Uncertainty or similar scores" parses as "scores similar to uncertainty" — the intended reading is "uncertainty estimates, or score stability across repeated runs". The sentence governs a 14-option checklist; a reviewer unsure what counts as "similar scores" under-ticks or over-ticks (e.g., does judge-consistency evidence belong here? Option :736 says yes, the preamble doesn't).
- **Fix:** "Record whether the documentation reports uncertainty estimates for scores (intervals, standard errors) or evidence of score stability across repeated evaluations, seeds, judges, or prompt variations."
- **EFPA link:** MESA-original (EFPA defers all reliability content to Part B §9); the Part A descriptive screen is a sound addition — one sentence should not undercut it.

### F-20-template-s03-5 — [Minor] 3.4 dropped EFPA's explanatory preamble and mixes transformation types with documentation status
- **Axis:** EFPA traceability
- **Where:** `MESA EFPA template official.md:672-686`
- **Quote:** > - [ ] Linear transformation
> - [ ] Non-linear transformation
> ...
> - [ ] Formula for combining item, task-family, or subscore results documented
> - [ ] Formula for combining item, task-family, or subscore results partially documented
- **Why it fails a user:** EFPA 3.4 precedes its options with a plain-language definition of what normalization is and when a look-up table is needed (`EFPA_Test_Review_Model_2025_Markdown.md:433`). MESA kept bare labels: a non-psychometrician cannot decide whether Elo updating or log-scaling is a "non-linear transformation". The list also splices in a three-option documented/partially/not-documented scale about the combining formula (:682-684) — a documentation-status dimension inside a transformation-type list, which reads as three mutually exclusive options amid select-all-that-apply types.
- **Fix:** Add one preamble sentence: "A transformation changes the scale of raw results (e.g., normalization to a reference model = linear; Elo updating or logistic scaling = non-linear)." Move the formula-documentation triple out of the checkbox list into a one-line prompt: "Combining formula documentation status (documented / partial / not documented):".
- **EFPA link:** EFPA 3.4 (`:431-437`) — drifted: options adapted, explanatory preamble dropped.

### F-20-template-s03-6 — [Minor] Escape options missing throughout Section 3 (extends F-20-template-s02a-2)
- **Axis:** EFPA traceability (dropped function)
- **Where:** `MESA EFPA template official.md:600-620` (3.1), `:647-668` (3.3), `:676-686` (3.4), `:694-707` (3.5)
- **Quote:** > - [ ] Manual adjudication
>
> Reviewer comments: *(end of 3.1 — no "Other"; EFPA 3.1 closes "Other (describe)", `EFPA:398`)*
- **Why it fails a user:** Same pattern as Section 2: EFPA 3.1 and 3.3 close every group with "Other (describe)" (`EFPA:398, 416, 423, 427`); MESA's 3.1, 3.3, 3.4, 3.5 have none, and 3.3 also lacks "Not explicitly stated" — despite metric zoos being the fastest-moving part of the field.
- **Fix:** As before: `- [ ] Other (describe in Reviewer comments)` per list; `- [ ] Not explicitly stated` first in 3.3. Parser-safe.
- **EFPA link:** EFPA 3.1/3.3 closing options — dropped.

### F-20-template-s03-7 — [Nit] Redundant clause in the first failure prompt
- **Axis:** verbosity
- **Where:** `MESA EFPA template official.md:635`
- **Quote:** > Treatment of responses that fail format, schema, refusal, completion, or parsing requirements, or are missing or refused:
- **Why it fails a user:** "Refusal ... requirements" and "or are ... refused" state refusal twice, and "fail ... refusal requirements" is not parseable English.
- **Fix:** "Treatment of responses that are missing, refused, incomplete, or that fail format, schema, or parsing requirements:"
- **EFPA link:** MESA-original prompt.

---

## Verdict
- **Disposition:** Trim (consolidate score descriptions per F-1; delete 3.5's checkbox layer; regroup 3.1)
- **Items:** 7 subsections, ~57 checkboxes + 12 fill-in rows + 4-row score table + 8-row comparator table → ~40 checkboxes, score content stated once, comparator content stated once (net ≈ −25 reviewer decisions)
- **Rationale:** The translations (norms→baselines, failure handling) are among Part A's best; the section's cost is pure duplication — score meaning is currently documented four times across Sections 2-3.
