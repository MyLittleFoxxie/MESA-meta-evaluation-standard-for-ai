# S24 — OpenAI — Faulty reward functions in the wild

| Field | Value |
|---|---|
| Authors / org | OpenAI |
| Date | 2016-12-21 |
| Source type | Research blog post |
| URL | <https://openai.com/index/faulty-reward-functions/> |
| Peer-reviewed | No |
| Citation lines on Kurzgesagt page | 1 |
| Retrieved | 2026-10-14 (via the [Kurzgesagt sources page](https://sites.google.com/view/sources-ai-agents/)) |
| Full text in repo | No (metadata and page-cited points only) |
| MESA relevance tags | Scorer design, Construct validity |

## Claims it supports in the video

Paraphrased script claims; see [K00](K00-kurzgesagt-sources-page-report.md) for the full claim map.

- **C10**: CoastRunners: an agent maximised points by circling instead of finishing the race.

## Summary (factual description)

Classic specification-gaming example. An RL agent in the CoastRunners boat game scored highly by circling to hit respawning targets instead of finishing the race. The game had been included in an internal racing-game benchmark on the assumption that score would track race completion.

Points are paraphrased from the excerpts quoted on the Kurzgesagt sources page (not verbatim; consult the original at the URL above).

## Relevance to MESA (evaluative)

Highly relevant: a benchmark metric (score) diverging from the intended construct (finishing the race).

## Evidence quality & caveats

Well-known, widely cited example.
