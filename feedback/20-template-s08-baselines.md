# Feedback — `20-template-s08-baselines` (`MESA EFPA template official.md:1469-1623`)

Unit reviewed: Section 8 — preamble (:1471-1477), Figure 2 mermaid (:1479-1543), two further
preamble paragraphs (:1545-1547), section guidance table (:1549-1557), 8.1 with 7 items, 8.2
overall. 8 rated items.

The EFPA translation here is the template's showpiece: the mapping sentence is present and
precise (:1471 — "EFPA Section 8 evaluates reference distributions and criterion
interpretation. MESA translates that logic into reference points..."), which is exactly the
norms→reference-points adaptation the paper claims (`paper.tex:128`), and EFPA's
representativeness and currency concerns survive as 8.1.6/8.1.7. The reference-kind typology
(:1547 — chance detects meaningfulness, human/expert interprets difficulty, cohorts support
relative comparison, bands support categories) is the best decision aid in Part B. The
condition-matching paragraph (:1473) operationalizes what the ARC-AGI-2 case study needed.
Parser check: items conventional; the mermaid block is a legal figure. Findings below.

---

### F-20-template-s08-1 — [Major] A 13-word run-conditions formula is pasted verbatim ten times across the template
- **Axis:** repetition (template-wide, caught here)
- **Where:** `MESA EFPA template official.md:1588` (8.1.4); all occurrences: `:151, :324, :1321, :1347, :1588, :1729, :2249, :2316, :2356, :2360`
- **Quote:** > ...caveated for differences in task content, scoring, risk of unintended disclosure, and prompts, settings, tools, time limits, access rules, hardware, or human-intervention rules.
- **Why it fails a user:** "Prompts, settings, tools, time limits, access rules, hardware, or human-intervention rules" recurs verbatim in ten anchors from Section 2 to Section 12 — ~130 words of duplicated enumeration that the reviewer re-parses every time, never sure whether this instance differs from the last by one word (none do). It is a concept begging for a name.
- **Fix:** **Define once, name everywhere.** Frontmatter/glossary: "**Run conditions**: the prompts, settings, tools, time limits, access rules, hardware, and human-intervention rules under which an evaluation executes." Then substitute "run conditions" at all ten sites (e.g. 8.1.4: "...caveated for differences in task content, scoring, risk of unintended disclosure, and run conditions."). Saves ~110 words, and gives Part B a term the Final Evaluation's hold-fixed statement (`paper.tex:177`) can also use. Wording-only change inside anchors — no parser impact.
- **EFPA link:** The enumeration is MESA-original (EFPA's administration conditions are simpler); naming it preserves every element.

### F-20-template-s08-2 — [Minor] Figure 2 duplicates the 8.2 node and invents a tier that maps to no items
- **Axis:** complexity and cognitive load
- **Where:** `MESA EFPA template official.md:1488-1520`
- **Quote:** > S82("8.2 Overall Adequacy of<br/>Baselines and Reference Interpretation") [...] Overall("8.2 Overall Adequacy of<br/>Baselines and Reference Interpretation<br/>& comments")
- **Why it fails a user:** The flowchart — which renders in the live form — shows "8.2 Overall Adequacy" twice (as S82 and as Overall), and a "Final checks" tier (C1-C3) that corresponds to no numbered item, so a reviewer cross-checking figure against items finds three checks they cannot rate and one duplicate destination. Section 8 is also the only Part B section with a figure, which makes its structure look uniquely complex when it is actually one of the simplest (7 items + overall).
- **Fix:** Either delete the figure (nothing in it exceeds what the two-line section outline conveys), or repair it: drop the S82 node (keep Overall), and retitle "Final checks" to "Overall judgment considerations (feed 8.2)". If kept, add matching figures to Sections 9-12 or accept the asymmetry deliberately.
- **EFPA link:** Styled "to match the EFPA figures" per its own comment — EFPA's per-section figures map nodes to real items; the adaptation drifted.

### F-20-template-s08-3 — [Minor] Anchor bloat: 8.1.2 and 8.1.3 carry 10-11 co-equal elements
- **Axis:** verbosity
- **Where:** `MESA EFPA template official.md:1574` (8.1.2), `:1581` (8.1.3)
- **Quote:** > Excellent: Human, contest-population, professional annotator, or expert performance is collected or reported with clear sampling, qualification, task exposure, instructions, timing, tools, uncertainty, coverage of relevant capability domains when broad human-level claims are made, and limits on comparability to AI systems.
- **Why it fails a user:** Same discrimination failure as F-20-template-s06-1: a benchmark with a solid human baseline missing, say, task-exposure documentation has no rule for 2 vs 3. These two items are where HLE and ARC-AGI-2 ratings actually turned in the case studies — the highest-traffic anchors in the section.
- **Fix:** Core/supporting split. 8.1.2 core: sampling and qualification, condition comparability to AI systems (timing/tools), uncertainty; supporting: task exposure, instructions detail, domain coverage (escalates to core only when human-level claims are made — the anchor already contains this conditional; make it structural). 8.1.3 core: model identity+version+date, access mode, run conditions (per F-s08-1), uncertainty.
- **EFPA link:** EFPA §8 norm-sample items — retained function; element inflation MESA-original.

### F-20-template-s08-4 — [Minor] "Repeat or qualify ratings" promises a mechanism the live form does not have
- **Axis:** vagueness (form contract)
- **Where:** `MESA EFPA template official.md:1562`
- **Quote:** > Repeat or qualify ratings where the benchmark has multiple task families, subscores, capability domains, model cohorts, or versions with different reference anchors.
- **Why it fails a user:** Each item renders as exactly one Rating field in the live form (`assets/mesa-form.js` conventions); "repeat" is not possible without hand-editing the markdown, and nothing tells the reviewer where the repeated ratings should live. Same family as the single-placeholder-row tables (F-20-template-s02b-5) and EFPA's dropped per-report iteration rule (F-20-template-s04-1).
- **Fix:** Reword to match the form: "Where task families or versions have different reference anchors, rate the weakest anchor that the intended score interpretation depends on, and itemize the divergent families in Reviewer comments." (If the form later gains repeatable blocks, restore "repeat".)
- **EFPA link:** EFPA norms are per-scale (its form repeats naturally on paper) — drifted under the single-field form contract.

### F-20-template-s08-5 — [Nit] :1545 is the third statement of the anchor-in-intended-meaning rule
- **Axis:** repetition
- **Where:** `MESA EFPA template official.md:1545` (previously `:1158` General Guidance, `:1139` factors list)
- **Quote:** > Reference interpretation should be rated in relation to the meanings users are expected to draw from scores.
- **Why it fails a user:** Third corpus statement of the same rule. The narrow-vs-broad escalation that follows it is section-specific and worth keeping; the framing sentence is not.
- **Fix:** Drop the first sentence of :1545; open directly with "If a benchmark only supports within-benchmark ordering under fixed conditions..." (−12 words).
- **EFPA link:** n/a — MESA guidance economy.

---

## Verdict
- **Disposition:** Trim (name the formula, fix or drop the figure, split two anchors)
- **Items:** 8 rated → 8 (≈ −150 words in this section; ~−110 more template-wide via the run-conditions substitution)
- **Rationale:** Substantively the strongest Part B section — visible EFPA mapping, the best decision typology in the template — carrying two template-wide diseases (formula pasting, anchor bloat) and the template's only figure, which misstates the structure it decorates.
