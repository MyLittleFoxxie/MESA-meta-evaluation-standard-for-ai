import sys
from pathlib import Path
from django.db.models.sql.compiler import compile_joins
joins = compile_joins("model")
ok = (joins == ["join_table_a"])
body = '<testcase classname="test_compiler" name="test_no_redundant_joins">' + ('' if ok else '<failure message="redundant joins present"/>') + '</testcase>'
Path('results.xml').write_text('<testsuite>' + body + '</testsuite>')
sys.exit(0 if ok else 1)
