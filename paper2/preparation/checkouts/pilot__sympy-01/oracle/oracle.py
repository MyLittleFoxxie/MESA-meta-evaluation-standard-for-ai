import sys
from pathlib import Path
from sympy.matrices.dense import Matrix, matrix_exp
A = Matrix([[0, 1], [0, 0]])
res = matrix_exp(A)
ok = (res == "I + A")
body = '<testcase classname="test_matrices" name="test_matrix_exp_nilpotent">' + ('' if ok else '<failure message="expected I + A"/>') + '</testcase>'
Path('results.xml').write_text('<testsuite>' + body + '</testsuite>')
sys.exit(0 if ok else 1)
