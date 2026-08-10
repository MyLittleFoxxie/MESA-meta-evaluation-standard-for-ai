# Feedback — `20-template-s07-materials` (`MESA EFPA template official.md:1383-1468`)

Unit reviewed: Section 7 — five preamble paragraphs (:1385-1393), section-level rating guidance
table (:1395-1403, present and consistent with Section 6's — good), and 7.1 with 8 rated items
(7.1.1-7.1.8).

The section's content is well chosen: the BetterBench-informed usable-resources framing
(:1387), the controlled-access-can-rate-well principle, and items 7.1.3/7.1.5 (parsing rules,
workflow usability) cover material AI-benchmark failure modes EFPA never contemplated. The
problems are concentration: five preamble paragraphs where three would do, and the template's
single clearest case of preamble-vs-anchor duplication. Parser check: all 8 items conventional;
"Reviewer comments:" (:1465) parses as intended. No form loss.

---

### F-20-template-s07-1 — [Major] The preamble's 18-item materials list is restated in the 7.1.2 anchor — the classic preamble/anchor duplication, plus anchor bloat
- **Axis:** repetition (with the s06-1 element-bloat pattern)
- **Where:** `MESA EFPA template official.md:1391` (preamble) vs `:1420` (7.1.2 anchor); also `:1434` (7.1.4)
- **Quote:** > They also include system prompts, task environments, Docker images, filesystem snapshots, tool/API configuration, simulator state, user simulators, GUI screenshot assets, video assets, document images or PDFs, layout annotations, dependency versions, scoring scripts, judge prompts, rubrics, examples, failure handling, and any infrastructure needed to produce comparable scores. *(:1391 — 18 items)* — vs — > Excellent: Prompts, task instructions, examples, system messages, input files, context windows, multimodal assets, GUI screenshot assets, video assets, document images or PDFs, layout annotations, filesystem or simulator state, and any hidden or private instructions are documented or controlled... *(:1420 — 13 items, ~8 shared)*
- **Why it fails a user:** The reviewer reads the same asset inventory twice within forty lines, and neither statement is authoritative — the preamble list has Docker images and judge prompts that the anchor lacks; the anchor has context windows the preamble lacks. Under Excellent-only anchoring, 7.1.2's 13 co-equal elements and 7.1.4's 12 ("runnable or auditable...tested, robust...version-pinned...smoke tests or CI...replication script") reproduce the s06-1 discrimination problem at the section's two most-used items.
- **Fix:** Preamble (:1391) shrinks to the principle: "For interactive, tool-use, multimodal, or environment-based benchmarks, materials include the full execution infrastructure needed to produce comparable scores, not only item text." The asset inventory lives once, in 7.1.2's anchor, trimmed to core-plus-supporting per the s06-1 pattern (core: prompts and instructions, multimodal assets, environment/simulator state, hidden-instruction handling; supporting: the rest). Same surgery for 7.1.4 (core: runnable/auditable route, error robustness, version pinning, replication example).
- **EFPA link:** EFPA §7 test-materials quality — retained function; both the duplication and the element inflation are MESA-original.

### F-20-template-s07-2 — [Minor] :1389 and :1393 state the controlled-access principle twice
- **Axis:** repetition
- **Where:** `MESA EFPA template official.md:1389` and `:1393`
- **Quote:** > A benchmark with controlled access can rate well when the controls are justified and reviewers can inspect enough information to judge quality. *(:1389)* — vs — > Hosted or private materials can rate well when access control is justified, the controlled audit route is documented, and enough evidence is available for reviewers to inspect, run, score, reproduce, or audit the benchmark within its stated access model. *(:1393)*
- **Why it fails a user:** The same rule — justified controls + inspectable evidence → can rate well — twice in one preamble, with :1393 adding only "documented audit route". Forty-five words of re-reading before the first item.
- **Fix:** Delete :1393; move "the controlled audit route is documented" into :1389's sentence: "...when the controls are justified, the audit route is documented, and reviewers can inspect enough information to judge quality."
- **EFPA link:** MESA-original principle (EFPA assumes publisher-supplied materials); function survives in the merged sentence.

### F-20-template-s07-3 — [Minor] No EFPA-mapping sentence — Section 6 set the pattern, Section 7 drops it
- **Axis:** EFPA traceability
- **Where:** `MESA EFPA template official.md:1385`
- **Quote:** > MESA evaluates benchmark materials needed to inspect, run, score, reproduce, or audit the evaluation...
- **Why it fails a user:** Section 6 opens "EFPA Section 6 asks whether... MESA asks whether..." — making the adaptation auditable in place. Section 7's preamble never mentions EFPA, so a reader cannot tell whether this section adapts EFPA §7 (it does — quality and usability of test materials) or is MESA-original. Inconsistent traceability is worse than absent traceability: it implies the unmarked sections are original.
- **Fix:** Open with: "EFPA Section 7 asks whether the test materials are well designed and usable; MESA asks the same of datasets, prompts, rubrics, scoring code, harnesses, and access routes." Then the existing text follows.
- **EFPA link:** EFPA §7 — retained but invisible; this finding is about making the link visible.

### F-20-template-s07-4 — [Minor] 7.1.6 half-ports a human-accessibility item without saying whose accessibility
- **Axis:** vagueness
- **Where:** `MESA EFPA template official.md:1448`
- **Quote:** > Excellent: Benchmark materials and workflows are usable by design for relevant modalities, languages, deployment modes, API or local systems, and assistive or alternate interaction needs, with justified adaptations when usability is limited.
- **Why it fails a user:** "Modalities, languages, deployment modes" concern the evaluated AI system; "assistive or alternate interaction needs" is EFPA's human test-taker accessibility concept, which in MESA's setting can only mean the human operator. The anchor never says which evaluand it means, so one reviewer rates system coverage while another rates researcher ergonomics — different ratings from the same evidence.
- **Fix:** Split the sentence by evaluand: "Excellent: Materials support the benchmark's relevant modalities, languages, and deployment modes (API or local) for evaluated systems; and the human operator workflow is usable without specialized tooling, with justified adaptations where either is limited."
- **EFPA link:** EFPA §7 accessibility (test-taker-facing) — drifted: the object of accessibility changed but the wording did not.

---

## Verdict
- **Disposition:** Trim
- **Items:** 8 rated → 8 (preamble 5 paragraphs → 3; ≈ −110 words with the anchor trims)
- **Rationale:** The right items with the right AI-specific scope, wrapped in a preamble that says the access rule twice and the asset inventory twice; the fixes are deletions and one traceability sentence, not redesign.
