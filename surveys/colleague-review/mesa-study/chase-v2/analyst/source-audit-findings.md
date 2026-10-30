# Source audit findings

29 October 2026. Assistant source inspection, not independent checking. The live survey and snapshot remain unchanged. These findings concern supplied material, not experimental responses; no reviewer sessions have run.

## DesignQA: confirmed conflicts with the supplied paper

The local PDF identifies arXiv 2404.07917v2, 23 August 2024. Its text and rendered pages were inspected. Page numbers below are PDF/printed pages in that document. The comparison is with participant packet 2.9, not with an assumed current web version of the survey.

| Packet location | Packet statement | Source finding | Implication |
| --- | --- | --- | --- |
| `designqa-baselines` model label | Claude 3 Opus received the full rulebook | Section 4.1.2, p. 9, explicitly states that Claude Opus was tested only with RAG (retrieved passages). Table 2 uses Claude-Opus-RAG. | A concrete comparison condition is mislabelled. |
| `designqa-baselines`, naive baseline | Presence 65.1%, Dimension 76.8%, Performance 68.8% | Table 2, p. 10, gives 0.5 for each of these accuracy baselines. | These values cannot be described as the official Table 2 baselines. |
| `designqa-baselines`, retrieval metrics | Naive retrieval 0.0%; Claude retrieval 78.2% | Table 2 gives 0.082 naive F1 BoW and 0.173 Claude-Opus-RAG F1 BoW. | The numbers and metric presentation need reconciliation; F1 is not simply accuracy. |
| `designqa-segments` | Compilation 67, Definition 57, Presence 63, Dimension 56 | Section 3.1 describes 30 Compilation questions, 31 Definition questions, 62 Presence questions and 120 Dimension questions. Together with 1,192 Retrieval and 16 Functional Performance questions, these sum to 1,451. | Matching the overall total does not validate the group counts. Check the full table against the PDF before correcting a version. |
| `designqa-segments`, Definition metric | Sentence transformer cosine similarity | Section 3.2.1 specifies F1 Bag of Characters for Definition. Similarity is one of the separate explanation metrics in Section 3.2.3. | The table conflates different scoring functions. |
| `designqa-variations` | GPT-4V tested with Guaranteed retrieval across five runs | Section 5, p. 12, identifies LLaVA-1.5 as the model tested with five GuaranteedRAG contexts. | The model label is inconsistent with the cited experiment. |
| `designqa-variations` and paragraph 4 | Range 68.1%–70.3% | The inspected source describes means and standard deviations across GuaranteedRAG contexts. This particular range has not been located in the inspected text. | Unverified number, not an established contradiction; find its source or remove it only in a new packet version. |

The packet's prose about different information conditions is broadly compatible with the paper. The first finding above specifically concerns the table label, not a claim that the prose names Claude as receiving all rules.

Evidence copies: [PDF p. 9](source-checks/DesignQA-page-9.png), [PDF p. 10](source-checks/DesignQA-page-10.png), [PDF p. 12](source-checks/DesignQA-page-12.png). The original remains [DesignQA.pdf](../../../../../literature/pdfs/DesignQA.pdf). The [extracted text](source-checks/DesignQA-extracted.txt) aids location but does not replace the PDF.

## ARC: source qualifications to preserve

- The pinned dataset README gives two trials in its task-success section but three trials in its later task-format explanation. A source-passage packet should retain or explicitly document this inconsistency rather than silently deleting it. See retrieved `AR.txt`, sections “Task success criterion” and “Task file format”. The summary uses two attempts.
- The scoring code computes the proportion of test pairs solved in a task. The README's whole-task success criterion requires all test inputs. These are different descriptions of the scoring unit and must remain visible.
- The retrieved current policy states that a single run is used. However, the source manifest records a visit on 7 October 2026 without preserving the policy body or its hash. The 29 October page cannot be certified as identical to that earlier page. Do not claim a matched historical source set until this is resolved or explicitly amend the design.

## Consequences for preparation

1. Proposed summary answers describe the packet a reviewer sees. They must not be called independent factual truth about the benchmark.
2. Original-passage answers need their own checked references. Differences caused by inaccurate supplied information are not automatically reviewer mistakes.
3. Study 2 can examine the existing packet as an artifact, but its report must distinguish factual discrepancies from neutral compression or phrasing effects. Alternatively, a corrected packet can be prepared as a new version before execution. These are different study questions, not silent implementation choices.
4. Do not rewrite participant records or change a live packet after collection without a version and analysis plan. No collection status or participant responses were inspected here.
5. Author review of the packet choice, source findings and proposed references is required before freeze. Existing references and conditions remain draft.
