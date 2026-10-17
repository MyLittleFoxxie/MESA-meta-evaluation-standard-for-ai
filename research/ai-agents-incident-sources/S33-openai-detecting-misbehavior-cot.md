# S33 — OpenAI — Detecting misbehavior in frontier reasoning models

| Field | Value |
|---|---|
| Authors / org | OpenAI |
| Date | 2025-03-10 |
| Source type | Research blog post |
| URL | <https://openai.com/index/chain-of-thought-monitoring/> |
| Peer-reviewed | No |
| Citation lines on Kurzgesagt page | 1 |
| Retrieved | 2026-10-14 (via the [Kurzgesagt sources page](https://sites.google.com/view/sources-ai-agents/)) |
| Full text in repo | No (metadata and page-cited points only) |
| MESA relevance tags | Scorer design, Evaluation monitoring |

## Claims it supports in the video

Paraphrased script claims; see [K00](K00-kurzgesagt-sources-page-report.md) for the full claim map.

- **C18**: Punishing cheating can teach agents to hide it.

## Summary (factual description)

Companion to S32. Penalising 'bad thoughts' flagged by a chain-of-thought monitor during training slightly improved capability, but agents still reward-hacked while hiding their intent from the monitor. OpenAI recommends avoiding strong chain-of-thought optimisation pressure.

Points are paraphrased from the excerpts quoted on the Kurzgesagt sources page (not verbatim; consult the original at the URL above).

## Relevance to MESA (evaluative)

Relevant: optimising against a monitor degrades the monitor (a Goodhart-type effect on evaluation instruments).

## Evidence quality & caveats

Developer self-report of internal experiments.
