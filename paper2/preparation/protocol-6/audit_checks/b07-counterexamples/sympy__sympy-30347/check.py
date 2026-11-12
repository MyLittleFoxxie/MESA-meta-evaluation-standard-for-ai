import sys
from sympy import erf, sqrt, S
from sympy.core.numbers import Float
from sympy.functions.special.error_functions import owens_t, Li


def test_owens_t_eval_evalf_returns_float():
    # Numeric owens_t(h, a)._eval_evalf(prec) should return a plain Float
    res1 = owens_t(1, 2)._eval_evalf(53)
    assert isinstance(res1, Float), f"Expected Float from owens_t(1, 2)._eval_evalf(53), got {type(res1)}: {res1}"

    res2 = owens_t(-6, 2)._eval_evalf(53)
    assert isinstance(res2, Float), f"Expected Float from owens_t(-6, 2)._eval_evalf(53), got {type(res2)}: {res2}"


def test_li_eval_evalf_returns_float():
    # Numeric Li(z)._eval_evalf(prec) should return a plain Float
    res = Li(3)._eval_evalf(53)
    assert isinstance(res, Float), f"Expected Float from Li(3)._eval_evalf(53), got {type(res)}: {res}"


def test_owens_t_add_cancellation():
    # Sums and differences containing Owen's T should resolve close cancellation
    # automatically at default precision, preserving the small result's sign and magnitude.
    # Reported expression at h = -6 and a = 2:
    h, a = -6, 2
    expr = erf(sqrt(2)*h/2)/2 + S.Half - 2*owens_t(h, a)
    val = expr.evalf()

    assert isinstance(val, Float), f"Expected Float from expr.evalf(), got {type(val)}: {val}"
    assert val > 0, f"Expected positive result, got {val}"

    # True value is approximately 7.118079190042937e-43
    expected = 7.118079190042937e-43
    rel_err = abs(float(val) - expected) / expected
    assert rel_err < 1e-4, f"Value {val} differs from expected {expected} with rel_err {rel_err}"


def test_skewnormal_cdf():
    # If SkewNormal is available in sympy.stats, test cdf directly
    try:
        from sympy.stats import SkewNormal, cdf
        sn_expr = cdf(SkewNormal('x', 0, 1, 2))(-6)
        val = sn_expr.evalf()
        assert isinstance(val, Float), f"Expected Float from SkewNormal cdf evalf(), got {type(val)}: {val}"
        assert val > 0, f"Expected positive result from SkewNormal cdf, got {val}"
        expected = 7.118079190042937e-43
        rel_err = abs(float(val) - expected) / expected
        assert rel_err < 1e-4, f"SkewNormal cdf value {val} differs from expected {expected} with rel_err {rel_err}"
    except (ImportError, AttributeError):
        pass


def main():
    test_owens_t_eval_evalf_returns_float()
    test_li_eval_evalf_returns_float()
    test_owens_t_add_cancellation()
    test_skewnormal_cdf()
    print("All checks passed.")


if __name__ == '__main__':
    main()
