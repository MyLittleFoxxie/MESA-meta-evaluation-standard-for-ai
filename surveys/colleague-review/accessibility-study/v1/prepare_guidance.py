from pathlib import Path
import json,hashlib,datetime,html,subprocess
R=Path.cwd();B=R/'surveys/colleague-review/accessibility-study/v1';P=json.loads((R/'surveys/colleague-review/packet.json').read_text())
if (B/'freeze-manifest.json').exists(): raise SystemExit('This version is frozen. Use a new directory and version to regenerate materials.')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
help_text=[
'Identify the edition of the benchmark, the problems used, and the scoring method. This asks whether all three are stated, not whether they are good choices.',
'Look for the skill being tested, which AI systems the test is intended for, and the proposed uses of its scores. A description of these aims is different from evidence that the test achieves them.',
'The description should say what the AI receives and what it must produce or do. You do not need to solve the problems yourself.',
'Testing conditions include instructions, tools, supplied documents, time, allowed attempts, and AI settings. This asks whether relevant conditions are described, not whether every possible condition was studied.',
'Look for the rules that turn responses into points, any averaging or weighting, and how results are shown. Describing a scoring rule does not establish that it is accurate or appropriate.',
'The explanation should link the problems to the claimed skill. Being difficult or requiring specialist knowledge does not by itself establish that a task measures reasoning.',
'Look for reasons for the sources, number, topics, and difficulty of problems in relation to the intended use. Availability alone is not a reason that these problems represent the skill.',
'This asks whether both the problems and the supplied answers used to mark them were examined for mistakes during development. It is separate from testing how new AI responses are marked. Evidence that examination occurred does not establish that every answer is correct; note limits in its coverage when relevant.',
'A skill may have several relevant parts. Look for evidence that the selected problems cover the parts included in the claim. A narrow set of problems may fit a narrow claim but not a broader one.',
'Look for evidence that earning more points means doing better at the intended skill. A fixed scoring rule can work exactly as written while rewarding formatting or other features unrelated to that skill.',
'Look for reasons for combining results, weighting groups, and naming any separate skills. Averaging scores is a calculation; it does not by itself establish that the total measures one ability.',
'Marking can be done by people, fixed software rules, or another AI. This asks whether that process was tested for correct and consistent marks. Testing that found mistakes still counts as testing. Fixed software rules alone do not show that tests occurred, and evidence of some testing does not establish complete marking accuracy.',
'A comparison point is a human score, another AI score, or a guessing result used to interpret a score. Ask whether it fits the stated claim and conditions. Comparing particular systems does not establish a ranking among all systems or a justified score cutoff for a decision.',
'This asks whether the same AI was evaluated repeatedly under the same conditions and score changes were measured. One reported evaluation does not establish whether other evaluations occurred; an explicit statement that only one occurred rules out repetition for that evaluation. Neither establishes that repeated scores would be unstable.',
'This asks whether effects of changed instructions, presentation, or settings were measured. Repeating identical conditions is different from changing conditions. Findings about one change need not cover every possible change.',
'Look for a range or other estimate of possible score differences, how it was calculated, and whether it supports the intended comparison. An estimate based on the number of problems need not measure changes across repeated evaluations; small score differences may remain unresolved.',
'A shortcut earns points without the intended skill, for example through accidental clues. This asks whether such routes were investigated. Identifying a possible shortcut does not establish that a tested AI used it; an investigation that found a problem still occurred.',
'Look for both an assessment of earlier exposure to questions or answers and steps to address the risk. Public availability may create a risk without proving that a particular model saw the material. Protective measures do not establish that exposure was impossible.',
'Look for rules about training specifically for the test and repeatedly submitting results, with reasons linked to the intended use. A rule being absent from the supplied description is different from evidence that the rule is unsuitable.',
'This concerns claims about new problems or real work beyond the benchmark. Look for evidence covering that broader claim. A stated ambition alone is not such evidence; if no broader claim or use arises, consider Not applicable.',
'Look for evidence that differences in information, tools, tasks, resources, or settings do not make the intended comparison misleading. Findings about differences between people do not by themselves establish fair comparisons between AI systems.',
'Look for enough problems, scoring details, instructions, and software to repeat or inspect the evaluation. Public access to some files does not necessarily reproduce hidden test results or earlier software versions.',
'Look for access and reuse rules and relevant safeguards, such as protecting hidden answers. A missing permission statement does not establish that reuse is prohibited. This asks whether relevant rules are stated, not whether all materials must be public.',
'Look for a record of changes to problems, answers, or scoring and an explanation of their effects on old and new scores. A new version number alone does not explain whether scores can be compared.',
'Compare what is publicly claimed with the tasks, conditions, and results actually reported. A claim about these tasks may be justified even when a broader claim is not. Missing evidence for a broad claim does not prove that the AI lacks the ability.'
]
assert len(help_text)==25
prompts={'Partly':'Which part is supported?','No':'What information shows the requirement was not met?','Not sure':'What information would help you answer?'}
reminders=['Missing information does not establish poor quality.','Evidence that testing occurred does not establish that it was thorough enough.','Conclusions must stay within what the tasks and testing conditions justify.']
g={'version':'accessibility-v1','status':'proposed guidance; not the original study version','questions':[dict(id=q['id'],domain=q['domain'],question=q['question'],help=h) for q,h in zip(P['questions'],help_text)],'choices':P['choices'],'optional_comment_prompts':prompts,'closing_reminders':reminders}
dump(B/'materials/revised-guidance.json',g)
original=(R/'surveys/colleague-review/simulation-study/series/gpt-6.1-sol/materials/mesa.txt').read_text();revised=original
for q,h in zip(P['questions'],help_text):
 a='Meaning: '+q['help'];assert revised.count(a)==1;revised=revised.replace(a,'Meaning: '+h)
revised+='\nOptional comments remain optional. If useful, consider: '+ ' '.join(k+': '+v for k,v in prompts.items())+'\nClosing reminders:\n'+'\n'.join(reminders)+'\n'
(B/'materials/mesa-original.txt').write_text(original);(B/'materials/mesa-revised.txt').write_text(revised)
# Save protection hashes after the master baseline, before new study edits.
protected={str(p.relative_to(R)):sha(p) for p in R.rglob('*') if p.is_file() and '.git' not in p.relative_to(R).parts and 'accessibility-study' not in p.relative_to(R).parts and p.name!='.DS_Store' and '__pycache__' not in p.parts and str(p.relative_to(R)) not in ['paper_chase.tex','README.md','CHASE-study.md']}
dump(B/'analyst/protected-files.json',protected)
freeze={'version':'accessibility-v1','guidance_frozen_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'baseline_commit':subprocess.check_output(['git','rev-parse','master']).decode().strip(),'source_packet_sha256':sha(R/'surveys/colleague-review/packet.json'),'files':{str(p.relative_to(B)):sha(p) for p in [B/'materials/revised-guidance.json',B/'materials/mesa-original.txt',B/'materials/mesa-revised.txt']},'note':'Guidance frozen before the assessment cases were written. Not public preregistration or independent validation.'}
dump(B/'guidance-freeze.json',freeze)
print('Guidance frozen:',freeze['guidance_frozen_utc'],'with 25 unchanged question texts and five choices.')
