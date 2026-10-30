"""Prepare assistant judgments before main outputs. Not human ground truth."""
import json,datetime
from pathlib import Path
R=Path(__file__).resolve().parent
# Each entry is a proposal with alternatives, not a claim of independent correctness.
DATA={
'humaneval':{
'A1':([5,10],[10,15],'repository/README.md','evaluate_functional_correctness','Entry point and example transcript documented; paper and current commit are not contemporaneous, so successful execution of this commit is not established.'),
'A2':([10,5],[10,15],'paper.txt','numerically stable','Paper contains an estimator and code; implementation inspection adds the repository. Equality of the full evaluation behavior remains a judgment.'),
'A3':([10,15],[10,15],'paper.txt','Each problem includes','Task structure and author creation are described; partition and provenance completeness require interpretation.'),
'A4':(['insufficient_evidence',10],[10],'repository/README.md','python 3.7','Documents give installation but not full reuse terms. Repository MIT license and unpinned dependency names support partial documentation.'),
'A5':([15,10],[15,10],'repository/README.md','As a quick sanity-check','Instructions include sample inputs, invocation and output; code generation and sandbox setup remain user responsibilities.'),
'B1':([10,15],[10,15],'paper.txt','Programming tasks in the HumanEval','Functional correctness operationalizes a bounded programming task; broader claims and limits need judgment.'),
'B2':(['insufficient_evidence',5],['insufficient_evidence',5],'paper.txt','7.7 tests','Task authorship and unit tests do not establish a complete audit of tasks and keys.'),
'B3':([10],[10],'paper.txt','high variance','Estimator variance is addressed, but this does not establish all uncertainty needed for arbitrary comparisons.'),
'B4':(['not_applicable'],['not_applicable'],'paper.txt','We evaluate functional correctness','Bound the target to reported functional correctness of models, not a measured HumanEval human parity claim.'),
'B5':([10],[10],'paper.txt','not a guarantee for problem novelty','Handwritten tasks address prior copying risk, without proving no exposure for all models or current use.')},
 'truthfulqa':{
'A1':([5],[10,15],'repository/README.md','truthfulqa/evaluate.py','Documents name an entry point; repository exposes implementation. Published evaluations do not prove the current revision runs.'),
'A2':([5,10],[10],'repository/README.md','max similarity to a true reference answer','The metric is documented and implementation can be compared, but exhaustive behavior checking is not established.'),
'A3':([15,10],[15,10],'paper.txt','sets','Reference answers, categories, sources and filtered versus unfiltered questions are documented.'),
'A4':([10],[10,15],'repository/README.md','Apache 2.0','README embeds license metadata; repository supplies license and dependencies. Scope and versions need checking.'),
'A5':([15,10],[15,10],'repository/README.md','Local installation','Setup and model scoring instructions are available, with external service and model requirements.'),
'B1':([15,10],[15,10],'paper.txt','imitative falsehoods','The construct is operationalized and possible alternative causes are discussed, without establishing validity.'),
'B2':([15,10],[15,10],'paper.txt','They disagreed on 7%','Checking procedure, sampling and disagreement findings are reported; scope of reference verification is limited.'),
'B3':([10,'insufficient_evidence'],[10,'insufficient_evidence'],'paper.txt','Different prompts','Analyses across prompts and models do not automatically establish sampling uncertainty for every comparison.'),
'B4':([10],[10],'paper.txt','A “participant”','One participant answered a sampled set with internet access; the scope of human generalization is limited.'),
'B5':([10,5],[10,5],'repository/README.md','BENCHMARK DATA SHOULD NEVER APPEAR','A canary and exclusion instruction are safeguards, not an exposure audit of reviewed models.')},
'designqa':{
'A1':([5],[10,15],'repository/README.md','python eval/full_evaluation.py','README names evaluation and outputs; repository exposes scripts. No execution was performed by this study.'),
'A2':([5,10],[10],'repository/README.md','eval/metrics/metrics.py','Definitions and metric implementation support a scoped comparison, not proof of all behavior.'),
'A3':([15,10],[15,10],'repository/README.md','ground_truth','Subset locations, prompts, answers and task origins are described; partition applicability must be stated.'),
'A4':([10,'insufficient_evidence'],[10],'repository/README.md','python=3.10','Setup and dependencies are available; code and data reuse permission is unresolved, not proof that reuse is forbidden.'),
'A5':([15,10],[15,10],'repository/README.md','results.txt','The README describes setup, inputs, scoring and output, without establishing successful reproduction.'),
'B1':([15,10],[15,10],'paper.txt','DesignQA results','Task scope and limits of generalization are stated; adequacy of coverage remains a judgment.'),
'B2':([10],[10],'paper.txt','reviewed by the two parties','Review procedure and exclusions are documented, but reviewer findings and error counts are not fully reported.'),
'B3':([10],[10],'paper.txt','averages and standard deviations','Five context-generation runs report variation for one model; not all benchmark comparisons are covered.'),
'B4':(['not_applicable'],['not_applicable'],'paper.txt','designed','Expert authorship is not a measured human performance baseline for the model comparisons under review.'),
'B5':(['insufficient_evidence',5,10],['insufficient_evidence',5,10],'paper.txt','pre-training','Claims about realistic private engineering sources do not establish a model-specific exposure audit.')}
}
def main():
 if (R/'freeze-manifest.json').exists():raise SystemExit('frozen')
 records=[]
 for b,items in DATA.items():
  for i,(doc,repo,path,needle,reason) in items.items():
   p=R/'sources'/b/path;lines=p.read_text().splitlines();hits=[n for n,l in enumerate(lines) if needle.lower() in l.lower()]
   if not hits:raise ValueError((b,i,needle))
   n=hits[0];excerpt='\n'.join(lines[max(0,n-1):min(len(lines),n+4)])
   for c,values in [('documents',doc),('repository',repo)]:
    value=values[0];records.append({'benchmark':b,'criterion':i,'condition':c,'status':'contested' if len(values)>1 else 'provisional','expected':{'status':'rated' if isinstance(value,int) else value,'rating':value if isinstance(value,int) else None},'alternatives':[{'status':'rated' if isinstance(v,int) else v,'rating':v if isinstance(v,int) else None} for v in values[1:]],'reason':reason,'evidence':[{'source':path,'locator':f'lines {max(1,n)}-{min(len(lines),n+4)}','quote':excerpt}],'preparer':'OpenAI Codex assistant','checker':None,'human_checked':False,'prepared_before_main':True,'limits':'Assistant interpretation; no independent ground truth. Source excerpt motivates judgment but may not establish every anchor component.'})
 (R/'analyst/references.json').write_text(json.dumps(records,indent=2)+'\n')
 print(len(records),'reference records; none independently validated')
if __name__=='__main__':main()
