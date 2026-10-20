"""Produce the separate follow-up report from saved analysis; no model calls."""
from pathlib import Path
import csv,json,collections
B=Path(__file__).resolve().parent
load=lambda n:list(csv.DictReader((B/'analysis'/n).open()))
def main():
 s=json.loads((B/'analysis/summary.json').read_text());c=load('claims.csv');a=load('mesa-answers.csv');pairs=load('paired-cases.csv');runs=load('runs.csv')
 alternative=sum(r['label']==('Contradicted' if (r['case'],r['claim'])==('P6B','claim1') else r['expected']) for r in c)
 mismatch=[{k:r[k] for k in ['id','case','claim','label','expected','reason']} for r in c if r['match']=='False']
 counts=collections.Counter(r['choice'] for r in a)
 d={'planned':s['planned'],'attempts':s['attempts'],'completed':s['completed'],'eligible':s['eligible'],'original_key_matches':sum(r['match']=='True' for r in c),'claim_answers':len(c),'p6b_alternative_matches':alternative,'matching_contrasts':sum(r['expected_change']==r['observed_change'] for r in pairs),'contrasts':len(pairs),'choice_counts':dict(counts),'mesa':s['mesa']['all'],'mismatches':mismatch,'designqa_q8_q12':[{'question':q,'choices':dict(collections.Counter(r['choice'] for r in a if r['benchmark']=='designqa' and r['question']==q))} for q in ['8','12']]}
 (B/'analysis/follow-up.json').write_text(json.dumps(d,indent=2)+'\n')
 text=f'''# Guidance-v2 follow-up results

This post hoc follow-up changes only the general occurrence-of-testing instruction and HLE Q8 example. It is separate from the original three-method study and does not replace its results.

All {d['planned']} planned conversations completed and all {d['eligible']} met the predefined schema. There were {d['attempts']} physical attempts: two sandbox authentication failures with zero model usage and ten completed conversations, including the two permitted retries. Both failures and retries are retained. The authentication error was a synthetic CLI message, not a generated study response; see ../launches/authentication-retry-decision.json and ../analysis-code-amendment.json.

| Measure | Revised guidance |
| --- | ---: |
| Usable benchmark conversations | 5/5 |
| Usable constructed-case conversations | 5/5 |
| Original-key matches | {d['original_key_matches']}/{d['claim_answers']} |
| P6B alternative-label matches | {alternative}/{d['claim_answers']} |
| Expected change/no-change contrasts | {d['matching_contrasts']}/{d['contrasts']} |
| Contrasts with both original-key labels | {s['cases']['cases']['mesa']['paired_matches']}/115 |
| Unjustified negative claims supported | 0/30 |
| Quotations located in supplied passages | 245/245 |
| MESA choices | 250 |
| Question–benchmark pairs with varying choices | {d['mesa']['variable_pairs']}/50 |
| Matching repeated-choice pairs | {d['mesa']['matching_answer_pairs']}/500 |

Choice counts: {', '.join(f'{k} {counts[k]}' for k in ['Yes','Partly','No','Not sure','Not applicable'])}.

All five DesignQA reviews still chose Partly for both Q8 and Q12. Comments mention exceptions in answer checking and limited marking tests. These observations do not identify the cause of the choices. The selected repetition-1 review recorded Not sure on DesignQA Q23 and Partly on Q24; other repetitions still selected No (three for Q23, two for Q24). Resolving the instruction/example inconsistency did not eliminate variation in application.

The original MESA batch matched 243/245 expected labels and 456/500 repeated choices, with nine varying question–benchmark pairs; this follow-up matched 242/245 and 435/500, with twelve varying pairs. These descriptive differences do not establish an improvement, deterioration, or causal effect of the guidance change. Sessions are repeated outputs of one model; the two guidance edits were made together, and the same cases have been used before. Original EFPA-TRM and general-instruction outputs are not newly run controls and are not pooled with this follow-up.

## Differences from the frozen key

'''
 for r in mismatch:text+=f"- `{r['id']}`, {r['case']} / {r['claim']}: {r['label']} rather than {r['expected']}. Recorded reason: “{r['reason']}”\n"
 text+='''
The P6B sensitivity calculation changes only the assumed expected label of P6B claim1 to Contradicted. The original key remains unchanged; neither label is an independently validated correctness standard.

OpenAI Codex prepared and analyzed this follow-up. The human author's reported check concerns the original six reviews and their coding, not these new responses. All numerical claims above are derived from the saved CSVs and JSON; interpretations of the comments are assistant interpretations. Human accessibility and effects on team decisions remain unmeasured.
'''
 (B/'analysis/follow-up.md').write_text(text);print(json.dumps(d,indent=2))
if __name__=='__main__':main()
