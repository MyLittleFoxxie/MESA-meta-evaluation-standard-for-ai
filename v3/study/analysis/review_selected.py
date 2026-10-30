"""Render all selected judgments with separately authored analyst observations."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[1]
NOTES={
'designqa':{
'A1':'The documents response uses 5 and repository response 10. The repository events show an entry point read. Both withhold execution claims. This is evidence of the intended distinction, not proof that the code runs.',
'A2':'The repository response assigns 10 but says no inspected code to rule comparison was established. Anchor 10 requires that comparison. Its evidence quote for the metric file is an analyst-like statement about file presence, not source text. This is an internal rating/reason tension. A metric read occurred, but reading alone does not establish a comparison.',
'A3':'The rating changes from 15 to 10 while both reasons describe formats and provenance. The second response demands complete instance metadata. Whether that is relevant to every task is not resolved by the rubric. Do not classify the change as improved accuracy.',
'A4':'The documents response rates 5 while stating that reuse terms are absent from supplied material. Anchor 5 requires an assertion of permissions and dependencies, so the response does not establish both components. Repository access supports dependency inspection, but neither response establishes permission scope. Missing a license is not proof of a prohibition.',
'A5':'The rating falls from 15 to 10 despite recognizing all four instruction steps. The repository reason additionally requires model inference steps and expected output for every input. The rubric asks for obtaining data, setup, execution and score interpretation; the need for this added scope is contested.',
'B1':'Both responses use 15, citing the task operationalization and limits. The paper discusses one document, task selection and limits of generalization. This supports a description rating, not empirical construct validity.',
'B2':'Both use 10 and distinguish review occurrence from missing findings. The paper names reviewers and exclusions. A documented procedure is not evidence that all answers are correct.',
'B3':'Both use 10 for variation over five GuaranteedRAG contexts and distinguish that experiment from all model comparisons. The source reports context regeneration; do not describe it as repeated identical setups.',
'B4':'Both mark not applicable because no measured human baseline supports the reported comparison. Expert authorship and review are not human task performance observations.',
'B5':'Both use 5 for a novelty claim without a model exposure audit. The evidence needs to distinguish the paper’s comparison to other datasets from its claims about its own images; no independent training corpus check was performed.'},
'humaneval':{
'A1':'The documents response uses 10 but cites only README instructions and a sample transcript. Those do not expose the entry point implementation. The repository response cites inspected implementation. The identical rating conceals a difference in what was available; the documents rating does not clearly satisfy anchor 10.',
'A2':'Both use 10. The paper includes estimator code, whereas the repository response additionally compares the product form in the implementation. This supports only the scoped estimator comparison, not all evaluation behavior or software tests.',
'A3':'Both use 10 and ask for partition and metadata detail. A benchmark need not have train and test partitions if it is an evaluation set; adequacy of the stated partition applicability remains a judgment.',
'A4':'Both use 10. Repository access adds the MIT license and dependency list, while unpinned versions and data permission scope remain concerns. This audit does not provide a legal interpretation of the license.',
'A5':'The rating changes from 10 to 15. The repository response identifies instruction elements already present in the shared README, including an example score. The change cannot be attributed solely to facts available only in the repository.',
'B1':'Both use 15 for functional correctness on standalone functions, with limits. The paper supports that bounded task description. It does not establish all broader programming claims.',
'B2':'The documents response rates 10 while explicitly saying the HumanEval checking procedure is not reported. It cites verification of a separate training set. The repository response instead uses insufficient evidence. The documents rating conflates evidence about another dataset with task/answer checking for this benchmark.',
'B3':'Both use 10, citing estimator variance. That does not establish uncertainty intervals for every model comparison. The source also contains analyses outside the target benchmark; those must remain scoped.',
'B4':'The documents response uses not applicable; the repository response uses 5 because the paper compares expected student performance in discussion. Both saw the same paper. This illustrates a scope ambiguity: measured benchmark comparisons versus broader interpretive claims. The reference proposal is not a settled key.',
'B5':'The rating changes from 10 to 5. Both cite hand authoring and the lack of a novelty guarantee. Treating hand authoring as a safeguard versus an unsupported novelty assertion explains the difference; no new exposure evidence establishes which rating is correct.'},
 'truthfulqa':{
'A1':'Both use 10. The documents response names an entry point but cannot inspect it. Published paper results do not make the repository implementation available in the documents condition. Repository access does supply implementation. The first rating therefore does not clearly satisfy anchor 10.',
'A2':'Both use 10. The documents response cites descriptions rather than a code comparison; the repository response links metric definitions and implementation. This is a distinction in support despite equal ratings. No execution checks were performed.',
'A3':'The rating falls from 15 to 10 while both describe fields, provenance and categories. The repository response asks for a partition scheme despite a test benchmark having different partition needs from a training dataset. This is not independently established as a correction.',
'A4':'Both use 10 and keep dependency and permission scope questions separate. License text is available only in the repository condition; the shared README also contains license metadata. No legal adequacy claim is made here.',
'A5':'The rating rises from 10 to 15. Much of the cited procedure is in the shared README. Additional repository evidence may help, but repetition and changes of sufficiency threshold cannot be separated from access in this small study.',
'B1':'Both use 15 and cite literal truthfulness, task operationalization and restrictions on wider claims. That documents the construct argument without validating it.',
'B2':'Both use 15 and acknowledge disagreements in the validation sample. The paper gives procedures, sample sizes and limitations. Disagreement findings are compatible with documenting that checking occurred.',
'B3':'Both use 10 and distinguish some reported error bars or evaluator variation from uncertainty over every model comparison. These sources of variation are not interchangeable.',
'B4':'Both use 10 for the single human participant with internet access. The source describes the procedure; it does not establish a population baseline or identical conditions across people and models.',
'B5':'Both use 10 while distinguishing prompt exclusion and benchmark training rules from an audit of model pretraining. The documentation supports safeguards but not an assurance that contamination is absent.'}}
def main():
 lines=['# Selected response audit','', 'Selection fixed by protocol: repetition 1 for every benchmark and access condition, six responses and sixty judgments. Analyst: the OpenAI Codex assistant that prepared the study. Human checking: none. Notes are interpretations, not independent adjudication or an error rate. Raw responses are unchanged.','']
 for b,notes in NOTES.items():
  data={c:json.loads((R/'outputs'/f'{b}-{c}-1/attempt-1/response.txt').read_text()) for c in ['documents','repository']}
  lines+=['## '+b,'']
  for i,note in notes.items():
   lines+=['### '+i,'']
   for c,d in data.items():
    j=next(x for x in d['judgments'] if x['id']==i)
    lines+=[f"{c}: {j['status']}, rating {j['rating']}. Reason recorded by reviewer:",'', '> '+j['reason'],'']
   lines+=['Assistant observation: '+note,'']
 (R/'analysis/selected-reviews.md').write_text('\n'.join(lines)+'\n')
if __name__=='__main__':main()
