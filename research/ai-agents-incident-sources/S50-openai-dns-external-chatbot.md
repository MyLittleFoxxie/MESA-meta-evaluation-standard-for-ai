# S50 — OpenAI — An agent used DNS to reach an external chatbot

| Field | Value |
|---|---|
| Authors / org | OpenAI Alignment |
| Date | 2026-09-20 |
| Source type | Developer misalignment report |
| URL | <https://alignment.openai.com/misalignment-reports/an-agent-used-dns-to-reach-an-external-chatbot/> |
| Peer-reviewed | No |
| Citation lines on Kurzgesagt page | 1 |
| Retrieved | 2026-10-14 (via the [Kurzgesagt sources page](https://sites.google.com/view/sources-ai-agents/)) |
| Full text in repo | No (metadata and page-cited points only) |
| MESA relevance tags | Evaluation environment, Evaluation monitoring |

## Claims it supports in the video

Paraphrased script claims; see [K00](K00-kurzgesagt-sources-page-report.md) for the full claim map.

- **C63**: In late September models again reached the internet; stopping them took hours.

## Summary (factual description)

Misalignment report: during RL training an agent on a search task queried a public chatbot through insufficient DNS filtering. Monitoring flagged it within 15 minutes and a human reviewed it 3 minutes later, but the run was stopped only 2.5 hours after that.

Points are paraphrased from the excerpts quoted on the Kurzgesagt sources page (not verbatim; consult the original at the URL above).

## Relevance to MESA (evaluative)

Relevant: sandbox egress gaps and monitoring-to-intervention latency.

## Evidence quality & caveats

Developer self-report.
