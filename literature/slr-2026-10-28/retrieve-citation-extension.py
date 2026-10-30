import retrieve,concurrent.futures,json,pathlib
p=pathlib.Path(__file__).resolve().parent
items=[
('B08','2311.02462','Levels of AGI: Operationalizing Progress on the Path to AGI','S06 References PDF19'),
('B09','2407.21792','Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?','S06 References PDF19'),
('B10','2503.06378','General scales unlock AI evaluation with explanatory and predictive power','S01 ref66'),
('B11','2401.00595','State of What Art? A Call for Multi-Prompt LLM Evaluation','S01 ref58; S02 References PDF38'),
('B12','2402.01781','When Benchmarks are Targets: Revealing the Sensitivity of Large Language Model Leaderboards','S07 ref6'),
('B13','2311.01964','Don’t Make Your LLM an Evaluation Benchmark Cheater','S01 ref59; S07 ref95'),
('B14','2311.04850','Rethinking Benchmark and Contamination for Language Models with Rephrased Samples','S02 References PDF42; S07 ref91'),
('B15','2412.04363','Challenges in Trustworthy Human Evaluation of Chatbots','S02 References PDF42'),
('B16','2501.07493','Exploring and Mitigating Adversarial Manipulation of Voting-Based Leaderboards','S02 References PDF36'),
('B17','2412.03304','Global MMLU: Understanding and Addressing Cultural and Linguistic Biases in Multilingual Evaluation','S01 ref27; S02 References PDF40'),
('B18','2401.15897','Red-Teaming for Generative AI: Silver Bullet or Security Theater?','S07 ref27'),
('B19','2401.06059','Investigating Data Contamination for Pre-training Language Models','S07 ref37'),
('B20','2411.03923','Evaluation data contamination in LLMs: how do we measure it and (when) does it matter?','S02 References PDF40'),
('B21','2506.10378','Discovering Hierarchical Latent Capabilities of Language Models via Causal Representation Learning','S06 References PDF18'),
('B22','2404.06647','From Protoscience to Epistemic Monoculture: How Benchmarking Set the Stage for the Deep Learning Revolution','S02 References PDF36'),
('B23','2501.17858','Improving Your Model Ranking on Chatbot Arena by Vote Rigging','S02 References PDF38'),
('B24','2312.17476','Exploring the Sensitivity of LLMs’ Decision-Making Capabilities: Insights from Prompt Variation and Hyperparameters','S07 ref55'),
('B25','2402.14016','Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot LLM Assessment','S02 References PDF39')]
(p/'backward-candidates.json').write_text(json.dumps([dict(zip(['source_id','arxiv','title','origin'],x)) for x in items],indent=2)+'\n')
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for r in ex.map(retrieve.fetch,[(x[0],'https://arxiv.org/pdf/'+x[1]) for x in items]):print(r['id'],r.get('file'),r.get('error'),flush=True)
