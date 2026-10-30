# Search log

Search date: 28 October 2026. Protocol SHA256 and freeze time are in protocol-freeze.json. Exact service syntax is preserved in each request URL and script; these queries are not assumed to be semantically equivalent across services.

| Service | Query | UTC start | Returned | Total hits reported | Record |
|---|---|---|---:|---:|---|
| openalex | Q1 | 2026-10-28T16:54:33.845963+00:00 | 50 | 263831 | [Request and records](searches/openalex-q1.json) |
| openalex | Q2 | 2026-10-28T16:54:34.779859+00:00 | 50 | 40585 | [Request and records](searches/openalex-q2.json) |
| openalex | Q3 | 2026-10-28T16:54:35.904096+00:00 | 50 | 16262 | [Request and records](searches/openalex-q3.json) |
| openalex | Q4 | 2026-10-28T16:54:36.346380+00:00 | 50 | 23736 | [Request and records](searches/openalex-q4.json) |
| crossref | Q1 | 2026-10-28T16:54:33.846465+00:00 | 50 | 2761621 | [Request and records](searches/crossref-q1.json) |
| crossref | Q2 | 2026-10-28T16:54:34.794397+00:00 | 50 | 1095808 | [Request and records](searches/crossref-q2.json) |
| crossref | Q3 | 2026-10-28T16:54:35.909950+00:00 | 50 | 927542 | [Request and records](searches/crossref-q3.json) |
| crossref | Q4 | 2026-10-28T16:54:36.947861+00:00 | 50 | 1711789 | [Request and records](searches/crossref-q4.json) |
| arxiv | Q1 | 2026-10-28T16:54:33.846537+00:00 | 50 | 76 | [Request and records](searches/arxiv-q1.json) |
| arxiv | Q2 | 2026-10-28T16:54:35.373389+00:00 | 28 | 28 | [Request and records](searches/arxiv-q2.json) |
| arxiv | Q3 | 2026-10-28T16:54:36.064670+00:00 | 3 | 3 | [Request and records](searches/arxiv-q3.json) |
| arxiv | Q4 | 2026-10-28T16:54:37.260897+00:00 | 0 | 0 | [Request and records](searches/arxiv-q4.json) |

## Query text and service syntax

- Q1: `AI benchmark quality review framework`
- Q2: `language model benchmark validity reliability fairness`
- Q3: `AI evaluation checklist guidance reproducibility`
- Q4: `benchmark review accessibility usability comprehension effort`

OpenAlex uses its text search with publication date filters; Crossref uses its query parameter and publication date filters; arXiv joins query words with AND and filters submittedDate. Each request asks for at most 50 results. Total hits are service reports, not screened counts. Raw database responses are in raw/.

## Additional discovery and verification

The seven seeds, one citation round and primary source verification supplement the database queries. Exact citation requests are in citation-search-log.md and searches/citation-*.json. Searches/seed-match-*.json retains the returned candidate matches, including rejected edition matches. Searches/web-*.json retains the web searches used to verify the seeds and investigate reference titles. Metadata-*.json records arXiv title, authors, first submission date and version history.

A further web verification used the exact queries `"Large Language Models are not Fair Evaluators" arxiv` and `"STAGER" "32" "2024"` on 28 October 2026. The former confirmed arXiv:2305.17926 dated 29 May 2023; its 2024 publication does not make it eligible. The latter was not treated as a source of additional included studies. Only primary records were used for factual extraction.

## Retrieval and access

Every attempted full text URL and its result is stored in searches/retrieve-*.json. The initial shell environment could not resolve network hosts; authorised network retrieval then succeeded for the databases. Publisher failures and nonarticle responses were retained. Later linked PDFs use separate request IDs with suffixes, preserving the initial attempts. A 200 response containing an abstract, OSF shell or browser check was not counted as a full text.

## Duplicate handling

The first pass grouped 481 database occurrences into 428 normalised title groups, retaining all occurrence identifiers and ranks. Identifier, author and title inspection then linked preprints/publications and duplicate citation results. The inspected author mismatch among repeated title groups concerned spelling variants for R213 rather than separate works. Explicit links are in duplicate-map.json; all identifiers and discovery routes remain in source-register.json. Books, chapters or editions with the same short title are not automatically treated as the same work. Substantive version differences are in version-audit.md.

## Retrieval manifest

The following generated manifest lists every request record with the source file, date, URL and access result; it is an index of requests, not an additional study count.

[All requests](request-manifest.tsv)
