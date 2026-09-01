# Feedback — `20-template-00-frontmatter` (`MESA EFPA template official.md:1-97`)

Unit reviewed: template title, Introduction (¶ at lines 5-13), "How the MESA Model Should Be
Used" (lines 15-25), Figure 1 mermaid (lines 27-95). EFPA counterpart: front matter of
`EFPA_Test_Review_Model_2025_Markdown.md:1-95` (Introduction :5-13, How Used :15-25, Figure 1
:27-93).

What holds up: the front matter is a visibly faithful EFPA adaptation at near-identical length
(97 lines vs EFPA's 95). The audience paragraph (:9 ↔ EFPA:9), "designed to guide reviewers,
not to provide a closed set of rules" (:19 ↔ EFPA:17, near-verbatim), and the no-endorsement
paragraph (:23 ↔ EFPA:21) are all retained with the link plainly visible. The
description-vs-evaluation discipline paragraph (:17) and the entity-identification requirement
(:13) are sensible MESA-original additions. Machine-contract check: this unit contains only
headings, prose, and one ```mermaid block — no parser-convention violations.

---

### F-20-template-00-1 — [Minor] Part B preview list duplicates Figure 1 and the section headings
- **Axis:** verbosity
- **Where:** `MESA EFPA template official.md:11`
- **Quote:** > Part B evaluates whether the benchmark supports the specific meaning users are supposed to draw from a score, using EFPA-style ratings translated for AI benchmark concerns such as evidence that scores support the intended capability interpretation, whether scoring rewards the target capability rather than irrelevant score effects, reproducibility, prior model exposure to benchmark items or answers, maintenance, fair comparison, and public reporting.
- **Why it fails a user:** A 62-word sentence whose seven-item "such as" list previews Part B contents the reader gets twice more on the same screen: the Figure 1 boxes (:59-65) and, later, the actual section headings. The list also contains the unparseable phrase "rewards the target capability rather than irrelevant score effects" — one cannot reward an effect; the intended concept (scores driven by shortcuts rather than the capability) recurs properly in Part B, so a garbled preview here only plants confusion. EFPA's counterpart sentence (EFPA:13) is 27 words and enumerates nothing.
- **Fix:** Cut the list; end the sentence at the mechanism: "Part B evaluates whether the benchmark supports the specific meaning users are supposed to draw from a score, using EFPA-style ratings adapted to AI benchmark concerns; Figure 1 lists the seven evaluation sections." (−45 words.)
- **EFPA link:** EFPA front matter structure statement (`EFPA_Test_Review_Model_2025_Markdown.md:13`) — drifted (EFPA states the split in one plain sentence; the enumeration is a MESA addition duplicating structure shown elsewhere).

### F-20-template-00-2 — [Minor] The entity taxonomy is stated twice with inconsistent names
- **Axis:** repetition (with terminology drift)
- **Where:** `MESA EFPA template official.md:13` and `:21`
- **Quote:** > The reviewed entity may be an original benchmark, derived benchmark, subset, evaluation slice, hosted leaderboard, private form, rolling version, hosted suite, benchmark suite, task environment, or evaluator-specific implementation. *(:13)* — vs. — > When the reviewed object is a slice, variant, suite component, hosted leaderboard, private form, rolling cohort, or evaluator-specific implementation... *(:21)*
- **Why it fails a user:** Eleven entity types at :13, seven overlapping-but-renamed ones at :21: "rolling version" becomes "rolling cohort", "evaluation slice" becomes "slice", "hosted suite / benchmark suite" becomes "suite component", and "variant" appears only in the second list. A reviewer deciding what entity they are reviewing meets two taxonomies eight paragraphs apart and cannot tell whether the differences are meaningful. A third variant of this list at `:1259` ("slices, variants, hosted leaderboards, private forms, rolling cohorts, and evaluator-specific implementations") confirms the labels are drifting rather than designed.
- **Fix:** State the taxonomy once, at :13, and thereafter refer to "any reviewed entity listed above". Standardize on one label per concept (recommend: "evaluation slice", "rolling cohort", "suite component") and use those exact labels wherever the list reappears, including Section 1's entity-type options and `:1259`.
- **EFPA link:** MESA-original — EFPA has no reviewed-entity taxonomy (its unit is "the test"); the addition is genuinely needed for AI benchmarks, which is exactly why its labels must be stable.

### F-20-template-00-3 — [Minor] MESA's validity anchor phrase is repeated verbatim instead of being made canonical
- **Axis:** repetition
- **Where:** `MESA EFPA template official.md:11` and `:19`
- **Quote:** > ...the specific meaning users are supposed to draw from a score... *(both lines, word-for-word)*
- **Why it fails a user:** This 11-word phrase is MESA's best plain-language rendering of "intended score interpretation" — but it appears twice in the front matter as incidental prose, and (per the phrase's role in Part B section preambles) will keep being re-spelled throughout. Repeating an 11-word definition inline every time inflates every section that needs the concept.
- **Fix:** Make it canonical: at :11 keep the full phrase and bind it — "...the specific meaning users are supposed to draw from a score (hereafter *the intended score meaning*)" — then use "the intended score meaning" at :19 and everywhere after. Saves ~8 words per later occurrence and gives reviewers a stable term.
- **EFPA link:** EFPA validity framing (Part B, "Evaluation of the Instrument", `EFPA_Test_Review_Model_2025_Markdown.md:613`) — retained in substance; the canonicalization is a MESA-internal editorial fix.

### F-20-template-00-4 — [Minor] Circular definition of missing documentation
- **Axis:** vagueness
- **Where:** `MESA EFPA template official.md:19`
- **Quote:** > Missing documentation is missing or inaccessible information needed for interpretation, not automatic proof that the benchmark is poor.
- **Why it fails a user:** "Missing documentation is missing ... information" defines the term with itself; a reviewer skims past without extracting the operative rule, which matters because it governs how every "unknown" is rated in Part B.
- **Fix:** "Treat missing documentation as an evidence gap: record what could not be found, and do not treat the gap itself as proof that the benchmark is poor." (Same length, states the rule as an instruction.)
- **EFPA link:** MESA-original — EFPA's front matter has no missing-evidence rule; this is a needed AI-benchmark addition (documentation gaps are the norm), so its one sentence must land.

### F-20-template-00-5 — [Minor] Opening-paragraph sentence with three nested lists
- **Axis:** complexity and cognitive load
- **Where:** `MESA EFPA template official.md:5`
- **Quote:** > It provides a structure for describing and evaluating AI benchmarks, task suites, leaderboards, evaluation harnesses that administer tasks and often run scoring, score reports, and benchmark materials needed to inspect, run, score, reproduce, or audit evaluations used in research, model development, safety evaluation, deployment governance, procurement, policy analysis, and public communication.
- **Why it fails a user:** 55 words, three lists deep. The relative clause "that administer tasks and often run scoring" breaks the first list mid-stream, so "score reports" reads as an object of "administer". This is the third sentence a first-time user reads; the persona risk is front-matter fatigue before Section 1.
- **Fix:** Split by role: "It provides a structure for describing and evaluating AI benchmarks and the artifacts around them: task suites, leaderboards, evaluation harnesses, score reports, and the materials needed to inspect, run, reproduce, or audit an evaluation. It applies wherever benchmark scores inform research, development, safety evaluation, governance, procurement, policy, or public communication." (Two sentences, one list each.)
- **EFPA link:** EFPA scope sentence (`EFPA_Test_Review_Model_2025_Markdown.md:7`) — retained in function; EFPA's version is equally list-heavy, so this is an adaptation-improvement opportunity rather than drift.

### F-20-template-00-6 — [Minor] The instrument definition paraphrases AERA without attribution
- **Axis:** EFPA traceability
- **Where:** `MESA EFPA template official.md:7`
- **Quote:** > ...it samples the behavior of an AI system in a specified domain, then quantifies, scores, interprets, and reports that behavior through a standardized or documented process for evaluative or comparative conclusions.
- **Why it fails a user:** This is a close, competent paraphrase of the AERA Standards definition that EFPA quotes and attributes ("a structured sample of an examinee's behaviour in a specified domain is obtained and subsequently quantified, scored, interpreted..." — `EFPA_Test_Review_Model_2025_Markdown.md:11`, citing AERA et al., 2014). MESA drops the attribution, so the reader cannot see that MESA's core definition inherits from the measurement-standards lineage — the exact authority MESA's whole pitch rests on.
- **Fix:** Add one clause: "...for evaluative or comparative conclusions, adapting the definition of a test in the AERA Standards (AERA et al., 2014) as used by the EFPA model." Add the AERA entry to the Bibliography (:2473) if absent.
- **EFPA link:** EFPA front matter (`EFPA_Test_Review_Model_2025_Markdown.md:11`) — drifted (definition retained, provenance dropped).

### F-20-template-00-7 — [Minor] Figure 1 advertises a deliverable no template section produces
- **Axis:** EFPA traceability (figure vs. artifact)
- **Where:** `MESA EFPA template official.md:36` (mermaid node), vs. `:1115` (Appendix A)
- **Quote:** > ShortDesc("Short stand-alone non-evaluative benchmark description")
- **Why it fails a user:** In EFPA's figure the short stand-alone description is a distinct deliverable of the review process (EFPA:36). MESA's Figure 1 keeps the box *and* separately shows "Appendix A. General Description of the Benchmark" (:46) — but the template body contains only Appendix A (:1115); no section instructs the reviewer to produce a short stand-alone description. A reviewer working from the figure looks for a deliverable that does not exist; a form user never sees it at all (mermaid figures render as figures, not fields).
- **Fix:** Either label the existing node as implemented by Appendix A ("Short stand-alone non-evaluative description — see Appendix A") and drop the duplicate AA node, or add a one-paragraph short-description prompt to the template and keep both nodes. The first option is cheaper and loses nothing if Appendix A already serves this role.
- **EFPA link:** EFPA Figure 1 (`EFPA_Test_Review_Model_2025_Markdown.md:36`) — drifted (figure element retained, implementing artifact ambiguous).

---

## Verdict
- **Disposition:** Trim
- **Items:** 13 prose paragraphs + 1 figure → 11 paragraphs + 1 figure (cut ~90 words: the Part B enumeration, the second entity list, tightened opening sentence)
- **Rationale:** Structure and EFPA fidelity are sound; the defects are duplicated enumerations and two sentences (missing-documentation rule, instrument definition) whose wording undersells load-bearing content.
