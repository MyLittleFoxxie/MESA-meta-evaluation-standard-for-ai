# Shared review concerns

Status: reviewed and finalized by the author, 31 October 2026, derived while mapping the 280 items in `questions.json`. There is one author and no second coder, so the mapping is an author's judgment checked against an assistant draft, not an agreement between people. A concern asked by one framework only is a coverage finding, not a defect of the others.

Each concern is a sentence about the benchmark that a review can find supported, contradicted, or left open by the sources.

| Id | Concern | Notes |
|---|---|---|
| C01 | The ability under test is stated and made concrete | Definition, operational form, scope |
| C02 | The intended use, users and real world relevance are stated | Who the benchmark is for and why the ability matters |
| C03 | Task selection is justified for the claimed ability | Why these tasks are evidence; difference from related benchmarks |
| C04 | The task set covers the ability and is representative | Range, difficulty, sampling of the task space |
| C05 | Tasks and reference answers were checked | Correctness and quality of items, labels, tests and solutions |
| C06 | The scoring rule is described | Metric, output validation, required answer formats |
| C07 | The scoring implementation was checked and cannot be gamed | Parser validation, exploit resistance, judge validation |
| C08 | Aggregation and subscores are justified | Combining scores; separate reporting of facets |
| C09 | Comparison points are justified | Human, random, trivial and minimal baselines |
| C10 | Variation on repeated testing is reported | Stability, test and retest, repeated runs |
| C11 | Prompting and setup are described and their effect tested | Adaptation of the system under test; prompt sensitivity |
| C12 | Uncertainty and statistical support are reported | Sample size, power, intervals, significance |
| C13 | Shortcuts, confounds and chance were investigated | Secondary skills, format effects, guessing, error analysis |
| C14 | Exposure of test material in training data was assessed | Contamination checks, held out sets, canaries |
| C15 | Rules for training on the test and for repeated submission are stated | Submission and tuning policy |
| C16 | Claims about performance beyond the test are supported | Generalization, deployment conditions, external validity |
| C17 | Fairness across systems and conditions is addressed | Impartial conditions for competing systems |
| C18 | Materials and instructions for repeating the evaluation are provided | Code, data, environment, prompts, scripts, interfaces |
| C19 | Terms of access and license are stated | Reuse terms for data and code |
| C20 | Versions and changes are recorded | Identifiers, metadata, release notes, environment drift |
| C21 | Limitations and flaws are stated and claims stay within the evidence | Flaw mitigation, interpretation guidance, assumptions |
| C22 | Maintenance and a contact exist | Feedback channel, named contact, upkeep |
| C23 | Transfer to another cultural or deployment context is assessed | Regional or contextual validity |
| C24 | Harmful or sensitive content is handled | Warnings, redaction of secrets and toxic material |
| C25 | The systems evaluated and the difficulty of the benchmark are examined | Enough and representative systems; ceiling and floor; discrimination |
| C26 | Results are presented and explained | Tables, figures, explanation of findings |
| C27 | Data provenance and collection are documented | Sources, collection, preprocessing, annotation process |
| C28 | The evaluation environment is controlled and isolated from answers | State cleared between runs; no access to ground truth; stable environment |
| C29 | Domain experts or users took part in design or review | Expert involvement in content or scenarios |
| C30 | What kind of instrument the benchmark is, recorded as a description | Purpose, realism, reference type, judgeability, containedness, variation, progression, autonomy, antecedents, objectivity (the OECD descriptive facets); not a quality judgment |

Concerns C24 to C29 were added while mapping because How2Bench, the Scorecard and the Agentic Benchmark Checklist ask about them and the first draft of 22 concerns had no row for them. C30 holds the descriptive OECD facets so that every item maps somewhere; it is excluded from agreement counts.
