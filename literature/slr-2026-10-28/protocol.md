# Review protocol v1

Frozen on 28 October 2026 before new search screening. The assistant and author had already read the seven seeds and discussed MESA; this is not a blind or prospectively registered review. The protocol file is hashed in `protocol-freeze.json`. Amendments must be separate and dated.

## Purpose

Establish context for MESA before changing its questions, manuscripts, experiments, or survey. Examine existing review methods and evidence about their use; do not assume MESA fills a gap.

## Questions

1. What concerns and procedures are proposed for reviewing AI benchmarks?
2. How do approaches explain concepts, guide judgments, and handle missing information?
3. What evidence concerns use by reviewers, including people without AI or measurement expertise?
4. What remains unresolved, and what is already addressed?

## Eligibility

Include English full texts first published between 2023-10-28 and 2026-10-28 that propose, assess, or provide evidence relevant to benchmark review. Include frameworks, checklists, measurement arguments, audits of evaluation practices, and studies of reviewer use. Distinguish empirical research, conceptual proposals, and standards. Include preprints with their status stated.

Include the seven requested seeds. The AERA/APA/NCME 2014 Standards are an explicit foundation exception and are counted separately. Older cited sources may explain concepts but are not counted as recent included studies. Date eligibility uses first public release of a work, not a later revision; document uncertain dates. A seed outside the window remains a foundation record rather than a recent study.

Exclude benchmark introductions or model score reports without a contribution to review methods or evaluation findings; unrelated meanings of benchmark or accessibility; non-English full texts; and records outside the date window except the stated foundation exception. Inaccessible or insufficiently inspected full texts remain unresolved, not included by abstract inference.

## Discovery

Search OpenAlex, Crossref, and arXiv using these exact text queries, adapted to each service's syntax:

- Q1: `AI benchmark quality review framework`
- Q2: `language model benchmark validity reliability fairness`
- Q3: `AI evaluation checklist guidance reproducibility`
- Q4: `benchmark review accessibility usability comprehension effort`

Query each service for up to its first 50 relevance-ranked results per query, with the date window where supported. This is a bounded search, not exhaustive database coverage. Retain every returned record, including out-of-scope records. Record total hits when provided; do not present total hits as screened records. Deduplicate returned records before screening by DOI/arXiv ID, then normalized title and author inspection. Keep preprint and publication identifiers together and document any version differences relevant to claims.

If a service fails or requires credentials, retain the response and attempt a web search restricted to its domain using the same query. Record this as a fallback, not equivalent database access. Supplement discovery with official publisher and institutional searches to verify seeds and obtain texts. Log exact requests, timestamps, result URLs, and access outcomes. Preserve raw responses where possible. Search ranking, service coverage, and fallback retrieval limit reproducibility.

## Citation search

One backward and one forward round from each of the seven seeds. Inspect seed reference lists for potentially eligible work and use an available citation index for citing works. If index access fails or a seed has no match, use exact-title web searches and record these as incomplete forward searches. Do not recurse from newly included studies. Log all selected candidate references and reasons, the reference-list sections inspected, citation index coverage, and unresolved retrieval. Apply the same eligibility rules. Source verification searches are not additional citation rounds.

## Screening and extraction

One assistant performs title/abstract screening followed by full-text assessment. No independent reviewer or agreement statistic is claimed. Record one final status per work: included_recent, included_foundation, excluded, or unresolved. Preserve a reason and discovery links. A human author must review decisions and gap claims before manuscript use; this review has not yet occurred.

Extract publication/version, source type, purpose, intended readers and assumed expertise, concepts and terminology, criteria and answer formats, guidance, missing information versus problems, testing versus outcomes, accessibility provisions, actual understanding/effort measurements, evaluation design and findings, and limitations. Every claim has page/section locators. Use `not reported in inspected sections` rather than claiming a procedure did not occur. Distinguish author recommendations, empirical observations, and assistant interpretations.

Assess standards by authority, scope, and applicability; conceptual work by definitions, reasoning, and support; empirical work by sampling, methods, denominators, controls, and limitations. Do not create a common quality score. Preserve disagreements in terminology and findings.

## Synthesis

Organize by review concerns and activities. Compare OECD terminology without forcing equivalence. Separate benchmark access from reviewer accessibility. For each proposed gap state supporting evidence, counterexamples, limits, uncertainty, and a possible MESA response. Missing retrieved evidence is not proof of field-wide absence. Brevity and agreement do not establish accessibility or correctness.

## Outputs and preservation

Write only within this review folder: protocol and freeze record; request/result logs; deduplicated register and screening decisions; extraction table; source summaries; terminology map; synthesis and candidate implications; limitations and counts; verification script/results. Reference existing sources without rewriting them. Do not alter questionnaires, manuscript files, bibliography, experiments, or participant records. Do not compile LaTeX.

Disclose assistant preparation, search, screening, extraction, and synthesis. Mechanical checks validate counts and paths, not research judgments. Record unfinished access/screening explicitly. No human validation, reviewer agreement, or preregistration may be inferred from this record.
