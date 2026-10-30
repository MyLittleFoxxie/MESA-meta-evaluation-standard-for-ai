# Protocol amendments

## A1 — citation retrieval bound, 28 October 2026

Before retrieving citation lists, specify up to 50 citing records per matched seed in OpenAlex, sorted by publication date descending within the review window. Retain the total citation count and do not claim the first 50 exhaust the list. Retrieve all indexed backward references for each matched seed and screen their titles/dates, supplemented by the actual seed reference lists. This makes the execution bound explicit; the four database queries remain unchanged. EFPA 2025 and AERA/APA/NCME 2014 require exact-edition matching; do not substitute similarly titled older editions or reviews.

## A2 — prior MESA work, 28 October 2026, after discovery

Forward searching returned the prior MESA manuscript. Exclude it from evidence used to justify or validate MESA, retaining its discovery and reason in the register. This follows the repository instruction not to treat earlier assistant supported development as validation. This decision was made after seeing the record, not before discovery.

## A3 — retrieval corrections, 28 October 2026

The OECD indexed reference request failed with HTTP 400. Retain that failure and retry in four smaller batches. All 127 indexed records were retrieved. The index list extends beyond the printed Chapter 6 reference list; it is recorded as an index retrieval with uncertain chapter attribution. It is not evidence that Chapter 6 cites every listed work. The printed references remain the authority for citation relationships.

## Execution qualifications

Backward searching used the printed reference lists and retained 26 selected candidate records, including an older contextual exclusion. This is a relevance selected citation search, not a census with a separate decision for every printed reference. Forward coverage is limited to matched index versions and fallback searches. These limits must accompany any report of the review. See citation-search-log.md for the source boundaries and search-log.md for requests.
