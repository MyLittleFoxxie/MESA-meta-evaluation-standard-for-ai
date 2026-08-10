# MESA Core Plan (`95-mesa-core-plan`)

Consumes the completed self-review (31/31 units `done`; 122 findings, 0 Blockers — see
`90-synthesis.md`). This is a **plan**: no template text, agent file, or website asset is
edited here. Every recommendation cites the finding that motivates it.

**Governing invariants**

1. *In-paper authorization:* "many RE workflows need a compact scorecard that preserves
   evidence without hiding caveats" (`paper.tex:307`; F-10-paper-09 preamble). Evidence and
   caveats must survive compression.
2. *Acceptance criterion for all deduplication:* "This is not redundant as long as each
   section preserves its role" (`paper.tex:180`, F-10-paper-04-1). After the migration, no
   two items may share a role.
3. *Traceability:* every EFPA item has a row in Part 3. An item absent from that table is a
   silent drop, which this deliverable exists to prevent.

**Architecture decision (affects every part below).** MESA remains **one template**, not two
documents. Each item carries a tier marker — a plain `- Tier: Core` or
`- Tier: Extended (…trigger…)` bullet, which the form parser renders as inert prose
(`assets/mesa-form.js:172-181`; parser contract preserved) — plus a Core index table in the
front matter. A "MESA Core review" completes the Core items; a full (certification-grade)
review completes Core plus every Extended block. This avoids a second artifact that would
drift against the seven sync surfaces catalogued in Part 5 (F-80-xcut-consistency-4).

**Numbering decision (stated up front, per Part 5 step 1).** Item IDs in the live form derive
from numeric heading prefixes (`assets/mesa-form.js:7, :90-95`), and the agent mirror declares
numbering load-bearing (`.codex/memory/template-structure.md`, F-80-xcut-consistency memo).
The migration therefore adopts **retire, don't renumber**: merged items keep the
lower-numbered ID and the absorbed ID is retired with a one-line tombstone note (2.6 → 2.9,
4.10 → 2.4, 10.6.2 → 10.6.1, 11.3.2 → 11.3.1); no surviving item changes its number. One
deliberate deviation from a filed finding follows from this: F-20-template-s09-2's flatten
(9.1.1→9.1, 9.5.1→9.5) is **not adopted** — the sub-section preambles are folded into the item
text, but the headings and IDs stay, because two cosmetic renumberings are not worth breaking
ID stability. Recorded here as a conflict resolution, not an oversight.

---

## Part 1 — MESA Core

**Target: 31 rated items (of the trimmed template's 84) plus a compressed Part A of
~26 descriptive units. Estimated completion time: 8-12 hours** (Part A ≈ 3-5 h, Part B ≈
4-6 h, Final Evaluation ≈ 1 h), versus 22-35 h for the full review after the filed trims
(`80-xcut-length-budget`). Item count and time target are the synthesis's own derivation
(`90-synthesis` §3: "approximately 30-35 rated items centered on the sections where the
case-study ratings actually turned (8-10 and 12), a compressed Part A, the Gap Register, and
the supported-use/non-use statement — targeting 8-12 hours").

**Selection principle.** Core Part B = the items whose ratings decided the three case-study
verdicts (Sections 8-10 and 12 per `80-xcut-length-budget`; anchor-traffic evidence in
F-20-template-s06-1, F-20-template-s08-3) plus the seven section overalls (so the Summary of
Ratings table is always completable) plus the claims pipeline (`90-synthesis` §4: 2.18
collects → 10.6 rates proportionality → 11.5 rates use guidance → 12.3 rates communication).
Core Part A = exactly the descriptive fields those Part B items consume, plus every field
that carries an Extended-block trigger (a trigger field must always be answered).

### Core Part B items (31)

| § | Core items | Grounding |
|---|---|---|
| 6 (6 of 25) | 6.1.1, 6.1.3, 6.2.3, 6.2.7, 6.3.1, 6.4 | 6.1.3/6.2.7/6.3.1 are the section's highest-traffic anchors and BetterBench's weak spots (F-20-template-s06-1); 6.1.1 + 6.1.3 fix the construct and the phenomenon-task-metric-claim chain that Section 10 consumes; 6.2.3 is the scoring documentation Part B cannot proceed without; 6.4 feeds the Summary |
| 7 (3 of 8) | 7.1.1, 7.1.4, 7.1.8 | availability and harness quality gate whether anything else is checkable (F-20-template-s07 preamble); 7.1.8 feeds the Summary |
| 8 (4 of 8) | 8.1.1, 8.1.2, 8.1.3, 8.2 | "8.1.2/8.1.3 are where HLE and ARC-AGI-2 ratings actually turned" (F-20-template-s08-3); the reference-kind typology (:1547) is on the protect list; 8.2 feeds the Summary |
| 9 (5 of 11) | 9.1.1, 9.2.1, 9.2.2, 9.5.1, 9.6 | 9.1.1 as inventory per F-20-template-s09-1; DesignQA's verdict hinged on uncertainty reporting (9.2.2) and item-count sensitivity (9.5.1; `paper.tex:232-234` thresholds, protect list); 9.6 feeds the Summary |
| 10 (7 of 14) | 10.1.1, 10.3.1, 10.3.2, 10.5.1, 10.5.2, 10.6.1, 10.7 | the section the synthesis calls the intellectual center; contamination/gameability and proportionality are the MESA-original additions the case studies exercised (F-20-template-s10b preamble); 10.6.1 is the merged proportionality item (F-20-template-s10b-3); 10.7 feeds the Summary |
| 11 (3 of 11) | 11.3.1, 11.5.1, 11.6 | 11.3.1 is the merged comparability item (F-20-template-s11-2); 11.5.1 is the claims-pipeline stage; 11.6 feeds the Summary |
| 12 (3 of 10) | 12.2.1, 12.3.1, 12.5 | the HLE pattern — careful paper, caveat-dropping leaderboard — is decided at 12.2.1 (condition/version labeling) and 12.3.1 (claim-score linkage) (F-20-template-s12-1 context; inference-level principle :2322 on the protect list); 12.5 feeds the Summary |

### Core Part A (~26 units)

Front matter (canonical entity list, evidence-gap rule, glossary) · **General Description**
(the merged Short Description + Appendix A — see Part 3 row for EFPA Appendix A; closes
F-20-template-00-7 / F-20-template-s05-3 / F-80-xcut-consistency-1) · **Source Inventory**
(promoted house convention, F-80-xcut-consistency-1) · 1.1, 1.2, 1.3 (section verdict: Keep
as-is, F-20-template-s01) · 2.1, 2.2, 2.3, 2.5, 2.8, 2.9 (absorbing 2.6), 2.11 (core rows
only, F-20-template-s02b-4), 2.12, 2.15, 2.16, 2.17, 2.18 · 3.1, 3.2, 3.5, 3.6 · 4.1, 4.2 ·
5.2, 5.5, 5.6, 5.7, 5.8 (deduped rows, F-20-template-s05-2) · Final Evaluation (all of it:
Evaluative Report with the hold-fixed-conditions statement per F-20-template-99-2,
Conclusions, Recommendations, Summary of Ratings, Gap Register).

Trigger-bearing fields are all Core by construction: 2.2 (high-stakes use), 2.15/2.16
(private/rolling forms), 2.18 (broad claims), 3.1 (model-scored), 4.1 (hosted leaderboard).

### What Core preserves, per section — and what a Core-only review cannot conclude

- **Part A (compressed):** preserves identity, provenance, the inspected-materials trail
  (1.3 + Source Inventory), the claimed construct in the benchmark's own words (2.1 with the
  relocated construct rows, F-20-template-s02a-5), the scoring pathway (3.1/3.2), reference
  points (3.5), forms and contamination surface (2.15-2.17, 5.5-5.8). Does not produce: the
  full classification profile (2.4, 2.7, 2.10, 2.13, 2.14), output-surface catalog beyond
  4.1-4.2, or distribution/qualification detail (5.1, 5.3, 5.4).
- **§6:** preserves whether the score has a stated meaning at all (construct + chain) and
  whether scoring, versioning, and setup are documented well enough to reproduce. Cannot
  certify documentation completeness or development-process quality (6.1.4-6.1.7, 6.2.x
  balance) — that is certification-tier work.
- **§7:** preserves whether the materials exist and the harness runs. Cannot judge usability,
  accessibility, or licensing risk.
- **§8:** preserves whether *any* reference anchors the intended score meaning (chance,
  human, model cohort — the typology at :1547). Cannot judge representativeness or currency
  of those references.
- **§9:** preserves whether reported differences are distinguishable from noise (evidence
  inventory, run-to-run stability, uncertainty, meaningfulness of differences). Cannot judge
  scorer-type-specific reliability unless the matching Extended trigger fires.
- **§10:** preserves the validity core the case studies actually used: content
  representativeness, scoring-pathway validity, shortcut sensitivity, contamination,
  gameability, claim proportionality. Cannot assess internal structure (10.2) or relations to
  other variables (10.4).
- **§11:** preserves cross-system comparability and the benchmark's own use guidance. Cannot
  assess subgroup fairness, inclusive design, or differential performance (11.1, 11.2, 11.4).
- **§12:** preserves whether the headline surface labels conditions/versions/uncertainty and
  whether public claims trace to scores. Cannot audit every surface or leaderboard
  governance depth.

**No section contributes zero Core items.** The closest is Section 4 (two of ten
subsections): its descriptive catalog is mostly leaderboard-conditional, and the evaluative
work on reports lives in Section 12 (F-20-template-s04-2 established that 4.x was already
duplicating other homes).

**What a Core-only review can conclude:** a source-grounded characterization of the
benchmark ("best characterized as X, rather than Y" — the case-study output form), a
supported-use / non-use statement with hold-fixed conditions, a Gap Register, and a
minimum-standard verdict on critical attributes (restored EFPA rule, F-20-template-partb-2).
**What it cannot conclude:** certification-grade fitness for procurement, policy, or safety
cases — which is precisely why the high-stakes trigger (E5, Part 2) forces the full item set.

**Evidence-sufficiency caveat.** The synthesis fixes the Core's *shape* (sections 8-10 and
12, 30-35 items) but no feedback unit produced an item-level list of which ratings moved in
the case studies. The item-grain choices above (e.g., 9.4.1 prompt sensitivity excluded from
Core; 12.2.2 excluded) are this plan's judgment. Before template v2 ships, run a 1-2 h check
of the three `reviews/gemini_supervising_editor/` rating tables: **every item rated 0 or 1
in any reconciled case study must be Core or have its Extended trigger fire for that
benchmark.** If any 0/1-rated item escapes both, promote it to Core and record the change
here. Do not ship the tier markers without this check.

---

## Part 2 — MESA Extended

Extended items stay in the template at their existing numbers; each block opens with a
one-sentence trigger the reviewer evaluates from Core Part A fields. If the trigger does not
fire, the block is skipped and its items are recorded as "not triggered" (distinct from n/a —
the Summary of Ratings notes untriggered blocks). If it fires, the block is mandatory.

| Block | Trigger (evaluated from) | Items |
|---|---|---|
| **E1 — Broad-capability claims** | 2.18 records claims of general intelligence, AGI, broad cross-domain capability, autonomy/agency, or human-level comparison. *Narrowed from the current screen: drop "reasoning" from the trigger list — it fires on essentially every modern benchmark and saves no one any work (Cross-cutting log :87, `80-xcut-length-budget` §1).* | 2.1 secondary-domain profile (beyond the 3-primary cap, F-20-template-s02a-3), 10.1.2, 10.4.2; the broad-claims conditional inside 10.6.1's merged anchor escalates (10.5.1 two-tier pattern, F-20-template-s10b-3) |
| **E2 — Model-based scoring** | 3.1 records an LLM equality-checker or LLM judge (boundary wording per F-20-template-s03-2). | 9.3.3; judge-validation elements of 10.3.1's anchor escalate; Part B source list's "tuning data for model-based scorers" (F-20-template-partb-3) becomes a required source to seek |
| **E3 — Hosted leaderboard / public results portal** | 4.1 records a hosted leaderboard, dashboard, or public results portal. | 2.4 (with recipient-competence column, F-20-template-s04-2), 4.3-4.9, 8.1.6, 12.1.1, 12.1.2, 12.2.2, 12.3.2, 12.4.1, 12.4.2, 12.4.3 |
| **E4 — Private, held-out, or rolling/refreshed forms** | 2.15 lists private/hidden forms, or 2.16 records dynamic/rolling task determination. | 8.1.4, 9.4.2, 11.3.3; the high-disclosure-risk tier of 10.5.1's anchor escalates (the anchor already contains this conditional — make it structural, F-20-template-s10b preamble) |
| **E5 — High-stakes use** | 2.2 or 2.18 records intended or observed use in procurement, policy, safety cases, or other high-stakes comparison. | **All remaining Extended items** — E5 forces every block plus the certification-tier items with no narrower trigger: 2.7*, 2.10*, 2.13*, 2.14, 3.3, 3.4*, 3.7, 5.1, 5.3, 5.4, 6.1.2, 6.1.4-6.1.9, 6.2.1, 6.2.2, 6.2.4-6.2.6, 6.2.8, 6.3.2-6.3.7, 7.1.2, 7.1.3, 7.1.5-7.1.7, 8.1.5*, 8.1.6, 8.1.7, 9.3.1*, 9.3.2*, 9.4.1, 9.4.3*, 10.2.1-10.2.3*, 10.4.1-10.4.3, 11.1.1, 11.1.2, 11.2.1, 11.2.2, 11.4.1, 11.4.2, 11.5.2*, 12.4.1, 12.4.2 |

*Starred items also carry a narrow item-level trigger that can fire without E5:*

| Item | Narrow trigger |
|---|---|
| 2.7, 2.13 | agentic, tool-using, or environment-based benchmark (2.9 interaction groups) |
| 2.10 | multimodal inputs recorded in 2.9/2.10 |
| 3.4 | transformed or derived scores exist (Elo, normalization — 3.2) |
| 6.1.8 | reviewed entity is derived, translated, adapted, or a slice (1.2 Entity Type) |
| 8.1.5 | documentation claims thresholds, bands, or performance categories (3.5) |
| 9.3.1 | automated parser/extractor in the scoring pathway (3.1) |
| 9.3.2 | human raters in the scoring pathway (2.17/3.1) |
| 9.4.3 | execution depends on external services, tools, or environments (2.13/2.8) |
| 10.2.1, 10.2.2 | subscores or capability-domain profiles are reported (3.2) |
| 11.5.2 | sensitive content or dual-use tasks documented (2.18/5.5) |

The full certification review is, by construction, Core + all Extended blocks — identical in
coverage to the trimmed template's 84 rated items, so the two-tier answer adds no third
maintenance surface.

---

## Part 3 — EFPA traceability table

Granularity: one row per numbered EFPA heading or rated sub-item in
`literature/EFPA_Test_Review_Model_2025_Markdown.md` (2,804 lines; duplicate tail content at
:2663-2706 is ignored — first occurrences cited). Dispositions: **Core** / **Extended** /
**Merged into §X** (function survives at the named MESA item) / **Dropped** (reason must be
AI-inapplicability). MESA § refers to the post-migration template (numbering preserved per
the retire-don't-renumber rule).

### Front matter and Part A

| EFPA § | EFPA line ref | MESA § (new) | Disposition | Note |
|---|---|---|---|---|
| Introduction | `:5` | Introduction | Core | near-verbatim adaptation held up (F-20-template-00 preamble); AERA attribution restored (F-20-template-00-6) |
| How the Model Should Be Used | `:15` | How Used | Core | canonical entity list stated once (F-20-template-00-2) |
| Figure 1 | `:27` | Figure 1 | Core | ShortDesc node implemented by the merged General Description (F-20-template-00-7, F-80-xcut-consistency-1) |
| Part A Information Sources | `:99` | front matter :17/:25 + §1.3 | Core | publisher-preference rule survives |
| §1 General information | `:107` | 1.1 + 1.2 | Core | "Response" column header restored (F-20-template-s01-3); Entity Type gets the closed vocabulary (F-20-template-s01-1) |
| 2.1 Content domains | `:129` | 2.1 | Core | ≤3-primary-domain cap restored (F-20-template-s02a-3); construct rows relocated here from 2.5 (F-20-template-s02a-5) |
| 2.2 Area of use | `:152` | 2.2 | Core | E5 trigger source; "Other" restored (F-20-template-s02a-2) |
| 2.3 Populations intended | `:168` | 2.3 | Core | intended AI systems feed Core 11.3.1 |
| 2.4 Main intended users | `:179` | 2.4 | Extended (E3/E5) | absorbs EFPA 4.10; recipient-competence dimension restored (F-20-template-s04-2) |
| 2.5 Scales and variables | `:192` | 2.5 | Core | score rows consolidated into 3.2 (F-20-template-s03-1); unit-term economy (F-20-template-s02a-4) |
| 2.6 Response mode | `:204` | — | Merged into §2.9 | human modality/format distinction did not survive AI translation (F-20-template-s02a-1); ID 2.6 retired |
| 2.7 Demands on the test taker | `:222` | 2.7 | Extended (agentic/tool-use) | prerequisites translation retained (praised, F-20-template-s02a preamble) |
| 2.8 Special testing conditions | `:247` | 2.8 | Core | home of run conditions |
| 2.9 Item response types | `:255` | 2.9 | Core | absorbs 2.6; escape options restored |
| 2.10 Item stimulus type | `:277` | 2.10 | Extended (multimodal) | escape option restored (F-20-template-s02b-3) |
| 2.11 Total number of items | `:290` | 2.11 | Core (core rows) | 5 core rows always; breakdown rows conditional (F-20-template-s02b-4) |
| 2.12.1 Mode of administration | `:299` | 2.12 | Core | venue/openness/cadence group labels (F-20-template-s02b-1) |
| 2.12.2 Mode of use (supervision spectrum) | `:309` | 2.12 | Core | EFPA level definitions restored (F-20-template-s02b-1) |
| 2.13 Technological arrangements | `:319` | 2.13 | Extended (environment/harness) | escape row restored |
| 2.14 Time required | `:332` | 2.14 | Extended (E5) | documented-estimates-only rule kept — protect list (`90-synthesis` §4) |
| 2.15 Different forms | `:347` | 2.15 | Core | multi-row placeholder fix (F-20-template-s02b-5); E4 trigger source |
| 2.16 Static or dynamic determination | `:354` | 2.16 | Core | E4 trigger source |
| 2.17 Informant in the test | `:367` | 2.17 | Core | best Part A translation (F-20-template-s02b preamble); consumed-vs-generated boundary sentence (F-20-template-s02b-2); "Not explicitly stated" first |
| 3.1 Scoring procedure | `:388` | 3.1 | Core | method groups + judge boundary (F-20-template-s03-2); E2 trigger source |
| 3.2 Scores | `:402` | 3.2 | Core | the single score-inventory home (F-20-template-s03-1) |
| 3.3 Scales used | `:410` | 3.3 | Extended (E5) | escape + not-stated options (F-20-template-s03-6) |
| 3.4 Score transformation | `:431` | 3.4 | Extended (transformed scores) | EFPA explanatory preamble restored (F-20-template-s03-5) |
| 3.5 Norming procedures | `:441` | 3.5 | Core | norms→reference points (verified against paper, F-10-paper-03 preamble); checkbox layer deleted, table kept (F-20-template-s03-3) |
| 4.1 Reports available | `:452` | 4.1 | Core | per-output iteration rule restored (F-20-template-s04-1); E3 trigger source; subset option fixed (F-20-template-s04-3) |
| 4.2 Name/description of report | `:460` | 4.2 | Core | three placeholder rows |
| 4.3 Design or presentation | `:466` | 4.3 | Extended (E3) | |
| 4.4 Structure | `:487` | 4.4 | Extended (E3) | ~8 options with EFPA-style inline definitions (F-20-template-s04-4) |
| 4.5 Sensitivity to context | `:499` | 4.5 | Extended (E3) | |
| 4.6 Development of the report | `:509` | 4.6 | Extended (E3) | "actuarial" substituted (F-20-template-s04-6) |
| 4.7 Modifiability | `:522` | 4.7 | Extended (E3) | |
| 4.8 Transparency | `:531` | 4.8 | Extended (E3) | three disjoint grades restored (F-20-template-s04-5) |
| 4.9 Type of content | `:540` | 4.9 | Extended (E3) | |
| 4.10 Intended recipients | `:554` | — | Merged into §2.4 | one audience home; competence question survives as a 2.4 column (F-20-template-s04-2); ID 4.10 retired |
| 5.1 Supporting information from distributor | `:571` | 5.1 (retitled) | Extended (E5) | retitle "Supporting Documentation Provided to Users" is ID-safe — form IDs use numeric prefixes (`assets/mesa-form.js:90-95`), correcting F-20-template-s05-1's migration worry; F-80-xcut-consistency-2 |
| 5.2 Methods of publication | `:583` | 5.3 | Extended (E5) | |
| 5.3 Test-related qualifications | `:593` | 5.4 | Extended (E5) | none-vs-unclear completion rule restored (F-20-template-s05-5) |
| Appendix A: General description | `:605` | General Description | Core | EFPA's content/length spec restored (F-20-template-s05-3); merged with the house Short Description so Figure 1 becomes true (F-80-xcut-consistency-1) |

### Part B preamble

| EFPA § | EFPA line ref | MESA § (new) | Disposition | Note |
|---|---|---|---|---|
| Part B Information Sources | `:615` | Part B Information Sources | Core | "tuning data for model-based scorers" rename (F-20-template-partb-3); publish-recommendation follow-through noted (F-20-template-partb-2) |
| Explanation of Ratings | `:627` | Explanation of Ratings | Core | below-minimum-standard verdict rule (`:633`) and bold-critical convention (`:631`) restored (F-20-template-partb-2) |
| Rating Scale | `:635` | Rating Scale | Core | 1-3 interpolation rule added (F-20-template-partb-1 — the highest-leverage Part B fix) |
| General Guidance | `:652` | General Guidance | Core | MESA's version judged superior to EFPA's (F-20-template-partb preamble); closing platitude deleted (F-20-template-partb-4) |

### Section 6

| EFPA § | EFPA line ref | MESA § (new) | Disposition | Note |
|---|---|---|---|---|
| 6.1.1 Theoretical foundations | `:674` | 6.1.1 | Core | |
| 6.1.2 Empirical research summary | `:680` | 6.1.2 | Extended (E5) | |
| 6.1.3.1 Test design | `:688` | 6.1.4 | Extended (E5) | |
| 6.1.3.2 Item content procedures | `:695` | 6.1.5 | Extended (E5) | |
| 6.1.3.3 Final pool selection | `:702` | 6.1.6 | Extended (E5) | |
| 6.1.4 Translation/adaptation | `:709` | 6.1.8 | Extended (derived entity) | |
| 6.1.5 Quantitative item evidence | `:716` | 6.1.7 | Extended (E5) | n/a decision rule added (F-20-template-s06-3) |
| 6.1.6 Item analysis methodology | `:742` | — | Merged into §6.1.7 | MESA consolidates EFPA's three quantitative items into one |
| 6.1.7 Item analysis results | `:755` | — | Merged into §6.1.7 | same consolidation |
| 6.1.8 Overall: rationale/development | `:767` | 6.1.9 | Extended (E5) | sub-overall retained — see conflict note below |
| 6.2.1 Rationale documentation | `:780` | 6.2.1 | Extended (E5) | |
| 6.2.2 Development documentation | `:784` | 6.2.2 | Extended (E5) | |
| 6.2.3 Translation/adaptation docs | `:788` | — | Merged into §6.1.8 | rated with the adaptation item it documents |
| 6.2.4 Standardisation procedure | `:792` | — | Merged into §8.1.2/8.1.6 | documented baseline-collection procedure is rated in situ at §8 |
| 6.2.5 Norms documentation | `:796` | — | Merged into §8 | reference-group documentation rated directly at 8.1.x (norms→reference points) |
| 6.2.6 Reliability documentation | `:800` | 6.2.4 | Extended (E5) | |
| 6.2.7 Validity docs: content | `:804` | — | Merged into §6.2.5 | MESA 6.2.5 consolidates EFPA 6.2.7-6.2.10 |
| 6.2.8 Validity docs: internal structure | `:808` | — | Merged into §6.2.5 | |
| 6.2.9 Validity docs: other variables | `:812` | — | Merged into §6.2.5 | |
| 6.2.10 Validity docs: other sources | `:816` | — | Merged into §6.2.5 | |
| 6.2.11 Fair-use support docs | `:820` | 6.2.6 | Extended (E5) | boundary with 11.1.2 stated (F-20-template-s11-3) |
| 6.2.12 Digitally generated report docs | `:824` | — | Merged into §12 | report quality rated directly in Section 12 |
| 6.2.13 Language (inclusive) | `:828` | — | Merged into §11.1.2 + §12.4.1 | inclusive-language function survives at both fairness surfaces |
| 6.2.14 Overall: documentation adequacy | `:832` | 6.2.8 | Extended (E5) | see conflict note below |
| 6.3.1 Test administration | `:840` | 6.3.1 | Core | anchor capped at ~6 core elements (F-20-template-s06-1) |
| 6.3.2 Test scoring | `:844` | 6.3.2 | Extended (E5) | |
| 6.3.3 Norming instructions | `:848` | — | Merged into §6.3.2 | automated score-transformation checks fold into scoring-procedure instructions |
| 6.3.4 Interpretation and reporting | `:852` | 6.3.3 | Extended (E5) | |
| 6.3.5 Feedback and debriefing | `:856` | — | Merged into §12.4.2 | no human test taker to debrief; the stakeholder-communication function survives in report acceptability |
| 6.3.6 Fairness/bias good practice | `:860` | — | Merged into §11.1.2 | |
| 6.3.7 Restrictions on use | `:864` | 6.3.4 | Extended (E5) | evaluative twin of Core 11.5.1 |
| 6.3.8 Software and technical support | `:868` | 6.3.5 | Extended (E5) | |
| 6.3.9 References and supporting materials | `:872` | 6.3.6 | Extended (E5) | |
| 6.3.10 Overall: procedural instructions | `:876` | 6.3.7 | Extended (E5) | see conflict note below |
| 6.4 Overall adequacy | `:880` | 6.4 | Core | |

> **Conflict note (surfaced per skill rules).** F-20-template-s06 and the Cross-cutting log
> (:155) treated MESA 6.2.8/6.3.7 as "MESA-added sub-overalls EFPA lacks" and offered them as
> optional cuts. Verified against the source: **EFPA does have them** — 6.2.14 (`:832`) and
> 6.3.10 (`:876`), and also 6.1.8 (`:767`). Cutting them would be a real EFPA drop with no
> inapplicability reason. Resolution: keep all three as Extended (E5); the optional cut is
> rejected and the feedback's premise corrected here.

### Section 7

| EFPA § | EFPA line ref | MESA § (new) | Disposition | Note |
|---|---|---|---|---|
| 7.1.1 Software design/robustness | `:899` | 7.1.4 | Core | harness/scorer quality; anchor tiered (F-20-template-s07-1) |
| 7.1.2 Task understandability | `:903` | 7.1.2 | Extended (E5) | asset inventory lives once, in this anchor (F-20-template-s07-1) |
| 7.1.3 Instructions clarity | `:907` | 7.1.3 | Extended (E5) | |
| 7.1.4 Ease of response | `:911` | — | Merged into §7.1.3 | response-format requirements |
| 7.1.5 UI design quality | `:915` | 7.1.5 | Extended (E5) | |
| 7.1.6 Accessibility (differently abled) | `:919` | 7.1.6 | Extended (E5) | evaluand ambiguity fixed (F-20-template-s07-4) |
| 7.1.7 Item content quality | `:924` | — | Merged into §7.1.2 | prompt/material quality |
| 7.1.8 Overall: technology materials | `:928` | 7.1.8 | Core | |
| 7.2.1 Look and feel (paper) | `:941` | — | Dropped | no paper-and-pencil administration of AI benchmarks; EFPA itself marks 7.2 skippable (`:937`); every function has a 7.1.x digital twin |
| 7.2.2 Task understandability (paper) | `:945` | — | Dropped | as 7.2.1 |
| 7.2.3 Instructions (paper) | `:949` | — | Dropped | as 7.2.1 |
| 7.2.4 Ease of response (paper) | `:953` | — | Dropped | as 7.2.1 |
| 7.2.5 Accessibility (paper) | `:957` | — | Dropped | as 7.2.1 |
| 7.2.6 Item content quality (paper) | `:961` | — | Dropped | as 7.2.1 |
| 7.2.7 Overall: paper materials | `:965` | — | Dropped | as 7.2.1 |
| 7.3 Reviewers' comments | `:970` | §7 comments | Core | |

### Section 8

| EFPA § | EFPA line ref | MESA § (new) | Disposition | Note |
|---|---|---|---|---|
| 8.1 Norm-referenced interpretation | `:1083` | 8.1.3 | Core | the model comparator cohort is the direct analog of the norm group |
| 8.1.1 Appropriateness for local use | `:1087` | — | Merged into §8.1.6 | local-population relevance generalizes to reference-group relevance |
| 8.1.2 Representativeness of norm samples | `:1102` | 8.1.6 | Extended (E3/E5) | the Leaderboard Illusion concern lives here |
| 8.1.3.1 Sample sizes (classical) | `:1119` | — | Merged into §8.1.2/8.1.3 + §9.2.2 | cohort size and uncertainty become anchor elements |
| 8.1.3.2 Continuous norming | `:1132` | — | Dropped | age/ability-continuum norming assumes human demographic covariates AI evaluands lack; the uncertainty function survives at 9.2.2 |
| 8.1.3.3 Continuous norming model quality | `:1145` | — | Dropped | as 8.1.3.2 |
| 8.1.4 Sample selection procedures | `:1164` | — | Merged into §8.1.2/8.1.6 | sampling/qualification anchor elements |
| 8.2 Criterion-referenced interpretation | `:1191` | — | Merged into §8.1.5 | |
| 8.2.1 Domain-referenced norming (expert) | `:1195` | 8.1.5 | Extended (thresholds/bands) | |
| 8.2.2 Criterion-referenced norming (empirical) | `:1244` | — | Merged into §8.1.5 + §10.4.3 | empirical criterion linkage rated as validity evidence |
| 8.3.1 Norms up to date | `:1253` | 8.1.7 | Extended (E5) | currency |
| 8.3.2 Acceptable norms provided (+ 8.3.2.1 `:1283`) | `:1279` | — | Merged into §8.2 | the no-reference-point case is carried by 0/1 rating semantics at the overall |
| 8.3.2.2 No norms provided | `:1300` | — | Merged into §8.2 | |
| 8.3.2.3 Fair use of tests | `:1306` | — | Merged into §11 | fairness lens on reference use |
| 8.3.3 Overall rating of the norms | `:1312` | 8.2 | Core | |
| §8 Reviewers' comments | `:1332` | §8 comments | Core | |

### Section 9

| EFPA § | EFPA line ref | MESA § (new) | Disposition | Note |
|---|---|---|---|---|
| 9.1 Data provided about reliability | `:1572` | 9.1.1 | Core | demoted to inventory role; 9.6 collision resolved (F-20-template-s09-1) |
| 9.2 Internal consistency (head) | `:1586` | — | Merged into §9.2.2 | the "how precise is the aggregate" function survives as score uncertainty |
| 9.2.1 Sample size | `:1591` | — | Dropped | coefficient machinery assumes a population of human test takers as the replication unit; MESA replicates over runs/seeds (9.2.1-9.2.2) and item structure (10.2.2) |
| 9.2.2 Kind of coefficients | `:1600` | — | Dropped | as 9.2.1 |
| 9.2.3 Size of coefficients | `:1612` | — | Dropped | as 9.2.1 (alpha thresholds are meaningless without person samples) |
| 9.2.4 Samples coefficients reported with | `:1623` | — | Dropped | as 9.2.1 |
| 9.3 Test-retest (head) | `:1636` | — | Merged into §9.2.1 | temporal stability of a stochastic system = repeated runs |
| 9.3.1 Sample size (retest) | `:1647` | — | Dropped | person-sample machinery; run-count reporting survives in 9.2.1's anchor |
| 9.3.2 Size of coefficients (retest) | `:1656` | — | Dropped | as 9.3.1 |
| 9.3.3 Test-retest interval | `:1667` | — | Merged into §9.4.3 | interval sensitivity becomes environment/dependency drift over time |
| 9.3.4 Coefficients match intended takers | `:1675` | — | Dropped | no human populations; cohort matching survives at §8.1.3 |
| 9.4 Equivalence/parallel forms (head) | `:1688` | — | Merged into §9.4.2 | form/split/version equivalence |
| 9.4.1 Sample size (forms) | `:1690` | — | Dropped | as 9.2.1 |
| 9.4.2 Size of coefficients (forms) | `:1699` | — | Dropped | as 9.2.1 |
| 9.4.3 Coefficients match intended takers | `:1710` | — | Dropped | as 9.3.4 |
| 9.5 IRT-based methods (head) | `:1723` | — | Dropped | latent-trait scaling over person samples has no AI counterpart; item difficulty/discrimination evidence survives at §6.1.7 and §10.2.2 |
| 9.5.1 Sample size (IRT) | `:1725` | — | Dropped | as 9.5 |
| 9.5.2 Kind of indicators (IRT) | `:1736` | — | Dropped | as 9.5 |
| 9.5.3 Size of coefficients (IRT) | `:1747` | — | Dropped | as 9.5 |
| 9.6 Inter-rater reliability (head) | `:1764` | — | Merged into §9.3 | scorer/judge/parser/rater reliability sub-section |
| 9.6.1 Study quality (IRA/IRR) | `:1768` | 9.3.2 | Extended (human raters) | |
| 9.6.2 Kind of coefficients (IRR) | `:1780` | — | Merged into §9.3.2 | anchor element |
| 9.6.3 Size of coefficients (IRR) | `:1788` | — | Merged into §9.3.2 | anchor element |
| 9.7 Other methods (head) | `:1801` | — | Merged into §9.1.1 | inventory records any additional evidence |
| 9.7.1 Sample size (other) | `:1805` | — | Merged into §9.1.1 | |
| 9.7.2 Describe method (other) | `:1819` | — | Merged into §9.1.1 | |
| 9.7.3 Results (other) | `:1823` | — | Merged into §9.1.1 | |
| 9.8 Overall adequacy | `:1836` | 9.6 | Core | |
| §9 Reviewers' comments | `:1855` | §9 comments | Core | |

### Section 10

| EFPA § | EFPA line ref | MESA § (new) | Disposition | Note |
|---|---|---|---|---|
| 10.1 Evidence based on content | `:1992` | 10.1.1 | Core | anchor tiered core/supporting (F-20-template-s10b-2) |
| 10.2.1 Designs/techniques (structure) | `:2000` | 10.2.1 | Extended (subscores/E5) | |
| 10.2.2 Factor-analysis support | `:2012` | — | Merged into §10.2.1 | factor-analytic machinery generalized to structure evidence |
| 10.2.3 Invariance / DIF | `:2023` | — | Merged into §11.4.1 | differential functioning across groups/contexts |
| 10.3.1.1 Designs/techniques (relations) | `:2042` | 10.4.1 | Extended (E5) | |
| 10.3.1.2 Group mean differences | `:2055` | — | Merged into §10.4.1 | |
| 10.3.1.3 Correlations with similar constructs | `:2068` | 10.4.2 | Extended (E1/E5) | |
| 10.3.1.4 Discriminant validity | `:2080` | — | Merged into §10.4.2 | |
| 10.3.1.5 MTMM designs | `:2092` | — | Merged into §10.4.2 | MTMM practice absent in AI benchmarking; convergent/discriminant function survives |
| 10.3.1.6 (Quasi)experimental designs | `:2106` | — | Merged into §10.4.1 | |
| 10.3.1.7 Other (describe) | `:2117` | — | Merged into §10.4.1 | |
| 10.3.1.8 Sample sizes | `:2130` | — | Merged into §10.4 anchors | study-quality element |
| 10.3.1.9 Quality of marker instruments | `:2144` | — | Merged into §10.4.1 anchor | |
| 10.3.1.10 Age of validity studies | `:2155` | — | Merged into §10.4 anchors + §8.1.7 | currency element |
| 10.3.1.11 Overall adequacy (relations) | `:2162` | — | Merged into §10.7 | |
| 10.3.2.1 Type of criterion study | `:2175` | 10.4.3 | Extended (E5) | ecological/predictive relevance |
| 10.3.2.2 Sample sizes (criterion) | `:2185` | — | Merged into §10.4.3 anchor | |
| 10.3.2.3 Quality of criterion measures | `:2198` | — | Merged into §10.4.3 anchor | |
| 10.3.2.4 Strength of test-criterion relation | `:2208` | — | Merged into §10.4.3 | |
| 10.3.2.5 Qualitative criterion (diagnostic) | `:2220` | — | Merged into §10.4.3 | |
| 10.3.2.6 Age of criterion studies | `:2232` | — | Merged into §10.4.3 anchor | |
| 10.3.2.7 Criterion evidence overall | `:2239` | — | Merged into §10.7 | |
| 10.4.1 Type of other validity evidence | `:2256` | — | Merged into §10.2.3 + §10.3 | response-process and scoring-pathway evidence |
| 10.4.2 Adequacy of other-source studies | `:2266` | — | Merged into §10.7 | |
| 10.4.3 Results support intended use | `:2279` | — | Merged into §10.6.1 | proportionality of use claims — the MESA home of this question |
| 10.5 Overall evidence validity | `:2290` | 10.7 | Core | |
| §10 Reviewers' comments | `:2305` | §10 comments | Core | |

### Section 11

| EFPA § | EFPA line ref | MESA § (new) | Disposition | Note |
|---|---|---|---|---|
| 11.1.1 Construct relevance across groups | `:2420` | 11.1.1 | Extended (E5) | |
| 11.1.2 Documentation (fair use) | `:2425` | 11.1.2 | Extended (E5) | boundary bullet vs 6.2.6 (F-20-template-s11-3) |
| 11.2 Development — design | `:2430` | 11.2.1 | Extended (E5) | |
| 11.3 Development — piloting and analysis | `:2435` | — | Merged into §11.4.1 + §11.2.2 | DIF-informed selection and coverage |
| 11.4 Reliability (subgroups) | `:2440` | — | Merged into §11.4.2 | |
| 11.5 Validity (subgroups) | `:2445` | — | Merged into §11.4.2 | MESA 11.4.2 carries both EFPA 11.4 and 11.5 |
| 11.6.1 Norm-referenced interpretation fairness | `:2452` | — | Merged into §11.3.1 + §8.1.6 | comparability across systems/conditions |
| 11.6.2 Criterion-referenced fairness | `:2457` | — | Merged into §8.1.5 anchor | EDI in threshold setting |
| 11.7 Reports (fairness) | `:2462` | — | Merged into §12.4.1 | EFPA itself cross-references 12.4 here |
| 11.8 Overall evaluation | `:2467` | 11.6 | Core | |
| §11 Reviewers' comments | `:2476` | §11 comments | Core | |

### Section 12 and Final Evaluation

| EFPA § | EFPA line ref | MESA § (new) | Disposition | Note |
|---|---|---|---|---|
| 12.1 Scope or coverage | `:2492` | 12.1.1 | Extended (E3) | |
| 12.2 Reliability of reports | `:2507` | 12.2.1 | Core | uncertainty/version/condition labeling |
| 12.3 Relevance or validity of reports | `:2519` | 12.3.1 | Core | claim-score linkage |
| 12.4 Fairness / freedom from bias | `:2534` | 12.4.1 | Extended (E3/E5) | |
| 12.5 Acceptability | `:2545` | 12.4.2 | Extended (E3/E5) | absorbs EFPA 6.3.5's stakeholder-communication function |
| 12.6 Level of detail | `:2558` | 12.1.2 | Extended (E3) | |
| 12.7 Overall adequacy (per report) | `:2568` | 12.5 | Core | per-surface iteration restored as a decision rule (F-20-template-s12-1) |
| §12 Reviewers' comments | `:2577` | §12 comments | Core | comments policy normalized (F-20-template-s12-2) |
| Final: Evaluative report | `:2587` | Final Evaluation — Evaluative Report | Core | + hold-fixed-conditions statement, minimum-standard trigger, §6 revisit checkpoint (F-20-template-99-2, F-20-template-partb-2, F-20-template-s06-2) |
| Final: Conclusions | `:2592` | Conclusions | Core | |
| Final: Summary of Ratings | `:2597` | Summary of Ratings | Core | row names regenerated verbatim from section headings (F-20-template-99-3) |
| Part C: Bibliography | `:2611` | Bibliography | Core | EFPA itself + The Leaderboard Illusion added (F-20-template-99-1) |

### MESA-original items (no EFPA ancestor — the adaptation boundary)

| MESA § | Item | Tier | Source/grounding |
|---|---|---|---|
| front matter | reviewed-entity taxonomy; evidence-gap rule; glossary + "run conditions" definition | Core | F-20-template-00-2/4; F-20-template-s08-1; `80-xcut-terminology` |
| pre-§1 | Source Inventory (promoted house convention) | Core | F-80-xcut-consistency-1 |
| 1.3 | Materials, Sources, & Access Tracking | Core | praised as model section (F-20-template-s01 preamble) |
| 2.1 (layer) | CHC capability-domain layer | Core | verified faithful to `A_Definition_of_AGI.md:18-38` |
| 2.18 | Broad-Claim Flags | Core | E1 trigger; screen wording narrowed (Part 2) |
| 3.1 (rows) | failure/refusal/retry handling prompts | Core | "excellent AI-native additions" (F-20-template-s03 preamble) |
| 3.6 | Score Uncertainty and Stability (descriptive screen) | Core | governing sentence fixed (F-20-template-s03-4) |
| 3.7 | Documented Metric Rationale | Extended (E5) | duplicated rows removed (F-20-template-s03-1) |
| 5.2 | Distribution and Access Model | Core | escape-hatch discipline — protect list |
| 5.5 | Dataset and Item Access | Core | BetterBench-grounded (F-20-template-s05 preamble) |
| 5.6 | Provenance and Contamination | Core | deduped vs 5.8 (F-20-template-s05-2) |
| 5.7 | Reproducibility Materials | Core | option clusters merged 22→15 (F-20-template-s05-4) |
| 5.8 | Maintenance and Versioning | Core | deduped rows (F-20-template-s05-2) |
| 6.1.3 | Phenomenon-task-metric-claim chain | Core | Bean et al. framing; anchor tiered (F-20-template-s06-1) |
| 6.2.3 | Documentation of scoring and metrics | Core | no EFPA 6.2 counterpart |
| 6.2.7 | Documentation of maintenance and versioning | Core | BetterBench-derived |
| 7.1.1 | Dataset/task/environment availability | Core | EFPA assumes materials are supplied |
| 7.1.7 | Licensing, use requirements, risk warnings | Extended (E5) | |
| 8.1.1 | Random/chance/floor/ceiling baselines | Core | EFPA has no chance-level norm concept |
| 8.1.4 | Historical, version, benchmark-family comparators | Extended (E4) | |
| 9.2.1 | Run-to-run stability, seeds, sampling | Core | receives EFPA 9.3's merged function |
| 9.2.2 | Score uncertainty / CIs / SEs | Core | receives EFPA 9.2's merged function |
| 9.3.1 | Automated scorer/parser reliability | Extended (parser) | AI-specific extension of EFPA 9.6's rater function |
| 9.3.3 | Model-as-judge reliability | Extended (E2) | as 9.3.1 |
| 9.4.1 | Prompt/instruction/formatting sensitivity | Extended (E5) | |
| 9.4.2 | Form/split/version/refresh equivalence | Extended (E4) | receives EFPA 9.4's merged function |
| 9.4.3 | Execution environment and dependency stability | Extended (env/E5) | |
| 9.5.1 | Meaningfulness of score differences | Core | the paper's quantified-threshold pattern (`paper.tex:224-234`) |
| 10.1.2 | Construct breadth / capability-domain coverage | Extended (E1) | CHC-grounded |
| 10.2.2 | Item/task behavior across score scale | Extended (subscores/E5) | |
| 10.2.3 | Failure modes and error analysis | Extended (E5) | receives EFPA 10.4.1's merged function |
| 10.3.1 | Metric, scorer, aggregation validity | Core | worst anchor rewritten — source-benchmark residue removed (F-20-template-s10b-1) |
| 10.3.2 | Shortcut sensitivity / construct-irrelevant variance | Core | terminology standardized (`80-xcut-terminology`) |
| 10.5.1 | Contamination and leakage controls | Core | the model two-tier anchor — pattern for all anchor surgery |
| 10.5.2 | Gameability and benchmark-specific tuning | Core | |
| 10.6.1 | Claim proportionality (merged 10.6.1+10.6.2) | Core | MESA's signature item; receives EFPA 10.4.3's merged function |
| 11.3.1 | Cross-system comparability (merged 11.3.1+11.3.2) | Core | F-20-template-s11-2; receives EFPA 11.6.1's merged function |
| 11.3.3 | Temporal comparability (rolling/live) | Extended (E4) | "first-class MESA-original item" (F-20-template-s11 preamble) |
| 11.5.1 | Appropriate-use guidance and non-use cases | Core | claims pipeline |
| 11.5.2 | Release rules and sensitive-content handling | Extended (sensitive content/E5) | |
| 12.2.2 | Reproducibility/traceability of reported scores | Extended (E3) | |
| 12.3.2 | Raw outputs / per-item data availability | Extended (E3) | |
| 12.4.3 | Public communication and leaderboard governance | Extended (E3) | anchor self-duplication fixed (F-20-template-s12-3); Leaderboard Illusion cited (F-20-template-99-1) |
| Final | Recommendations (separate heading); Gap Register (multi-row) | Core | Gap Register = "the template's single best MESA-original device" (F-20-template-99 preamble, 99-4) |

### Count

**EFPA rows: 192** (every numbered heading and rated sub-item above) —
**Core 52 · Extended 54 · Merged 63 · Dropped 23.**
Every Merged row names its surviving home; every Dropped row's reason is AI-inapplicability
(paper-and-pencil administration ×7, human-sample coefficient machinery ×10, IRT latent-trait
scaling ×4, continuous norming ×2). MESA-original items: 44 rows in the second table. The
table shows the intended headline: the template gets shorter for the common case (31 Core
ratings instead of 89) while **no EFPA function disappears silently** — 88% of EFPA items
survive as Core, Extended, or a named merge target.

---

## Part 4 — Terminology migration

Executable find-and-replace list from `80-xcut-terminology`, applied **repo-wide** except the
frozen surfaces (Part 5 step 5): `reviews/`, `feedback/`, `literature/`, `Papers/`,
`critique_plan.md`, `dist/` (until regenerated). Files-affected column verified by grep
2026-08-09.

| # | Find (pattern) | Verdict | Replace with | Files affected |
|---|---|---|---|---|
| 1 | `review base` | Substitute | "the specific materials that were actually inspected" | template `:103` only |
| 2 | `capability-area` | Substitute | "capability-domain" | `paper.tex:61` |
| 3 | `execution or contamination bias` | Substitute | "contamination and unstable-implementation artifacts" | `paper.tex:61` |
| 4 | `four-element anchoring model` | Substitute | "a four-element profile" (introduce, then define) | `paper.tex:204` |
| 5 | `requirements object` | Substitute | "requirements-relevant review object" | `paper.tex:142` |
| 6 | `the specific meaning users are supposed to draw from a score` | Substitute (canonicalize) | "the intended score meaning" (bind once at template :11) | template `:11, :19, :1824` |
| 7 | run-conditions formula (`prompts, settings, tools, time limits, access rules, hardware, …`) | Substitute (define once) | "run conditions" + one glossary definition | template ×10 (`:151, :324, :1321, :1347, :1588, :1729, :2249, :2316, :2356, :2360`) |
| 8 | `irrelevant score effects` | Substitute | "score effects from outside the target capability" | template `:11` |
| 9 | `non-target rewarded behavior` | Substitute | "score effects from outside the target capability" (or drop the row per F-20-template-s03-1) | template `:753`; `.codex/memory/template-structure.md:88` |
| 10 | `calibration data for scoring by another model` | Split (sense 2) | "tuning data for model-based scorers" | template `:1135` |
| 11 | `calibration campaign` | Split (sense 3) | "human difficulty-norming campaign" | `paper.tex:222` |
| 12 | entity-list variants (`rolling version(s)`, `hosted suite`, `derived variant`, bare `harness` as entity type) | Substitute (canonicalize) | one canonical list at template :13; elsewhere "any reviewed entity listed in the front matter". Standard labels: **evaluation slice, rolling cohort, suite component** | template `:13, :21, :119, :1259`; `.claude/agents/benchmark-reviewer.md:27`; `.codex/agents/benchmark-reviewer.md:22`; `.codex/agents/benchmark-reviewer.toml:25` |
| 13 | `MESA EFPA Template` (H1), `MESA Review Model` (Figure 1 root) | Substitute (canonicalize) | framework = "the MESA Test Review Model"; document = "the MESA template" | template `:1, :33`; README; mirror |
| 14 | `Supply & Materials` | Substitute | "Access, Materials, and Lifecycle" | `README.md:24` |
| 15 | Summary-of-Ratings row names ≠ section headings | Substitute (regenerate) | verbatim section headings, single source = regenerated mirror | template `:2457-2463`; `paper.tex` Table III `:247-253` |

> **Conflict note.** F-20-template-00-2 recommends "evaluation slice" as the canonical label;
> the `80-xcut-terminology` table row says standardize on "slice". Resolution: **"evaluation
> slice"** in the canonical list and at first use (self-describing), "slice" permitted as
> shorthand after first use. Recorded as a deviation from the xcut row.

**Keep + define — the glossary (exactly these 10 entries, wording already drafted in
`80-xcut-terminology`):** construct validity · capability domain · claim proportionality ·
reference interpretation · run conditions · evidence gap · supported-use/non-use statement ·
gameability · model-as-judge · construct-irrelevant variance (10.3.2 heading gloss only).
The glossary is short by design; nothing else is added to it.

Paper-side Keep+define actions ride with step 6: define construct validity at `paper.tex:55`
(F-10-paper-01-2), claim proportionality at `:175` (F-10-paper-04-3), traceability rewrite at
`:59` (F-10-paper-01-3).

---

## Part 5 — Sequenced repo migration plan

Order: 1 → (2 ∥ 3) → 4 → 5 (decision, before 6) → 6 → 7. Estimated total effort:
**5-7 working days**, dominated by step 1.

### Step 1 — Template (`MESA EFPA template official.md`)

- **Nature:** judgment-dependent. **Effort: 2-3 days.** **Breaks if skipped:** everything —
  all other steps implement this one.
- Apply the ten change-packages from `90-synthesis` §2 (interpolation rule; anchor surgery on
  the 12 bloat anchors using 10.5.1's two-tier pattern; run-conditions definition + 10
  substitutions; the merge/dedup batch; Final Evaluation upgrade; General Description + Source
  Inventory promotion; bibliography additions; canonical names; glossary; the terminology list
  in Part 4).
- Add tier markers (`- Tier: Core` / `- Tier: Extended (trigger)`) per Parts 1-2, the Core
  index table in the front matter, and the five Extended block trigger sentences.
- **Numbering:** retire-don't-renumber (see header). Retired IDs (2.6, 4.10, 10.6.2, 11.3.2)
  get one-line tombstones ("merged into §X in v2") so old citations resolve.
- Run the case-study coverage check from Part 1 (evidence-sufficiency caveat) before
  finalizing tier markers.
- Protect list (`90-synthesis` §4) is the review gate for this step: escape-hatch discipline,
  2.14's documented-estimates rule, 10.5.1's anchor, the reference-kind typology (:1547), the
  anti-difficulty rule (:1932), :1747 and :2322, the Gap Register, n/a-0-1 semantics.

### Step 2 — Agent / skill assets

- **Files:** `.claude/agents/benchmark-reviewer.md`, `.claude/skills/review-benchmark/SKILL.md`,
  `.codex/agents/benchmark-reviewer.md`, `.codex/agents/benchmark-reviewer.toml` (all verified
  present). **Nature:** mostly mechanical. **Effort: 2-4 h.**
- Update: entity-type list (currently "rolling versions" in all three agent files — Part 4
  row 12), section names, Part A/Part B output conventions, and add the tier system (a MESA
  review request must state Core or full; default Core unless a trigger forces more).
- **Breaks if skipped:** new reviews are silently produced against the v1 structure — the
  exact failure F-80-xcut-consistency-4 warns about.

### Step 3 — Agent memory

- **Files:** `.codex/memory/template-structure.md` (regenerate **from** the v2 template — it
  is a self-declared mirror whose numbering is load-bearing; never hand-patch),
  `.codex/memory/source-checklist.md` (remap source types → new destinations: score inventory
  now 3.2-only, audience now 2.4-only, General Description home), `.codex/memory/research-method.md`
  (check references to section numbers). **Nature:** mechanical regeneration + short review.
  **Effort: 2-3 h.**
- Make the regenerated mirror the declared name authority for section names
  (F-80-xcut-consistency-4); README/paper tables are regenerated from it in step 6.
- **Breaks if skipped:** agents trust a stale mirror that *declares itself* authoritative —
  worse than no mirror.

### Step 4 — Website (`assets/mesa-form.js`, `assets/mesa-pdf.js`, `index.html`)

- **Nature:** decision + smoke test; no code change required. **Effort: 1-2 h.**
- The form parses the template at load (`assets/mesa-form.js:19`); the plan's structural
  changes all stay inside the authoring conventions at `assets/mesa-form.js:6-14` (tier
  bullets are prose; retitles are ID-safe because IDs derive from numeric prefixes,
  `:90-95`; added checkbox options/rows are first-class fields). Smoke test after step 1:
  load the form, confirm item counts per section match the v2 template and no field vanished.
- **Storage key decision (explicit, as required): bump `STORAGE_KEY` to
  `"mesa-form-answers-v2"` (`assets/mesa-form.js:20`).** Rationale: control IDs embed
  label slugs (`:227-229, :266`), so the many label rewrites (2.12 definitions, 4.4 labels,
  5.6/5.8 row merges) would orphan answers piecemeal even with numbering preserved; a
  half-loaded saved review is worse than a clean break. *Assumption flagged:* the pilot has
  no external users with in-progress saved reviews — if that is wrong, add a one-time export
  prompt before switching keys.
- Optional, separately scheduled parser enhancement (not required for v2): a Core/Full toggle
  that reads the tier bullets. Until then the Core index table serves human navigation.
- **Breaks if skipped:** silent item loss in the live form (convention drift) or
  corrupt-looking half-orphaned saved reviews.

### Step 5 — Case studies (`reviews/` — 9 files, ~12,000 lines)

- **Decision: freeze all nine with a version stamp.** Add one line under each title:
  *"Reviewed against MESA template v1 (pre-Core, 89 items), 2025-2026. Section numbers cite
  v1; see `feedback/95-mesa-core-plan.md` Part 3 for the v1→v2 mapping."* **Nature:**
  mechanical. **Effort: ~1 h.**
- Costs of the alternatives, stated honestly: migrating all nine means re-adjudicating every
  rating touched by a merge (10.6, 11.3, 2.6/2.9, 2.4/4.10, 5.6/5.8 rows) across ~12,000
  lines — judgment work, **≈ 30-50 h**, and it would rewrite the evidence the paper cites.
  Migrating only the three `gemini_supervising_editor/` finals (**≈ 12-20 h**) breaks
  reviewer-draft ↔ final traceability, which is the pipeline's whole point. The reviews are
  dated evidence, not living documents; freezing is cheapest **and** most honest.
- **Breaks if skipped:** Part 6's greps never run clean, and readers assume the reviews match
  the current template.

### Step 6 — Paper and docs (`paper.tex`, `README.md`, thesis PDF)

- **Nature:** judgment-dependent editing. **Effort: 1-2 days** (folds in the camera-ready
  pass, `90-synthesis` §2 #10).
- §IV (`paper.tex:140-189`): regenerate Table II row names from the mirror; add the 2/3/4
  rating meanings (F-10-paper-04-2); fix the claim-proportionality gloss (F-10-paper-04-3)
  and the averaging attribution (F-10-paper-04-4). After the dedup batch, the :180 coherence
  defense becomes *true* — cite it as the acceptance criterion met (F-10-paper-04-1). :177's
  hold-fixed list now exists in the template (F-20-template-99-2 lands it).
- Add one paragraph to §IV or Future Work presenting the Core/Extended tiers as the compact
  scorecard `paper.tex:307` already promises — the paper must describe the artifact that
  exists (the axis-7 rule).
- Remaining camera-ready items: PTB citation (F-10-paper-02-1), III-A/III-B dedup
  (F-10-paper-03-1), 15-benchmark procedure statement (F-10-paper-03-2), External Validity
  rewrite (F-10-paper-08-1), abstract fixes (F-10-paper-00-1/2/4), RQ1/RQ3 markers
  (F-10-paper-07-1), Table III names (F-10-paper-06-1).
- README: section list regenerated from the mirror; "Supply & Materials" fixed (Part 4 #14);
  phase list updated to name the two-tier structure.
- **`MESA___Thesis___Vitor_Brandao_Raposo.pdf` must be recompiled by the user** — this plan
  and its executors do not compile LaTeX (`CLAUDE.md`).
- **Breaks if skipped:** the paper describes a template that no longer exists — its artifact
  claim becomes false, the exact inverse-drift F-20-template-99-2 documents.

### Step 7 — Generated export (`dist/hf_mesa_dataset/`, untracked)

- **Nature:** manual, flagged. **Effort: 1-2 h when performed.** No build script exists in the
  repo; regeneration is done **by the user** (repository owner) by hand.
- Because step 5 freezes the reviews at v1, the dataset stays keyed to v1: add a version note
  to its README rather than regenerating schemas now. Regenerate `schema/*.schema.json` and
  the data files only when a first v2 review exists.
- **Breaks if skipped:** the HF export silently claims to represent current MESA while keyed
  to v1 fields — flagged instead by the version note.

---

## Part 6 — Consistency check

Run after steps 1-6; expected result for every command: **zero hits** outside the frozen
surfaces. Standard exclusions: `feedback/`, `reviews/`, `literature/`, `Papers/`, `dist/`,
`critique_plan.md` (plus `.git/`). Commands as run from the repo root (Git Bash / ripgrep):

```bash
EX=(-g '!feedback/**' -g '!reviews/**' -g '!literature/**' -g '!Papers/**' -g '!dist/**' -g '!critique_plan.md')

# Substituted / retired terms (Part 4 rows 1-11)
rg -n "${EX[@]}" "review base|capability-area|execution bias|four-element anchoring model|requirements object"
rg -n "${EX[@]}" "irrelevant score effects|non-target rewarded behavior"
rg -n "${EX[@]}" "specific meaning users are supposed to draw"
rg -n "${EX[@]}" "calibration data for scoring|calibration campaign"

# Run-conditions formula: exactly ONE hit allowed — the glossary definition
rg -n "${EX[@]}" "prompts, settings, tools, time limits"

# Entity-taxonomy variants (Part 4 row 12)
rg -n "${EX[@]}" "rolling version|hosted suite|derived variant"

# Framework/section naming (Part 4 rows 13-14)
rg -n "${EX[@]}" "MESA EFPA Template|MESA Review Model"
rg -n "${EX[@]}" "Supply & Materials"

# Retired item IDs — only tombstone lines in the template may match
rg -n "${EX[@]}" "\b(4\.10|10\.6\.2|11\.3\.2)\b"
rg -n "${EX[@]}" "\b2\.6\b" "MESA EFPA template official.md" .claude .codex assets README.md paper.tex

# Old Summary-of-Ratings row names (drift origin, F-20-template-99-3)
rg -n "${EX[@]}" "Reference points and documented comparison groups|Validity support"

# Tier-marker integrity: every rated item carries exactly one Tier bullet
rg -c "^- Tier: (Core|Extended)" "MESA EFPA template official.md"   # must equal the rated-item count (84)
rg -n "Rating: \[n/a" "MESA EFPA template official.md" | wc -l      # cross-check: also 84
```

Acceptance: all substitution greps zero; the run-conditions grep exactly 1; the retired-ID
greps match only tombstones; the two tier counts equal each other and the v2 item count.
Finally, reload the live form and confirm per-section field counts against the v2 template
(step 4 smoke test).

---

## Success check

The success condition is visible in Part 3's close: 192 EFPA rows, none silently dropped —
52 Core, 54 Extended, 63 with a named merge home, 23 dropped for stated AI-inapplicability
reasons only. A reviewer completes 31 ratings instead of 89 in the common case, in 8-12 hours
instead of a working week, and every removed or deferred item is either recoverable through a
trigger or traceable to the line of EFPA it came from. The trim makes MESA shorter without
making it less faithful — and where the feedback could not support a cut (6.1.8/6.2.14/6.3.10,
the item-grain Core membership pending the case-study check), this plan says so rather than
cutting.
