# Evaluating the Evaluations: A Perspective on Benchmarks

OPINION PAPER

Evaluating the Evaluations: A Perspective on Benchmarks

Omar Alonso
Amazon Palo Alto, CA, USA omralon@amazon.com

Kenneth Church
Northeastern University Boston, MA, USA
k.church@northeastern.edu

## Abstract
More and more benchmarks, datasets, and evaluation tasks are becoming available. This is extremely useful for the community because it enables researchers and practitioners to test and evaluate new techniques. However, the construction, evaluation, and maintenance of data sets and benchmarks is opaque which creates problems with respect to stability and true representations. Our position is that we need to revisit how we design and implement benchmarks. The SPEC benchmark offers interesting perspectives that our community should consider. We use a data set of influential papers and resources to discuss important benchmark aspects such as realistic workloads, reliability, validity, leakage, and labeling. We conclude by proposing a list of principles for constructing evaluation benchmarks.

## 1 Introduction
Evaluation and benchmarking are at the center of IR, NLP, ML, and related areas. Quantifying improvements of new methods is very important for measuring progress. There are a huge number of datasets and benchmarks available online. There will surely be even more such resources in the future because these resources are extremely useful for the community; they have made it possible for researchers and practitioners to test and evaluate new techniques. Testing and evaluating the quality of a model can be done in a few steps and provide signal on next steps. A problem with this black-box approach is dependence on assumptions that are often unstated, involving data quality, reliability and validity.
Because these resources play such a crucial role, we think that there should be more in-depth assessment and peer reviewing, not only of methods but also of benchmarks. This also applies in industrial settings where domain specific evaluations are conducted. The construction, evaluation, and maintenance of such benchmarks should not only be more transparent but should also be held to software engineering standards.
The data collection, validation, and curation processes of different benchmarks and evaluation data sets raise a number of methodological concerns. Business decisions based on missing
Work does not relate to the author’s position at Amazon.

ACM SIGIR Forum

1

Vol. 58 No. 2 – December 2024

data points, incorrect values, stale values and misleading values can lead to disastrous customer experience and low adoption.
Experiments are an important part of the research process in our community and one may argue that it is very difficult to get published without them. Given the importance of experiments and benchmarks in our field, we’re interested in evaluating the evaluations.
To improve reliability, a benchmark should be structured to enable users to measure agreement of labels from different sources. A common problem with validity is leakage. If there is leakage between the training and test sets, it is possible to do well on the test without mastering the material. The tendency to increase the number of tasks makes it difficult to ensure high quality in terms of validity and reliability. To ensure transparency, a benchmark should share necessary details, especially on data collection and label assignment.
Tasks should be relevant to use cases. There should be more characterizations of use cases and workloads in our field. A benchmark can be misleading if the sample is not representative of a population of interest. A benchmark needs to be used as a learning tool for researchers and practitioners and not only as leader board.
We start by listing influential papers and resources, organized by dimensions of success. As part of our data analysis, we identify issues and challenges. As an example, from a design perspective, the TREC QA benchmark seems more technically solid compared to SQuAD but it has fewer citations. We conclude the paper with a list of principles that are especially important for highstakes use cases with commercial relevance.

## 2 Analysis of Influential Articles
Consider the following dimensions of success: 1. Awards: Test of Time 2. Popularity Metrics: Citations in Google Scholar and Semantic Scholar [Wade, 2022], likes on HuggingFace (HF),1 stars on Papers with Code (PwC)2 3. Interdisciplinary Impact: Benchmarks that appeal to more fields and larger fields tend to be more influential (in terms of popularity metrics) than those that appeal to fewer fields. 4. Technical Merit: Reliability, Validity, etc. 5. Commercial Impact: See Section 3.2.
We will discuss three tables that list a number of influential papers along with popularity metrics such as citations in Semantic Scholar:
 Table 1 lists some influential TREC papers sorted by popularity.  Table 2 shows papers that won Test of Time awards up to 2017 [Allan et al., 2017], sorted
by time.  Table 3 lists some influential resources, benchmarks and models in IR and related fields.
Before discussing these tables in more detail, we are concerned that benchmarks have a way of taking on a life of their own, as will be discussed in Section 5 on the Penn TreeBank (PTB).
1https://huggingface.co/ 2https://paperswithcode.com/

ACM SIGIR Forum

2

Vol. 58 No. 2 – December 2024

Cites 2360 1138 1071 707 629 459 457 406 397 393 393 385 329 308 245 179 177 173

Reference [Robertson et al., 1994] [Voorhees, 1999] [Gonza´lez and G´omez, 2007] [Voorhees, 2004] [Buckley et al., 1994] [Garofolo et al., 2000] [Hersh et al., 2007] [Clarke et al., 2009] [Robertson et al., 1995] [Craswell et al., 2020] [Voorhees and Tice, 2000] [Craswell et al., 2005] [Craswell et al., 2021] [Jaleel et al., 2004] [Ounis et al., 2011] [Roberts et al., 2014] [Voorhees and Hersh, 2012] [Alonso and Mizzaro, 2012]

Title Okapi at TREC-3 The TREC-8 Question Answering Track Report TREC: Experiment and evaluation in information retrieval Overview of the TREC 2003 Question Answering Track Automatic Query Expansion Using SMART: TREC 3 The TREC Spoken Document Retrieval Track... TREC 2007 Genomics Track Overview Overview of the TREC 2009 Web Track Okapi at TREC-4 Overview of the TREC 2019 deep learning track The TREC-8 Question Answering Track Evaluation Overview of the TREC 2005 Enterprise Track Overview of the TREC 2020 Deep Learning Track UMass at TREC 2004: Novelty and HARD Overview of the TREC 2011 Microblog Track Overview of the TREC 2014 Clinical Decision Support Track Overview of the TREC 2012 Medical Records Track Using crowdsourcing for TREC relevance assessment

Table 1. Citations in Semantic Scholar for some influential TREC papers.

The authors, Marcus et al. [1993], originally designed the PTB for one purpose (parsing), but it has been recently repurposed by the community for a very different use (perplexity) in a way that is not as meaningful as it might appear. Once a benchmark is released into the wild, it has a tendency to take on a life of its own. We, as a community, should be more careful with credit assignment, especially when introducing serious weaknesses into other people’s work.
### 2.1 Benchmarks Should Make a Point
We view benchmark design like Brooks views programming languages. Brooks managed the development of software for IBM mainframe computers and later wrote candidly about that experience in The Mythical Man-Month [Brooks, 1995]. The second author heard Brooks give a talk at Bell Labs in front of the people responsible for Unix. This talk referred to Figure 1 of [Brooks, 1987]:
 More exciting products: Unix, APL, Pascal, Modula, Smalltalk, Fortran  Less exciting products: Cobol, PL/1, Algol, MVS/370, MS-DOS
where Brooks asserted that all of these products were successful, at least in terms of awareness. His point was that the more exciting products were designed by a few remarkable people making a point; the less exciting products were designed by committees making compromises:
The differences are not minor–it is rather like Salieri and Mozart. Study after study shows that the very best designers produce structures that are faster, smaller, simpler, cleaner, and produced with less effort. The differences between the great and the average approach an order of magnitude. [Brooks, 1987]

ACM SIGIR Forum

3

Vol. 58 No. 2 – December 2024

Reference [Katzer et al., 1983]
[Voorhees, 1985] [Rijsbergen, 1986]
[Fagan, 1987] [Jones, 1988] [Harman, 1988] [Furnas et al., 1988]
[Belew, 1989]
[Pejtersen, 1989]
[Turtle and Croft, 1989] [Cutting et al., 1992]
[Callan et al., 1995]
[Xu and Croft, 1996]
[Singhal et al., 1996] [Allan et al., 1998] [Bharat and Henzinger, 1998]
[Ponte and Croft, 1998]
[Carbonell and Goldstein-Stewart, 1998] [Hofmann, 1999] [Berger and Lafferty, 1999] [Herlocker et al., 1999]
[Buckley and Voorhees, 2000] [J¨arvelin and Keka¨l¨ainen, 2000] [Lafferty and Zhai, 2001]
[Lavrenko and Croft, 2001] [Zhai and Lafferty, 2001]

Cites 193
189 215
40 24 13 98
99
59
454 1830
665
1298
612 621 736
695
2014
2094 740 2453
205 1356
198
1742 1321

Title A study of the overlap among document representations The cluster hypothesis revisited A New Theoretical Framework for Information Retrieval Automatic phrase indexing for document retrieval A Look Back and a Look Forward Towards interactive query expansion Information retrieval using a singular value decomposition model of latent semantic structure Adaptive information retrieval: Using a connectionist representation to retrieve and learn about documents A library system for information retrieval based on a cognitive task analysis and supported by an icon-based interface Inference networks for document retrieval Scatter/Gather: a cluster-based approach to browsing large document collections Searching distributed collections with inference networks Query expansion using local and global document analysis Pivoted Document Length Normalization On-line new event detection and tracking Improved algorithms for topic distillation in a hyperlinked environment A language modeling approach to information retrieval The Use of MMR, Diversity-Based Reranking for Reordering Documents and Producing Summaries Probabilistic Latent Semantic Indexing Information retrieval as statistical translation An algorithmic framework for performing collaborative filtering Evaluating Evaluation Measure Stability IR evaluation methods for retrieving highly relevant documents Document language models, query models, and risk minimization for information retrieval Relevance-Based Language Models A study of smoothing methods for language models applied to Ad Hoc information retrieval

Table 2. Award Winning Papers: Test of Time (from [Allan et al., 2017]).

ACM SIGIR Forum

4

Vol. 58 No. 2 – December 2024

Resource/Benchmark/Model
ResNet [He et al., 2016] BERT [Devlin et al., 2019] ImageNet [Russakovsky et al., 2015] GPT-3 [Brown et al., 2020] CIFAR [Krizhevsky et al., 2009] GPT-2 [Radford et al., 2019] Penn TreeBank (PTB) [Marcus et al., 1993] SQuAD [Rajpurkar et al., 2016] GLUE [Wang et al., 2018] LibriSpeech [Panayotov et al., 2015] cc100 [Conneau et al., 2020] Visual Genome [Krishna et al., 2017] PaLM [Chowdhery et al., 2022] IMDB [Maas et al., 2011] Reuters-21578 [Lewis et al., 2004] Natural Questions [Kwiatkowski et al., 2019] SQuAD 2.0 [Rajpurkar et al., 2018] MS Marco [Bajaj et al., 2016] Wikitext-103 [Merity et al., 2016] Switchboard [Godfrey et al., 1992] MNIST [LeCun et al., 2010; Deng, 2012] SuperGLUE [Wang et al., 2019] The Pile [Gao et al., 2020] MUSE [Conneau et al., 2017] CogComp/trec [Li and Roth, 2002] BIG-Bench [Srivastava et al., 2022] Common Voice [Ardila et al., 2020] Brown Corpus [Francis and Kuˇcera, 1982] TIMIT [Garofolo et al., 1983] FLORES [Goyal et al., 2022] ERNIE [Sun et al., 2021] MRQA [Fisch et al., 2019] MUC-3/4 [Sundheim, 1991, 1992] CulturaX [Nguyen et al., 2023] allenai/c4 DuReader [He et al., 2018] Callhome [Canavan et al., 1997] WMT-19 [Wikimedia, 2019]

Semantic Scholar 177,065 84,392 37,332 33,349 32,366 19,527 8802 7492 6415 5791 5743 5258 5168 4894 2997 2699 2591 2394 2346 2245 2163 2089 1682 1587 1529 1432 1334 1262 1067 462 356 285 69/129 60
12

Google Scholar 244,794 119,203
47,929 35,576 31,907 14,289 10,854
8903 7611 7130 6372 6043 5022 6336 3784 2805 3063 786 2408 2936 5750 2309 645 1328 1907 1146 1636
3832 417 463 295 94/155
61
316 223 28

HF Likes
739 1.91k
416 645
62 2.37k
15 265 372 129
74 66
250 16 85
179 123
6 111 113 156 399
40 61 195
21 66 92 20
475 314
10 13

PwC Stars 77,201 135,247
746
1403 1647
256 350
1647 3190
11,655 292
6918

Table 3. Metrics for some influential resources: HF = HuggingFace; PwC = Papers with Code. Note that SQuAD (7492 for [Rajpurkar et al., 2016]) has more citations than TREC-8 (1138 for [Voorhees, 1999]), though TREC-8 is closer to real-world workloads, as discussed in Section 3.3.

ACM SIGIR Forum

5

Vol. 58 No. 2 – December 2024

Committees do what committees do. Bloat is inevitable. Committees are good for reaching consensus, but not for creativity and inspiration. BIG-bench is an example of a committee effort:
BIG-bench currently consists of 204 tasks, contributed by 450 authors across 132 institutions. [Srivastava et al., 2022]
The Mythical Man-Month is deeply skeptical of large teams. It is hard to make a point with hundreds of authors. A benchmark should have a single point (and not too many points); it should be large enough to make that point, and no larger.
SPEC3 [Dixit, 1993] has had more commercial impact than benchmarks in our field because it focuses on a question that matters to an important audience (suppliers and consumers of CPUs): which CPU should I buy? Like many benchmarks in our field, SPEC is a collection of programs (tasks), intended to measure different needs of different users. Some programs are bounded by cycles and some are bounded by memory.
In Summarizing performance is no mean feat, Mashey [2005] argues that geometric means are better than arithmetic means, as a single metric for different customers with different workloads. So too, our benchmarks should be designed to address different workloads. Elsewhere,4 Mashey suggests replacing arithmetic means in our benchmarks with geometric means.5 It is hard to interpret averages over tasks using metrics with incompatible units: accuracy, correlations, F1, etc. If we report performance relative to a baseline, then the units are dimensionless, and can be combined with geometric means.
In this way, SPEC makes an important point, establishing that modern CPUs are 50,000 times faster than they were 40 years ago (relative to a VAX 11/780 in 1978).6 In [Church and Alonso, 2024], we suggest following Mashey’s advice so many of our benchmarks can be used to make a similar point. The tech sector has benefited by its ability to demonstrate remarkable progress over decades. So too, we should be able to use our benchmarks to make statements about performance of LLMs over years/decades relative to a baseline such as human performance. Too many of our benchmarks are used for (pointless) SOTA-chasing [Church and Kordoni, 2022].
## 3 What Has Worked Well in the Past?
This section will discuss Tables 1-3, as well as measures of success: awards (Test of Time), popularity metrics (citations), interdisciplinary impact, technical merit and commercial impact.
### 3.1 Popularity Metrics and Interdisciplinary Impact
Tables 1, 2 & 3 show influential papers with popularity metrics such as citations in Semantic Scholar. Table 2 (Test of Time) is sorted by time, unlike Tables 1 & 3, which are sorted by
3https://www.spec.org/ 4https://github.com/kwchurch/Benchmarking_past_present_future?tab=readme-ov-file#Mashey 5Robertson [2006] suggested using geometric mean to aggregate over items in a test set. 6See slide 9 of https://courses.grainger.illinois.edu/CS433/fa2021/slides/chapter1-part1-post-l ecture.pdf; there is a similar chart in Figure 1.1 of [Hennessy and Patterson, 2012].

ACM SIGIR Forum

6

Vol. 58 No. 2 – December 2024

citations. Citations tend to increase with recency because the literature is expanding rapidly, doubling every decade or two7 [Price, 1965; Bornmann and Mutz, 2014; Bornmann et al., 2021].
It is useful to compare Table 1, influential papers in TREC [Voorhees and Harman, 2005], with Table 3, influential resources in related fields. In addition to recency, citations also increase for resources that appeal to more fields and larger fields. For example, tasks such as question answering have been studied in IR (TREC-8) as well as ML and NLP (SQuAD), though SQuAD has more citations than TREC-8 (7492 versus 1138), perhaps because SQuAD is more recent and it appeals to more fields and larger fields.
Popularity metrics such as citations are a good place to start because they are easy to collect, though there are a number of drawbacks. In particular, although SQuAD may have more citations than TREC-8, we are not convinced that SQuAD is better, as will be discussed below in sections on technical merit and commercial impact.
SOTA-chasing is another drawback. SOTA-chasing attracts even more citations than interdisciplinary appeal, despite the fact that SOTA-chasing encourages pointless activities that are unlikely to generalize to commercially important use cases. TREC has resisted the temptation to promote SOTA-chasing, emphasizing cooperation over competition:8
competing may give you a bigger piece of the pie ... ... while cooperation makes the whole pie bigger 9
TREC participants are asked to sign a form that forbids explicit advertising of TREC results. This prohibition was mentioned a number of times in the videos of the 25th anniversary of TREC.10 While participants appreciate the principle, the temptation to boast is difficult to resist. Since SOTA-chasing is popular, TREC’s rules against SOTA-chasing may have consequences in terms of popularity metrics.
### 3.2 Technical Merit and Constructed Queries
Setting popularity metrics aside for the moment, based on technical merit, how do the benchmarks in Table 3 compare with the the benchmarks in Table 1? When evaluating benchmarks, we should be concerned about classic questions in psychology such as reliability and validity [Krippendorff, 2018], which will be discussed in more detail in Section 4.
More specifically, how does SQuAD compare with TREC-8? One difference involves the methods used to generate questions:
 SQuAD (crowdsourcing): popular in academia (especially when logs are unavailable)  TREC-8 (logs): more common in industry (especially when logs are available)
7https://blogs.nature.com/news/2014/05/global-scientific-output-doubles-every-nine-years.h tml
8https://github.com/kwchurch/Benchmarking_past_present_future/blob/master/README.md#Voorhees 9slides 6-7 of https://github.com/kwchurch/Benchmarking_past_present_future/blob/master/slides/ session3/Ellen_benchmarking.pdf 10https://trec.nist.gov/celebration/25thcelebration.html

ACM SIGIR Forum

7

Vol. 58 No. 2 – December 2024

Here are some examples of questions in TREC-8 and SQuAD:
 TREC-8 questions (from Figure 1 of [Voorhees, 1999]): 1. How many calories are there in a big mac? 2. What two US biochemist won the Nobel Prize in medicine in 1992? 3. Who was the first American in space?
 A SQuAD question with context and gold answer: – Question: What year was the DOE report about fuel consumption published? – Context: Several studies have suggested that DST increases motor fuel consumption. The 2008 DOE report found no significant increase in motor gasoline consumption due to the 2007 United States extension of DST. – Answer: 2008 (starts at character offset 78 in context).
The QA track in TREC started with constructed questions in 1999, but moved to query logs for subsequent TREC QA tracks (2000-2007) because constructed questions are too easy for systems, and unrealistic [Voorhees, 2001]. TREC-8 questions were extracted from logs of a system called FAQFinder [Hammond et al., 1995]. These questions were submitted by undergraduate students “who were genuinely interested in the answers to the questions.”11
SQuAD starts with a context from a Wikipedia article such as this12 and then MTurk workers generate questions based on these contexts. The gold answers are substrings of the context. Note that SQuAD questions often depend on the context, as in this case. When we give the SQuAD question above to search engines in today’s context, they tell us about more recent DOE reports.
Crowdsourcing is a popular strategy for collecting data, especially when you do not have big tech resources. It was used for 9 of 18 question-answering benchmarks in MRQA (See Table 1 in [Fisch et al., 2019]):
 Crowdsourced (9 benchmarks): ComplexWebQ, DROP, DuoRC, HotpotQA, MCTest, NewsQA, QAMR, SQuAD, TREC
 Domain Experts (5 benchmarks): BioASQ, BioProcess, QAST, RACE, TextbookQA  Search logs (1 benchmark): Natural Questions  Jeopardy (1 benchmark): SearchQA  Synthetic (1 benchmark): RelationExtraction  Trivia (1 benchmark): TriviaQA
Industry is more likely to have access to search logs and other instrumentation. Natural Questions [Kwiatkowski et al., 2019] is the only benchmark in MRQA to use search logs. Most of the authors of benchmarks work in academia and do not have access to logs, but Natural Questions is a notable exception.
11See Section 2.1 of [Voorhees and Tice, 2000] 12https://en.wikipedia.org/wiki/Analysis_of_daylight_saving_time

ACM SIGIR Forum

8

Vol. 58 No. 2 – December 2024

3.3 Commercial Impact: Lessons from SPEC
Since TREC is organized by NIST, which is part of the US Department of Commerce, it may not be surprising that benchmarks from TREC would be more closely related to commercial concerns than many of the benchmarks in Table 3. We ran Microsoft Bing and Google on questions in the TREC-8 and SQuAD examples above. Instant answers are more successful for TREC-8 questions than SQuAD questions, suggesting search companies place a higher priority on TREC-8 questions. TREC-8 may come closer to real-world workloads.
In terms of commercial impact, SPEC [Dixit, 1993] has had more influence than most benchmarks in Tables 1-3 because SPEC addresses a question with more commercial importance: which computer should I buy? Customers want a single number, not a long complicated story such as a precision/recall curve. Consumers will not read a thoughtful review like you might see in Consumer Reports. A simple credible number is also good for suppliers. Previous benchmarks such as Whetstone13 and Dhrystone14 encouraged pointless SOTA-chasing exercises that do not generalize to commercial use cases.
## 4 Realistic Use Cases and Workloads
Typical workloads are a moving target in our community. Over the past year or so, usage of AI-based applications has increased considerably. As workloads evolve, so too, benchmarks need to catch up. Ideally, performance on benchmarks should be a leading indicator of what customers will experience, not a lagging indicator. One of the principles in Section 9 involves maintenance and evolution.
The challenge is to come up with a single number that is useful for predicting performance over a wide variety of workloads. SPEC replaced previous benchmarks such as Whetstone and Drystone with a larger set of larger programs, intended to be more representative of typical workloads. The older benchmarks tended to focus on cycles – integer and floating point arithmetic (MIPS and FLOPS); SPEC added concerns that came along later such as workloads that made use of vector arithmetic and memory. It is standard practice in many fields to estimate workloads: databases [Zhang et al., 2018], networking [Calzarossa et al., 2016], and web search [Broder, 2002].
We are facing similar challenges with benchmarks for IR and LLMs. We would like to come up with a single number that generalizes over many (unknown) use cases. One might hope that averaging over many tasks might address this concern, though SPEC was designed to meet the needs of a clearly identified community. For benchmarks such as GLUE, it is harder to characterize (a) typical workloads, (b) user communities and (c) their use cases.
There are a few benchmarks in our field that are based on data from real customers [Kwiatkowski et al., 2019], but most benchmarks in our field were not designed to be representative of typical workloads. SPEC is different from many of the academic benchmarks in our field because many computer companies chose to use SPEC, whereas in our field, companies have their own internal benchmarks that are more representative of the needs of their customers. Going forward, when we build new benchmarks, we should aim to come up with a benchmark like SPEC that is so
13https://www.netlib.org/benchmark/whetstone.c 14https://en.wikipedia.org/wiki/Dhrystone

ACM SIGIR Forum

9

Vol. 58 No. 2 – December 2024

compelling that industry would choose to use our benchmark instead of building their own. When we list principles in Section 9, a key metric of success will be adoption.
There is recent work on search evaluation that suggests moving away from evaluating ranking quality to a more utilitarian approach [Broder and McAfee, 2023]. The authors argue that algorithmic ranking partially determines search utility and that there are search engine aspects (or features) that help users with their tasks. Thus, we think that a realistic workload should be as close as possible to user goals. There should be fewer tasks that are more relevant, as opposed to many irrelevant tasks, found in many benchmarks.

## 5 Benchmark Deep-Dive into the Penn TreeBank (PTB)

This section will do a deep dive into the Penn TreeBank (PTB) [Marcus et al., 1993], a benchmark that is often used for two very different purposes. The authors of this benchmark originally designed the PTB for one purpose but it has been recently repurposed by the community for something else in ways that are not as meaningful as it might seem. It is not clear who did this when and why, but now that the mistake has become standard practice, reviewers are likely to reject papers that do not repeat the mistake. More generally, we are concerned about how current practice is using benchmarks in ways that can be hard to defend, and diverge considerably from the original intention of the authors.
Here are some highly cited papers that use the PTB in these two ways:  Parsing: [Collins, 1997, 2003; Charniak, 2000]  Perplexity: [Zhao et al., 2023; Zhuang et al., 2020; Dong and Yang, 2019; Khandelwal et al.,
2018]
Figure 1a uses citing sentences to show how the community views the PTB. The parsing usage used to be more popular, but recently, the perplexity use has been gaining popularity. The black line in Figure 1a shows the distribution of 8677 papers that cite the PTB over time. The blue points counts papers that cite PTB using the word “parse” in the citing sentence. The red points are similar to the blue points but for the word “perplexity.” Note that the blue points peaked several years ago, whereas the red points are larger in more recent years, indicating that the use of the PTB for perplexity is more recent than the use of the PTB for parsing.
### 5.1 Inappropriate Processing
What is wrong with the text-only version15 of PTB? After rare words and numbers were removed by the community downstream of the LDC version,16 <unk> (rare words) has become the most common “word” in the test set, as shown in Table 2a. We should not confuse <unk>-prediction with perplexity; perplexity has many important applications [Shannon, 1948, 1951] unlike <unk>prediction. Note that estimates of perplexity becomes trivial (and completely meaningless) if we replace all words with <unk>; the more words we replace with <unk>, the easier (and less
15https://huggingface.co/ptb-text-only 16https://catalog.ldc.upenn.edu/LDC99T42

ACM SIGIR Forum

10

Vol. 58 No. 2 – December 2024

Citing Sentences

500

200

100

parse

50

20

perplexity

10

5

2 1

1995 2000 2005 2010 2015 2020 2025

Year

(a) Black line shows 8677 citing sentences that refer to PTB. Blue shows citing sentences that mention parse. Red shows citing sentences that mention perplexity.

2000 1500 1000
500 0

Validation Split

1500 1000
500 0

Test Split

Nr 1 3 5 7 9 11 13 15 17 19
Nr 1 3 5 7 9 11 13 15 17 19

Freq (r)

Freq (r)

1000 800 600 400 200 0

Train Split

All Splits Combined
600 400 200
0

Nr 1 3 5 7 9 11 13 15 17 19
Nr 5 7 9 11 13 15 17 19 21 23

Freq (r)

Freq (r)

(b) Nr is the number of words that appear r times. We expect Nr ≫ Nr+1, but the bottom row has surprisingly small Nr for r ≤ 5, because of Figure 2.
Figure 1. Penn TreeBank (PTB) [Marcus et al., 1993] was originally constructed to study parsing, though more recently, it has been repurposed to also study perplexity.

ACM SIGIR Forum

11

Vol. 58 No. 2 – December 2024

test train val words

word the <unk> <N> of to a in and ’s

train 50,770 45,020 32,481 24,400 23,638 21,196 18,000 17,474
9784

val 4122 3485 2603 1832 1750 1738 1392 1391 868

test 4529 4794 2523 2195 2042 1821 1640 1539 903

111 010 110 011 100 001 101 Totals

4475 2404 1574 1547
0 0 0 10,000

(a) <unk> and <N> are more fre- (b) Venn Diagram: four of seven (c) four of seven cases

quent than many function words. cases are non-zero

are non-zero.

Figure 2. When PTB was repurposed to study perplexity, the vocabulary was reduced to 10,000 words by assigning rare words to <unk> and numbers to <N>. This construction makes it (too) easy to predict the next “word,” especially because the test set does not generalize beyond the training set. That is, there are no words in the test set that do not appear in the training set.

meaningful) the task becomes. Issues with this processing have been called out elsewhere such as this discussion of WikiText-103 on Papers with Code (PwC):17
Compared to the preprocessed version of Penn Treebank (PTB), WikiText-2 is over 2 times larger and WikiText-103 is over 110 times larger. The WikiText dataset also features a far larger vocabulary and retains the original case, punctuation and numbers – all of which are removed in PTB. As it is composed of full articles, the dataset is well suited for models that can take advantage of long term dependencies.
Venn diagrams in Figures 2b and 2c point out an additional undesirable consequence of this processing. Normally, we would expect to see non-zero counts in all seven cells of the Venn diagram, but so many rare words have been removed that many of the cells are empty. In particular, there are no words in the test set that were not seen during training, casting serious doubts on the ability of this benchmark to measure generalizations beyond the training set.
We, as a community, should be more careful with credit assignment, especially when introducing serious problems into other people’s work. It is ironic that the community refers to the text-only version of the Penn TreeBank as “PTB” since this version has little to do with P (Penn) or T (trees). As explained in the LDC version in footnote 16, the text was collected elsewhere, largely from the 1989 Wall Street Journal (WSJ) and the 1961 Brown Corpus. Penn contributed the trees, but not the text (or the inappropriate processing).
17https://paperswithcode.com/dataset/wikitext-103

ACM SIGIR Forum

12

Vol. 58 No. 2 – December 2024

6 Common Assumptions in Estimates of Perplexity

There are many potential pitfalls for benchmarks for estimating perplexity. In addition to inap-

propriate processing, there can also be leakage and deviations from i.i.d. assumptions, as will be

discussed below. Before those discussions, let us review methods for estimating perplexity. Suppose we have a training set and a test set. The training set is used to fit Pˆr(w|history),

estimates of the probability of the next word (or token) given the previous context (history). At test time, we apply this model, Pˆr(w|history), to estimate probabilities based on a sample of

strings (the test set). Finally, we use a geometric mean to aggregate the probabilities to produce

a single number.

Theoretically, entropy, H, is the number of bits required, on average, to predict the next symbol. Perplexity is simply 2H. Perplexity can be interpreted as a branching factor in a search

space, or the typical number of choices.

Entropy is defined in terms of an (unknowable) probability distribution. If we have a set of

events {e1, e2, ..., en} with probabilities P r(e1), P r(e2), ..., P r(en), then H = − i P r(ei)log2P r(ei).

In practice, since we do not know the probabilities, we use the training set to fit estimates,

Pˆr. And then, we treat the test set as n samples, si, from the event space. As mentioned above,

perplexity can be thought of as the branching factor in a search space. That is, the number

of

choices

for

sample

si

is

1 Pˆr(si

)

.

If we have n samples, then the “typical” number of choices

(perplexity) is:

2Hˆ =

n1

1/n

s=1 Pˆr(s)

The geometric mean can be rewritten as an arithmetic mean of logs:

Hˆ

=

1 −

n

n

log2Pˆr(s)

i=1

In general, Hˆ ≥ H, where H is based on unknowable probabilities, P r, and Hˆ is based on estimates, Pˆr. We refer to Hˆ as cross entropy, and H as entropy. The gap between Hˆ and H becomes smaller and smaller with better and better estimates of P r.
This approach assumes that the test set consists of i.i.d. samples, si, drawn from a log normal distribution. Obviously, the test set should be different from the training set. If there is too much leakage, then the test set will fail to measure generalizations to unseen inputs. In practice, there are a number of challenging realities. Real documents have all sorts of non-i.i.d. structures such as topics, genre, style, discourse structure, plots, character arcs, languages and more. There is a literature on robust statistics where it is recommended that one split the test set up into many subsets and estimate many means (and moments) over many subsets. In this way, one can identify outliers, subsets of the test set that are surprisingly easy and surprisingly hard. There are often interesting explanations for many of the outliers as will be discussed below. These explanations typically involve deviations from i.i.d. assumptions. As the cliche goes, all models are wrong, but some are useful.18 We know that realistic texts are not i.i.d., but we want to know which are good enough, and which are truly problematic.

18https://en.wikipedia.org/wiki/All_models_are_wrong

ACM SIGIR Forum

13

Vol. 58 No. 2 – December 2024

The discussion of Wikitext-103 above suggested that bigger test sets are better. In fact, that may not be the case. Under the log normal assumption mentioned above, the size requirements on the test set involve the variance. If we split the test set up into many subsets and they all produce similar results as expected under a log normal distribution, then there is little point to increasing the size of the test set. Unfortunately, the literature rarely reports results on subsets of the test set, let alone comparisons of such results with expectations under a log normal distribution.
Another concern is coverage. The test set should be a representative sample of a population of interest such as the text that the application is likely to see in the future. Test sets are often based on news wire and Wikipedia, but it should be possible to construct more representative samples. The problem with the <unk>-prediction task above is that real use cases are unlikely to contain <unk> tokens.
### 6.1 Representative Samples: Leakage, Duplication, Balance and Age
Estimating perplexity has become more challenging now that LLMs are trained and tested on data from undisclosed sources. When corpora were curated by dictionary publishers, they were more careful about quality, especially clearing rights and documenting provenance.19 These days, the research community is less careful. LLM companies consider their sources to be trade secret.
Given these realities, duplication may be unavoidable. There is considerable literature on duplication in discussions of web crawling [Manasse, 2015], but less so in discussions of perplexity and LLMs. As a result, it is likely that LLMs have been trained on the test data, or some data that is (too) similar to the test data. Lee et al. [2022], Carlini et al. [2023] and Nasr et al. [2023] have been studying duplication in standard corpora that are likely to be used to train chatbots. They have been using hashing methods [Broder, 1997] and suffix arrays [Manber and Myers, 1993] to estimate memorization in chatbots. When bots are prompted with the beginning of long sequences such as 50-grams that are frequent in corpora that were probably used to train the bot, many bots often return the rest of the repeated sequence. Larger bots with more parameters are more likely to memorize more 50-grams with smaller frequencies. Estimates of perplexity are based on strong i.i.d. assumptions that are violated by this kind of duplication and leakage. A corpus should be a representative sample of what the model is likely to encounter at inference time.
The literature on corpus-based methods has a long history. There used to be more concern for duplication and balance. Corpora such as the Brown Corpus were designed to be a representative sample of Contemporary American English. When they collected this sample in the 1960s, they stratified the sample over different genre. Fiction is different from non-fiction, and local news is different from international news. For example, the word “said” is as frequent as a function word in the news, but extremely rare in technical abstracts. Estimates of perplexity based on the Brown Corpus will be relatively high compared to the Wall Street Journal because the WSJ represents a relatively homogeneous genre unlike the Brown Corpus, which contains, by construction, a diverse variety of genres.
In addition to balance, we should be concerned about age. The use of the phrase “presentday” in descriptions of the Brown Corpus20 do not age well since the Brown Corpus was based
19https://www.nytimes.com/2023/12/27/business/media/new-york-times-open-ai-microsoft-lawsuit .html
20https://en.wikipedia.org/wiki/Brown_Corpus

ACM SIGIR Forum

14

Vol. 58 No. 2 – December 2024

on works published in the United States in 1961. The WSJ data in PTB was from 1989; that is also far from “present-day” though not as dated as the Brown Corpus. Dictionaries are updated frequently because it is well-known that languages evolve considerably over decades.

6.2 A Constructive Proposal for Estimating Perplexity
The discussion of WikiText-103 above called out size and processing, but not duplication, leakage, sampling and age. Is size an advantage or a disadvantage? When the test set becomes larger and larger, it becomes harder and harder to know where it came from, or what it represents. It also becomes harder to know if there is leakage. Who knows what commercial bots are trained on, but it is hard to imagine that they have not been trained on Wikitext-103.
A suggestion in [Borgeaud et al., 2022] is to estimate perplexity on text from the “future.” In their Appendix A2, they describe a test set of Wikipedia articles that were created after training time. In addition to Wikipedia, many sources of text have a natural time dimension. Two examples are academic papers and news articles, both of which have publication dates. Suppose we train on publications up to time t, and test at time t + h, where h is the forecasting horizon. We would expect estimates of perplexity to improve with t and degrade with h.
In addition to publishing a single number, estimates of perplexity should also provide details. Perplexity is a geometric mean. One would hope that the values that contribute to the mean are distributed as log normal. How appropriate is that assumption? A standard method for testing that assumption is qqnorm,21 a special case of a q-q (quantile-quantile) plot.22 This plot will help us find outliers from assumptions of normality. After identifying outliers, we should decide if they are a concern.
It has been our experience that size is not always an advantage. Larger collections tend to have more corner cases (outliers). Since outliers can have a large impact on estimates of perplexity, one should check to see how sensitive estimates are to particular outliers. If the estimate depends on just a few outliers, we should decide how much we trust those outliers. If the outliers are uninteresting corner cases, then the estimate of perplexity is less trustworthy than if the outliers are central to the population of interest.
Large collections of news will include many outliers that can lead to iffy estimates of perplexity. Examples include stories with both high and low estimates of perplexity:
 Surprisingly low perplexity: file stories, tables, weather, plagiarism, duplication.  Surprisingly high perplexity: documents in languages other than English, summaries of the
news of the day/week/year.
By file stories, we are referring to stories that appear on slow news days, especially when much of the staff is on vacation. Tables on votes in congress are often predictable. The list of representatives does not change much, and they usually vote along party lines. The main difference from one vote to the next is the question they are voting on, but that is a relatively small faction of the story.
At the other end of the spectrum, we often find a few documents in languages that we were not expecting. One might expect papers in Semantic Scholar to be in English, but 17% are in other languages. One might also expect the beginning and the end of a news article to be on the same
21https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/qqnorm 22https://en.wikipedia.org/wiki/Q%E2%80%93Q_plot

ACM SIGIR Forum

15

Vol. 58 No. 2 – December 2024

topic, but there are many summary articles that combine a couple of sentences from a couple of different articles.
It becomes much easier for the community to become aware of corner cases such as these if we not only publish estimates of perplexity on standard collections, but we also share
 estimates of perplexity on articles from the future, such as papers from Academic Search websites, grouped by publication year,
 as well as details that make it easy to identify outliers and test assumptions such as log normal distributions.

## 7 Labeling and Inter-Annotator Agreement
Most of the AI-based solutions require ground truth data that is created in a labeling step. Largescale labeling (annotations) is very hard; it needs software development to get good results, and requires quality control processes and metrics [Alonso, 2019; Garcia-Molina et al., 2016; Roh et al., 2021]. Many aggregation models have been proposed for simple annotation tasks, but far less work has considered more complex tasks that involve open-ended, multivariate, or structured responses [Braylan et al., 2023].
There is very recent work on using LLMs for labeling as a mechanism to scale up the process and reduce the human cost. Using humans for labeling is expensive and LLMs offer advantages in terms of cost and performance. That said, the same principles with respect to reliability and quality control apply here. Faggioli et al. [2023] provides a spectrum of human-machine collaboration for different configurations. Thomas et al. [2023] compare LLM labels with TREC labels and report variations on κ for inter-annotator agreement.
Data wrangling, task design, task complexity, and aggregation techniques are still required. This is hard work that needs to be done for labeling. As previous work has noted, in practice nobody wants to work on data issues, and everyone expects clean labels. Labeling keeps getting harder as more complex tasks require more labels.
Unreliability results from two factors: (1) disagreements among independent ways of generating data about the phenomena in question and (2) lack of information (variation) in the resulting data to answer given research questions about these phenomena. In content analysis [Krippendorff, 2018], the first is assessed by agreement coefficients, such as α, applied to how several observers unitize the same continuum and/or record, describe, or code the same set of units. The second becomes evident by tracing the information in data throughout an analytical process to its results. When variation is absent, data cannot be correlated with anything; and when undetected noise in the data is not eliminated during an analysis, the answers to research questions may well be unrelated to the phenomena of interest.

## 8 Beyond Unambiguous Uncontroversial Factoid Queries
Many benchmarks assume there is a single correct answer in the answer key, but many tasks are not so simple: translation, web search, etc. It is standard practice for translation and web search to score systems with metrics such as BLEU and NDCG that aggregate over multiple references

ACM SIGIR Forum

16

Vol. 58 No. 2 – December 2024

Entity Description
Yes/No

Fact On which day will iphone be released? Why are firetrucks red? Is 39.5 degrees a high fever?

Opinion Top 10 movies of 2017 How good is the Toyota Corolla? Does learning to play Go improve intelligence?

(a) Six Types of Questions in DuReader (Table 2 of [He et al., 2018])

(b) Candidate labels: baseball cap, cap, green hat, hat and head ; which label is in the answer key?

Figure 3. The most interesting questions are rarely objective and unambiguous.

(answers in the answer key). Question-answering benchmarks such as SQuAD and TREC-8 focus on factoid questions, but some of the most interesting questions involve subjective opinions, as illustrated by the following three examples:
1. DuReader, for example, contains six types of questions extracted from Baidu query logs (in Chinese). Table 3a shows English glosses for the six types which include opinions in addition to factoids.
2. Historically, vision tasks have tended to label bounding boxes, but Figure 3b shows considerable room for annotators to disagree with one another.
3. Progress on part of speech tagging was limited by benchmarks that left too little room for differences of opinion. One might think that the difference between a noun and a verb would be unambiguous, but it turns out that annotators disagree about 3% of the time. When a machine differs from an annotator, the machine is wrong. But when two judges disagree, it is a difference of agreement. We could make progress on tagging if we could distinguish machine errors from differences of opinion. It would help to enhance answer keys with multiple answers, and replace metrics like accuracy with metrics like BLEU and NDCG that aggregate over multiple references.
In more recent work [Mohamed et al., 2024], we have been trying to move past unambiguous objective labels by asking annotators to add emotion labels and captions in 28 languages to WikiArt.23 For a particular portrait, many annotators thought the woman was beautiful but some objected to her dress as too revealing. One reviewer insisted on an ethics review, objecting to the objection to the dress. We object to the objection to the objection; it is inappropriate to impose our views on the rest of the world. We are not siding with one annotator over another, but rather than remove bias from corpora, we hope to build models that will be more aware of regional sensitivities to topics such as: dress, religion and alcohol. In addition to publishing a benchmark, we offer baseline implementations of captioning systems. Hopefully, the community will accept the challenge and come up with even better systems that embrace diversity over many regions, cultures and languages.
23https://www.wikiart.org/

ACM SIGIR Forum

17

Vol. 58 No. 2 – December 2024

Web, news and social media offer many different perspectives and points of view. Search engines have developed strategies for addressing these realities, but QA systems and chatbots tend to focus on an over-simplified view of the world with “right” and “wrong” answers, based on a single “possible world.” American bots are trained on American corpora; these bots currently lack a historian’s ability to approach conflicts from multiple perspectives.
The second author asked his NLP class to use bots to help them write essays about a controversial topic (the Opium Wars) from multiple perspectives including both the East and the West [Church, 2024]. He had hoped that international students would rewrite the output from the bot to reflect diverse perspectives, but most students found it easier to hand in the output from the American bot, as is. American bots do not mention “the century of humiliation,”24 a view that is motivating efforts to compete with the West in artificial intelligence so China does not fall behind in technology like it did during the Opium Wars, as suggested by some historians [Platt, 2019].
When bots and QA systems over-simplify the truth and take our side of conflicts, that could create dangerous filter bubbles, causing trade wars and worse. More generally, a major challenge for AI (and evaluation of AI) is to move beyond unambiguous, uncontroversial factoid questions. Many questions do not have simple right and wrong answers, but rather lots of opinions, sensitivities, and perspectives. Typical workloads on the web, news and social media go well beyond unambiguous uncontroversial factoid queries.
## 9 Conclusions: List of Principles
We propose to think about evaluation benchmarks the same way the community develops software techniques. In short, it needs to address a real customer problem, the workload is representative of the real-world, the metric is easy to interpret, and the data set evolves over time.
There are a few questions that the benchmark should focus on. How realistic is the task? Are we trying to solve a common use case or is this something that looks a bit artificial? Commercial relevance?
We outline the following list of principles that we think need to be taken into consideration when creating a new evaluation benchmark. At the same time, depending on the stage of the development process, some of these principles might take priority.
1. Realistic workloads: characterize the intended use case and audience. 2. Validity. Is the evaluation task relevant to the intended use case? What are we supposed to
learn from the benchmark? A benchmark should make a point (and not too many points). 3. Reliability with respect to the data.
 Inter-annotator agreement scores and disagreement analysis.  Labeling and annotation. How was it done? Availability of task instructions.  Outlier analysis and robust statistics: can we trust the metrics?  Simplicity? A benchmark should be large enough to make the point (and no larger).
24https://www.uscc.gov/sites/default/files/3.10.11Kaufman.pdf

ACM SIGIR Forum

18

Vol. 58 No. 2 – December 2024

4. Maintenance.
 Include a feedback loop mechanism to maximize adoption.  Workload evolution.  Lessons learned and addendum(s).  Lifecyle and deprecation.
5. High standards (for high-stakes use cases).
 Use of established software engineering and data management techniques (e.g., code review, versioning, configurations, dependencies, and testing).
 How the data was sourced? Can the data set be generated again easily?  Clean and well-documented data model.

## References
James Allan, Ron Papka, and Victor Lavrenko. On-line new event detection and tracking. In Proc. of SIGIR, pages 37–45, 1998.
James Allan, Nicholas J. Belkin, Paul N. Bennett, Jamie Callan, Charles L. A. Clarke, Fernando Diaz, Susan T. Dumais, Nicola Ferro, Donna Harman, Djoerd Hiemstra, Ian Ruthven, Tetsuya Sakai, Mark D. Smucker, and Justin Zobel. Overview of special issue. SIGIR Forum, 51(2): 1–25, 2017.
Omar Alonso. The Practice of Crowdsourcing. Synthesis Lectures on Information Concepts, Retrieval, and Services. Morgan & Claypool Publishers, 2019.
Omar Alonso and Stefano Mizzaro. Using crowdsourcing for TREC relevance assessment. In Information Processing & Management, volume 48, pages 1053–1066, 2012.
Rosana Ardila, Megan Branson, Kelly Davis, et al. Common Voice: A massively-multilingual speech corpus. In LREC, pages 4211–4215, 2020.
Payal Bajaj, Daniel Campos, Nick Craswell, et al. MS Marco: A human generated machine reading comprehension dataset. arXiv preprint arXiv:1611.09268, 2016.
Richard Belew. Adaptive information retrieval: Using a connectionist representation to retrieve and learn about documents. In Proc. of SIGIR, pages 11–20, 1989.
Adam Berger and John Lafferty. Information retrieval as statistical translation. In Proc. of SIGIR, volume 51, pages 219–226, 1999.
Krishna Bharat and Monika Henzinger. Improved algorithms for topic distillation in a hyperlinked environment. In Proc. of SIGIR, pages 104–111, 1998.
Sebastian Borgeaud, Arthur Mensch, Jordan Hoffmann, et al. Improving language models by retrieving from trillions of tokens. In International conference on machine learning, pages 2206–2240. PMLR, 2022.

ACM SIGIR Forum

19

Vol. 58 No. 2 – December 2024

Lutz Bornmann and Ru¨diger Mutz. Growth rates of modern science: A bibliometric analysis based on the number of publications and cited references. Journal of the Association for Information Science and Technology, 66, 2014.
Lutz Bornmann, Robin Haunschild, and Ru¨diger Mutz. Growth rates of modern science: a latent piecewise growth curve approach to model publication numbers from established and new literature databases. Humanities and Social Sciences Communications, 8(1):1–15, 2021.
Alexander Braylan, Madalyn Marabella, Omar Alonso, and Matthew Lease. A general model for aggregating annotations across simple, complex, and multi-object annotation tasks. J. Artif. Intell. Res., 78:901–973, 2023.
Andrei Broder. On the resemblance and containment of documents. Proceedings. Compression and Complexity of SEQUENCES 1997 (Cat. No.97TB100171), pages 21–29, 1997.
Andrei Broder. A taxonomy of web search. In SIGIR Forum, volume 36:2, pages 3–10, 2002.
Andrei Broder and Preston McAfee. Delphic costs and benefits in web search: A utilitarian and historical analysis, 2023. URL https://arxiv.org/abs/2308.07525.
Frederick P. Brooks. No silver bullet essence and accidents of software engineering. Computer, 20 (4):10–19, 1987.
Frederick P. Brooks. The mythical man-month: essays on software engineering. Pearson Education, 1995.
Tom B. Brown, Benjamin Mann, Nick Ryder, et al. Language models are few-shot learners. NeurIPS, 2020.
Chris Buckley and Ellen Voorhees. Evaluating evaluation measure stability. In SIGIR Forum, volume 51, pages 235 – 242, 2000.
Chris Buckley, Gerard Salton, James Allan, and Amit Singhal. Automatic query expansion using SMART: TREC 3. In Text Retrieval Conference, pages 69–80, 1994.
Jamie Callan, Zhihong Lu, and W. Bruce Croft. Searching distributed collections with inference networks. In Proc. of SIGIR, pages 21–28, 1995.
Maria Carla Calzarossa, Luisa Massari, and Daniele Tessera. Workload characterization: A survey revisited. ACM Computing Surveys, 48(3):1–43, 2016.
Alexandra Canavan, David Graff, and George Zipperlen. Callhome american english speech. Linguistic Data Consortium, 1997.
Jaime Carbonell and Jade Goldstein-Stewart. The use of MMR, diversity-based reranking for reordering documents and producing summaries. In SIGIR Forum, volume 51, pages 209 – 210, 1998.

ACM SIGIR Forum

20

Vol. 58 No. 2 – December 2024

Nicholas Carlini, Daphne Ippolito, Matthew Jagielski, Katherine Lee, Florian Tramer, and Chiyuan Zhang. Quantifying memorization across neural language models. Proc. of ICLR, 2023.
Eugene Charniak. A maximum-entropy-inspired parser. In NAACL, 2000. URL https://acla nthology.org/A00-2018.
Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, et al. PaLM: Scaling language modeling with pathways. ArXiv, abs/2204.02311, 2022.
Kenneth Church. Emerging trends: When can users trust GPT, and when should they intervene? Natural Language Engineering, pages 1–11, 2024.
Kenneth Church and Omar Alonso. Emerging trends: evaluating general purpose foundation models. Natural Language Engineering, 30(6):1323–1335, 2024.
Kenneth Church and Valia Kordoni. Emerging trends: SOTA-chasing. Natural Language Engineering, 28(2):249–269, 2022.
Charles L. A. Clarke, Nick Craswell, and Ian Soboroff. Overview of the TREC 2009 web track. In Text Retrieval Conference, 2009.
Michael Collins. Three generative, lexicalised models for statistical parsing. In EACL, pages 16–23. ACL, 1997.
Michael Collins. Head-driven statistical models for natural language parsing. Computational Linguistics, 29(4):589–637, 2003.
Alexis Conneau, Guillaume Lample, Marc’Aurelio Ranzato, et al. Word translation without parallel data. arXiv preprint arXiv:1710.04087, 2017.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal, et al. Unsupervised cross-lingual representation learning at scale. In ACL, pages 8440–8451. ACL, 2020.
Nick Craswell, Arjen de Vries, and Ian Soboroff. Overview of the TREC 2005 enterprise track. In Text Retrieval Conference, 2005.
Nick Craswell, Bhaskar Mitra, Emine Yilmaz, Daniel Fernando Campos, and Ellen Voorhees. Overview of the TREC 2019 deep learning track. In arXiv.org, volume abs/2003.07820, 2020.
Nick Craswell, Bhaskar Mitra, Emine Yilmaz, Daniel Fernando Campos, and Ellen Voorhees. Overview of the TREC 2020 deep learning track. In Text Retrieval Conference, volume abs/2102.07662, 2021.
Douglas R. Cutting, Jan O. Pedersen, David R. Karger, and John W. Tukey. Scatter/gather: a cluster-based approach to browsing large document collections. In Proc. of SIGIR, volume 51, pages 148 – 159, 1992.
Li Deng. The mnist database of handwritten digit images for machine learning research [best of the web]. IEEE signal processing magazine, 29(6):141–142, 2012.

ACM SIGIR Forum

21

Vol. 58 No. 2 – December 2024

Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. BERT: Pre-training of deep bidirectional transformers for language understanding. In NAACL, pages 4171–4186. ACL, 2019.
Kaivalya M Dixit. Overview of the SPEC benchmarks. The Benchmark Handbook, 7, 1993.
Xuanyi Dong and Yezhou Yang. Searching for a robust neural architecture in four gpu hours. IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 1761–1770, 2019.
Joel Fagan. Automatic phrase indexing for document retrieval: An examination of syntactic and non-syntactic methods. In Proc. of SIGIR, 1987.
Guglielmo Faggioli, Laura Dietz, Charles L. A. Clarke, et al. Perspectives on large language models for relevance judgment. In Proc. of ICTIR, pages 39–50, 2023.
Adam Fisch, Alon Talmor, Robin Jia, Minjoon Seo, et al. MRQA 2019 shared task: Evaluating generalization in reading comprehension. In Proceedings of 2nd Machine Reading for Reading Comprehension (MRQA) Workshop at EMNLP, 2019.
Winthrop Nelson Francis and Henry Kuˇcera. Frequency analysis of English usage: Lexicon and grammar. Houghton Mifflin, 1982.
George Furnas, Scott Deerwester, Susan Dumais, Thomas Landauer, et al. Information retrieval using a singular value decomposition model of latent semantic structure. In Proc. of SIGIR, pages 465–480, 1988.
Leo Gao, Stella Biderman, Sid Black, et al. The Pile: An 800GB dataset of diverse text for language modeling. arXiv preprint arXiv:2101.00027, 2020.
Hector Garcia-Molina, Manas Joglekar, Adam Marcus, Aditya G. Parameswaran, and Vasilis Verroios. Challenges in data crowdsourcing. IEEE Trans. Knowl. Data Eng., 28(4):901–911, 2016.
John S. Garofolo, Cedric G. P. Auzanne, and Ellen Voorhees. The TREC spoken document retrieval track: A success story. In Text Retrieval Conference, pages 1–20, 2000.
John S. Garofolo et al. TIMIT acoustic-phonetic continuous speech corpus. Linguistic Data Consortium, Philadelphia, 1983.
John J Godfrey, Edward C Holliman, and Jane McDaniel. Switchboard: Telephone speech corpus for research and development. In Acoustics, speech, and signal processing, ieee international conference on, volume 1, pages 517–520. IEEE Computer Society, 1992.
Jos´e Gonz´alez and Jaime Go´mez. TREC: Experiment and evaluation in information retrieval. In J. Assoc. Inf. Sci. Technol., volume 58, pages 910–911, 2007.
Naman Goyal, Cynthia Gao, Vishrav Chaudhary, Peng-Jen Chen, Guillaume Wenzek, Da Ju, Sanjana Krishnan, Marc’Aurelio Ranzato, Francisco Guzma´n, and Angela Fan. The Flores-101 evaluation benchmark for low-resource and multilingual machine translation. Transactions of the Association for Computational Linguistics, 10:522–538, 2022.

ACM SIGIR Forum

22

Vol. 58 No. 2 – December 2024

Kristian J. Hammond, R. Burke, C. Martin, and Steven L. Lytinen. FAQ finder: a case-based approach to knowledge navigation. Proc. of the 11th Conference on Artificial Intelligence for Applications, pages 80–86, 1995.
Donna Harman. Towards interactive query expansion. In Proc. of SIGIR, pages 321–331, 1988.
Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. Deep residual learning for image recognition. In Proc. of the IEEE conference on computer vision and pattern recognition, pages 770–778, 2016.
Wei He, Kai Liu, Jing Liu, et al. DuReader: a Chinese machine reading comprehension dataset from real-world applications. In Eunsol Choi, Minjoon Seo, Danqi Chen, Robin Jia, and Jonathan Berant, editors, Proc. of the Workshop on Machine Reading for Question Answering, pages 37–46. ACL, 2018.
John Hennessy and David Patterson. Computer Architecture: A Quantitative Approach. Elsevier, 2012.
Jonathan L. Herlocker, J. Konstan, Al Borchers, and J. Riedl. An algorithmic framework for performing collaborative filtering. In Proc. of SIGIR, pages 230–237, 1999.
William R. Hersh, Aaron M. Cohen, Lynn Ruslen, and Phoebe M. Roberts. TREC 2007 genomics track overview. In Text Retrieval Conference, 2007.
Thomas Hofmann. Probabilistic latent semantic indexing. In SIGIR Forum, volume 51, pages 211 – 218, 1999.
Nasreen Abdul Jaleel, James Allan, W. Bruce Croft, Fernando Diaz, Leah S. Larkey, Xiaoyan Li, Mark D. Smucker, and Courtney Wade. Umass at TREC 2004: Novelty and hard. In Text Retrieval Conference, 2004.
Karen Spa¨rck Jones. A look back and a look forward. In SIGIR Forum, volume 51, pages 62 – 78, 1988.
Kalervo Ja¨rvelin and Jaana Kek¨ala¨inen. IR evaluation methods for retrieving highly relevant documents. In Proc. of SIGIR, pages 41–48, 2000.
Jeffrey Katzer, Judith Tessier, William Frakes, and Padmini Das-Gupta. A study of the overlap among document representations. In Proc. of SIGIR, page 106–114. ACM, 1983.
Urvashi Khandelwal, He He, Peng Qi, and Dan Jurafsky. Sharp nearby, fuzzy far away: How neural language models use context. In ACL, pages 284–294. ACL, 2018.
Klaus Krippendorff. Content analysis: An introduction to its methodology. Sage publications, 2018.
Ranjay Krishna, Yuke Zhu, Oliver Groth, et al. Visual genome: Connecting language and vision using crowdsourced dense image annotations. International Journal of Computer Vision, 123: 32–73, 2017.

ACM SIGIR Forum

23

Vol. 58 No. 2 – December 2024

Alex Krizhevsky, Geoffrey Hinton, et al. Learning multiple layers of features from tiny images. https://www.cs.utoronto.ca/~kriz/learning-features-2009-TR.pdf, 2009.
Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, et al. Natural questions: a benchmark for question answering research. Transactions of the Association for Computational Linguistics, 7:453–466, 2019.
John Lafferty and ChengXiang Zhai. Document language models, query models, and risk minimization for information retrieval. In Proc. of SIGIR, pages 111–119, 2001.
Victor Lavrenko and W. Bruce Croft. Relevance-based language models. In Proc. of SIGIR, volume 51, pages 260 – 267, 2001.
Yann LeCun, Corinna Cortes, and Christopher Burges. MNIST handwritten digit database. ATT Labs [Online]. Available: http://yann.lecun.com/exdb/mnist, 2, 2010.
Katherine Lee, Daphne Ippolito, Andrew Nystrom, et al. Deduplicating training data makes language models better. In ACL, pages 8424–8445. ACL, 2022.
David D Lewis, Yiming Yang, Tony Russell-Rose, and Fan Li. Rcv1: A new benchmark collection for text categorization research. Journal of machine learning research, 5(Apr):361–397, 2004.
Xin Li and Dan Roth. Learning question classifiers. In COLING 2002: The 19th International Conference on Computational Linguistics, 2002.
Andrew L. Maas, Raymond E. Daly, Peter T. Pham, et al. Learning word vectors for sentiment analysis. In ACL, pages 142–150. ACL, 2011.
Mark S. Manasse. On the efficient determination of most near neighbors: horseshoes, hand grenades, web search and other situations when close is close enough. Morgan & Claypool Publishers, 2015.
Udi Manber and Gene Myers. Suffix arrays: a new method for on-line string searches. siam Journal on Computing, 22(5):935–948, 1993.
Mitchell P. Marcus, Beatrice Santorini, and Mary Ann Marcinkiewicz. Building a large annotated corpus of English: The Penn Treebank. Computational Linguistics, 19(2):313–330, 1993.
John Mashey. Summarizing performance is no mean feat [computer performance analysis]. In Proc. of the IEEE Workload Characterization Symposium, page 1, 2005.
Stephen Merity, Caiming Xiong, James Bradbury, and Richard Socher. Pointer sentinel mixture models. arXiv preprint arXiv:1609.07843, 2016.
Youssef Mohamed, Runjia Li, Ibrahim Said Ahmad, et al. No culture left behind: ArtELingo-28, a benchmark of WikiArt with captions in 28 languages. In EMNLP, pages 20939–20962. ACL, 2024.
Milad Nasr, Nicholas Carlini, Jonathan Hayase, et al. Scalable extraction of training data from (production) language models. arXiv preprint arXiv:2311.17035, 2023.

ACM SIGIR Forum

24

Vol. 58 No. 2 – December 2024

Thuat Nguyen, Chien Van Nguyen, Viet Dac Lai, Hieu Man, Nghia Trung Ngo, Franck Dernoncourt, Ryan A. Rossi, and Thien Huu Nguyen. Culturax: A cleaned, enormous, and multilingual dataset for large language models in 167 languages, 2023.
Iadh Ounis, Craig Macdonald, Jimmy J. Lin, and Ian Soboroff. Overview of the TREC 2011 microblog track. In Text Retrieval Conference, 2011.
Vassil Panayotov, Guoguo Chen, Daniel Povey, and Sanjeev Khudanpur. Librispeech: an asr corpus based on public domain audio books. In ICASSP, pages 5206–5210, 2015.
Annelise M. Pejtersen. A library system for information retrieval based on a cognitive task analysis and supported by an icon-based interface. In Proc. of SIGIR, pages 40–47, 1989.
Stephen R Platt. Imperial Twilight: The Opium War and the End of China’s Last Golden Age. Vintage, 2019.
Jay Ponte and W. Bruce Croft. A language modeling approach to information retrieval. In Proc. of SIGIR, pages 275–281, 1998.
Derek J De Solla Price. Networks of scientific papers: The pattern of bibliographic references indicates the nature of the scientific research front. Science, 149(3683):510–515, 1965.
Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. Language models are unsupervised multitask learners. OpenAI blog, 1(8):9, 2019.
Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. SQuAD: 100,000+ questions for machine comprehension of text. In EMNLP, pages 2383–2392. ACL, 2016.
Pranav Rajpurkar, Robin Jia, and Percy Liang. Know what you don’t know: Unanswerable questions for SQuAD. In ACL, pages 784–789. ACL, 2018.
C. J. Van Rijsbergen. A new theoretical framework for information retrieval. In SIGIR Forum, volume 21, pages 23–29, 1986.
Kirk Roberts, Dina Demner-Fushman, Ellen Voorhees, and W. Hersh. Overview of the TREC 2014 clinical decision support track. In Text Retrieval Conference, 2014.
Stephen Robertson. On GMAP: and other transformations. In Proc. of CIKM, page 78–83, 2006.
Stephen Robertson, Steve Walker, Susan Jones, Micheline Hancock-Beaulieu, and Mike Gatford. Okapi at TREC-3. In Text Retrieval Conference, pages 109–126, 1994.
Stephen Robertson, Steve Walker, Micheline Hancock-Beaulieu, Mike Gatford, and A. Payne. Okapi at TREC-4. In Text Retrieval Conference, 1995.
Yuji Roh, Geon Heo, and Steven Euijong Whang. A survey on data collection for machine learning: A big data - AI integration perspective. IEEE Trans. Knowl. Data Eng., 33(4):1328–1347, 2021.
Olga Russakovsky, Jia Deng, Hao Su, et al. Imagenet large scale visual recognition challenge. International journal of computer vision, 115:211–252, 2015.

ACM SIGIR Forum

25

Vol. 58 No. 2 – December 2024

Claude Shannon. A mathematical theory of communication. Bell system technical journal, 27(3): 379–423, 1948.
Claude Shannon. Prediction and entropy of printed english. Bell system technical journal, 30(1): 50–64, 1951.
Amit Singhal, Chris Buckley, and Mandar Mitra. Pivoted document length normalization. In SIGIR Forum, volume 51, pages 176 – 184, 1996.
Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao, et al. Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. arXiv preprint arXiv:2206.04615, 2022.
Yu Sun, Shuohuan Wang, Shikun Feng, et al. Ernie 3.0: Large-scale knowledge enhanced pretraining for language understanding and generation. arXiv preprint arXiv:2107.02137, 2021.
Beth M. Sundheim. Overview of the third Message Understanding Evaluation and Conference. In Third Message Understanding Conference (MUC-3), 1991.
Beth M. Sundheim. Overview of the fourth Message Understanding Evaluation and Conference. In Fourth Message Understanding Conference (MUC-4), 1992.
Paul Thomas, Seth Spielman, Nick Craswell, and Bhaskar Mitra. Large language models can accurately predict searcher preferences. CoRR, abs/2309.10621, 2023.
Howard R. Turtle and W. Bruce Croft. Inference networks for document retrieval. In Proc. of SIGIR, pages 1–24, 1989.
Ellen Voorhees. The cluster hypothesis revisited. In Proc. of SIGIR, pages 188–196, 1985.
Ellen Voorhees. The TREC-8 question answering track report. In Text Retrieval Conference, 1999.
Ellen Voorhees. The TREC question answering track. Natural Language Engineering, 7(4): 361–378, 2001.
Ellen Voorhees. Overview of the TREC 2003 question answering track. In Text Retrieval Conference, pages 54–68, 2004.
Ellen Voorhees and Donna Harman. TREC: Experiment and evaluation in information retrieval, 2005.
Ellen Voorhees and W. Hersh. Overview of the TREC 2012 medical records track. In Text Retrieval Conference, 2012.
Ellen Voorhees and Dawn Tice. The TREC-8 question answering track evaluation. In Text Retrieval Conference, volume 3, 2000.
Alex Wade. The semantic scholar academic graph (S2AG). Companion Proceedings of the Web Conference, 2022.

ACM SIGIR Forum

26

Vol. 58 No. 2 – December 2024

Alex Wang, Amanpreet Singh, Julian Michael, et al. GLUE: A multi-task benchmark and analysis platform for natural language understanding. In Proc. of the EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP, pages 353–355. ACL, 2018.
Alex Wang, Yada Pruksachatkun, Nikita Nangia, et al. SuperGLUE: A stickier benchmark for general-purpose language understanding systems. Advances in neural information processing systems, 32, 2019.
Wikimedia. ACL fourth conference on machine translation (WMT19), shared task: Machine translation of news. http://www.statmt.org/wmt19/translation-task.html, 2019.
Jinxi Xu and W. Bruce Croft. Query expansion using local and global document analysis. In Proc. of SIGIR, pages 4–11, 1996.
ChengXiang Zhai and J. Lafferty. A study of smoothing methods for language models applied to ad hoc information retrieval. In Proc. of SIGIR, pages 334–342, 2001.
Mingyi Zhang, Patrick Martin, Wendy Powley, and Jianjun Chen. Workload management in database management systems: A taxonomy. IEEE Transactions on Knowledge and Data Engineering, 30(7):1386–1402, 2018.
Wayne Xin Zhao, Kun Zhou, Junyi Li, et al. A survey of large language models. ArXiv, abs/2303.18223, 2023.
Juntang Zhuang, Tommy Tang, Yifan Ding, et al. AdaBelief optimizer: Adapting stepsizes by the belief in observed gradients. In NeuIPS, volume 33, pages 18795–18806, 2020.

ACM SIGIR Forum

27

Vol. 58 No. 2 – December 2024
