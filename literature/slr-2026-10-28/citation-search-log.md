# Citation search

One round from the seven seeds; no recursion from newly found papers. All searches occurred on 28 October 2026. Exact index requests, timestamps and responses are in searches/citation-*.json and searches/seed-match-*.json.

| Seed | Backward source inspected | Forward route and result |
|---|---|---|
| S01 | References, PDF pp. 12–15. Selected B01, B02, B04–B07 and further methods in backward-candidates.json; BetterBench already a seed. | OpenAlex W4416268504: 9 records. |
| S02 | References, PDF pp. 31–42. Selected work on votes, evaluator behavior, prompt sensitivity and contamination; R296 already retrieved. | OpenAlex W4417172194: 6 records. |
| S03 | Part C, PDF pp. 86–89. Most references predate the window. Recent test adaptation, statistical or national review references were not treated as AI benchmark evidence merely because EFPA cited them. | No exact 2025 edition match. Exact title web fallback recorded; no verified citing work added. This is incomplete forward coverage. |
| S04 | Foundation source and its bibliography; publication in 2014 places its references before the recent window. | No exact 2014 edition match in returned records. Exact title fallback did not provide a complete citing list. |
| S05 | Chapter 6 references, printed pp. 112–115. Original chapter references predate the cutoff; the 2022 predecessor is contextual, not recent. | OpenAlex W4388802936: 0 returned citing records. This is an index result, not proof that nobody cites the chapter. |
| S06 | References, PDF pp. 16–21. Selected Levels of AGI, Safetywashing and latent capability analysis. Test manuals and ordinary benchmark introductions were not selected. | OpenAlex W4415967303: 3 records. |
| S07 | References, local PDF pp. 11–17. Selected ECBD, evaluation sensitivity and contamination work; retained older releases separately. | OpenAlex W4415798415: 28 records. |

The five matched forward lists contain 46 occurrences and 41 index work IDs before title/version handling. The index versions are a coverage limit: a proceedings entry and a preprint entry may have different citation lists. This review did not combine every possible index version’s citing list.

Most matched seeds had empty indexed reference lists despite references in their PDFs. The OECD lookup initially failed, then returned 127 records in smaller batches. That list covers material beyond the printed Chapter 6 references, including older expert elicitation and education sources. All 127 are retained with screening decisions and an attribution caution. Three have later index publication dates but concern benchmark introductions or model exam performance; none was included on the strength of those dates.

Backward candidate selection retained 26 records for this review, including one older contextual exclusion. The printed lists contain many more citations. Their page ranges and extracted text are preserved, but the count of 26 is **not** the total number of references inspected and **not** a complete inventory of eligible work in those lists. This relevance selection and the lack of an independent citation screen limit coverage.

Selected backward origins are stored in source-register.json and backward-candidates.json. Forward occurrences remain linked to the exact response file. Abstracts, unrelated web hits and source verification pages are not silently counted as included studies.
