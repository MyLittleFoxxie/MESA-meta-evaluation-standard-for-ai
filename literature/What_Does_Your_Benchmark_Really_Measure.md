# What Does Your Benchmark Really Measure? A Framework for Robust Inference of AI Capabilities

WHAT DOES YOUR BENCHMARK REALLY MEASURE? A FRAMEWORK FOR ROBUST INFERENCE OF AI CAPABILITIES

Nathanael Jo MIT EECS nathanjo@mit.edu

Ashia Wilson MIT EECS ashia07@mit.edu

arXiv:2509.19590v1 [cs.AI] 23 Sep 2025

## ABSTRACT

Evaluations of generative models on benchmark data are now ubiquitous, and their outcomes critically shape public and scientific expectations of AI’s capabilities. Yet growing skepticism surrounds their reliability. How can we know that a reported accuracy genuinely reflects a model’s true performance? Evaluations are often presented as simple measurements, but in reality they are inferences: to treat benchmark scores as evidence of capability is already to assume a theory of what capability is and how it manifests in a test. We make this step explicit by proposing a principled framework for evaluation as inference: begin from a theory of capability, and then derive methods for estimating it. This perspective, familiar in fields such as psychometrics, has not yet become commonplace in AI evaluation. As a proof of concept, we address a central challenge that undermines reliability: sensitivity to perturbations. After formulating a model of ability, we introduce methods that infer ability while accounting for uncertainty from sensitivity and finite samples, including an adaptive algorithm that significantly reduces sample complexity. Together, these contributions lay the groundwork for more reliable and trustworthy estimates of AI capabilities as measured through benchmarks.

Part 1: Start with a theory of AI capability

Part 2: Develop inference strategies from that theory

Figure 1: Diagram of our proposed framework.
## 1 INTRODUCTION
Evaluations (from hereon, “evals”) of generative models have become ubiquitous as a way to probe each models’ capabilities or harms. Companies developing large language models (LLMs) routinely assess their systems’ intelligence using standardized knowledge tasks, while research papers proposing new methods often conduct comparative evaluations against state-of-the-art models. Leaderboards hosted on Vellum and Huggingface have also emerged as open-source platforms for directly comparing the capabilities of various LLMs. The rapidly growing interest in evals reflects our collective desire to understand how generative models behave, especially as they are now widely utilized, touted as highly capable, but inherently black box in nature.
In this work, we focus on evals that use standardized benchmark datasets. Despite the many criticisms of benchmarking (Alzahrani et al., 2024; Raji et al., 2021), benchmark data still comprise the vast majority of evals today. Benchmark results can carry significant influence in calibrating public and scientific expectations of AI capabilities1, which motivates the need for robust and trustworthy methods for inferring and reporting these capabilities. Yet, there is growing consensus that generative AI evals using benchmarks are brittle and unreliable (Mitchell, 2023; Eriksson et al., 2025).
We believe two key reasons contribute to this lack of reliability. The first is that most evals report point estimates without quantifying uncertainty. This practice is common even among the most widely cited evaluations (Hendrycks et al., 2021; Lin et al., 2022; Achiam et al., 2023; Srivastava
1Notably, companies that develop LLMs publish heavily cited reports on their models’ performance on various benchmarks (Achiam et al., 2023; Team et al., 2023; Guo et al., 2025).

1

et al., 2023; Liang et al., 2023), which offer little interpretation of the significance of their results (e.g., in comparing two models’ capabilities on a given task). This stands in stark contrast to evaluations of classical predictive models, which were historically grounded in statistical inference and hypothesis testing (Rainio et al., 2024). Recent efforts such as Chatbot Arena2 (Chiang et al., 2024) and Miller (2024) have begun to advocate for calculating and reporting confidence intervals. However, these works remain focused primarily on finite-sample uncertainty.
The second issue is that evals are rarely grounded in sound theories of AI capability. Most report standard metrics (e.g., accuracy) without considering what it actually means for an AI system to be “capable” of a task. High benchmark accuracy is, at best, a weak proxy for capability. For example, a growing body of work shows that minor changes to the phrasing or structure of inputs can significantly alter model outputs (Mizrahi et al., 2024; Sclar et al., 2023; Zhuo et al., 2024; Zheng et al., 2023; Errica et al., 2024). Yet this type of uncertainty — how models respond to the natural variation in user queries — is rarely captured in benchmark evals.
We argue that evals in the era of generative models must not only return back to its roots of statistical inference, but also carefully define what “capabilities” truly mean. To that end, we draw inspiration from psychometrics, where statistical models have long been used to robustly estimate latent traits of human ability. Our work aims to develop a theory of AI capability that incorporates various sources of uncertainty in service of informing robust methods for inferring generative models’ capabilities.
Contributions. (1) We propose a principled framework to robustly infer AI capabilities from benchmark data: start from a theory of performance, and develop methods for inference from that theory. As a proof of concept, we tackle a crucial problem that confounds evaluations: model sensitivity to perturbations. Our proposed theories of capability are intuitive and clearly expose why traditional benchmarks might produce biased estimates due to violated statistical assumptions.
(2) We empirically demonstrate that existing LLM benchmarks indeed violate these assumptions, leading to systematically inflated or deflated performance estimates. This finding aligns with previous works that have similarly quantified AI sensitivity to perturbations (Mizrahi et al., 2024; Sclar et al., 2023), but we are the first to quantify this phenomenon in the context of systematic bias in measuring performance. We also show that even state-of-the-art models (e.g., gpt-4.1) suffer from this bias, and discuss implications of evaluating larger, more capable models.
(3) Finally, building on our theory of capabilities, we propose two inference techniques: (a) clustered bootstrapping to estimate accuracy; and (b) an adaptive test based on item response theory to estimate a model’s latent ability. The latter method imposes some additional assumptions but significantly reduces the number of evaluations required and can better identify a more robust notion of capability.
### 1.1 RELATED WORK
Psychometric principles in AI evals. Our model and methods are largely inspired from psychometric testing. Wang et al. (2023) provide a comprehensive overview of the many ways psychometrics can provide a useful lens for improving AI evaluations. Notably, a good test must be (1) valid, meaning that it properly measures the construct of interest; and (2) reliable, in that the resulting measure is replicable and consistent. Improving construct validity is indeed an important open problem in AI benchmarks (Raji et al., 2021), but our work focuses on improving reliability by proposing methods that provide credible intervals on performance.
Critiques of AI evals. Many works have proposed ways to improve AI assessments through benchmarking. For example, Siska et al. (2024) challenge the representativeness of certain questions in a benchmark on real-life tasks; Myrzakhan et al. (2024) convert multiple choice benchmarks to open-ended questions and show that LLMs perform worse on open-ended questions. Both works question the validity of benchmarks in measuring the relevant ability (in this case, tasks in deployment). Some other works tackle the problem of data contamination in artificially inflating benchmark performance (Dong et al., 2024; Singh et al., 2024). Our work can be interpreted as a way to circumvent data contamination by generating artificial perturbations in the input data (that is presumably unseen before). Vendrow et al. (2025) tackle a different definition of “reliability”: achieving 100% performance on saturated, relatively easy benchmarks in which LLMs supposedly excel, yet still make unexpected mistakes.
2Though admittedly not based on benchmark data.
2

Closely related to our work is the literature on LLM prompt sensitivity. Zhuo et al. (2024); Errica et al. (2024) propose metrics to quantify prompt sensitivity. Sclar et al. (2023) propose a method to perturb prompt grammar and a method to measure the full range of performance across perturbations, while Mizrahi et al. (2024) empirically demonstrate that perturbations in instruction formatting can distort leaderboard rankings. Building on these findings, we propose methods for robust inference and reporting of AI capabilities that explicitly account for prompt sensitivity. More broadly, our critique targets the lack of theoretical grounding in how evaluations conceptualize capability.

## 2 BACKGROUND: A TALE OF TWO MODELS
In this section, we introduce two test models that underpin much of the theory of measuring human abilities. Classical Test Theory (CTT) is primarily concerned with accuracy, while Item Response Theory (IRT) models latent ability. We later adapt both to the context of AI evals.

2.1 CLASSICAL TEST THEORY (CTT)

Originating in the early 20th century, CTT models an observed test score ϕ as the sum of a true score θ and random error ϵ (Raykov & Marcoulides, 2011):

ϕ “ θ ` ϵ.

(1)

Assumption 1 requires that ϵ has mean zero and is independent of θ. It is mainly a behavioral assumption on human test-takers: that humans only make random errors that are independent to their true score3. Thus, repeated tests converge on the true score, or equivalently, θ is the expected score over parallel forms of a test (Lord & Novick, 2008). Importantly, ϵ conflates randomness in the test-taker and randomness induced by the quality of the test. In our setting, we treat the latter as exogenous because our goal is not in measuring the quality of questions4. Rather, holding test quality fixed, we demonstrate that measuring capability in AI models poses different challenges to humans because of the structural differences in measurement error.
Assumption 1. Under the CTT model in (1), Erϵs “ 0 and Covpθ, ϵq “ 0.

2.2 ITEM RESPONSE THEORY (IRT)

Modern psychology and educational testing incorporates IRT, a latent trait framework that models ability θ as driving the probability of a correct response. For example, the Rasch model specifies

fipθq “ Prpϕi “ 1 | θq “ σpθ ´ biq,

(2)

where bi is item difficulty. Observed responses are noisy Bernoulli draws,

ϕi “ fipθq ` ϵi,

(3)

with fi given by, e.g., (2). By modeling ability as a function of item parameters, IRT produces more robust estimates and underlies adaptive testing used in exams like the SAT (College Board, 2025). IRT also implicitly satisfies Assumption 1, see Proposition 4.

### 2.3 CONVENTIONAL BENCHMARKS FALL UNDER CTT

In practice, CTT reduces to averaging correctness across items, assuming all questions are equally informative. This mirrors AI evals, which almost always report aggregate accuracy. Formally, let

ϕi “ θi ` ϵi,

(4)

so that θ “ Eirθis5. Unlike IRT, which posits a single latent ability generating item-level probabilities, this formulation treats per-item performance as noisy but unbiased.

In short, CTT captures accuracy, while IRT captures ability. We will use θ to denote both, clarifying from context which interpretation applies.

3Another implicit assumption is that humans make independent errors across test questions, which is a strong assumption and yet commonplace (even later in the IRT model) for its convenient statistical properties. We refer the interested reader to cognitive diagnostic models (Williamson, 2023). In the context of AI evals, generative models do exhibit independent errors across questions, and thus this difference is less relevant.
4Though this is an important epistemological question around reliability and validity. 5Disaggregating by item i is uncommon in standard CTT models, which typically care about test-wide performance only. However, Assumption 1 still holds under (4) by asserting that Erϵis “ 0, Covpθi, ϵiq @i.

3

3 FRAMEWORK FOR ROBUST INFERENCE OF CAPABILITIES

Our framework consists of two parts:

Part 1: Start with a theory of AI capability

Part 2: Develop inference strategies from that theory

In particular, we argue that conventional benchmarks assume a theory of capability (4) that is misspecified and incorrectly assume Assumption 1. For example, numerous empirical evidence suggests that AI does not exhibit semantic generalization and are sensitive to perturbations (Mizrahi et al., 2024; Sclar et al., 2023; Zheng et al., 2023; Zhuo et al., 2024; Errica et al., 2024; Du et al., 2022). Another problem is that experiments are often done with specific choices of hyperparameters (such as top-p sampling or temperature) and additional context/environment variables (e.g., system prompts). We present an example of a more nuanced model of AI capability under the CTT model:

ϕi “ θi ` spxiq ` rphq ` gpcq ` ¨ ¨ ¨ ` ϵi,

(5)

where xi captures input for item i (e.g., phrasing), h is AI hyperparameters, and c is additional context/environment. s, r, and g are deterministic functions that bias and confound estimation of θi when xi, h, c are chosen improperly. We add “. . . ” to emphasize that other problems exist that further confound robust evaluations, see Section 6.2 for further discussion. From this theory of capability,
we can then develop inference strategies, as we demonstrate in Section 5. As a proof of concept, in
the remainder of this paper we apply our framework to only one of these aforementioned problems: sensitivity to perturbations.

## 4 PART 1: MODEL OF AI CAPABILITY

CTT Model. Following (5), we focus on model sensitivity to perturbations:

ϕi “ θi ` spxiq ` ϵi.

(6)

Assumption 2. Let Pi be the distribution of all natural perturbations of question/concept i. Then, Exi„Pi rspxiqs “ 0.

Critically, we make Assumption 2, which assumes that phrasing of a particular question i results in systematically different true accuracies θi ` spxiq. However, a generative model can still have a notion of true performance θi that is in expectation over natural perturbations of the same question.

IRT Model. We present a revised model of AI ability under the IRT model:

ϕi “ f pθ, xiq ` ϵi,

(7)

where, under the one-parameter model for example,

f pθ, xiq “ σpθ ´ biq ` spxiq

is a probability and ϵi is stochasticity from the Bernoulli random trial. We similarly impose that Assumption 2 holds. Then, Proposition 3 states that θ is similarly unidentifiable.

### 4.1 BENCHMARK CURATION VIOLATES AN INDEPENDENCE ASSUMPTION
For ease of exposition, the remainder of this section will focus on the CTT model, though the same argument holds trivially for the IRT model as well, see e.g. Proposition 3. Assume we have a benchmark dataset D :“ txiuni“1. We can think of a generative model over benchmark data as a two step process — Stage 1: Sampling over the question/concept space P. Stage 2: Sampling over the phrasing space for each question Pi.
Our claim is that most benchmarks are independently sampling from P in Stage 1, but are dependently sampling from Pi in Stage 2. Indeed, one can view P as being implicitly constructed by the benchmark curator; given a certain set of questions (e.g., some proportion of math and reading comprehension questions), P can be constructed such that questions are sampled independently from that distribution. However, conditional on question i, Pi is induced by nature and out of the benchmark curator’s control. Since Pi is high-dimensional and unknowable in practice, the benchmark curator

4

creates question phrases that are correlated with each other and thus generates dependent samples from Pi. This dependent sampling makes it impossible to identify θi under (6), which is not the case under (4). We formally state this in Proposition 1. All proofs can be found in Appendix C.
Proposition 1. Under (6), if phrasing is dependently sampled from Pi, then θi is not identifiable: for any constant c, the pair pθi ` c, spxq ´ cq yields the same distribution over ϕi.
In Section 4.3, we test this hypothesis by demonstrating that most benchmarks induce performance estimates that are systematically biased (i.e., does not recover true accuracy θ).

### 4.2 RANDOM PERTURBATIONS FOR PSEUDO-INDEPENDENCE
We propose a simple method to recover true accuracy θ. Again, as we noted above, the same argument applies trivially for recovering true ability θ under IRT (3). The key idea is to randomly generate perturbations that reasonably represent the space of possible answers. Generate mi natural perturbations for each question i – perhaps using a very capable generative model (Mizrahi et al., 2024) or using grammatical rules (Sclar et al., 2023). We now have a new benchmark dataset D˜ :“ ttxi,jujm“i1uni“1, where the perturbations for question i effectively create pseudo-independent samples from Pi. We can now re-write the ability parameter indexed by perturbations j: ϕij “ θi ` spxijq ` ϵi. It is straightforward to show that if xij are almost like independent draws of Pi, we can recover θi, as in Proposition 5.
Examples of perturbations. The set of “natural” perturbations can encompass a variety of changes, such as perturbing the instruction prompt (Mizrahi et al., 2024), ordering of answer choices (Zheng et al., 2023), and the question prompt itself (Sclar et al., 2023). Regardless, all relevant information should still be conveyed clearly.
Effect of Scaling, Reasoning, and Test-time Inference. Assuming a fixed benchmark (i.e., fixed correlation of phrases), a natural question is the extent to which θˆi remains biased as V arpsq “ σs2 shrinks with larger models that incorporate sophisticated post-processing such as reasoning and test-time inference. Formally, Proposition 6 shows that as a generative model becomes more robust to perturbations for a particular question/dataset, the number of samples mi needed to reach a good enough estimate shrinks linearly with σs2.
However, we believe accounting for sensitivity remains crucial for two reasons: (1) State-of-theart models will continue to struggle with frontier problems (as we demonstrate in Section 4.3.2), and much attention is directed to these hardest problems that AI cannot yet solve. (2) Even on “saturated” benchmarks with easier problems, generative models are unlikely to achieve perfect semantic generalizability (Vendrow et al., 2025), and quantifying their sensitivity (as in Equation 8) is still an important exercise to calibrate the public’s expectations on robustness.

### 4.3 SYSTEMATIC BIAS EXPERIMENTS

#### 4.3.1 EXPERIMENTS ON OPEN-SOURCE MODELS

Setup. We test on two benchmarks, Big-Bench Hard (BBH) (Suzgun et al., 2023) and LMEntry (Efrat et al., 2023), both of which have perturbed versions from (Mizrahi et al., 2024). Each dataset contains sub-tasks testing different concepts, and we use four from each category. For LMEntry, we use all words from category (AWFC), first alphabetically (FA), more letters (ML), and rhyming word (RW). For BBH, we use causal judgment (CJ), movie recommendation (MR), formal fallacies (FF), and snarks (S). We test 7 open-source autoregressive language models from three model families: Llama-3.2 (1B and 3B parameters), Qwen-2.5 (1.5B, 3B, 7B parameters), and gemma (1B, 4B params). All models were instruction-tuned. See Appendix D.1 for more details on the experiment setup.

Benchmarks Induce Systematically Biased Estimates. We demonstrate that conventional bench-

marks induce some systematic bias under our behavioral model. Formally, we will define

ϕiorig “ θi ` si ` ϵi, where as above si “ spxiq is for notational convenience since there is

only

one

xi

per

question.

In

order

to

disentagle

θi

and

si,

we

need

to

estimate

θˆi

“

1 mi

řmi
j“1

ϕij

as justified above. Then, we have sˆi “ ϕoirig ´ θˆi as a noisy estimate of si. Finally, we define

sˆ¯

“

1 n

řn
i“1

sˆi

as

the

mean

estimated

bias

term

over

all

questions

in

the

benchmark

dataset.

5

Figure 2: (a) Systematic bias between estimates of performance based on the original benchmark data (ϕoirig) and estimate of true performance accounting for natural perturbations. (b) Mean absolute distance M , quantifying
the expected deviation in performance for a new question/prompt from the benchmark distribution. Results are
over all eight tasks from LMEntry and BBH, tested on three select LLMs. See Appendix D.1.2 for more results.

Figure 3: Same as Figure 2 but with gpt-4.1 and gpt-4.1-mini models and only on MR, GPQA data.

Figure 2 shows that indeed, original benchmark datasets are systematically biased on open-source LLMs. We show results on all tested models in Appendix D.1. 38 out of 56 experiments reveal a systematic bias between the original benchmark dataset and the perturbed data with pseudoindependent samples of phrasing. Notably, there is no noticeable pattern in the direction of bias across LLMs; for example, for RW, Llama-3B exhibits a negative bias on the original benchmark, while Qwen-7B and gemma-4b exhibit positive bias. In the worst case, estimated performance from the original data can deviate by up to 15 percentage points in either direction when the model is tested with a perturbed dataset. This can distort leaderboards of model capability as we demonstrate in Figure 7, which aligns with previous findings (Mizrahi et al., 2024; Sclar et al., 2023). However, we frame model sensitivity in the context of a systematic bias in inferring model capability.

Reporting LLM Sensitivity. While the above analysis shows that on average original benchmarks

are biased, the error bars only capture variability in data and not variability due to model sensitivity.

Here, we investigate how sensitive various models are to perturbations. We need not assume that

we generate sufficiently large m perturbations to simulate psuedo-independent samples. Instead, let

ϕ¯i

“

1 mi

řmi
j“1

ϕij

,

which

may

or

may

not

converge

to

θi.

We

define

the

following

metric:

mean absolute distance (MAD):

Mi “

1 mi

mi
ÿ |ϕij
j“1

´

ϕ¯i|

@i P D.

(8)

We then recover an empirical distribution of the random variable M over the benchmark dataset. The random variable M gives a full probabilistic statement on how performance may vary on random datapoint from the benchmark distribution P.6 Figure 2(b) shows the distribution of M for various datasets and across models. Across all models, variance is quite high, and one can expect anywhere
from 10-50 percentage points (p.p.) deviation in accuracy among perturbations for a given datapoint.

4.3.2 EXPERIMENTS ON STATE-OF-THE-ART (SOTA) MODELS
Setup. We test gpt-4.1 and gpt-4.1-mini on two datasets: MR as described above and GPQA (Rein et al., 2024). GPQA contains multiple-choice, graduate-level science questions. We use gpt-4.1-mini to randomly generate question perturbations on GPQA. gpt-4.1 achieves 71% and 47% accuracy on the original benchmarks MR and GPQA, while gpt-4.1-mini achieve 65% and 47%, respectively. See Appendix D.2 for details on the experiment setup, including dataset tasks and perturbation procedure. We only test on MR due to budget constraints.
6This is different from other works, which generally aim to quantify sensitivity as a worst-case bound (Sclar et al., 2023), as a point estimate (Zhuo et al., 2024), or measures sensitivity at the raw output level rather than the performance level (Errica et al., 2024).

6

Algorithm 1 Clustered Bootstrap for Estimating Accuracy (CBA)

Require: Observed scores tϕiju for i “ 1, . . . , n, prompts per item tmiu, number of resamples B

1: Initialize empty vector T Ð r s

2: for b Ð 1 to B do

Ź one bootstrap draw

3: Sample with replacement n indices Ipbq Ď t1, . . . , nu

4: for all i P Ipbq do

5:

Compute

per-item

mean

θˆipbq

Ð

1 mi

řmi
j“1

ϕij

6: end for

7:

Compute

bootstrap

replicate

θˆpbq

Ð

1 n

ř
iPIpbq

θˆipbq

8: Append θˆpbq to T

9: end for 10: return Empirical distribution T “ r θˆp1q, . . . , θˆpBq s

Ź Use its percentiles for a p1 ´ αq CI

SoTA models exhibit systematic bias on frontier benchmarks. Figure 3 shows that both models tested still exhibit some amount of bias between the original estimate and the perturbed estimate, by at most 8 percentage points for MR on gpt-4.1-mini. In general, both models are more robust than the smaller models tested (D spans 0-30 p.p. compared to 10-50 p.p. for smaller models). However, these results suggest that gpt-4.1 models are still highly sensitive to perturbations.

## 5 PART 2: INFERENCE STRATEGIES

We have proposed theories of capability, where θ can be accuracy (as in CTT from (6)) or ability (as in IRT from (7)). We now build on this theory and propose two methods to infer capability θ from benchmark data, one for accuracy and another for ability.

### 5.1 CTT: INFERRING ACCURACY VIA CLUSTERED BOOTSTRAPPING

From

(6),

we

estimate

θˆ

“

1 n

řn
i“1

θˆi,

which

gives

strong

guarantees

asymptotically,

see

Prop.

2.

Proposition 2.

From Proposition 5, let θˆ “

1 n

řn
i“1

θˆi

be

an

estimator

for

θ

“

1 n

řn
i“1

θi.

Suppose

Varpθˆi ´ θiq “ σi2 ă 8 and let σ2

“

limnÑ8

1 n

řn
i“1

σi2,

assuming

the

limit

exists

and

the

Lindeberg condition holds. Then as n Ñ 8:

θˆ Ñas θ,

? n

pθˆ

´

θq

Ñd

N `0, σ2˘.

Clustered Bootstrapping. In practice, σ2 can be quite hard to estimate. One standard solution for constructing valid confidence intervals is bootsrapping. In this case, we have a hierarchical structure, and works on this topic (Ren et al., 2010; Field & Welsh, 2007) suggest bootstrapping only the highest-level of the hierarchy (i.e., questions) and not the lower-level (i.e., perturbations). We can assume that questions (clusters) are independent and identically distributed from some distribution P as per Section 4.1. And since our statistic (mean) is a smooth function, the bootstrap approximates a valid CLT distribution by standard results (Bickel & Freedman, 1981). The bootstrap procedure (CBA) is outlined in Algorithm 1.

Reducing computational complexity. In practice, specifying a constant number of perturbations m “ mi for all i can be computationally prohibitive given a finite budget. In Appendix E.1, we propose a two-step optimal sampling procedure using Neyman allocation (Neyman, 1992).

### 5.2 IRT: INFERRING LATENT ABILITY VIA ADAPTIVE TESTING

Whereas the previous strategy is concerned with accuracy, we propose an alternative method for inferring latent ability using IRT. Formally, suppose we have an ecosystem of K models. We assume that each model k has a latent ability θk and the probability of a correct answer is modeled by:

Pijkpθq “ Prpϕijk “ 1|θk, bi, ai, xijq “ σpaipθk ´ biqq ` spxijq,

(9)

where ai and bi are discrimination and difficulty parameters for question i respectively, spxijq adds systematic bias conditional on prompt, and σp¨q is a logistic function. By adding s, we are extending

7

Feature
Interpretation of θ Model assumptions Addl. data required Under finite budget

CBA (Algorithm 1)
Accuracy over dataset Simple additive model (6) None Decide nsamples a priori, larger SE

LAAT (Algorithm 2)
Ability relative to prior (e.g. N p0, 1q) Probabilistic model w/ item params (9) Infer item parameters (ai, bi) a priori Adapt test up to budget, tighter SE

Table 1: Key differences between bootstrap method and adaptive testing method.
the classic two-parameter IRT model (Raykov & Marcoulides, 2011) to account for perturbations that confound inference on θ, since s is unlearnable. This model allows us to infer ability with fewer samples because certain questions are more informative than others, but it also requires more information about the question features (difficulty and discrimination) a priori. Note that the idea to incorporate IRT to reduce sample complexity has similarly been proposed (Zhuang et al., 2023; Maia Polo et al., 2024), but we are the first to propose an adaptive test that accounts for prompt sensitivity, which is critical for obtaining valid estimates.
Adaptive Testing Setup. First, we need to obtain good estimates of ai, bi, see Appendix F.1 for the inference procedure we use, of which there are many well-established ones. Then, using the item parameters, we infer ability for each model k using the adaptive test in Algorithm 2.7 Note that we drop the subscript k because we are now holding the model fixed. The key idea of this adaptive test is to ask questions that are most informative in updating our estimate of ability θ, where informativeness is measured by Fisher information Ii. See Appendix E.2.1 for detailed derivations and proofs.

Algorithm 2 Latent Ability Adaptive Test (LAAT)

Require: Item parameters tpai, biquNi“1, stopping criterion C, prior mean µ0, prior variance σ02, stopping

threshold ε, and constant number of perturbations m

1:

Initialize: θ Ð µ0, I

Ð

1 σ02

,

t

Ð

1,

A

Ð

H

2: while stopping criterion C not met, do

Ź loop until budget or precision

3: Select i˚ “ arg maxiRA Iipθq, Iipθq “ mai2 P¯ipθq p1 ´ P¯ipθqq, P¯ipθq “ σpaipθ ´ biqq

4: A Ð A Y ti˚u

5: Query model on m perturbations of item i˚ to get scores tϕi˚jujm“1

6:

ϕi˚

Ð

1 m

řm
j“1

ϕi˚ j

7:

Compute

S

Ð

ř
iPA

mai`ϕi

´

P¯ipθq˘,

I

Ð

ř
iPA

ma2i

P¯ipθq

p1

´

P¯ipθqq

8:

Update

(Newton–Raphson):

θ

Ð

θ

`

S I

9: t Ð t ` 1

10: end while

?

11: return ability estimate θ, standard error 1{ I, items asked A

We highlight one key observation: LAAT is possible because we impose stronger assumptions about the data generating process (9). While this is a widely-accepted parametric model (Baker, 2001), inferences on ability will be misspecified if the true data generating process is different from (9). Another assumption is that we must a priori obtain item parameters ai, bi that are properly calibrated to the true data generating process. We summarize the key differences between both inference strategies in Table 1, and discuss fundamental limitations of both methods in Section 6.2.
### 5.3 EMPIRICAL STUDY
We use the same datasets and models as our experiments in Section 4.3.1. Figures 4(a) and (b) show estimates of accuracy and ability from Algorithms 1 and 2, respectively, over seven LLMs on three select benchmark tasks. We show the full suite of results in Appendix F.2 . Generally, the ordering in model rankings is consistent between the two methods. However, LAAT yields more separation between models when bootstrapping cannot. For example, Qwen-3.5B on S benchmark has the highest inferred performance using both methods, but LAAT infers much higher ability for that model compared to the rest because it happens to perform well on harder questions. This result is despite LAAT requiring fewer samples, requiring only 4-27% of the full benchmark dataset to achieve comparable standard errors.
7We can technically recover θ jointly in the first step when we infer ai, bi. However, this first step should be a preliminary stage to obtain ai, bi given a fixed prior on θ. Ideally, this inference step should include a large sample of models that are representative of the population of interest, and are intended only to calibrate ai, bi.

8

Figure 4: (a) Estimates of accuracy using CBA (Alg. 1, and (b) Estimates of ability using LAAT (Alg. 2), on three benchmark tasks (FA, ML from LMentry and S from BBH) and over seven open-source LLMs. Numbers in bold indicate number of questions asked in the adaptive test. For CBP, the number of questions asked is 500 for FA, ML and 178 for S. Each question is associated with 20 random perturbations.
## 6 DISCUSSION
### 6.1 TAKEAWAYS AND CONCRETE RECOMMENDATIONS
Theories of ability inform inference methods. Our work demonstrates that starting from a theory of measuring ability naturally yields methods for robustly inferring parameters of interest. This pipeline provides a principled and defensible framework for inference of AI capabilities.
Report sensitivity metrics in addition to overall accuracy or ability. Metrics like MAD (8) properly calibrate people’s expectations of how variable performance may be in single uses of the model, rather than in expectation. The models we experimented with could result in up to 50 percentage points over or under the reported accuracy when given perturbed inputs.
Scaling. As models become more capable and semantically robust, it remains crucial to both quantify uncertainty and report sensitivity metrics. We demonstrated in Section 4.3.2 that systematic biases remain even in larger state-of-the-art models (gpt-4.1) for frontier benchmark tasks, and that these models can still be unreliable even when given simple perturbations.
Which to measure: accuracy or ability? Table 1 outlines key differences between both methods proposed in this work, where θ have fundamentally different interpretations. While accuracy aligns with the classical machine learning paradigm of evals, measuring ability allows for more efficient inference methods that may yield a more meaningful understanding of model capabilities. Regardless of which paradigm the field evolves toward, standardizing best practices and quantities of interest is fundamental to ensure fair and accurate comparisons across different evals.
### 6.2 LIMITATIONS AND FUTURE WORK
Other issues confounding evaluations. While our methods focused on tackling sensitivity to perturbations, many other issues exist as described in Section 3 (e.g., effect of hyperparameters and additional context). Our work is merely a proof of concept of this framework, and future work should incorporate these additional robustness measures in evals.
Construct validity remains a crucial issue. Our work mainly focuses on benchmark reliability rather than ensuring that benchmarks truly assess the construct of interest to begin with. Perhaps benchmarks may be fundamentally limited in this regard (Raji et al., 2021), but psychometrics may provide more insights to improve the construct validity of benchmarks (Wang et al., 2023).
Assumptions on our model of ability. In proposing models for AI ability, we are making assumptions about how generative models behave based on empirical evidence. The IRT model (9) imposes even stronger structural assumptions, and in general these models can be misspecified or missing key components (e.g., other sources of uncertainty). As our understanding of generative models’ cognitive abilities evolve, so too should these models and respective inference methods evolve.
Of course, even defining parameters such as question difficulty and latent ability poses philosophical questions. What does it mean for a question to be fundamentally difficult to solve, and how should or does that relate to a notion of ability? In our work, ability and difficulty are measured on a specific benchmark task, and over a finite set of models. But researchers have recently posited that generative models have a uni-dimensional measure of general intelligence/ability (Ilic´ & Gignac, 2024), which begs the question of how to properly test its existence and robustly measure it. We view our work as contributing to an exciting body of work on the science of benchmarks (Hardt, 2025) and measuring artificial general intelligence (Mitchell, 2024), of which there is much to understand.
9

REFERENCES
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. arXiv preprint arXiv:2303.08774, 2023.
Norah Alzahrani, Hisham Alyahya, Yazeed Alnumay, Sultan Alrashed, Shaykhah Alsubaie, Yousef Almushayqih, Faisal Mirza, Nouf Alotaibi, Nora Al-Twairesh, Areeb Alowisheq, et al. When benchmarks are targets: Revealing the sensitivity of large language model leaderboards. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 13787–13805, 2024.
Dominik Bachmann, Oskar van der Wal, Edita Chvojka, Willem H Zuidema, Leendert van Maanen, and Katrin Schulz. fl-irt-ing with psychometrics to improve nlp bias measurement. Minds and Machines, 34(4):37, 2024.
Frank B Baker. The basics of item response theory. ERIC, 2001.
Frank B Baker and Seock-Ho Kim. Item response theory: Parameter estimation techniques. CRC press, 2004.
Peter J Bickel and David A Freedman. Some asymptotic theory for the bootstrap. The annals of statistics, 9(6):1196–1217, 1981.
Robert L Brennan. Generalizability theory. In The history of educational measurement, pp. 206–231. Routledge, 2021.
George Casella and Roger Berger. Statistical inference. CRC press, 2024.
Pin-Yu Chen and Cho-Jui Hsieh. Adversarial robustness for machine learning. Academic Press, 2022.
Wei-Lin Chiang, Lianmin Zheng, Ying Sheng, Anastasios Nikolas Angelopoulos, Tianle Li, Dacheng Li, Banghua Zhu, Hao Zhang, Michael Jordan, Joseph E Gonzalez, et al. Chatbot arena: An open platform for evaluating llms by human preference. In Forty-first International Conference on Machine Learning, 2024.
François Chollet. On the measure of intelligence. arXiv preprint arXiv:1911.01547, 2019.
College Board. How scores are calculated, 2025. URL https://satsuite.collegeboard. org/scores/what-scores-mean/how-scores-calculated. Accessed: 2025-0514.
Yihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, Bin Gu, Mengfei Yang, and Ge Li. Generalization or memorization: Data contamination and trustworthy evaluation for large language models. arXiv preprint arXiv:2402.15938, 2024.
Mengnan Du, Fengxiang He, Na Zou, Dacheng Tao, and Xia Hu. Robustness challenges of large language models in natural language understanding: A survey, 2022.
Avia Efrat, Or Honovich, and Omer Levy. Lmentry: A language model benchmark of elementary language tasks. In Findings of the Association for Computational Linguistics: ACL 2023, pp. 10476–10501, 2023.
Maria Eriksson, Erasmo Purificato, Arman Noroozian, Joao Vinagre, Guillaume Chaslot, Emilia Gomez, and David Fernandez-Llorca. Can we trust ai benchmarks? an interdisciplinary review of current issues in ai evaluation. arXiv preprint arXiv:2502.06559, 2025.
Federico Errica, Giuseppe Siracusano, Davide Sanvito, and Roberto Bifulco. What did i do wrong? quantifying llms’ sensitivity and consistency to prompt engineering. arXiv preprint arXiv:2406.12334, 2024.
Christopher A Field and Alan H Welsh. Bootstrapping clustered data. Journal of the Royal Statistical Society Series B: Statistical Methodology, 69(3):369–390, 2007.
10

Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948, 2025.
Moritz Hardt. The emerging science of machine learning benchmarks. Online at https:// mlbenchmarks.org, 2025. Manuscript.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. Measuring massive multitask language understanding. In International Conference on Learning Representations, 2021. URL https://openreview.net/forum?id= d7KBjmI3GmQ.
José Hernández-Orallo, Bao Sheng Loe, Lucy Cheke, Fernando Martínez-Plumed, and Seán Ó hÉigeartaigh. General intelligence disentangled via a generality metric for natural and artificial intelligence. Scientific reports, 11(1):22822, 2021.
David Ilic´ and Gilles E Gignac. Evidence of interrelated cognitive-like capabilities in large language models: Indications of artificial general intelligence or achievement? Intelligence, 106:101858, 2024.
Moxin Li, Wenjie Wang, Fuli Feng, Yixin Cao, Jizhi Zhang, and Tat-Seng Chua. Robust prompt optimization for large language models against distribution shifts. arXiv preprint arXiv:2305.13954, 2023.
Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar, et al. Holistic evaluation of language models. Transactions on Machine Learning Research, 2023. ISSN 2835-8856. URL https:// openreview.net/forum?id=iO4LZibEqW. Featured Certification, Expert Certification, Outstanding Certification.
Stephanie Lin, Jacob Hilton, and Owain Evans. TruthfulQA: Measuring how models mimic human falsehoods. In Smaranda Muresan, Preslav Nakov, and Aline Villavicencio (eds.), Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 3214–3252, Dublin, Ireland, May 2022. Association for Computational Linguistics. doi: 10.18653/v1/2022.acl-long.229. URL https://aclanthology.org/2022.acl-long. 229/.
Frederic M Lord and Melvin R Novick. Statistical theories of mental test scores. IAP, 2008.
Felipe Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, and Mikhail Yurochkin. tinyBenchmarks: evaluating LLMs with fewer examples. In Ruslan Salakhutdinov, Zico Kolter, Katherine Heller, Adrian Weller, Nuria Oliver, Jonathan Scarlett, and Felix Berkenkamp (eds.), Proceedings of the 41st International Conference on Machine Learning, volume 235 of Proceedings of Machine Learning Research, pp. 34303–34326. PMLR, 21–27 Jul 2024. URL https:// proceedings.mlr.press/v235/maia-polo24a.html.
Evan Miller. Adding error bars to evals: A statistical approach to language model evaluations. arXiv preprint arXiv:2411.00640, 2024.
Melanie Mitchell. How do we know how smart ai systems are?, 2023.
Melanie Mitchell. Debates on the nature of artificial general intelligence, 2024.
Moran Mizrahi, Guy Kaplan, Dan Malkin, Rotem Dror, Dafna Shahaf, and Gabriel Stanovsky. State of what art? a call for multi-prompt llm evaluation. Transactions of the Association for Computational Linguistics, 12:933–949, 2024.
Aidar Myrzakhan, Sondos Mahmoud Bsharat, and Zhiqiang Shen. Open-llm-leaderboard: From multi-choice to open-style questions for llms evaluation, benchmark, and arena. arXiv preprint arXiv:2406.07545, 2024.
Jerzy Neyman. On the two different aspects of the representative method: the method of stratified sampling and the method of purposive selection. In Breakthroughs in statistics: Methodology and distribution, pp. 123–150. Springer, 1992.
11

Jorge Nocedal and Stephen J Wright. Numerical optimization. Springer, 1999.
Oona Rainio, Jarmo Teuho, and Riku Klén. Evaluation metrics and statistical tests for machine learning. Scientific Reports, 14(1):6086, 2024.
Deborah Raji, Emily Denton, Emily M. Bender, Alex Hanna, and Amandalynne Paullada. Ai and the everything in the whole wide world benchmark. In J. Vanschoren and S. Yeung (eds.), Proceedings of the Neural Information Processing Systems Track on Datasets and Benchmarks, volume 1, 2021. URL https: //datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/ 2021/file/084b6fbb10729ed4da8c3d3f5a3ae7c9-Paper-round2.pdf.
Tenko Raykov and George A Marcoulides. Introduction to psychometric theory. Routledge, 2011.
David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R. Bowman. GPQA: A graduate-level google-proof q&a benchmark. In First Conference on Language Modeling, 2024. URL https://openreview. net/forum?id=Ti67584b98.
Shiquan Ren, Hong Lai, Wenjing Tong, Mostafa Aminzadeh, Xuezhang Hou, and Shenghan Lai. Nonparametric bootstrapping for hierarchical data. Journal of Applied Statistics, 37(9):1487–1498, 2010.
Pedro Rodriguez, Joe Barrow, Alexander Miserlis Hoyle, John P Lalor, Robin Jia, and Jordan Boyd-Graber. Evaluation examples are not equally informative: How should that change nlp leaderboards? In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers), pp. 4486–4503, 2021.
Melanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane Suhr. Quantifying language models’ sensitivity to spurious features in prompt design or: How i learned to start worrying about prompt formatting. arXiv preprint arXiv:2310.11324, 2023.
Aaditya K Singh, Muhammed Yusuf Kocyigit, Andrew Poulton, David Esiobu, Maria Lomeli, Gergely Szilvasy, and Dieuwke Hupkes. Evaluation data contamination in llms: how do we measure it and (when) does it matter? arXiv preprint arXiv:2411.03923, 2024.
Charlotte Siska, Katerina Marazopoulou, Melissa Ailem, and James Bono. Examining the robustness of llm evaluation to the distributional assumptions of benchmarks. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 10406–10421, 2024.
Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao, Abu Awal Md Shoeb, Abubakar Abid, Adam Fisch, Adam R. Brown, Adam Santoro, Aditya Gupta, Adrià Garriga-Alonso, et al. Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. Transactions on Machine Learning Research, 2023. ISSN 2835-8856. URL https://openreview.net/ forum?id=uyTL5Bvosj. Featured Certification.
Mirac Suzgun, Nathan Scales, Nathanael Schärli, Sebastian Gehrmann, Yi Tay, Hyung Won Chung, Aakanksha Chowdhery, Quoc Le, Ed Chi, Denny Zhou, et al. Challenging big-bench tasks and whether chain-of-thought can solve them. In Findings of the Association for Computational Linguistics: ACL 2023, pp. 13003–13051, 2023.
Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, Katie Millican, et al. Gemini: a family of highly capable multimodal models. arXiv preprint arXiv:2312.11805, 2023.
David Thissen and Lynne Steinberg. An intellectual history of parametric item response theory models in the twentieth century. Chinese/English Journal of Educational Measurement and Evaluation, 1 (1):5, 2020.
Clara Vania, Phu Mon Htut, William Huang, Dhara Mungra, Richard Yuanzhe Pang, Jason Phang, Haokun Liu, Kyunghyun Cho, and Samuel R Bowman. Comparing test sets with item response theory. arXiv preprint arXiv:2106.00840, 2021.
12

Joshua Vendrow, Edward Vendrow, Sara Beery, and Aleksander Madry. Do large language model benchmarks test reliability? arXiv preprint arXiv:2502.03461, 2025.
Xiting Wang, Liming Jiang, Jose Hernandez-Orallo, David Stillwell, Luning Sun, Fang Luo, and Xing Xie. Evaluating general-purpose ai with psychometrics. arXiv preprint arXiv:2310.16379, 2023.
Joanna Williamson. Cognitive diagnostic models and how they can be useful. research report. Cambridge University Press & Assessment, 2023.
Yukun Zhao, Lingyong Yan, Weiwei Sun, Guoliang Xing, Shuaiqiang Wang, Chong Meng, Zhicong Cheng, Zhaochun Ren, and Dawei Yin. Improving the robustness of large language models via consistency alignment. arXiv preprint arXiv:2403.14221, 2024.
Chujie Zheng, Hao Zhou, Fandong Meng, Jie Zhou, and Minlie Huang. Large language models are not robust multiple choice selectors. arXiv preprint arXiv:2309.03882, 2023.
Wanjun Zhong, Ruixiang Cui, Yiduo Guo, Yaobo Liang, Shuai Lu, Yanlin Wang, Amin Saied, Weizhu Chen, and Nan Duan. Agieval: A human-centric benchmark for evaluating foundation models. arXiv preprint arXiv:2304.06364, 2023.
Yan Zhuang, Qi Liu, Yuting Ning, Weizhe Huang, Zachary A Pardos, Patrick C Kyllonen, Jiyun Zu, Qingyang Mao, Rui Lv, Zhenya Huang, et al. From static benchmarks to adaptive testing: Psychometrics in ai evaluation. arXiv preprint arXiv:2306.10512, 2023.
Jingming Zhuo, Songyang Zhang, Xinyu Fang, Haodong Duan, Dahua Lin, and Kai Chen. Prosa: Assessing and understanding the prompt sensitivity of llms. arXiv preprint arXiv:2410.12405, 2024.
13

A OTHER RELATED WORK
Psychometric principles in AI evaluations (continued). Another stream of literature involves using item response theory (IRT) – the predominant paradigm of psychometric testing – to improve the reliability of AI evals (Rodriguez et al., 2021; Bachmann et al., 2024) or to improve efficiency by filtering only on test data that are informative of AI ability (Vania et al., 2021; Maia Polo et al., 2024). One of our contributions also involves IRT testing, but we are the first to propose IRT that accounts for sensitivity to input perturbations. We also present the IRT-based method in an adaptive setting following (Zhuang et al., 2023).
Artificial General Intelligence (AGI). Definitions of general intelligence vary widely, though a popular definition is to achieve good performance on a variety of tasks (Hernández-Orallo et al., 2021). A second definition of intelligence is the ability to acquire new skills by building on skills taught by the training data, similar to how human knowledge and skills are an accumulation of experiences and priors through life (Chollet, 2019). In our framing, we are more concerned with measuring capabilities on benchmarks that are often task-specific, which falls better under the first definition. However, benchmarks have grown to test much broader skills that can be aggregated (e.g., general knowledge (Hendrycks et al., 2021), general standardized tests (Zhong et al., 2023)). There even exists a benchmark designed to measure the second definition of intelligence (see ARG-AGI). Our proposed model must be extended to accommodate these more general benchmarks, but the principled pipeline remains the same: we should understand AI’s cognitive capabilities (and converge on a definition of intelligence) in order to devise methods to infer this latent parameter.
(Adversarial) robustness. There is a mature literature on adversarial robustness in deep learning, canonically in the context of noise-injected images that result in misclassification (Chen & Hsieh, 2022). In the same vein, there is a growing literature on the robustness of LLMs. However, perturbations need not be adversarial in natural language. Instead, one can “naturally” perturb the input space and still induce degraded performance. For example, previous works have shown that LLMs are not robust to changes in ordering of multiple choice questions (Zheng et al., 2023) and changes in instruction phrasing (Mizrahi et al., 2024). Du et al. (2022) attributes this behavior to LLMs learning non-robust features, such as lexical, style, and positional biases, which in turn results in degraded “out-of-distribution” performance. In turn, some recent work (Li et al., 2023; Zhao et al., 2024) propose methods to improve LLM robustness. Our work accounts for natural language perturbations to improve the robustness of AI evaluations, rather than in the training process.

B LIMITATIONS AND FUTURE WORK (CONTINUED)
Quality of perturbations. We assume that perturbations are of high-quality and are not confusing. In general, it is hard to disentangle the effect of question quality and the effect of model sensitivity to perturbations. As such, we interpret our results as an upper bound on model sensitivity, confounded by question quality. Future work might attempt to disentangle these two effects using more sophisticated methods like generalizability theory (Brennan, 2021).

C PROOFS AND OTHER PROPOSITIONS

Proposition 3. Under (7), if phrasing is dependently sampled from Pi, then θ is not identifiable: for any constant c, the pair pθ ` c, spxq ´ cq yields the same distribution over ϕi.

Proof. Denote the parameter tuple by α “ pθi, sq, and write Pθi,s for the joint distribution of a single observation ϕij. Under the model,

ϕij

ˇ ˇ

xij

„

N `θi ` spxijq, σ2˘.

Define a second parameterization

θi1 “ θi ` c, s1pxq “ spxq ´ c,

for an arbitrary constant c. Then

θi1 ` s1pxq “ pθi ` cq ` `spxq ´ c˘ “ θi ` spxq,

14

so for every x,

N `θi1 ` s1pxq, σ2˘ “ N `θi ` spxq, σ2˘.

It follows that

Pθi1 , s1 “ Pθi, s.

Since θi1 ‰ θi whenever c ‰ 0, we have found two distinct parameter settings that induce the same distribution on the data. Thus pθi, sq is non-identifiable.

Proposition 4. Under the IRT model (2)–(3), the residuals ϵi “ ϕi ´ fipθq satisfy Erϵis “ 0, Cov`θ, ϵi˘ “ 0.

Hence IRT implicitly meets Assumption 1.

Proof. The key to this proof is that and assuming local independence (i.e. the responses tϕiu are conditionally independent given θ),

By definition of the model,

ϕi “ fipθq ` ϵi,

so equivalently ϵi “ ϕi ´ fipθq.
1. Zero mean. Since ϕi | θ „ Bernoulli`fipθq˘,

Erϵi | θs “ Erϕi | θs ´ fipθq “ fipθq ´ fipθq “ 0.

Taking the outer expectation gives

Erϵis “ E“Erϵi | θs‰ “ 0.

2. Zero covariance. We compute

”

ı

Covpθ, ϵiq “ E“pθ ´ Erθsq ϵi‰ “ E E“pθ ´ Erθsq ϵi | θ‰ .

Inside the inner expectation, θ is fixed, so E“pθ ´ Erθsq ϵi | θ‰ “ pθ ´ Erθsq Erϵi | θs “ pθ ´ Erθsq ¨ 0 “ 0.
Hence Covpθ, ϵiq “ 0.

Proposition 5.

If xij

is independently sampled from Pi, then define an estimator θˆi

“

1 mi

řmi
j“1

ϕij

.

By

Assumption

2,

we

have

θˆi

as
Ñ

θi

as mi Ñ 8

Proof. Taking expectations,

Erϕij s “ θi ` Erspxij qs ` Erϵij s A“sn. 2 θi ` 0 ` 0 “ θi.

Since the ϕij are (pseudo-)independent draws with finite mean, the Strong Law of Large Numbers

gives

θˆi

“

1 mi

mi
ÿ ϕij
j“1

Ñas

Erϕijs “ θi,

as mi Ñ 8.

Proposition 6 (Finite Sample Concentration for θi). Define the same estimator as above: θˆi “

1 mi

řmi
j“1

ϕij .

Then,

to

guarantee

|θˆi

´

pθi

`

ϵiq|

ď

ε

with

probability

at

least

1

´

δ,

mi

ě

2σs2 ε

ˆ2˙ ln ,
δ

where σs2 “ Varjrspxijqs, provided that spxijq satisfies Assumption 2 and is sub-Gaussian.

15

Proof. Define the centered random variables

Yj “ ϕij ´ pθi ` ϵiq “ spxij q,

so
1
mi

that Y1, . . .

řmi
j“1

Yj

is

, Ymi itself

are i.i.d. sub-Gaussianp0, σs2q. In sub-Gaussian with parameter σs2{mi.

particular, their empirical Standard sub-Gaussian tail

mean Y¯ “ bounds give,

for any t ą 0,

Pr`|Y¯ | ě t˘

ď

2

´ exp ´

mi t2 2 σs2

¯ .

Since θˆi ´ pθi ` ϵiq “ Y¯ , we obtain

Pr´ˇˇθˆi

´

pθi

`

ϵiqˇˇ

ě

¯ t

ď

2

´ exp ´

mi t2 2 σs2

¯ .

Set the right-hand side equal to δ, solve for t, and note that the bound holds with probability 1 ´ δ:

d

2

´ exp ´

mi t2 2 σs2

¯

“

δ

ùñ

t “ σs

2 lnp2{δq . mi

This yields the stated concentration inequality. Rearranging to solve for mi in order to achieve |θˆi ´ pθi ` ϵiq| ď ε with probability 1 ´ δ gives

´ exp ´

mi ε2 2 σs2

¯

“

δ 2

ùñ

mi “

2 σs2 ε2

´2¯ ln ,
δ

completing the proof.

C.1 PROOF OF PROPOSITION 3

Proof. Define a shifted parameterization

θ1 “ θ ` c, s1pxq “ spxq ´ c.

Then for every phrasing xi,

f

pθ1,

xiq

`

s1pxiq

“

“σpθ

`

c

´

bi

‰ q

`

“spxiq ´ c‰ “ σpθ ´ biq ` spxiq “ f pθ, xiq.

Hence

Prpϕi “ 1 | θ1, s1q “ Prpϕi “ 1 | θ, sq,

and similarly for Prpϕi “ 0q. Because the entire Bernoulli law is unchanged, no statistical procedure can distinguish pθ, sq from pθ1, s1q. In other words, θ is not identifiable whenever phrasing-induced
shifts spxq admit a nonzero constant component.

C.2 PROOF OF THEOREM 2

Proof. Write

θˆ “

1 n

n
ÿ

θˆi

and

1

n
ÿ

θ “ n θi,

i“1

i“1

so that

θˆ ´ θ

“

1 n

n
ÿ pθˆi

´ θiq.

i“1

By Proposition 5, each θˆi is an (almost-surely) consistent estimator of θi, hence θˆi ´ θi Ñ 0 a.s.

Since the differences tθˆi ´ θiuin“1 are independent with finite variance, Kolmogorov’s Strong Law of

Large Numbers implies

1 n

n
ÿpθˆi ´ θiq

as
Ñ

0,

i“1

and therefore θˆ Ñas θ.

16

Table 2: Description of each benchmark task, along with the number of datapoints.

Task LMEntry Any word from category First alphabetically
More letters
Rhyming word
BBH Causal Judgment
Movie Recommendation Formal Fallacies
Snarks
GPQA

Description
Yes or no question – decide if any of the five words belong to a given category One of two words – decide which comes first alphabetically One of two words – decide which one has more letters One of two words – decide which one rhymes with a given word
Yes or no question – decide if the statement is causal in nature Given four movies, decide which of the four options is most similar. Determine whether or not the argument is deductively valid. Determine which of the two statements is sarcastic.
Decide which of the four options is factually correct.

Number of datapoints
3,000 (randomly sampled 500) 3,000 (randomly sampled 500) 3,000 (randomly sampled 500) 3,000 (randomly sampled 500)
146
250
250
178
448

Next, set Xi “ θˆi ´ θi, so that ErXis “ 0 and VarpXiq “ σi2 ă 8. By the Lindeberg–Feller Central Limit Theorem for independent (but not necessarily identically distributed) variables, provided the
Lindeberg condition holds,

1 ?n

n
ÿ

Xi

Ñd

´ N 0, lim
nÑ8

1 n

n
ÿ

¯ σi2 .

i“1

i“1

Noting

that

?n pθˆ ´ θq

“

?1 n

řn
i“1

Xi

,

we

obtain

the

stated

asymptotic

normality

with

variance

σ2

“

limnÑ8

1 n

řn
i“1

σi2.

D BIAS EXPERIMENT DETAILS

D.1 SMALLER MODELS
D.1.1 SETUP
Datasets. We test on two benchmarks, Big-Bench Hard (BBH) (Suzgun et al., 2023) and LMEntry (Efrat et al., 2023), both of which have perturbed versions from (Mizrahi et al., 2024). Each dataset contains sub-tasks testing different concepts, and we use four from each category. For LMEntry, we use any word from category (AWFC), first alphabetically (FA), more letters (ML), and rhyming word (RW). For BBH, we use causal judgment (CJ), movie recommendation (MR), formal fallacies (FF), and snarks (S). See Tables 2 and 3 for details of each task.
Table 3: Sample question and perturbation for each of the benchmark datasets tested.

Task

Sample

LMEntry

Continued on next page

17

Table 3 – continued from previous page

Task

Sample

All word from category

Sample Question: Q: Are all of the words "peach", "couch", "coat", "truck", and "shirt" types of animals? Answer either "yes" or "no". A: Sample Perturbation: Is "animal" represented by all of the words "peach", "couch", "coat", "truck", and "shirt"? Please respond with a "yes" or "no".

First alphabetically

Sample Question: Q: In an alphabetical order, which of the words "beach" and "silver" comes first? A: Sample Perturbation: Which word precedes the other in alphabetical order, "silver" or "beach"?

More let- Sample Question: Q: Which word has more letters, "fit" or "rice"? A:

ters

Sample Perturbation: Which of the two words, "rice" or "fit", is longer?

Rhyming word
BBH Causal Judgment

Sample Question: Q: Which word rhymes with the word "declare", "beer" or "wear"? A: Sample Perturbation: Which word, "bear" or "wear", rhymes with the word "declare"?
Sample Question: How would a typical person answer each of the following questions about causation? Brown is playing a simple game of dice. The game requires that Brown roll a six to win. So, hoping to get a six, Brown throws a die onto the table. Unluckily for the other players, the die lands six-up and Brown wins the game. Did Brown intentionally roll a six? Options: - Yes - No Sample Perturbation: Given a question about causation, classify whether a typical person would answer with "Yes" or "No". Question: Brown is playing a simple game of dice. The game requires that Brown roll a six to win. So, hoping to get a six, Brown throws a die onto the table. Unluckily for the other players, the die lands six-up and Brown wins the game. Did Brown intentionally roll a six? Answer:

Movie Recommendation

Sample Question: Find a movie similar to Batman, The Mask, The Fugitive, and Pretty Woman: Options: (A) The Front Page (B) Maelstrom (C) The Lion King (D) Lamerica Sample Perturbation: Please suggest a movie that is similar to Batman, The Mask, The Fugitive, and Pretty Woman. You can choose from the following options: (A) The Lion King (B) Lamerica (C) The Front Page (D) Maelstrom

Continued on next page

18

Task Formal Fallacies
Snarks
GPQA GPQA

Sample

Table 3 – continued from previous page

Sample Question: Here comes a perfectly valid argument: First, being a cousin of Chris is sufficient for not being a son of Kermit. We may conclude that whoever is not a son of Kermit is a cousin of Chris. Is the argument, given the explicitly stated premises, deductively valid or invalid? Options: - valid - invalid Sample Perturbation: Q: Is the argument, given the explicitly stated premises, deductively valid or invalid? First, being a cousin of Chris is sufficient for not being a son of Kermit. We may conclude that whoever is not a son of Kermit is a cousin of Chris.
Sample Question: Which statement is sarcastic? Options: (A) Hey, just be happy then you won’t be depressed anymore (B) Hey, just be happy that you won’t be depressed anymore Sample Perturbation: Which of the following sentences is sarcastic? Options: (A) Hey, just be happy then you won’t be depressed anymore (B) Hey, just be happy that you won’t be depressed anymore Answer:

Sample Question: In a parallel universe where a magnet can have an isolated North or South pole, Maxwell’s equations look different. But, specifically, which of those equations are different? Options: (A) The ones related to the circulation of the electric field and the divergence of the magnetic field. (B) The ones related to the divergence and the curl of the magnetic field. (C) The one related to the divergence of the magnetic field. (D) The one related to the circulation of the magnetic field and the flux of the electric field. Sample Perturbation: In an alternate universe where magnets can possess a lone North or South pole, how do Maxwell’s equations change? Which particular equations differ in this scenario? Options: (A) The ones related to the circulation of the electric field and the divergence of the magnetic field. (B) The one related to the circulation of the magnetic field and the flux of the electric field. (C) The ones related to the divergence and the curl of the magnetic field. (D) The one related to the divergence of the magnetic field.

We use all questions from all benchmarks except for LMEntry, where we randomly sampled 500 questions from each task due to computational constraints. The perturbed dataset of LMEntry and BBH (Mizrahi et al., 2024) consist of different instruction formatting that was generated by both a very capable LLM and manual human labor. All prompts have been checked manually by human annotators. Each task (from both LMEntry and BBH) has around 150 distinct formatting perturbations, from which we randomly sampled 20 for each question, again due to computational constraints. Apart from the formatting perturbations, we also perturbed multiple choice order when relevant.
Models. We test 7 open-source autoregressive language models from three model families: Llama-3.2 (1B and 3B parameters), Qwen-2.5 (1.5B, 3B, 7B parameters), and gemma (1B, 4B params). All models were instruction-tuned. For each model, we use a temperature of 0.9. For each question, we sample 20 times to account for output stochasticity. Then, we parse each question using

19

Figure 5: Systematic bias between estimates of accuracy based on the original benchmark data and estimate of true performance accounting for natural perturbations, across eight benchmark tasks and tested on seven LLMs.
Figure 6: Mean absolute distance M , quantifying the expected deviation in performance for a new question/prompt from the benchmark distribution. Results are over all eight benchmark tasks, tested on seven LLMs. soft regex rules tailored to the question type. Note that we do not use LLM as a judge because the questions all present multiple answer choices, and thus answers were relatively easy to extract from raw outputs. We obtain θi for each question i by averaging correctness over the 20 queries. The same procedure also applies to the original benchmark data, with the exception that each question was not associated with 20 different perturbations. All experiments were done using one NVIDIA L40 GPU. D.1.2 ADDITIONAL RESULTS Figures 5 and 6 present the average systematic bias induced by the original benchmark (s¯) and the distribution of mean average distance (Mi from (8)) for all 7 models tested, over the eight benchmark tasks. Given this systematic bias, leaderboard rankings can be distorted as seen in Figure 7. First, we note that the error bars for the perturbed dataset are significantly smaller than the original dataset – this is
Figure 7: Estimated accuracies with bootstrap confidence intervals, over the original benchmark [top] and over the perturbed benchmark [bottom], for all eight benchmark tasks and over seven LLMs.
20

because by averaging over 20 perturbations, we are reducing some of the internal variance in our estimate. This reduction in uncertainty allows us to better compare model performances even before considering re-rankings. For example, Qwen-1B and Qwen-3.5B are quite undifferentiated for the original S, we see sufficient separation between the two estimated accuracies for the perturbed S. Additionally, perturbed data could result in re-rankings. For example, for the original CJ, Qwen-3.5B outperforms Qwen-7B and Gemma-1B outperforms Gemma-4B, but the ordering is flipped for the perturbed CJ – which is the ordering we would have expected given the difference in model sizes.
D.2 STATE-OF-THE-ART MODELS
Datasets. We use two datasets, movie recommendation (MR) from BBH as described above, and GPQA. GPQA contains multiple-choice, graduate-level questions from the natural sciences (e.g., mathematics, chemistry). The questions are designed to be hard, in that non-experts cannot easily Google the question and retrieve the correct answer. For each question, we generate five random perturbations using gpt-4.1-mini using the following prompt: Please generate 5 different perturbations of the prompt below, keeping all the pertinent information but expressed in a different way. When the prompt gives multiple choices, DO NOT SHUFFLE THE OPTIONS, but feel free to re-word each option. Be as clear as possible. Structure your response with "Perturbation 1: [PROMPT] Perturbation 2: [PROMPT]" and so on. Prompt:
All of the questions were qualitatively checked to ensure that the perturbations remain clear and do not lose any pertinent information. Then, we randomly shuffle the answer choices and add them onto the question to construct the full input prompt. See Table 3 for an example.
Models. We test gpt-4.1 and gpt-4.1-mini, state-of-the-art autoregressive language models. We use gpt-4.1-mini to randomly generate question perturbations on GPQA. gpt-4.1 achieves 71% and 47% accuracy on the original benchmarks MR and GPQA, while gpt-4.1-mini achieve 65% and 47%, respectively. This suggests that GPQA is a frontier dataset, since even the best current models (save for reasoning/test-time inference) are incorrect most of the time on that benchmark. For each model, we use a temperature of 0.7. For each question, we sample 5 times to account for output stochasticity. Then, we parse each question using soft regex rules tailored to the question type, and recover θi by averaging correctness for each query. All experiments were done through API calls to OpenAI.8

E INFERENCE METHODS

E.1 OPTIMAL SAMPLING UNDER BUDGET CONSTRAINT

Given budget B, we can optimize the number of samples mi for each question i using Neyman allocation (Neyman, 1992). Assume that B is the number of times we can query the LLM. We treat each question i as an equally weighted stratum. Given the standard deviation in performance of each stratum σi (i.e., how much performance deviates across perturbations of the same question), the optimal sample size is given by:

mi

“

σiB

řn
j“1

σj

.

However, σi is unknown a priori, so we need to first estimate it. We propose a two-step procedure in Algorithm 3.

8See https://openai.com/api/.

21

Algorithm 3 Two-Step Neyman Allocation Procedure

Require: Budget B, number of questions n, initial sample size m0 Ensure: Allocation of total samples mi “ mip0q ` mip1q for each question i 1: [Step 1] Initial Sampling:

2: for each question i “ 1 to n do

3: Query the LLM m0 times for question i to obtain responses tϕijum j“01

4:

Compute

empirical

mean:

θˆi

“

1 m0

řm0
j“1

ϕij

5:

Estimate

standard

deviation:

σˆi

“

b
1
m0 ´1

řm0
j“1

pϕij

´

θˆiq2

6: end for

7: Compute remaining budget: B1 “ B ´ n ¨ m0

8: [Step 2] Neyman Allocation:

9: for each question i “ 1 to n do

10:

Allocate

additional

samples:

mip1q

“

Y σˆiB1

řn
j“1

σˆj

]

11: Total samples for question i: mi “ m0 ` mip1q

12: end for

13: return tmiuin“1, tϕij um j“01

E.1.1 TRADE-OFF BETWEEN n, mi AND REPEATED SAMPLING
So far, we’ve discussed given a fixed n, how to choose mi for each question i. For some large datasets, however, n is too large given one’s budget. In this case, we recommend choosing some small m ě 3 for each question to get a sufficient estimate of variance, and backing out how much n one can afford with B queries. This is because in order for confidence intervals to be accurate, we need enough m to simulate “independent” draws of question phrasings. However, we need sufficient n since it is the most influential in reducing variance.
Note that we do not advocate for repeated sampling of outcomes for every perturbation to reduce the variance of ϵi. This is because we are sampling independently, and that variance term will wash out as n becomes large.

E.2 ITEM RESPONSE THEORY (DETAILS)

E.2.1 ADAPTIVE TESTING ALGORITHM (DETAILS)

We formally justify the Newton–Raphson update rule used in our adaptive testing algorithm to

estimate the latent ability parameter θ. From (7), we let Pipθq “ σpaipθ ´ bi ´ δqq, where we

drop the subscript k since we are fixing a given model. Let ai, bi denote the known discrimination

and difficulty of item i, and suppose the model answers item i with m independently perturbed

prompts, each with a score ϕij.

Let

ϕi

“

1 m

řm
j“1

ϕij

P

r0, 1s

denote

the empirical average

of correct

responses over m samples. Note that by definition of (7), we have

ϕij|xij „ Bernoulli`Pij˘, Pij “ σ`aipθ ´ biq ` spxijq˘,

Proposition 7.

Let Yi

“

řm
j“1

ϕij .

Then,

ϕi1, . . . , ϕim are i.i.d. Bernoulli`P¯ipθq˘, P¯ipθq “ σpaipθ ´ biqq

and hence

Yi „ Binomial`m, P¯ipθq˘.

At time T , Binomial`m,

wP¯iepθhq˘a,vwe eahdamveinaisltiekreeldihotoid1,f.u.n.citTio´n1fuorqYue: stion

so

far.

Then, since Yi „

T ´1

T ´1

Lpθq “ ź P¯it pθqYit p1 ´ P¯it pθqqpm´Yit q “ ź P¯it pθqmϕit p1 ´ P¯it pθqqpm´mϕit q

t“1

t“1

22

and we can derive the log-likelihood:

T ´1

ℓpθq “ ÿ m “ϕit log P¯it pθq ` p1 ´ ϕit q logp1 ´ P¯it pθqq‰ .

(10)

t“1

Proposition 8 (Newton–Raphson Update for Ability). Given the log-likelihood function (10), the

Newton–Raphson update

θ

Ð

θ

`

Spθq I pθq

,

where

T ´1
Spθq “ ÿ m ait `ϕit ´ P¯it pθq˘,
t“1

T ´1
Ipθq “ ÿ m ai2t P¯it pθq`1 ´ P¯it pθq˘,
t“1

is a consistent one-step update toward the maximum likelihood estimate of θ.

Moreover, under standard regularity conditions, the observed Fisher information Ipθˆq yields an asymptotically valid 95% confidence interval of the form:

d

θˆ ˘ 1.96 ¨

1 Ipθˆq .

E.2.2 PROOF OF PROPOSITION 7

Proof. Since the prompts xij are drawn i.i.d. from Pi, and each offset spxijq is a deterministic function of xij, the sequence tspxijqujm“1 is i.i.d. with

E“spxijq‰ “ 0.

Conditional on xij, we have

Pr`ϕij

“ 1 | xij ˘ “ pij

“

σ`aipθ

´

bi

˘ q

`

spxij q.

By the law of total probability,

Prpϕij

“

1q

“

Ex“Prpϕij

“

1

|

xq‰

“

”

ı

Ex σ`aipθ´biq˘`spxq

“

σ`aipθ´biq˘

`

Exrspxqs

“

P¯ipθq.

Similarly, Prpϕij “ 0q “ 1 ´ P¯ipθq. Moreover, for j ‰ k, the draws ϕij and ϕik are marginally independent because they depend on independent prompts xij and xik and—conditional on those—are independent Bernoulli draws. Formally, for any x, y P t0, 1u,

Prpϕij “ x, ϕik “ yq “ Exij,xik “Prpϕij “ x | xij q Prpϕik “ y | xikq‰ “ Prpϕij “ xq Prpϕik “ yq. Hence ϕi1, . . . , ϕim are i.i.d. Bernoulli`P¯ipθq˘, and thus

m

ÿ Yi “ ϕij

„

Binomial`m, P¯ipθq˘,

j“1

completing the proof.

E.2.3 PROOF OF PROPOSITION 8

Proof. 1. Score and information. Differentiating (10) term-by-term gives:

ℓ1pθq

“

T
ÿ

m

d” dθ ϕit

log P¯it

`

p1

´

ϕit q logp1

´

P¯it

ı q

“

T
ÿ

m ait `ϕit

´

P¯it pθq˘,

t“1

t“1

and
T
ℓ2pθq “ ´ ÿ m ai2t P¯it pθq`1 ´ P¯it pθq˘.
t“1
2. Existence and uniqueness of MLE. Because each term in (10) is twice continuously differentiable

23

in θ, and because
T
ℓ2pθq “ ´ ÿ m a2it P¯it pθq`1 ´ P¯it pθq˘ ă 0 @ θ,
t“1
the log-likelihood is strictly concave and has a unique maximizer θˆ.

3. Asymptotic normality of the MLE. Under the regularity conditions for i.i.d. logistic-type models (existence of bounded third derivatives, identifiability, see (Casella & Berger, 2024)), the MLE θˆ

satisfies

? T

pθˆ

´

θq

ÝÑd

N`0,

I pθq´1 ˘,

where Ipθq “ ´Erℓ2pθqs is the Fisher information. Equivalently

θˆ « N`θ, Ipθˆq´1˘,

which yields the Wald interval θˆ ˘ 1.96 Ipθˆq´1{2.

4. Newton–Raphson convergence. Since ℓpθq is twice continuously differentiable and strictly concave, and ℓ2pθˆq ‰ 0, classical results guarantee that the Newton–Raphson iterates converge quadratically to θˆ whenever the initial guess θp0q is in a neighborhood of θˆ (Nocedal & Wright,
1999).

F INFERENCE EXPERIMENT DETAILS
F.1 INFERENCE OF ITEM PARAMETERS
Assume we have an ecosystem of K generative models. We will use Laplace-approximated marginal maximum likelihood estimation, which places priors on parameters θ, integrates them out by taking their mode (using Laplace approximation), then directly maximizes the marginal likelihood over the remaining parameters. Note that any valid inference method will work, and there are wellestablished methods in the literature; for example, Thissen & Steinberg (2020) outline an expectationmaximization (EM) algorithm and a Markov chain Monte Carlo algorithm based on Bayesian inference. Note that these parameters are identifiable as long as either θk or bi are anchored (Baker & Kim, 2004), hence why we anchor θk to be mean zero and variance one through our prior θk „ N p0, 1q.
Preliminaries. Recall from Proposition 7 that ϕijk „ BernoullipP¯ikpθqq, P¯ikpθq “ σpaipθk ´ biqq,
where we re-introduce the index k because we have multiple models now). We therefore have
m
Yik “ ÿ ϕijk „ Binpm, P¯ikpθqq.
j“1
Log-Likelihood. We now derive the log-likelihood for which we optimize. Let ξ “ ta1, . . . , an, b1, . . . , bn, θ1, . . . , θK q capture the set of parameters we want to infer. By Bayes rule, ppξ|Y q 9 ppY |ξqppξq and thus

log ppξ|Y q 9 log ppY |ξq ` log ppξq.
Since Y follows a binomial distribution,
nK
log ppY |ξq “ ÿ ÿ “Yik log P¯ik ` pm ´ Yikq logp1 ´ P¯ikq‰ .
i“1 k“1
For the prior likelihood, we a prior on θk so that parameters are identifiable. In particular, θk „ N p0, 1q, which yields
log ppθq “ ´0.5 ÿ θk2.
k

24

Figure 8: Estimates of accuracy using CBA (Algorithm 1) on eight benchmark tasks and over seven open-source LLMs.

Figure 9: Estimates of ability using LAAT (Algorithm 2) on eight benchmark tasks and over seven open-source LLMs. Numbers in bold indicate number of questions asked in the adaptive test. Each question is associated with 20 random perturbations.

In sum, we have the following posterior log likelihood:

ℓpost

“

ÿ

“Yik

log

P¯ik

`

pm

´

Yik q

logp1

´

P¯ik

‰ q

´

1 2

ÿ

θk2 .

(11)

i,k

k

We then minimize ´ℓpost using L-BFGS-B9 over rlog ai, bi, θks, and taking the exponentials over log ai to enforce positivity.
We summarize the procedure below:
1. Construct ℓpost on parameter vector ξ˜ “ rlog ai, bi, θks. 2. Optimize ´ℓpost using L-BFGS-B 3. Recover ξ by taking aˆi “ expplogˆaiqq.

F.2 ADDITIONAL DETAILS AND RESULTS
We provide details on our implementation of Algorithm 2 in our experiments. In particular, we used the following stopping criterion: stop when the difference in standard errors between the most recent iteration and the previous one is less than 0.0001. This stopping condition allows us to stop inference until we have squeezed out as much information as possible from the given questions; any additional questions will only improve our estimates marginally.
Figures 8 and 9 show inferences of accuracy and ability based on Algorithms 1 and 2, respectively, on all eight benchmark tasks and over seven open-source LLMs.

9See https://docs.scipy.org/doc/scipy/reference/optimize.minimize-lbfgsb. html.
25
