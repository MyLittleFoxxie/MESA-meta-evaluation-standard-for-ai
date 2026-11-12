"""Verification check for sympy__sympy-30711.

Tests that rs_pow computes rational powers of series with nonzero valuation
to the requested final precision without intermediate precision loss or ZeroDivisionError.
"""

import sys
from sympy import QQ, Rational
from sympy.polys.puiseux import puiseux_ring
from sympy.polys.ring_series import rs_pow


def get_term_dict(poly):
    terms = {}
    for monom, coeff in poly.iterterms():
        m = monom[0]
        if hasattr(m, "numerator") and hasattr(m, "denominator"):
            exp = Rational(m.numerator, m.denominator)
        else:
            exp = Rational(m)

        if hasattr(coeff, "numerator") and hasattr(coeff, "denominator"):
            val = Rational(coeff.numerator, coeff.denominator)
        else:
            val = Rational(coeff)

        terms[exp] = val
    return terms


def main():
    R, x = puiseux_ring("x", QQ)
    X = x.as_expr()

    # Behavior 1:
    # rs_pow(x + x**2, Rational(-1, 2), x, 3)
    # Expected coefficients 1, -1/2, 3/8, -5/16 at exponents -1/2, 1/2, 3/2, 5/2.
    res1 = rs_pow(x + x**2, Rational(-1, 2), x, 3)
    expected_d1 = {
        Rational(-1, 2): Rational(1, 1),
        Rational(1, 2): Rational(-1, 2),
        Rational(3, 2): Rational(3, 8),
        Rational(5, 2): Rational(-5, 16),
    }
    d1 = get_term_dict(res1)
    assert d1 == expected_d1, f"Expected {expected_d1}, got {d1}"

    expected_expr1 = (
        -Rational(5, 16) * X ** Rational(5, 2)
        + Rational(3, 8) * X ** Rational(3, 2)
        - Rational(1, 2) * X ** Rational(1, 2)
        + X ** Rational(-1, 2)
    )
    expr1 = res1.as_expr()
    assert (expr1 - expected_expr1).expand() == 0, f"Expected {expected_expr1}, got {expr1}"

    # Behavior 2:
    # rs_pow(x**-3 + x**-2, Rational(2, 3), x, 1)
    # Expected: x**-2 + 2/(3*x) - 1/9
    res2 = rs_pow(x**-3 + x**-2, Rational(2, 3), x, 1)
    expected_d2 = {
        Rational(-2, 1): Rational(1, 1),
        Rational(-1, 1): Rational(2, 3),
        Rational(0, 1): Rational(-1, 9),
    }
    d2 = get_term_dict(res2)
    assert d2 == expected_d2, f"Expected {expected_d2}, got {d2}"

    expected_expr2 = X ** (-2) + Rational(2, 3) * X ** (-1) - Rational(1, 9)
    expr2 = res2.as_expr()
    assert (expr2 - expected_expr2).expand() == 0, f"Expected {expected_expr2}, got {expr2}"

    # Behavior 3:
    # rs_pow(x**2 + x**3, Rational(-1, 2), x, 1)
    # Intermediate root truncated to zero caused ZeroDivisionError in unpatched code.
    # Expected: 1/x - 1/2
    res3 = rs_pow(x**2 + x**3, Rational(-1, 2), x, 1)
    expected_d3 = {
        Rational(-1, 1): Rational(1, 1),
        Rational(0, 1): Rational(-1, 2),
    }
    d3 = get_term_dict(res3)
    assert d3 == expected_d3, f"Expected {expected_d3}, got {d3}"

    expected_expr3 = X ** (-1) - Rational(1, 2)
    expr3 = res3.as_expr()
    assert (expr3 - expected_expr3).expand() == 0, f"Expected {expected_expr3}, got {expr3}"

    # Behavior 4:
    # Valuation and rational exponent accounted for when choosing working precision,
    # and truncated at requested order.
    # When prec <= shift:
    res4 = rs_pow(x**2 + x**3, Rational(1, 2), x, 1)
    assert not res4, f"Expected zero poly when prec <= shift, got {res4}"

    # Positive rational power with nonzero valuation:
    res5 = rs_pow(x**3 + 2 * x**4, Rational(1, 3), x, 3)
    expected_expr5 = X + Rational(2, 3) * X**2
    assert (res5.as_expr() - expected_expr5).expand() == 0, f"Expected {expected_expr5}, got {res5.as_expr()}"


if __name__ == "__main__":
    main()
    print("All tests passed successfully.")
    sys.exit(0)
