# CHASE v2 study preparation

Prepared 29 October 2026. **Draft, not frozen and not executed.** This folder supports [paper_chase_v2.tex](../../../../paper_chase_v2.tex). The earlier model study remains in [CHASE-study.md](../../../../CHASE-study.md); none of its results is relabelled as a result of this design.

## Prepared

- An exact snapshot of participant packet 2.9, including the 25 questions, choices, explanations, definitions, benchmark readings and HLE teaching example: [packet](materials/packet-2.9.json).
- [24 fictional cases](materials/fictional-cases.json), with [proposed reference answers](analyst/fictional-reference-draft.json) stored separately. These have not been tested or checked by the author.
- A [50-entry real reference register](analyst/real-reference-register.json), one entry per question and benchmark. All 50 summary choices now have draft reasons and alternatives where relevant; 30 are flagged as contested. Original-passage choices remain unset. None has author approval. See the [reference review](analyst/reference-review.md).
- A [14-paragraph summary audit register](analyst/summary-audit.json), preserving text and its declared source IDs. Source checks have started. The [source audit](analyst/source-audit-findings.md) records conflicts in DesignQA tables and qualifications in ARC sources. This is not a completed audit.
- A [30-session schedule](preparation/schedule.json), using a recorded rotation rather than randomisation.
- [Condition definitions](preparation/conditions.json), [response schema](preparation/response-schema.json) and [protocol draft](protocol-draft.md).
- [Packet and protected-file hashes](preparation/source-snapshot.json). These identify inputs and preservation checks, not a protocol freeze.

## Conditions and size

| Condition | Question explanations | Benchmark reading |
| --- | --- | --- |
| A | Absent; shared choice definitions and general rules retained | Existing survey summary |
| B | Present | Existing survey summary |
| C | Present | Selected original passages, not yet prepared |

All conditions receive the same HLE example. A versus B measures the additional question explanations and definitions given that example. B versus C examines the reading material. B is reused across the two studies.

For each of Luna and Terra: six fictional-case sessions (A/B, three each) and nine real-benchmark sessions (A/B/C, three each). Total: 30 proposed sessions. No sessions have run. Model availability and the ability to isolate reviewers from project records must be checked before execution.

## Work required before execution

1. Read and record original passages from the dated benchmark sources, including relevant software. Complete the original-passage packet; selection itself can introduce bias.
2. Complete the two reference answers for each real question, keeping alternatives and unresolved items. Audit summary omissions and answer cues.
3. Check tables, diagrams and images as well as paragraphs. The copied packet contains those elements. A text-only projection has not been prepared or validated, and must not be called an exact reproduction of the human reading experience.
4. Have the author check fictional labels and real references. Pay attention to Q20's “any claim” wording versus the whole-condition answer rule and Q22's “repeat ... or examine” wording. Resolve or flag these interpretations before seeing outputs, without rewriting the live questionnaire.
5. Complete input assembly and isolation checks, and review the [analysis rules](analysis-plan.md) and saved execution schedule. Reviewers must not have access to `analyst/`, this README or project history.
6. Freeze the checked version and record the freeze time before collecting responses. Retain a separate version for any later correction.

The questionnaire and live survey were not changed. Human responses are not required to finish the CHASE model study. The existing survey will be Study 3 in the later extension; this folder does not retrieve or contain participant responses.

## Case revisions

The task was briefly reduced to ten cases, then restored to all 24 at the user’s request before execution. See the [revision record](preparation/case-selection.md). Both drafts are archived; the active design uses 24 cases and 30 sessions across both models.
