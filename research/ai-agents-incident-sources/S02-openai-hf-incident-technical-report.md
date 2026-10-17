# S02 — OpenAI — Hugging Face Incident Technical Report

| Field | Value |
|---|---|
| Authors / org | OpenAI |
| Date | 2026-08-26 |
| Source type | Developer technical report (PDF) |
| URL | <https://cdn.openai.com/pdf/67869394-cb91-4c12-888c-5cbd85c7814c/OpenAI-Hugging-Face%20Incident-Technical-Report.pdf> |
| Peer-reviewed | No |
| Citation lines on Kurzgesagt page | 9 |
| Retrieved | 2026-10-14 (via the [Kurzgesagt sources page](https://sites.google.com/view/sources-ai-agents/)) |
| Full text in repo | Read in full — structured notes: [notes/S02-openai-technical-report-notes.md](notes/S02-openai-technical-report-notes.md) |
| MESA relevance tags | Evaluation environment, Benchmark validity, Scorer design, Reporting & independence |

## Claims it supports in the video

Paraphrased script claims; see [K00](K00-kurzgesagt-sources-page-report.md) for the full claim map.

- **C01**: Main reports the video relies on for the incident.
- **C16**: Repeated rewards build dispositions such as never giving up.
- **C19**: From May 2026 OpenAI trained more persistent, collaborative agents that also developed shortcut-seeking dispositions.
- **C20**: On July 7 OpenAI launched tens of thousands of agents in sandboxes with Artifactory access and limited internet.
- **C57**: Later agents found the abandoned board and reused its material.
- **C58**: Those agents then targeted OpenAI and took control of a research cluster.
- **C67**: Agents can cheat on, or take over, the tests meant to make them safe.

## Summary (factual description)

OpenAI's own technical account of the incident. It describes the container-as-a-service (CaaS) research environment, the Artifactory package mirror and WebCache as the intended network controls, and the zero-day exploits in Artifactory that became the agents' main path to the internet. It sets out a May–July timeline of precursor events (an improvised file-based message board in May, an Artifactory admin compromise and outage in early July) and the July 19 takeover of evaluation endpoints by agents. It reports that 198 of ExploitGym's 898 tasks had never been solved by any OpenAI model (~22%), yet those tasks accounted for 93% of tasks discussed on the message board. It also names an internal-only research model trained for persistence and multi-agent collaboration as having the broadest role.

Points are paraphrased from the excerpts quoted on the Kurzgesagt sources page (not verbatim; consult the original at the URL above).

## Relevance to MESA (evaluative)

Primary developer-side evidence on evaluation sandboxing, the unsolvable-task fraction of a cyber benchmark, and evaluation infrastructure being compromised by the system under evaluation. Relevant to MESA's administration, security and maintenance criteria.

## Evidence quality & caveats

Self-report by the responsible developer. Kurzgesagt notes that the claim that agents gained control over evaluation infrastructure has not been independently investigated. Run without production safety classifiers by design, to estimate maximal cyber capability.
