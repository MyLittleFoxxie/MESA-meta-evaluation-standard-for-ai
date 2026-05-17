# Benchmark Official Documentation Inventory

Generated: 2026-05-14

This inventory lists the benchmarks from the provided image and the closest official or primary documentation located for each. "Official" is interpreted as documentation from benchmark authors, maintainers, dataset owners, official repositories, official leaderboards, or source papers. Where a benchmark entry is a leaderboard/evaluator-specific slice rather than a standalone benchmark, that limitation is noted.

| # | Benchmark | Description from image | Official / primary documentation |
|---:|---|---|---|
| 1 | Humanity's Last Exam | Academic reasoning | Official repo: https://github.com/centerforaisafety/hle ; paper: https://arxiv.org/abs/2501.14249 ; dataset: https://huggingface.co/datasets/cais/hle |
| 2 | ARC-AGI-2 | Visual reasoning puzzles | Official benchmark page: https://arcprize.org/arc-agi/2 ; official repo: https://github.com/arcprize/ARC-AGI-2 ; technical report: https://arcprize.org/blog/arc-agi-2-technical-report |
| 3 | GPQA Diamond | Scientific knowledge | Official repo: https://github.com/idavidrein/gpqa ; dataset: https://huggingface.co/datasets/Idavidrein/gpqa ; paper: https://arxiv.org/abs/2311.12022 |
| 4 | AIME 2025 | Mathematics | AIME program page: https://maa.org/math-competitions/aime/ ; benchmark/evaluator page: https://artificialanalysis.ai/evaluations/aime-2025 ; methodology: https://artificialanalysis.ai/methodology/intelligence-benchmarking ; note: AIME is an official math competition, while "AIME 2025" as an LLM benchmark is typically an evaluator-defined use of the contest problems. |
| 5 | MathArena Apex | Challenging Math Contest problems | Official page: https://matharena.ai/apex/ ; MathArena paper: https://arxiv.org/abs/2505.23281 |
| 6 | MMMU-Pro | Multimodal understanding and reasoning | Official repo: https://github.com/MMMU-Benchmark/MMMU ; paper: https://arxiv.org/abs/2409.02813 ; homepage/leaderboard: https://mmmu-benchmark.github.io/ |
| 7 | ScreenSpot-Pro | Screen understanding | Official project/leaderboard: https://gui-agent.github.io/grounding-leaderboard ; official repo: https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding ; paper: https://arxiv.org/abs/2504.07981 ; dataset: https://huggingface.co/datasets/likaixin/ScreenSpot-Pro |
| 8 | CharXiv Reasoning | Information synthesis from complex charts | Official project page: https://charxiv.github.io/ ; paper: https://arxiv.org/abs/2406.18521 ; NeurIPS proceedings page: https://papers.nips.cc/paper_files/paper/2024/hash/cdf6f8e9fd9aeaf79b6024caec24f15b-Abstract-Datasets_and_Benchmarks_Track.html |
| 9 | OmniDocBench 1.5 | OCR | Official repo: https://github.com/opendatalab/OmniDocBench ; paper: https://arxiv.org/abs/2412.07626 ; note: the official repo now tracks later versions too, so use the v1.5 branch/tag or dataset version when reconstructing this exact benchmark. |
| 10 | Video-MMMU | Knowledge acquisition from videos | Official site: https://videommmu.github.io/ ; official repo: https://github.com/EvolvingLMMs-Lab/VideoMMMU ; paper: https://arxiv.org/abs/2501.13826 |
| 11 | LiveCodeBench Pro | Competitive coding problems from Codeforces, ICPC, and IOI | Paper: https://arxiv.org/abs/2506.11928 ; project page cited by paper: https://livecodebenchpro.com/ ; dataset: https://huggingface.co/datasets/QAQAQAQAQ/LiveCodeBench-Pro ; note: public code/docs appear more limited than for standard LiveCodeBench. |
| 12 | Terminal-Bench 2.0 | Agentic terminal coding | Official site: https://www.tbench.ai/ ; official repo: https://github.com/harbor-framework/terminal-bench ; Harbor registry for 2.0: https://www.harborframework.com/registry/terminal-bench/2.0 ; paper: https://arxiv.org/abs/2601.11868 |
| 13 | SWE-Bench Verified | Agentic coding | Official docs: https://www.swebench.com/SWE-bench/guides/datasets/ ; official repo: https://github.com/SWE-bench/SWE-bench ; dataset: https://huggingface.co/datasets/SWE-bench/SWE-bench_Verified ; OpenAI announcement/report: https://openai.com/index/introducing-swe-bench-verified/ |
| 14 | tau2-bench | Agentic tool use | Official repo: https://github.com/sierra-research/tau2-bench ; paper: https://arxiv.org/abs/2506.07982 ; leaderboard/docs: https://taubench.com/ |
| 15 | Vending-Bench 2 | Long-horizon agentic tasks | Official page: https://andonlabs.com/evals/vending-bench-2 ; original Vending-Bench page: https://andonlabs.com/evals/vending-bench ; original paper: https://arxiv.org/abs/2502.15840 |
| 16 | FACTS Benchmark Suite | Held-out internal grounding, parametric, MM, and search retrieval benchmarks | Official DeepMind blog: https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models/ ; tech report: https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf ; Kaggle benchmark: https://www.kaggle.com/benchmarks/google/facts |
| 17 | SimpleQA Verified | Parametric knowledge | Dataset card: https://huggingface.co/datasets/google/simpleqa-verified ; Kaggle benchmark: https://www.kaggle.com/benchmarks/deepmind/simpleqa-verified ; technical report: https://arxiv.org/abs/2509.07968 |
| 18 | MMMLU | Multilingual MQA | Dataset card: https://huggingface.co/datasets/openai/MMMLU ; source/eval implementation noted by dataset: https://github.com/openai/simple-evals ; source MMLU paper: https://arxiv.org/abs/2009.03300 |
| 19 | Global PIQA | Commonsense reasoning across 101 languages and cultures | Parallel dataset card: https://huggingface.co/datasets/mrlbenchmarks/global-piqa-parallel ; non-parallel dataset card: https://huggingface.co/datasets/mrlbenchmarks/global-piqa-nonparallel ; paper: https://arxiv.org/abs/2510.24081 |
| 20 | MRCR v2 (8-needle) | Long context performance | OpenAI MRCR dataset: https://huggingface.co/datasets/openai/mrcr ; evaluation documentation: https://evalscope.readthedocs.io/en/latest/benchmarks/openai_mrcr.html ; note: the public OpenAI MRCR dataset documents 2-, 4-, and 8-needle variants and token-length bins; "v2 (8-needle)" is usually a specific evaluation slice rather than a separately documented benchmark. |

## Source Notes

- The image appears to mix original benchmark names, evaluator-specific benchmark slices, and current leaderboard labels.
- For MESA Part A work, use the official/primary links above as the source inventory starting point, then record exact benchmark version, split, scorer, prompt format, and leaderboard methodology separately.
- Do not treat missing standalone documentation for a slice as proof of poor quality; record it as an evidence gap until the benchmark maintainer or evaluator provides more detail.
