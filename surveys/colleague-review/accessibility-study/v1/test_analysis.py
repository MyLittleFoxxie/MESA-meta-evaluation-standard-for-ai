"""Meaningful schema checks: missing claims cannot become apparent perfect scores."""
import unittest,copy
from analyze import validate
class Validation(unittest.TestCase):
 def test_incomplete_case_set_rejected(self):self.assertTrue(validate({'cases':[],'closing_note':''},{'batch':'controlled'}))
 def test_duplicate_benchmark_rejected(self):
  r={'benchmark':'arc','instrument_review':'','supported_claims':[],'documented_problems':[],'missing_information':[],'reinterpretations':[],'closing_note':''}
  self.assertTrue(validate({'reviews':[r,copy.deepcopy(r)]},{'batch':'real','condition':'ordinary'}))
 def test_optional_comment_and_all_categories(self):
  r={'benchmark':'arc','instrument_review':'','supported_claims':[],'documented_problems':[],'missing_information':[],'reinterpretations':[],'closing_note':'','mesa_answers':[{'id':i,'choice':'Not sure'} for i in range(1,26)]}
  other=copy.deepcopy(r);other['benchmark']='designqa';other['mesa_answers'][0]['comment']=None
  self.assertFalse(validate({'reviews':[r,other]},{'batch':'real','condition':'mesa_revised'}))
 def test_missing_question_rejected(self):
  r={'benchmark':'arc','instrument_review':'','supported_claims':[],'documented_problems':[],'missing_information':[],'reinterpretations':[],'closing_note':'','mesa_answers':[]}
  other=copy.deepcopy(r);other['benchmark']='designqa';self.assertTrue(validate({'reviews':[r,other]},{'batch':'real','condition':'mesa_original'}))
if __name__=='__main__':unittest.main()
