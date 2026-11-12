"""
Verification check script for sympy__sympy-13372.
"""

import sys
from sympy import symbols, Mul, Max, I
from sympy.core.evalf import evalf
from sympy.core.expr import Expr


def test_mul_max_unevaluated():
    x, y = symbols('x y')

    # Behavior 1: Calling Mul(Max(0, y), x, evaluate=False).evalf() must return x*Max(0, y) without UnboundLocalError
    expr1 = Mul(Max(0, y), x, evaluate=False)
    res1 = expr1.evalf()
    expected = x * Max(0, y)
    assert res1 == expected, f"Mul(Max(0, y), x, evaluate=False).evalf() returned {res1!r}, expected {expected!r}"

    # Behavior 2: Reversing the two unevaluated multiplication arguments must preserve that successful symbolic result
    expr2 = Mul(x, Max(0, y), evaluate=False)
    res2 = expr2.evalf()
    assert res2 == expected, f"Mul(x, Max(0, y), evaluate=False).evalf() returned {res2!r}, expected {expected!r}"
    assert res1 == res2, f"Reversed arguments produced different results: {res1!r} != {res2!r}"


def test_evalf_fallback_non_numeric_real_and_imag():
    x, y = symbols('x y')

    # Behavior 3: In the ordinary evalf fallback, a nonzero real or imaginary part that is not numeric
    # must raise NotImplementedError, allowing symbolic evaluation to fall back safely instead of
    # using an unset precision variable (which previously caused UnboundLocalError).

    # 3a. Nonzero real part that is not numeric (via Max(0, y))
    try:
        evalf(Max(0, y), 53, {})
    except NotImplementedError:
        pass
    except UnboundLocalError as e:
        raise AssertionError(f"evalf(Max(0, y), 53, {{}}) raised UnboundLocalError: {e}")
    except Exception as e:
        raise AssertionError(f"evalf(Max(0, y), 53, {{}}) raised unexpected {type(e).__name__}: {e}")
    else:
        raise AssertionError("evalf(Max(0, y), 53, {}) did not raise NotImplementedError")

    # 3b. Nonzero real part that is not numeric (via custom Expr fallback)
    class DummyNonNumericRe(Expr):
        def _eval_evalf(self, prec):
            return y

    try:
        evalf(DummyNonNumericRe(), 53, {})
    except NotImplementedError:
        pass
    except UnboundLocalError as e:
        raise AssertionError(f"evalf(DummyNonNumericRe(), 53, {{}}) raised UnboundLocalError: {e}")
    except Exception as e:
        raise AssertionError(f"evalf(DummyNonNumericRe(), 53, {{}}) raised unexpected {type(e).__name__}: {e}")
    else:
        raise AssertionError("evalf(DummyNonNumericRe(), 53, {}) did not raise NotImplementedError")

    # 3c. Nonzero imaginary part that is not numeric (via custom Expr fallback)
    class DummyNonNumericIm(Expr):
        def _eval_evalf(self, prec):
            return I * y

    try:
        evalf(DummyNonNumericIm(), 53, {})
    except NotImplementedError:
        pass
    except UnboundLocalError as e:
        raise AssertionError(f"evalf(DummyNonNumericIm(), 53, {{}}) raised UnboundLocalError: {e}")
    except Exception as e:
        raise AssertionError(f"evalf(DummyNonNumericIm(), 53, {{}}) raised unexpected {type(e).__name__}: {e}")
    else:
        raise AssertionError("evalf(DummyNonNumericIm(), 53, {}) did not raise NotImplementedError")

    # 3d. Verify symbolic evaluation falls back safely for DummyNonNumericIm in unevaluated Mul
    res_im = Mul(DummyNonNumericIm(), x, evaluate=False).evalf()
    assert res_im == I * x * y, f"Mul(DummyNonNumericIm(), x, evaluate=False).evalf() returned {res_im!r}, expected {I*x*y!r}"


def main():
    test_mul_max_unevaluated()
    test_evalf_fallback_non_numeric_real_and_imag()
    print("All tests passed successfully.")


if __name__ == '__main__':
    main()
