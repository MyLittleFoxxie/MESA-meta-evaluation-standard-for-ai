# Feedback — `20-template-s02-classification-a` (`MESA EFPA template official.md:149-397`)

Unit reviewed: Section 2 preamble + CHC domain list (:151-166), 2.1 Claimed Capability Domains
(:168-196), 2.2 Area of Use (:198-214), 2.3 Intended AI Systems (:216-234), 2.4 Intended Users
(:236-251), 2.5 Task Families, Subdomains, and Scores (:253-274), 2.6 Model Response Mode
(:276-296), 2.7 Prerequisites (:298-320), 2.8 Evaluation Conditions (:322-343), 2.9 Task
Interaction and Observable Evidence Types (:345-396). EFPA counterparts: 2.1-2.9
(`EFPA_Test_Review_Model_2025_Markdown.md:129-275`). CHC source:
`literature/A_Definition_of_AGI.md:18-38` (ten-domain list).

What holds up: the ten CHC-derived domain descriptions (:157-166) are faithful paraphrases of
the Hendrycks et al. source (`A_Definition_of_AGI.md:18-38`), and the preamble's caution that
the taxonomy is "not ... final or exhaustive" (:153) is exactly the right epistemic register.
The adaptation notes in 2.7 (:300, "EFPA asks about demands placed on the person being
assessed. MESA translates this into prerequisites placed on the evaluated AI system") and 2.8
(:324) make the EFPA link visible in-line — the best traceability practice in Part A so far.
2.8's fourteen administration conditions are a genuinely strong AI translation of EFPA 2.8's
free-text prompt. Machine-contract check: I verified the live-form parser handles this unit's
colon-terminated group captions ("Selection or judgment tasks:", :349 etc.) as group labels,
not spurious input fields (`assets/mesa-form.js:210-211`); checkbox lists, the 2.7 `[ ]`
matrix, and fill-in tables all parse. No contract violations.

---

### F-20-template-s02a-1 — [Major] 2.6 and 2.9 collapse into near-duplicate checklists
- **Axis:** repetition
- **Where:** `MESA EFPA template official.md:276-296` (2.6) vs `:345-380` (2.9, first three groups)
- **Quote:** > - [ ] Code *(2.6, :285)* — vs — > - [ ] Code generation *(2.9, :360)*; similarly Multiple choice (:281/:351), Tool call vs Tool use (:287/:371), Browser or web action vs Browser or web navigation (:288/:372), Structured output vs Structured data (:284/:362), Interaction in a simulated environment vs Simulated environment task (:293/:375), Interaction in a real or external environment vs Real or external environment task (:294/:376)
- **Why it fails a user:** EFPA distinguishes 2.6 Response mode (physical modality: oral, paper-and-pencil, keyboard — `EFPA_Test_Review_Model_2025_Markdown.md:204-218`) from 2.9 Item response types (format: multiple choice, open, interaction — `:255-273`). For AI systems both dimensions collapse into "what kind of output does the model produce", so the MESA translation yields two checklists sharing at least eight options under slightly different names. The reviewer makes ~25 near-identical decisions twice, and a reader of a completed review cannot tell which section is authoritative when they disagree. The one sentence acknowledging the problem ("Use 2.6 for the model's response format", :347) restates 2.6's title rather than drawing a boundary.
- **Fix:** Merge: keep 2.9's three task-interaction groups and its Observable-evidence group, delete 2.6 as a separate checklist, and retitle 2.9 "Task Interaction, Response Types, and Observable Evidence". If 2.6 must survive for EFPA numbering parity, redefine it as the *interface* dimension only (text-in/text-out, image input, audio I/O, function-calling API, environment API) and strip every task-format option from it. Parser impact: deleting a `###` subsection removes its items from the live form by design; no orphaned markup results.
- **EFPA link:** EFPA 2.6 (`:204`) and 2.9 (`:255`) — drifted: the human modality/format distinction did not survive translation, but both sections were kept.

### F-20-template-s02a-2 — [Major] Every checklist in 2.1-2.9 lost EFPA's "Other (describe)" escape option
- **Axis:** EFPA traceability (dropped function)
- **Where:** `MESA EFPA template official.md:172-194` (2.1), `:202-212` (2.2), `:220-232` (2.3), `:240-249` (2.4), `:280-294` (2.6), `:302-318` (2.7 matrix), `:349-394` (2.9)
- **Quote:** > - [ ] Robustness
> - [ ] Calibration or uncertainty
>
> Reviewer comments: *(end of 2.1 options, :193-196 — no "Other")*
- **Why it fails a user:** EFPA closes every classification list with "Other (describe)" (`EFPA_Test_Review_Model_2025_Markdown.md:148, 164, 188, 218, 243, 273`). MESA dropped it from all seven checklists in this unit — in the one field where option sets age fastest. A reviewer classifying a benchmark type the 2023-2025-era lists don't anticipate (say, a memory-persistence or multi-agent-negotiation benchmark) must either shoehorn a wrong box or leave the section silently incomplete; the free-text "Reviewer comments:" line exists but nothing licenses using it to extend the option list, and anything recorded there is invisible to structured consumers of the review (the HF dataset export reads the checkboxes).
- **Fix:** Append `- [ ] Other (describe in Reviewer comments)` as the final option of 2.1, 2.2, 2.3, 2.4, 2.6 (if retained), and each group of 2.9; add an "Other requirement" row to the 2.7 matrix. Parser impact: none — new `- [ ]` lines and a new `[ ]` matrix row are first-class form items (`assets/mesa-form.js:8, 12`).
- **EFPA link:** EFPA 2.1/2.2/2.4/2.6/2.7/2.9 closing options — dropped; restoring them is pure retention.

### F-20-template-s02a-3 — [Major] 2.1 mixes two taxonomies with no combination rule, and drops EFPA's prioritization cap
- **Axis:** vagueness
- **Where:** `MESA EFPA template official.md:168-194`
- **Quote:** > Specify the capabilities, phenomena, or qualities the benchmark claims to measure, using the CHC-inspired domains above where applicable.
- **Why it fails a user:** The option list is ten CHC domains followed by thirteen applied labels (Coding, Tool use, Agency, Safety, Robustness, Calibration...) with no rule for how they combine. For a coding benchmark, does a reviewer tick "Coding or software engineering" alone, or also On-the-Spot Reasoning (R) and Reading/Writing (RW)? Does "Factuality or grounding" replace or accompany Long-Term Memory Retrieval, whose description already covers "avoiding confabulated recall" (:163)? Two competent reviewers of the same benchmark will produce different domain profiles, and the profile is what Sections 2.18 and 10 later consume. Compounding this, EFPA's 2.1 caps the answer at "up to 3 keywords" (`EFPA_Test_Review_Model_2025_Markdown.md:131`) precisely to force commitment to what the instrument *mainly* measures; MESA silently removed the cap, so sprawling benchmarks (an HLE-type review) can tick ten boxes and classification loses all discriminative value.
- **Fix:** Add two sentences to the 2.1 instruction: "Select at most three primary domains — the capabilities the documentation itself claims; note any secondary domains in Reviewer comments. CHC domains name the claimed cognitive interpretation; the applied labels below the line name the task family. Select from both rows only when the documentation claims both (e.g., a coding benchmark claims 'Coding'; add 'R' only if the authors claim reasoning)." Insert a plain `---` or blank-line separator between the CHC block and the applied block for the visual break (parser-safe; `---` breaks a paragraph scan but is not itself parsed as an item).
- **EFPA link:** EFPA 2.1 Content domains (`:129-148`) — drifted (option list adapted well, prioritization constraint dropped); the CHC layer is MESA-original via `A_Definition_of_AGI.md`.

### F-20-template-s02a-4 — [Minor] One nine-word phrase repeated verbatim in four consecutive 2.5 row labels
- **Axis:** verbosity
- **Where:** `MESA EFPA template official.md:263-266`
- **Quote:** > | Benchmark item, prompt, episode, environment, or interaction families or subdomains | ... | Sources for benchmark items, prompts, episodes, environments, or interactions | ... | Sampling method for benchmark items, prompts, episodes, environments, or interactions | ... | Selection or filtering logic for benchmark items, prompts, episodes, environments, or interactions |
- **Why it fails a user:** The enumeration "items, prompts, episodes, environments, or interactions" appears four times in four consecutive rows (36 repeated words). The reviewer re-reads the same disclaimer while scanning for the actual distinction between the rows (families / sources / sampling / filtering), which is exactly what gets buried.
- **Fix:** Define once above the table — "In this table, *unit* means an item, prompt, episode, environment, or interaction." — then label the rows "Unit families or subdomains", "Unit sources", "Unit sampling method", "Unit selection or filtering logic". Parser impact: none (label cells are not parsed as fields; placeholder cells are unchanged).
- **EFPA link:** EFPA 2.5 (`:192-200`) — MESA-original expansion; the cut preserves all content.

### F-20-template-s02a-5 — [Minor] 2.5's first four rows are construct-definition content hiding under a task-structure title
- **Axis:** complexity and cognitive load
- **Where:** `MESA EFPA template official.md:259-262`
- **Quote:** > | Capability, phenomenon, or quality the benchmark claims to measure | ... | Definition of the capability or quality being measured | ... | Subcomponents of the claimed capability... | ... | Excluded scope or non-target abilities |
- **Why it fails a user:** The claimed construct, its documented definition, its subcomponents, and its excluded scope are the anchor for the whole validity review (Section 10 will ask whether evidence supports *this* claim) — but they sit as rows 1-4 of a table titled "Task Families, Subdomains, and Scores" in a subsection whose preamble talks about "task families, subdomains, splits, score families". A reviewer looking for "where do I record what the benchmark claims to measure" finds checkboxes in 2.1 and will not expect the free-text definition to live here; a reader auditing a completed review hunts for it.
- **Fix:** Move rows 1-4 into 2.1 as a four-row fill-in table directly under the checkbox list (titled "Claimed construct in the benchmark's own words"), leaving 2.5 to start at the item/task-family rows its title promises. Parser impact: none — the rows remain `_(placeholder)_` table cells; they simply move under the 2.1 heading.
- **EFPA link:** EFPA 2.1 (`:131`, "Specify what the test measures") — the move *restores* EFPA's location of construct content in 2.1; 2.5's remaining rows keep the EFPA 2.5 scales function (`:192`).

### F-20-template-s02a-6 — [Nit] Subject-verb disagreement introducing the domain list
- **Axis:** verbosity (grammar)
- **Where:** `MESA EFPA template official.md:155`
- **Quote:** > A brief description of the ten AGI-derived domains are:
- **Why it fails a user:** "A description ... are" — first grammar error a reader meets in Part A.
- **Fix:** "Brief descriptions of the ten AGI-derived domains:" (also drops the filler verb).
- **EFPA link:** n/a — MESA-original preamble.

---

## Verdict
- **Disposition:** Trim (merge 2.6 into 2.9; move 2.5's construct rows into 2.1; restore "Other" options)
- **Items:** 9 subsections, ~100 checkboxes + 28 fill-in rows + 15-row matrix → 8 subsections, ~80 checkboxes (duplicates removed, 7 "Other" options added), same fill-in content relocated
- **Rationale:** The CHC grounding and the 2.7/2.8 adaptations are strong; the section's real costs are one wholesale duplicated checklist (2.6/2.9), a construct-definition block filed under the wrong title, and the systematic loss of EFPA's escape options.
