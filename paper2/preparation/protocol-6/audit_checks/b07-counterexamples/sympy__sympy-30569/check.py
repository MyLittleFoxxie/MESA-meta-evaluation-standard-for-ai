"""
Verification check for sympy__sympy-30569.
Issue: limit() raises NotImplementedError for expressions involving Min/Max
"""
import sys
from sympy import symbols, limit, Min, Max, exp, sin, oo
from sympy.series.gruntz import gruntz, mrv


def test_min_max_limits():
    x = symbols('x', real=True)

    # 1. limit(Min(x, x**2), x, 0) == 0
    res1 = limit(Min(x, x**2), x, 0)
    assert res1 == 0, f"Expected 0, got {res1}"

    # 2. limit(Max(x, sin(x)), x, 0) == 0
    res2 = limit(Max(x, sin(x)), x, 0)
    assert res2 == 0, f"Expected 0, got {res2}"

    # 3. limit(Min(exp(x), exp(2*x)), x, oo) == oo
    res3 = limit(Min(exp(x), exp(2*x)), x, oo)
    assert res3 == oo, f"Expected oo, got {res3}"

    # 4. limit(Max(exp(x), exp(2*x)), x, oo) == oo
    res4 = limit(Max(exp(x), exp(2*x)), x, oo)
    assert res4 == oo, f"Expected oo, got {res4}"

    # 5. gruntz directly on Min and Max
    gz1 = gruntz(Min(x, x**2), x, 0)
    assert gz1 == 0, f"Expected 0, got {gz1}"

    gz2 = gruntz(Max(x, sin(x)), x, 0)
    assert gz2 == 0, f"Expected 0, got {gz2}"

    gz3 = gruntz(Min(exp(x), exp(2*x)), x, oo)
    assert gz3 == oo, f"Expected oo, got {gz3}"

    gz4 = gruntz(Max(exp(x), exp(2*x)), x, oo)
    assert gz4 == oo, f"Expected oo, got {gz4}"

    # 6. mrv on Min / Max expressions does not raise multi-arg NotImplementedError
    s1, e1 = mrv(Min(x, x**2), x)
    assert s1 is not None and e1 is not None

    s2, e2 = mrv(Max(x, sin(x)), x)
    assert s2 is not None and e2 is not None

    s3, e3 = mrv(Min(exp(x), exp(2*x)), x)
    assert s3 is not None and e3 is not None

    s4, e4 = mrv(Max(exp(x), exp(2*x)), x)
    assert s4 is not None and e4 is not None


if __name__ == '__main__':
    test_min_max_limits()
    sys.exit(0)
