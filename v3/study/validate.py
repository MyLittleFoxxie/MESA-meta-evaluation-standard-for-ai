import json
from pathlib import Path
R=Path(__file__).resolve().parent
IDS={f'{g}{i}' for g in 'AB' for i in range(1,6)}
def validate(data):
 errors=[]
 if not isinstance(data,dict) or set(data)!={'benchmark','limits','judgments'}:return ['top level keys']
 js=data['judgments']
 if not isinstance(js,list) or len(js)!=10:return ['requires ten judgments']
 if {j.get('id') for j in js}!=IDS:errors.append('duplicate, missing or unknown criterion')
 for j in js:
  if set(j)!={'id','status','rating','reason','evidence','missing','checks'}:errors.append('judgment keys')
  if j.get('status') not in ['rated','insufficient_evidence','not_applicable']:errors.append('status')
  if j.get('status')=='rated':
   if type(j.get('rating')) is not int or j['rating'] not in [0,5,10,15]:errors.append('rating')
  elif j.get('rating') is not None:errors.append('nonrated must have null rating')
  for k in ['reason','missing','checks']:
   if not isinstance(j.get(k),str):errors.append(k)
  if not isinstance(j.get('evidence'),list):errors.append('evidence')
  else:
   for e in j['evidence']:
    if set(e)!={'source','locator','quote'} or not all(isinstance(v,str) for v in e.values()):errors.append('evidence fields')
 return errors
if __name__=='__main__':
 for p in sorted((R/'outputs').glob('*/attempt-*/response.txt')):
  try:errors=validate(json.loads(p.read_text()))
  except Exception as e:errors=[str(e)]
  print(p.relative_to(R),errors or 'valid')
