## Summary Assessment of Iteration 1 Changes

**The statistical controls pass. The requested metadata corrections pass. Literature provenance still requires revision.**

I inspected the code and all 576 saved parameter cells, then replayed the sweep with seed 42 and 2,000 trials per cell. All 576 result records matched the saved JSON. Output writes were intercepted in memory; no repository files were changed.

The four search files disclose reconstruction and withdraw unsupported hit totals. However, three excluded candidates remain without source identifiers or evidence supporting their screening decisions.

## Detailed Findings on Statistical Controls (Coverage & Sampling Mechanics)

| Audit question | Finding | Assessment |
|---|---|---|
| Does Control 1 sample only decisive M2 cases? | Lines 95–102 construct `decisive_m2_indices` using `dec != "Unresolved"` and sample exactly `k_m3` indices without replacement. | **PASS** |
| Does Control 2 use the same eligible pool? | Lines 104–108 sort only decisive M2 indices by distance from the threshold and retain exactly `k_m3`. | **PASS** |
| Is coverage equal across all 576 cells? | All 576 parameter combinations occur once. There are zero coverage mismatches between M3 and either control. | **PASS** |
| Is equality enforced at runtime? | Lines 110–116 count decisions before rounding and raise `RuntimeError` on any discrepancy. These checks remain active under Python optimization. | **PASS** |
| Do saved results match execution? | The replay reproduced every cell’s parameters and outcomes. | **PASS** |

The mechanics establish exact equality:

- M3 either retains M2’s decision or changes it to `Unresolved`.
- Therefore, M3’s decisive cases are a subset of M2’s decisive cases.
- Each control retains exactly the number of decisive cases retained by M3.
- All methods divide that count by the same trial count.

Thus, equality holds before serialization; it is not an artifact of rounding. Saved M3 coverage ranges from **0.034 to 0.1445**.

Control 2’s tie handling is disclosed: sorting preserves trial order when distances match. Control 1 uses one random selection per cell. These choices satisfy the coverage comparison, but a single seed does not quantify Monte Carlo uncertainty. The sweep supports conclusions about the assumed gate mechanics, not human review performance.

Evidence: [simulation code](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/paper2/protocol/simulate_detector_sensitivity.py:90).

## Detailed Findings on Literature Provenance & Metadata

### Reconstruction labels and withdrawn totals

**PASS for all four files.** Each contains:

- `record_type: "reconstructed_search_notes"`
- `reconstruction_date: "2026-11-05"`
- `total_results: null`
- A note stating that synthetic totals were withdrawn.

The search log and screening register also disclose reconstruction. The totals reconcile arithmetically: **14 query candidates plus five baseline records equals 19 records; 15 included plus four excluded equals 19.**

These are counts of register entries. They do not establish database hit totals or search completeness.

### DOI and publication metadata

| Record | Verification | Assessment |
|---|---|---|
| Singh & Kaewprapha (2026) | The publisher confirms Vishakha Singh and Phisan Kaewprapha, the recorded title, *Applied Sciences* **16(21), 10447**, and DOI **10.3390/app162110447**. [Publisher record](https://www.mdpi.com/2076-3417/16/21/10447) | **PASS** |
| Evaluation Cards | The JSON’s 48 author names and their order match arXiv v2, including “Wm. Matthew Kennedy” and “Mykel Kochenderfer.” The title, DOI, year, and designation as an arXiv preprint match. No conference or journal venue is established by that record. [arXiv v2](https://arxiv.org/abs/2606.09809v2) | **PASS** |
| Beyond the Hype | Eneko Pizarro, Maider Azanza, and Beatriz Pérez Lamancha match the publisher record, as do the title, *Science of Computer Programming*, volume **254**, article **103530**, and DOI **10.1016/j.scico.2026.103530**. [Publisher record](https://www.sciencedirect.com/science/article/pii/S0167642326000961) | **PASS** |

### Remaining provenance issues

**1. Three exclusions remain unverified.** The Habli, Troubitsyna, and Burton candidates lack DOI, repository identifier, source URL, or source snapshot. Searches for their recorded titles did not locate matching source records during this audit. That does not prove nonexistence, but their identity and exclusion rationales remain unverified. They should not yet count as confirmed screened publications.

**2. Reconstruction does not establish retrieval history.** The log asserts retrieval on 3–4 November, but the inspected records do not preserve database responses, execution timestamps, pagination, or the basis for selecting candidates. They support a reconstructed candidate register, not reproduction of the original search.

**3. Screening rules need clarification.** Criterion 3 excludes conceptual or secondary work, while Hou et al. is retained as a survey. Baseline inclusion may explain this, but the exception needs to be stated. “Superseded by” another paper also needs a selection rule; it does not by itself establish exclusion.

Evidence: [search log](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/literature/slr-extension-2026-11/search-log.md:39), [screening decisions](/Users/mylittlefoxxie/Desktop/MESA-meta-evaluation-standard-for-ai/literature/slr-extension-2026-11/screening-decisions.md:38).

## Concrete Actionable Recommendations

1. Verify the three unresolved candidate identities and attach source evidence. Otherwise, preserve them as unverified reconstruction entries and revise the confirmed screening counts.
2. Distinguish recorded retrieval dates from dates supported by retained evidence. State which parts of the search history cannot be recovered.
3. Explain baseline exceptions and replace “superseded by” rationales with decisions tied to stated criteria.
4. For later statistical reporting, retain decision counts and quantify Monte Carlo uncertainty if making claims about performance differences.

No correction to the control sampling or coverage enforcement is required.

## Iteration 1 Verdict: **REVISION REQUIRED**

The statistical controls and requested publication metadata pass. Approval of literature record integrity remains pending verification or reclassification of the three excluded candidates and clarification of the search provenance claims.