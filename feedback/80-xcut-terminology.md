# Feedback — `80-xcut-terminology`

Scope: consolidate every term flagged in the Cross-cutting log into one decision table.
Verdicts follow the skill's test: **Substitute** (plain words, no precision loss),
**Keep + define** (load-bearing; inline definition at first use + glossary entry),
**Split** (one word, two jobs). The glossary is the residue — Keep+define rows only.

## Decision table

| Term | First use | Senses observed | Verdict | Action / proposed wording |
|---|---|---|---|---|
| `calibration` | template `:7`; paper `:214`; template `:1135`; paper `:222` | (1) model-confidence calibration; (2) scorer-tuning data; (3) human difficulty calibration | **Split** | Keep sense 1 with paper `:214`'s footnote definition ("gap between a model's stated confidence and its accuracy"). Rename sense 2 → "tuning data for model-based scorers" (F-20-template-partb-3). Sense 3 → "human difficulty-norming campaign" at paper `:222`. |
| `claim proportionality` | paper `:44` | one (claims bounded by measured evidence) — but its only near-definition glosses gameability (F-10-paper-04-3) | **Keep + define** | Load-bearing: names template §10.6, MESA-original. Define at paper `:175` per F-10-paper-04-3 ("whether public claims stay within what the measured evidence supports") + glossary. Abstract keeps the plain substitute (F-10-paper-00-5). |
| `construct validity` | paper `:44`, body `:55` | one (standard psychometric) | **Keep + define** | EFPA/AERA-standard — substitution breaks traceability to EFPA §10. Inline definition at paper `:55` per F-10-paper-01-2 ("whether the benchmark actually measures the capability it claims to measure") + glossary. |
| `construct-irrelevant variance` | template `:2000` (10.3.2 heading); paraphrased at `:11` ("irrelevant score effects"), `:753` ("non-target rewarded behavior"), `:2002` ("score variation caused by factors outside the target capability") | one concept, four phrasings | **Keep + define** (heading) / **Substitute** (prose) | Keep the technical term only in the 10.3.2 heading with a one-line gloss; standardize all prose paraphrases to one: "score effects from outside the target capability". Retire "irrelevant score effects" and "non-target rewarded behavior". |
| `capability domain` | template `:153` (§2.1); paper `:61` variant "capability-area" | one (CHC-grounded) | **Keep + define** | Load-bearing: CHC traceability (A Definition of AGI). One-line gloss at template 2.1 + glossary; fix the paper's "capability-area" variant (F-10-paper-01-4). |
| `reference interpretation` | template §8 title; effectively defined `:1471` | one | **Keep + define** | EFPA §8 traceability (norms→reference points). Promote `:1471`'s definition into a one-liner at first frontmatter use + glossary. |
| `run conditions` | proposed term (F-20-template-s08-1) | — (replaces the 13-word formula found verbatim 10×) | **Keep + define** (new) | Glossary: "the prompts, settings, tools, time limits, access rules, hardware, and human-intervention rules under which an evaluation executes." Substitute at all ten formula sites. |
| `intended score meaning` | template `:1158`, `:1545` | one; competes with "the specific meaning users are supposed to draw from a score" (`:11`, `:19`, `:1824`) | **Substitute** (canonicalize) | Replace the ten-word formula with "the intended score meaning" at `:11`, `:19`, `:1824` (F-20-template-s10a-1). Self-explanatory; no glossary entry needed. |
| `precision` | template §9 title; defined `:1630` | one ("consistency and uncertainty of benchmark scores across replications") | **Keep** (already defined) | No action beyond keeping `:1630`'s in-situ definition through the S9 trims. |
| `evidence gap` | paper `:44`; template passim; Gap Register | one | **Keep + define** | MESA's signature concept; glossary: "descriptive or evaluative information that is missing or inaccessible, recorded rather than guessed; a gap is not automatically a defect (see rating `0` vs `1`)." |
| `supported-use / non-use statement` | paper `:44`/`:204`; template 2.18, 11.5.1, Final Evaluation | one | **Keep + define** | Glossary: "the review's closing statement of what interpretations the scores support, what they do not, and the run conditions that must hold" — wording doubles as the F-20-template-99-2 prompt. |
| `gameability` | paper `:175`; template §10.5 | one | **Keep + define** | Defined by the F-10-paper-04-3 fix ("a high score obtainable through shortcuts, exposure, formatting, tuning, or scaffolding rather than the target capability"); reuse as glossary line. |
| `traceability` | paper `:59` | one, but defined circularly | **Keep + define** (paper-side) | F-10-paper-01-3's rewrite is the definition; no template glossary entry needed (template uses the concept via "traced/traceable" plainly). |
| `model-as-judge` / `judge` | template `:122`; paper `:214` | one | **Keep + define** | Paper `:214` already glosses ("a separate AI model that decides whether an answer matches the reference"); copy that line into the glossary; watch no drift toward human judges (none observed). |
| `review base` | template `:103` | one, single use | **Substitute** | Per F-20-template-s01-2: "the materials actually inspected for this review". |
| `execution bias` | paper `:61` | unclear | **Substitute** | Per F-10-paper-01-4: "contamination and unstable-implementation artifacts". |
| `four-element anchoring model` | paper `:204` | one, single use | **Substitute** | Per F-10-paper-05-2: introduce as "a four-element profile" — no term of art needed. |
| `requirements object` | paper `:142` | one, single use | **Substitute** | Per F-10-paper-04-5: "requirements-relevant review object" (matches `:84`). |
| reviewed-entity type list | template `:13`, `:21`, `:119`, `:1259` (four variant lists; "rolling version"↔"rolling cohort", "evaluation slice"↔"slice") | one taxonomy, four inventories | **Substitute** (canonicalize) | Per F-20-template-s01-1: one canonical entity-type list in the frontmatter; all other sites reference it. Standardize on "rolling cohort" and "slice". |
| framework name | paper `:140`, `:61`; template `:1`, `:33` | four names, one artifact | **Substitute** (canonicalize) | Per F-80-xcut-consistency-3: "MESA Test Review Model" (framework) / "MESA template" (document). |

## Resulting glossary (the residue — 10 entries)

construct validity · capability domain · claim proportionality · reference interpretation ·
run conditions · evidence gap · supported-use/non-use statement · gameability ·
model-as-judge · construct-irrelevant variance (10.3.2 heading gloss)

Ten one-line entries, each already drafted above — short by design, exactly as the skill
requires. Everything else resolves by substitution or renaming, which is the correct outcome:
the template's dominant terminology strategy (plain-language paraphrase with footnote-style
glosses, as practiced in the paper's Case Study Results) survives intact.

## Verdict
- **Disposition:** Keep as-is (this file is the deliverable; no template text reviewed beyond the log)
- **Items:** 20 flagged terms → 6 Substitute, 10 Keep+define, 1 Split, 3 canonicalizations
- **Rationale:** The corpus needs a ten-line glossary and about twenty point substitutions — not a terminology overhaul; the one genuinely dangerous word was `calibration`, and its three senses now have three names.
