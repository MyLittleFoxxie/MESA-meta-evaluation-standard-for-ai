import unittest
import validation_helpers as V
class SchemaTests(unittest.TestCase):
 def real(self):
  return {'reviews':[{'benchmark':b,'instrument_review':'Review','supported_claims':[],'documented_problems':[],'missing_information':[],'reinterpretations':[],'closing_note':'','mesa_answers':[{'id':i,'choice':'Not sure'} for i in range(1,26)]} for b in ['arc','designqa']]}
 def test_duplicate_json_keys_rejected(self):
  with self.assertRaises(ValueError):V.parse('{"reviews":[],"reviews":[]}')
 def test_missing_comment_is_permitted(self):
  self.assertEqual(V.validate(self.real(),{'batch':'real','condition':'mesa'},{}),[])
 def test_object_conclusion_is_invalid(self):
  r=self.real();r['reviews'][0]['supported_claims']=[{'claim':'example'}]
  self.assertTrue(V.validate(r,{'batch':'real','condition':'mesa'},{}))
 def test_repeated_question_is_invalid(self):
  r=self.real();r['reviews'][0]['mesa_answers'][-1]['id']=1
  self.assertTrue(V.validate(r,{'batch':'real','condition':'mesa'},{}))
 def test_wrong_label_is_invalid(self):
  r={'cases':[{'id':'C1','instrument_review':'Review','probes':[{'id':'x','label':'Yes','quote':'text','reason':'reason'}]}],'closing_note':''}
  self.assertTrue(V.validate(r,{'batch':'eight','condition':'mesa'},{'C1':{'x':{'label':'Supported'}}}))
if __name__=='__main__':unittest.main()
