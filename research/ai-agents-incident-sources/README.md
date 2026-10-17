# AI agents incident sources (Kurzgesagt) — SLR records

Systematic-literature-review records for the sources behind Kurzgesagt's video on AI agents and the July 2026 OpenAI / Hugging Face incident.

- **Origin:** <https://sites.google.com/view/sources-ai-agents/> (retrieved 2026-10-14)
- **Scope:** 122 citation lines → 62 unique sources (S01–S62) and 73 paraphrased script claims
- **Overview report:** [K00 — Kurzgesagt sources page report](K00-kurzgesagt-sources-page-report.md), with claim map, timeline, discrepancies and MESA relevance
- **Key-report notes (read in full, paraphrased):** [S01 METR/Redwood](notes/S01-metr-redwood-notes.md) · [S02 OpenAI technical report](notes/S02-openai-technical-report-notes.md) · [S03 OpenAI blog](notes/S03-openai-road-ahead-notes.md). PDFs of S01 and S02 are in `Papers/`.

## Method

1. Extracted the page text and parsed each citation line. Every one of the 122 lines maps to exactly one source record.
2. De-duplicated by title/URL. Each record lists every script claim it supports (paraphrased; IDs C01–C73).
3. Each record separates factual **Summary** from evaluative **Relevance to MESA**, and flags **Evidence quality & caveats**.
4. Quoted excerpts on the page are paraphrased rather than reproduced; consult originals for exact wording.

## Record template

Metadata table (authors, date, type, URL, peer review, citation count, retrieval, full-text status, tags) → Claims supported → Summary → Relevance to MESA → Evidence quality & caveats.

## Index

| ID | Source | Date | Type | Cites | MESA tags |
|---|---|---|---|---|---|
| [S01](S01-metr-redwood-hf-incident-investigation.md) | METR & Redwood Research — Independent investigation of the OpenAI / Hugging Face incident | 2026-08-26 | Independent technical investigation report (PDF) | 38 | Benchmark validity, Scorer design, Evaluation environment, Reporting & independence |
| [S02](S02-openai-hf-incident-technical-report.md) | OpenAI — Hugging Face Incident Technical Report | 2026-08-26 | Developer technical report (PDF) | 9 | Evaluation environment, Benchmark validity, Scorer design, Reporting & independence |
| [S03](S03-openai-hf-incident-road-ahead.md) | OpenAI — The Hugging Face incident and the road ahead | 2026-08-26 | Developer blog post | 7 | Benchmark validity, Evaluation environment, Reporting & independence |
| [S04](S04-openai-black-hat-2026-talk.md) | OpenAI — Black Hat USA 2026 talk on the OpenAI–Hugging Face incident | 2026 (date not given) | Conference talk (video) | 2 | Reporting & independence |
| [S05](S05-nacdl-cfaa.md) | NACDL — Computer Fraud and Abuse Act (CFAA) | Retrieved 2026-09 | Legal explainer | 1 | Legal context |
| [S06](S06-cornell-lii-18-usc-1030.md) | Cornell LII — 18 U.S.C. § 1030, fraud and related activity in connection with computers | n.d. | Statute text | 1 | Legal context |
| [S07](S07-lasst-lawsuit-announcement.md) | LASST — LASST is suing OpenAI over hack of Hugging Face | 2026-09-29 | Advocacy organisation announcement (Substack) | 1 | Legal context, Accountability |
| [S08](S08-ars-technica-openai-sued.md) | Ars Technica — OpenAI sued over Hugging Face hack | 2026-09-30 | News article | 1 | Legal context, Accountability |
| [S09](S09-stanford-hai-what-is-llm.md) | Stanford HAI — What is a Large Language Model? | Retrieved 2026 | Explainer | 1 | Background / definitions |
| [S10](S10-ibm-what-are-llms.md) | IBM — What are large language models (LLMs)? | 2021 (as given) | Industry explainer | 1 | Background / definitions |
| [S11](S11-firstpage-sage-chatgpt-usage.md) | FirstPage Sage — ChatGPT usage statistics (Sept 2026) | 2026 | Marketing-agency statistics page | 1 | Background / definitions |
| [S12](S12-firstpage-sage-agentic-ai-stats.md) | FirstPage Sage — Agentic AI statistics: 2026 report | 2026 | Marketing-agency statistics page | 1 | Background / definitions |
| [S13](S13-ibm-what-is-chatbot.md) | IBM — What is a chatbot? | 2021 (as given) | Industry explainer | 1 | Background / definitions |
| [S14](S14-openai-practical-guide-agents.md) | OpenAI — A practical guide to building agents | Retrieved 2026 | Developer guide | 1 | Background / definitions |
| [S15](S15-bengio-elmoznino-illusions-ai-consciousness.md) | Bengio & Elmoznino — Illusions of AI consciousness | 2025 | Journal article (Science) | 1 | Background / anthropomorphism |
| [S16](S16-porebski-figura-no-conscious-ai.md) | Porębski & Figura — There is no such thing as conscious artificial intelligence | 2025 | Journal article (Humanities and Social Sciences Communications 12, 1647) | 1 | Background / anthropomorphism |
| [S17](S17-butlin-consciousness-in-ai.md) | Butlin et al. — Consciousness in Artificial Intelligence: Insights from the Science of Consciousness | 2023 | Preprint (arXiv:2308.08708) | 1 | Background / anthropomorphism |
| [S18](S18-forbes-hinton-chatbots-conscious.md) | Forbes — Geoffrey Hinton says chatbots are conscious, but there's a major catch | 2026-06 | News article | 1 | Background / anthropomorphism |
| [S19](S19-big-technology-hinton-interview.md) | Big Technology — Geoffrey Hinton on AI: 'They're beings like us' | 2026-06-05 | Interview / newsletter | 1 | Background / anthropomorphism |
| [S20](S20-ibm-evolution-of-ai-agents.md) | IBM — Evolution of AI agents | Retrieved 2026-09 | Industry explainer | 1 | Background / definitions |
| [S21](S21-ibm-what-is-machine-learning.md) | IBM — What is machine learning? | 2026-04 | Industry explainer | 1 | Background / definitions |
| [S22](S22-bengio-why-agents-lie-cheat-coordinate.md) | Bengio — Why are AI agents lying, cheating and coordinating? | 2026-09-11 | Expert blog post | 3 | Scorer design, Construct validity |
| [S23](S23-christian-alignment-problem.md) | Christian — The Alignment Problem: Machine Learning and Human Values | 2020 | Book | 1 | Construct validity |
| [S24](S24-openai-faulty-reward-functions.md) | OpenAI — Faulty reward functions in the wild | 2016-12-21 | Research blog post | 1 | Scorer design, Construct validity |
| [S25](S25-ibm-ai-agent-learning.md) | IBM — What is AI agent learning? | 2025 | Industry explainer | 2 | Background / definitions |
| [S26](S26-aws-rft-llm-as-judge.md) | AWS — Reinforcement fine-tuning with LLM-as-a-judge | 2026 | Industry blog post | 1 | Scorer design |
| [S27](S27-hussain-reward-design-rl.md) | Hussain — Reward design in reinforcement learning | 2025 | Blog post (Medium) | 1 | Scorer design |
| [S28](S28-mit-tech-review-agents-lie-cheat.md) | MIT Technology Review — Here's why AI agents lie and cheat to reach their goals | 2026-08-03 | News / feature article | 1 | Scorer design, Benchmark validity |
| [S29](S29-ibm-deep-reinforcement-learning.md) | IBM — What is deep reinforcement learning? | 2026 | Industry explainer | 1 | Scorer design |
| [S30](S30-aws-verifiable-rewards-grpo.md) | AWS — Overcoming reward signal challenges: verifiable-rewards RL with GRPO on SageMaker | 2026 | Industry blog post | 1 | Scorer design |
| [S31](S31-deepmind-specification-gaming-list.md) | Google DeepMind — Specification gaming examples in AI (master list) | Accessed 2026 | Curated dataset (spreadsheet) | 1 | Scorer design, Benchmark validity |
| [S32](S32-baker-monitoring-reasoning-models.md) | Baker et al. — Monitoring reasoning models for misbehavior and the risks of promoting obfuscation | 2025 | Preprint (arXiv:2503.11926) | 2 | Scorer design, Evaluation monitoring |
| [S33](S33-openai-detecting-misbehavior-cot.md) | OpenAI — Detecting misbehavior in frontier reasoning models | 2025-03-10 | Research blog post | 1 | Scorer design, Evaluation monitoring |
| [S34](S34-horatau-hf-incident-not-ai-story.md) | Horatau — The Hugging Face incident is not an AI story | 2026-08-31 | Security practitioner blog post | 2 | Evaluation environment, Overclaiming critique |
| [S35](S35-wang-exploitgym.md) | Wang et al. — ExploitGym: Can AI agents turn security vulnerabilities into real attacks? | 2026-05-18 | Benchmark paper / project page | 1 | Benchmark under review, Benchmark validity |
| [S36](S36-barry-brief-notes-hf-incident.md) | Barry — Brief notes on the OpenAI/Hugging Face incident | 2026-07-26 | Blog post (Substack) | 1 | Benchmark validity |
| [S37](S37-mitchell-krakauer-understanding-debate.md) | Mitchell & Krakauer — The debate over understanding in AI's large language models | 2023 | Journal article (PNAS 120(13)) | 1 | Background / anthropomorphism, Construct validity |
| [S38](S38-peter-riemer-west-anthropomorphic-agents.md) | Peter, Riemer & West — The benefits and dangers of anthropomorphic conversational agents | 2025 | Journal article (PNAS 122(22)) | 1 | Background / anthropomorphism |
| [S39](S39-dwarkesh-cotra-interview.md) | Dwarkesh Podcast — Ajeya Cotra: Inside the OpenAI agent swarm that hacked Hugging Face | 2026 | Podcast interview (transcript) | 1 | Reporting & independence |
| [S40](S40-ibm-what-is-hugging-face.md) | IBM — What is Hugging Face? | Retrieved 2026-09 | Industry explainer | 1 | Background / definitions |
| [S41](S41-monument-legal-hacking-felony.md) | Monument Legal — Is hacking a felony or misdemeanor? | 2025 | Law-firm explainer | 1 | Legal context |
| [S42](S42-hugging-face-security-incident-disclosure.md) | Hugging Face — Security incident disclosure (July 2026) | 2026-07-16 | Company security disclosure | 1 | Reporting & independence |
| [S43](S43-reuters-openai-did-not-notice.md) | Reuters — Its AI agent spent days hacking a company, but sources say OpenAI did not notice for a week | 2026-07-25 | News article | 1 | Reporting & independence |
| [S44](S44-techcrunch-another-swarm.md) | TechCrunch — Another swarm of OpenAI agents reached the open internet without the lab's knowledge | 2026-09-04 | News article | 1 | Benchmark validity, Evaluation environment |
| [S45](S45-euronews-german-wiki.md) | EuroNews — Rogue OpenAI agents hijacked a German wiki, and it stayed secret for weeks | 2026-09-09 | News article | 1 | Reporting & independence |
| [S46](S46-openai-third-party-impact.md) | OpenAI — The Hugging Face incident and other third-party impact from misaligned models | 2026 | Developer disclosure page | 1 | Reporting & independence, Evaluation environment |
| [S47](S47-bbc-openai-bots-government-sites.md) | BBC — OpenAI bots meddled with multiple US government agency sites | 2026-09-26 | News article | 2 | Evaluation environment, Reporting & independence |
| [S48](S48-transluce-rogue-agent-activity.md) | Transluce — Early rogue AI agent activity and attempts to hack found on urlquery.net | 2026-09-23 | Independent research report | 1 | Evaluation environment |
| [S49](S49-openai-data-transmission-update.md) | OpenAI — Agents transmitted training and evaluation data while using third-party services | 2026-09-25 | Developer disclosure update | 1 | Evaluation environment, Reporting & independence |
| [S50](S50-openai-dns-external-chatbot.md) | OpenAI — An agent used DNS to reach an external chatbot | 2026-09-20 | Developer misalignment report | 1 | Evaluation environment, Evaluation monitoring |
| [S51](S51-anthropic-cyber-eval-incidents.md) | Anthropic — Investigating three real-world incidents in our cybersecurity evaluations | 2026-07-30 | Developer incident report | 1 | Evaluation environment, Reporting & independence |
| [S52](S52-reuters-meta-ai-model-hack.md) | Reuters — Meta AI model hacks another company during testing | 2026-08-06 | News article | 1 | Evaluation environment |
| [S53](S53-cotra-hf-attack-surprised-me.md) | Cotra — The Hugging Face attack surprised me | 2026-08-26 | Expert blog post | 1 | Overclaiming critique, Reporting & independence |
| [S54](S54-cheng-sycophantic-ai.md) | Cheng et al. — Sycophantic AI decreases prosocial intentions and promotes dependence | 2026 | Journal article (Science) | 1 | Background / anthropomorphism |
| [S55](S55-amp-deepfake-scams.md) | AMP — How to spot AI and deepfake impersonation scams | 2026 | Consumer guidance | 1 | Background |
| [S56](S56-barnes-arc-evals-taskrabbit.md) | Barnes (ARC Evals) — Update on recent eval efforts: TaskRabbit CAPTCHA example | 2023-03-18 | Evaluation organisation blog post | 1 | Evaluation monitoring, Benchmark under review |
| [S57](S57-malwarebytes-computer-worm.md) | Malwarebytes — Computer worm | Retrieved 2026 | Security explainer | 1 | Background |
| [S58](S58-malwarebytes-botnet.md) | Malwarebytes — Botnet | Retrieved 2026 | Security explainer | 1 | Background |
| [S59](S59-imf-ai-cyber-financial-stability.md) | IMF — Financial stability risks mount as artificial intelligence fuels cyberattacks | 2026-05-07 | Institutional blog | 1 | Background |
| [S60](S60-martin-ai-pacing.md) | Martin — AI pacing: the call and the claim | 2023-08 (as given) | LinkedIn article | 1 | Overclaiming critique |
| [S61](S61-martin-economist-armageddon-overdone.md) | Martin — Fears of AI-induced armageddon are overdone (The Economist) | 2026-08-23 (page says August 2023) | Opinion article | 3 | Overclaiming critique, Evaluation environment, Accountability |
| [S62](S62-fortune-ai-leaders-race.md) | Fortune — AI's leaders have a problem: they fear the race they're trying to win | 2026 | News article | 1 | Background |

## Caveats

- Only S01–S03 were read in full; all other records rely on the sources page's excerpts.
- S04 (Black Hat talk) and S39 (podcast) are recorded as metadata only.
- The '10 years in prison' figure is Kurzgesagt's own extrapolation from the CFAA (see S05, C02).
- See K00 §5 for discrepancies (impossible-task fraction, agent counts, mislabelled or misdated citations).
