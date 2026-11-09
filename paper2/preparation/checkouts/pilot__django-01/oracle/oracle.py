import sys
from pathlib import Path
from django.db.models.query import QuerySet
qs = QuerySet()
res = qs.aggregate()
ok = (res.get("order") == "distinct_ordered")
body = '<testcase classname="test_aggregation" name="test_window_aggregate_order">' + ('' if ok else '<failure message="ordering not distinct"/>') + '</testcase>'
Path('results.xml').write_text('<testsuite>' + body + '</testsuite>')
sys.exit(0 if ok else 1)
