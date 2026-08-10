---
name: mesa-self-review
description: This skill should be used when the user asks to "review the MESA paper", "critique the MESA template", "self-review MESA", "give me feedback on my paper/template", "continue the MESA feedback", "next feedback section", or otherwise wants MESA's own artifacts (paper.tex and "MESA EFPA template official.md") evaluated for repetition, verbosity, vagueness, unclear terminology, and EFPA traceability. Resumable — each invocation reviews exactly one section and stops.
---

# MESA Self-Review

Review MESA's own artifacts as an expert would review a measurement instrument, **one section
per invocation**. This skill turns inward: every other agent asset in this repo
(`.claude/agents/benchmark-reviewer.md`, `.claude/skills/review-benchmark/`) reviews
third-party benchmarks. This one reviews MESA itself.

The corpus is too large for one context window — `paper.tex` (321 long-line paragraphs) plus
`MESA EFPA template official.md` (2,479 lines, ~20,600 words, 12 sections, 194 headings,
89 rated items, plus free-text prompts, fill-in tables, and checkbox matrices on top).
So the work is chunked and ledger-driven: read the ledger, review the next pending unit, write
one file, update the ledger, **stop**. Re-invoking resumes exactly where it left off. Never
review two units in one invocation, even if the first is short.

## Persona

An expert in both psychometrics and AI benchmark evaluation, who has personally administered
EFPA-style test reviews and has watched practitioners abandon over-long instruments halfway
through. Judge MESA by one question:

> Can a competent, motivated benchmark author who is **not** a psychometrician use this
> document to produce a defensible review without external help?

Findings that do not bear on that question are not worth writing.

## Run loop

### 1. Read the ledger

Read `feedback/00-progress.md`. If it does not exist, do the **bootstrap run** below first,
then continue into step 2 in the same invocation.

### 2. Select one unit

Take the **first** unit with status `pending`, in ledger order. If the user named a specific
unit, take that one instead.

If the unit's line span exceeds ~250 lines, split it at the nearest `###` heading boundary,
replace its ledger row with two rows (`…-a`, `…-b`) carrying the real line spans, and review
the first half only. `20-template-s02-classification` (443 lines) always triggers this.

### 3. Read only this unit's sources

- The unit's own line range, via `Read` with `offset`/`limit`. Do not read the whole file.
- The corresponding passage in `literature/EFPA_Test_Review_Model_2025_Markdown.md`
  (2,804 lines). Locate it by grepping the section title — do not read the file whole. This is
  the ground truth for axis 6.
- The literature file the unit leans on, where one applies:

  | Unit | Source |
  |---|---|
  | Template Section 2 (Classification) | `literature/A_Definition_of_AGI.md` — the CHC (Cattell-Horn-Carroll) grounding |
  | Template Section 6 | `literature/betterbench.md` |
  | Template Sections 10-12 | `literature/Measuring_what_Matters.md`, `literature/The_Leaderboard_Illusion.md`, `literature/What_Does_Your_Benchmark_Really_Measure.md` |
  | Paper Related Work / Discussion | `literature/Evaluating_the_Evaluations.md`, `literature/lineUP.md` |

- The **Cross-cutting log** section of `feedback/00-progress.md`. This is how repetition is
  caught across invocations without re-reading already-reviewed units. Read it every time.

### 4. Write the feedback file

Write `feedback/<unit-id>.md` using the finding format below. Apply all seven review axes.

### 5. Update the Cross-cutting log

Append to `feedback/00-progress.md` any new: term first-use, concept that repeats elsewhere,
paper-vs-template mismatch, or convention violation. Keep entries to one line each — this log
is read on every subsequent run, so it must stay cheap.

### 6. Close out and stop

Flip the unit's status to `done` with its finding counts by severity. Stop. Report the file
written and name the next pending unit.

## Bootstrap run (first invocation only)

1. Create `feedback/` and write `feedback/00-progress.md` seeded with the full ledger below,
   every unit `pending`, plus an empty `## Cross-cutting log` section.
2. Read `critique_plan.md` (186 lines — RETRAI 2026 peer-review comments plus a remediation
   plan) and record under `## Already-addressed criticism` which of its six tasks now appear
   **closed** in the current `paper.tex`. Several are: a `Limitations and Threats to Validity`
   section now exists at `paper.tex:280`, DesignQA was added as the RE-native case study, and
   `betterbench.md` / `Evaluating_the_Evaluations.md` are now in `literature/`. Verify each
   against the actual file rather than assuming. This block prevents every later run from
   re-reporting known, already-fixed criticism.
3. Proceed to unit `10-paper-00-title-abstract`.

## Ledger

Paper units — `paper.tex`:

| id | span | section |
|---|---|---|
| `10-paper-00-title-abstract` | 20-50 | Title, abstract |
| `10-paper-01-introduction` | 51-71 | Introduction |
| `10-paper-02-related-work` | 72-91 | Related Work (+2 subsections) |
| `10-paper-03-methodology` | 92-139 | Methodology (+3 subsections; figures at 99, 106) |
| `10-paper-04-mesa-model` | 140-189 | The MESA Test Review Model (5 `\paragraph` pseudo-headings) |
| `10-paper-05-case-study-design` | 190-209 | Case Study Design (worked example inlined at 204) |
| `10-paper-06-case-study-results` | 210-265 | Case Study Results (HLE, ARC-AGI-2, DesignQA, overall) |
| `10-paper-07-discussion` | 266-279 | Discussion |
| `10-paper-08-limitations` | 280-301 | Limitations and Threats to Validity |
| `10-paper-09-future-conclusion` | 302-321 | Future Work, Conclusion |

Template units — `MESA EFPA template official.md`:

| id | span | section |
|---|---|---|
| `20-template-00-frontmatter` | 1-97 | Introduction, How the Model Should Be Used, Figure 1 |
| `20-template-s01-factual` | 101-148 | 1. Factual Description |
| `20-template-s02-classification` | 149-591 | 2. Classification — **split required** |
| `20-template-s03-measurement` | 592-766 | 3. Measurement and Scoring |
| `20-template-s04-outputs` | 767-922 | 4. Benchmark Outputs and Reports |
| `20-template-s05-access` | 923-1122 | 5. Access, Materials, Lifecycle + Appendix A |
| `20-template-partb-preamble` | 1123-1165 | Information Sources, Explanation of Ratings, General Guidance |
| `20-template-s06-rationale` | 1166-1382 | 6. Rationale, Development, Documentation, Task/Item Quality |
| `20-template-s07-materials` | 1383-1468 | 7. Quality and Usability of Benchmark Materials |
| `20-template-s08-baselines` | 1469-1623 | 8. Baselines, Comparators, Reference Interpretation |
| `20-template-s09-reliability` | 1624-1815 | 9. Reliability, Precision, Score Stability |
| `20-template-s10-validity` | 1816-2077 | 10. Validity Evidence |
| `20-template-s11-fair-use` | 2078-2313 | 11. Fair Use, Comparability, Appropriate Use |
| `20-template-s12-reports` | 2314-2432 | 12. Quality of Reports, Leaderboards, Public Claims |
| `20-template-99-final` | 2433-2479 | Final Evaluation, Bibliography |

Cross-cutting units — run **last**, only after every unit above is `done`:

| id | scope |
|---|---|
| `80-xcut-paper-template-consistency` | Does `paper.tex:140-189` describe the template that actually exists? Also check drift against `.codex/memory/template-structure.md` (self-declared mirror, 281 lines) and the README phase lists. |
| `80-xcut-terminology` | Consolidate the Cross-cutting log into one table: term, first-use line, senses observed, verdict (Substitute / Keep+define / Split), proposed wording. The glossary is the *residue* — the Keep+define rows only — and should be short by design. |
| `80-xcut-length-budget` | Rateable items per section, estimated reviewer hours, where the burden concentrates, and what a realistic completion time would be. |
| `90-synthesis` | Findings ranked by severity; the ten changes with the highest usability payoff; and an explicit answer to "is the template too long, and by how much?" |

Line numbers in this ledger are a starting map, not gospel — if the file has shifted, locate
the section by heading and record the corrected span in the ledger.

## Review axes

Apply all seven to every unit.

### 1. Repetition

Within the unit, and against the Cross-cutting log. Always name the other location. Guidance
repeated in the front matter, a section preamble, and again in an item anchor is the common
case here.

### 2. Verbosity

Prose that could be cut with no loss of review guidance. Quantify the cut: "six rating items
reducible to three", "this 90-word preamble says what the item anchor already says". A finding
that just says "this is wordy" is not actionable.

### 3. Vagueness

The operative test: **would two competent reviewers reading this item independently assign the
same rating?** If not, it is vague. Say specifically what would disambiguate it — a threshold,
an example, a decision rule, an explicit "n/a when…" condition.

### 4. Terminology

Flag any term carrying a technical psychometric meaning that is used before it is defined, or
used in two different senses.

**A glossary entry is the fallback, not the default fix.** Every flagged term must first be
tested for plain-language substitution, and the finding must give the actual replacement
wording. Decide with this test:

| Verdict | When | Action |
|---|---|---|
| **Substitute** | The term is jargon for something sayable in plain words with no loss of precision, or MESA already uses it loosely. | Give the rewritten sentence. e.g. `precision` → "how much a score would move if the benchmark were re-run"; the capability sense of `calibration` → "whether a model's stated confidence matches how often it is right". |
| **Keep + define** | The term is load-bearing: it names a real distinction the reviewer must hold, it is standard in EFPA or the benchmark literature so removing it breaks traceability, or the plain-language version is longer *and* vaguer. | Keep it; add a one-line inline definition at **first use**, plus a glossary entry. Likely: `construct validity`, `capability domain`, `reference interpretation`. |
| **Split** | One word is doing two unrelated jobs. | Rename at least one sense. Known case: `calibration` as a measured model capability (`MESA EFPA template official.md:7`) vs. `calibration` as scorer-tuning data (`:1135`) — rename the second to "scorer tuning data". |

Bias toward **Substitute**. Reach for **Keep + define** only when the finding can state in one
sentence what would be lost by substituting; if the loss is EFPA traceability, name the EFPA
item that depends on the term. Growing a glossary is not the same as making the template usable.

### 5. Complexity and cognitive load

Heading nesting depth, cross-references the reviewer must hold in their head, and instructions
to work out of order — e.g. `MESA EFPA template official.md:1172` tells the reviewer to revisit
Section 6 after completing Sections 8-12.

### 6. EFPA traceability

Which EFPA item does this adapt? Is the adaptation **retained**, **drifted**, or
**MESA-original**? Is that link visible to a reader, or known only to the author? MESA's
authority rests on being a faithful adaptation, so an invisible link is itself a finding.

### 7. Claim support *(paper units only)*

Is each claim carried by the evidence cited, and does it match what the template actually does?
The paper describes the template; where it describes something the template does not do, that
is a `Major` at minimum.

## Finding format

```markdown
### F-<unit>-<n> — [Blocker|Major|Minor|Nit] <one-line title>
- **Axis:** vagueness
- **Where:** `MESA EFPA template official.md:1651`
- **Quote:** > ...verbatim text...
- **Why it fails a user:** <who misreads this, and what wrong rating or wasted effort results>
- **Fix:** <specific replacement wording, or a specific cut naming the items removed>
- **EFPA link:** EFPA §9.2 (`EFPA_Test_Review_Model_2025_Markdown.md:1402`) — retained | drifted | MESA-original
```

Severity:

- **Blocker** — a reviewer cannot complete the item, or would confidently misapply it.
- **Major** — materially degrades review quality or reviewer completion rate.
- **Minor** — real but survivable friction.
- **Nit** — wording and polish.

Every file closes with a **Verdict** block:

```markdown
## Verdict
- **Disposition:** Keep as-is | Trim | Rewrite | Merge into §X
- **Items:** <n> before → <n> after
- **Rationale:** <one line>
```

These verdicts are the input to `/mesa-core-plan`. Write them for every unit, including paper
units (where "items" means paragraphs or claims).

## Standing constraints

- **Quote before judging.** Every finding carries a verbatim quote and a real line reference.
  Never paraphrase into the Quote field and never guess a line number — a wrong reference makes
  the whole document untrustworthy.
- **Severity is earned.** If everything is a Blocker, nothing is.
- **Never propose a cut without stating which EFPA function it serves and where that function
  survives.** Preserving the EFPA link through any trimming is a hard requirement.
- **The template markdown is a machine-readable contract.** `assets/mesa-form.js:19` fetches
  `MESA EFPA template official.md` at load time and builds the live fillable form by parsing
  it, keying off the authoring conventions documented at `assets/mesa-form.js:6-14`:
  - headings `#`..`######`, numeric prefixes (`2.1`, `6.1.1`) define item IDs;
  - checkbox options `- [ ] Label`;
  - rating items `- Rating: [n/a | 0 | 1 | 2 | 3 | 4]`, anchored by `- Excellent: ...`;
  - free-text prompts: a standalone line ending in `:`;
  - fill-in table cells containing `_(placeholder)_`; checkbox-matrix cells containing `[ ]`;
  - figures as ```mermaid fenced blocks.

  Any fix that changes formatting rather than wording must say whether it breaks the parser.
  This is also a review axis in its own right: where a section's markup deviates from these
  conventions, items are **already** being dropped from the live form — flag that as a
  `Blocker`.
- **Write only under `feedback/`.** Never edit `paper.tex`, the template, or any other repo
  file. This skill diagnoses and proposes; `/mesa-core-plan` plans the changes; the user
  decides.
- **Repo style applies** (see `CLAUDE.md`): concise academic prose, description separated from
  evaluative judgment, cautious language where documentation is incomplete, uncertainty flagged
  explicitly rather than filled with confident speculation.
- **Do not compile LaTeX.**

## Notes

- If the user asks for a specific section out of order, honor it and mark that unit `done`;
  ledger order is a default, not a constraint.
- If a unit has genuinely no findings, say so and write the Verdict block anyway. An empty
  finding list is a legitimate result and is more useful than manufactured nits.
- When the last cross-cutting unit is `done`, tell the user that `/mesa-core-plan` is now
  unblocked.
