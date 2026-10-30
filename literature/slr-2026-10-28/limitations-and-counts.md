# Review limits and record counts

## Counts

The machine readable totals are in [counts.json](counts.json). Counts describe this retrieval and screening record, not the size of the research field.

| Discovery stream | Retained occurrences |
|---|---:|
| Twelve database queries | 481 |
| Forward citation index results | 46 |
| Recovered OECD indexed backward results | 127 |
| Selected references from printed backward searches | 26 |
| Requested starting sources | 7 |
| Total occurrences in these streams | 687 |

These streams overlap. After recorded title, identifier and version handling, the register contains **622 records treated as separate works or editions**: **66 recent included sources**, **1 included foundation source**, **517 exclusions**, and **38 unresolved records**. The database stage alone initially grouped 481 occurrences into 428 title groups. Do not add that intermediate count to the later register count.

“Source” does not mean “empirical study.” The 67 extractions include standards, conceptual proposals, reviews, methods, audits and tool studies. No pooled quality score or meta analysis was calculated. Older records are not part of the 66 recent sources. The OECD indexed backward list has a scope mismatch with the printed chapter references and is labelled accordingly.

The 26 selected backward records do not enumerate every printed citation. Web searches used for verification or access are logged separately; their page hits are not treated as independent study records. Accordingly, this is not a PRISMA claim of complete identification and screening across every citation and web result.

## Search and screening limits

The protocol was frozen before screening new search results, but after familiarity with the seeds and MESA. It was not registered externally. Each database query was limited to the first 50 results. OpenAlex and Crossref interpret text queries differently from arXiv’s explicit conjunctions. Crossref returned many unrelated items. Search ranking, date fields, indexing delays and English full text eligibility can omit relevant research.

Citation coverage was limited by index matches and a relevance selected backward pass. Some exact editions were not indexed, and the OECD index reference set did not match the printed chapter scope. These are coverage limits, not evidence that the sources have no citations or references.

One assistant screened and extracted the evidence. Many exclusions were made at title screening, with the stage stated in the register. These can be mistaken and require author audit. No independent screening, adjudication by a second reviewer or coder agreement was performed. The assistant also wrote the synthesis; extracting and synthesising with the same assistant can reinforce interpretive errors.

Access failures include HTTP 403 responses, application shells, browser checks, redirects and publisher abstracts without full text. A successful HTTP response did not count as full text access by itself. The 38 unresolved sources were not used as evidence about what their contents do or do not establish. Their absence can change the synthesis, particularly the scope of claimed gaps.

## Evidence and interpretation limits

Extraction focuses on sections relevant to the four questions. It is not an independent replication or verification of datasets, code, clinical labels or statistical analyses. “Not reported in inspected sections” must not become “not performed.” Reported findings remain attributed to their authors.

Standards were assessed for authority and applicability; frameworks for definitions, guidance and supporting reasoning; experiments for design, sample, comparison and limitations. Human consultation, author case studies, perceptions, observed task behavior and repeated model outputs are distinct evidence. Agreement is not correctness, and observations from one tool cannot validate another.

Version differences were retained where found. The review did not perform a line by line comparison of every preprint with every publication. Some first release dates remain based on the earliest verified record rather than a complete publication history. BetterBench and Evaluation Cards contain unresolved reporting conflicts; STAGER’s final text was unavailable. See [version audit](version-audit.md).

The evidence does not establish that shorter reviews are more accessible, that a solution is absent from the field, or that MESA improves human decisions. Accessibility is used as a family of outcomes requiring specification, not a synonym for open access or few questions.

## Assistant involvement and author review

The Codex assistant prepared the protocol, performed searches and retrieval, screened records, extracted and interpreted source material, generated tables and summaries, and ran mechanical checks. No subagents, independent reviewers, human participants or new model experiments were used. Shell scripts and source reading tools supported this research record; they were not MESA reviewer sessions.

The author must review inclusion decisions, exclusions, uncertain dates and versions, and every candidate gap before using them as manuscript conclusions. Each source and gap is marked pending. Mechanical verification checks counts, hashes and links; it does not certify the research judgments.

No manuscript, questionnaire, experiment or human survey was changed. LaTeX layout and page length were not checked, and no LaTeX compilation was run.
