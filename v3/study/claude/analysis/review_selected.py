"""Render all selected Claude batch judgments with separately authored analyst observations.

Selection rule is the same as the Codex batch: repetition 1 for every benchmark and access condition.
Analyst: Claude Fable 5.1, the same model as the reviewer. Human checking: none.
"""
import json
from pathlib import Path
C=Path(__file__).resolve().parents[1]
NOTES={
'humaneval':{
'A1':'The documents response uses 5 and withholds 10 because the implementation was not supplied; it also records that the README describes the execution call as commented out. The repository response uses 10 after reading the entry point chain and reports that line 50 of execution.py is active in this snapshot, contradicting the README. The snapshot confirms both the README sentence and the active line. Neither response claims execution. The documents rating here follows anchor 5 more closely than the Codex documents response, which used 10 from the same README.',
'A2':'Both use 10. The documents response compares the Figure 3 snippet in the paper with Equation 1, which is a comparison between two parts of the paper, not with shipped code; the response says so. The repository response compares evaluation.py with the paper line by line and notes the absence of tests. Equal ratings rest on different comparisons; the documents rating relies on the paper reproducing its own code.',
'A3':'Both use 10 and both record the 164 versus 158 problem count inconsistency in the paper, which the Codex responses did not raise. The missing partition statement is treated as a gap, although an evaluation only set may not need one. The second repetition in the documents condition differs on this criterion, so this threshold is unstable within the configuration.',
'A4':'The documents response uses 10 while stating that no license appears in the supplied text and that only the Python version is constrained. Anchor 10 requires that terms or dependencies be specified; the Python constraint is treated as a dependency specification. This is a generous reading of anchor 10. The repository response reads the MIT license and unpinned requirements and uses 10 with a clearer basis.',
'A5':'Both use 15, mapping README sections to the four steps. The repository response records two README inaccuracies, the commented out claim and a file name that does not exist in the snapshot, and still keeps 15 because the anchor concerns instructions. Whether an instruction that misdescribes the code is complete is a judgment the rubric does not settle. The Codex responses used 10 and 15 for the same material.',
'B1':'Both use 15 with the same paper passages. This documents a stated construct and limits; it is not evidence of validity, and both responses say so.',
'B2':'Both use 5, distinguishing hand authorship from a documented checking procedure and noting that the filtering procedure in Section 4.3 concerns training problems. The Codex documents response had rated 10 using that section. The Claude reading follows the anchor more closely, but it does not prove the absence of checking, and the response does not claim that.',
'B3':'Both use 10 for estimator variance analysis without intervals on headline results. The judgments scope the analysis to the estimator rather than to model comparisons, which is the distinction the anchor asks for.',
'B4':'Both use 5 because the paper invokes expected student performance without a human procedure. Codex used not applicable in the documents condition and 5 in the repository condition. The rubric does not settle whether an interpretive comparison in a discussion section brings the criterion into scope. The Claude responses treat it as in scope in both conditions and both repetitions.',
'B5':'Both use 10 for a stated risk, a hand authoring safeguard and no corpus check. Codex used 10 and 5. The difference is whether hand authoring counts as a documented safeguard or an unsupported novelty assertion; the anchor wording allows either reading.'},
'truthfulqa':{
'A1':'The documents response uses 5 because the named entry point cannot be inspected. The repository response uses 10 after reading evaluate.py and finds a recorded notebook run on a three question demo from 2021, which it declines to treat as execution of the current edition. Both follow their anchors. Codex used 10 in both conditions from the same documents.',
'A2':'The documents response uses 5, stating that no code comparison is possible. The repository response uses 10 and reports an undocumented injection of a fixed reference answer into the true answer list and the absence of code for the 2025 binary setting. The snapshot contains that injection at the cited lines. These are findings from inspection, not from the paper, and the response keeps them separate from the rating rationale.',
'A3':'The documents response uses 15, treating the zero shot design as the reason no training partition exists. The repository response uses 10 because the current edition size is unspecified after dropped questions. Both saw the same README update note. The change reflects a sufficiency threshold about edition metadata, not a new fact unique to the repository; the second repetition reverses the direction.',
'A4':'The documents response uses 10 because the license is stated only in a metadata block. The repository response uses 15 after reading the license file and pinned requirements, while noting unpinned PyTorch. Anchor 15 asks for permissions covering data and code and for version constraints; an unpinned required package is a limit the response records but does not count against the rating.',
'A5':'Both use 15. Both note that the human evaluated results cannot be reproduced and that the judge model must be fine tuned by the user through a legacy interface. The rating concerns instructions, so these are recorded as limits. Codex used 10 in the documents condition for the same README.',
'B1':'Both use 15 with the same definitions and stated limits. Documented construct statements, not validity.',
'B2':'Both use 15, citing the validation procedure, coverage, findings and the correction of 43 questions, and both record that the 2025 revision is not fully validated. This matches the rubric statement that found errors do not lower the rating.',
'B3':'Both use 10 and distinguish the reported disagreement rate and standard errors on one figure from uncertainty on the main comparisons. Consistent with Codex.',
'B4':'Both use 10 for a documented single participant procedure with unresolved sample and condition comparability. The repository response adds that evaluators were blinded to model name, a paper passage not cited by the documents response. The same rating with more evidence.',
'B5':'Both use 10 for stated safeguards without a contamination check. The responses distinguish the canary string and zero shot rule from an audit of training data, as the anchor requires.'},
'designqa':{
'A1':'The documents response uses 5 because no tools were offered and no execution output is supplied. The repository response uses 10 after reading the entry point and metric code, and finds result files whose values match the paper but which come from older per subset scripts. It withholds 15 for that reason. This is the kind of distinction the anchor intends.',
'A2':'The documents response uses 5 and explains that the README overall average is a convention not described in the paper, declining to call it a discrepancy. The repository response uses 10 and reports a line by line comparison with four findings: the similarity metric is commented out, a ground truth normalization edge case, a fixed divisor of six, and test inputs without expected outputs. The snapshot confirms the first and third. The rating is 10 rather than 0 because the main rules match; the rubric requires an inspected discrepancy to violate the documented rule for 0, and the response argues the commented metric is a reproducibility gap rather than a rule violation. That is a judgment.',
'A3':'The rating changes from 10 to 15. The repository response reads CSV headers and finds the metadata fields the documents response could not confirm. This is a change supported by information available only in the repository, unlike several threshold changes elsewhere.',
'A4':'Both use 10. The documents response records the absence of any license statement from the supplied text; the repository response infers the absence of a license file from the complete listing and reports packages imported but not listed in requirements. Missing a license is not a prohibition, and both responses say the reuse terms are unstated rather than forbidden.',
'A5':'Both use 10 and both ask for instructions to regenerate model predictions. The repository response finds blank API token fields in the run scripts. Codex used 15 and 10 for the same material. The question is whether the reported task includes model inference or only scoring; the rubric does not say.',
'B1':'Both use 15 citing the same passages. Documented construct and limits only.',
'B2':'Both use 10 for a described review procedure without reported findings. Consistent with Codex.',
'B3':'Both use 10 for variation reported over five context generations and single runs elsewhere. Consistent with Codex.',
'B4':'Both use not applicable because no human performance comparison is claimed. The second Claude documents repetition is the same; the Codex second documents repetition had used 10. Which reading is right depends on whether expert authorship counts as a human comparison, and the rubric says it does not.',
'B5':'Both use 10, treating the unseen image claim as a documented safeguard and recording that exposure to the public rules text is not assessed. Codex used 5. The difference again turns on whether a stated design choice is a safeguard or an assertion.'}}
def main():
 lines=['# Selected response audit, Claude batch','', 'Selection fixed by protocol: repetition 1 for every benchmark and access condition, six responses and sixty judgments. Analyst: Claude Fable 5.1, the same model as the reviewer, running as the assistant that prepared this batch. Human checking: none. Notes are interpretations, not independent adjudication or error counts. Where a note says the snapshot confirms a claim, the assistant read the cited file lines offline after the sessions; this does not make the rating correct.','']
 for b,notes in NOTES.items():
  data={c:json.loads((C/'outputs'/f'{b}-{c}-1/attempt-1/response.txt').read_text()) for c in ['documents','repository']}
  lines+=['## '+b,'']
  for i,note in notes.items():
   lines+=['### '+i,'']
   for c,d in data.items():
    j=next(x for x in d['judgments'] if x['id']==i)
    lines+=[f"{c}: {j['status']}, rating {j['rating']}. Reason recorded by reviewer:",'', '> '+j['reason'],'']
   lines+=['Assistant observation: '+note,'']
 (C/'analysis/selected-reviews.md').write_text('\n'.join(lines)+'\n')
if __name__=='__main__':main()
