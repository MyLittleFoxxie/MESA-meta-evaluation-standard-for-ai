"""Verification script for sympy__sympy-19040:
Factor with extension drops factors in multivariate polynomials.
"""
import sys
from sympy import symbols, expand, factor, I, sqrt


def test_issue_factor_extension():
    # Factoring x*y - x - y + 1 with extension=[I] must retain both factors, (x - 1)*(y - 1).
    x, y = symbols('x y')
    z = expand((x - 1)*(y - 1))
    res = factor(z, extension=[I])
    assert res == (x - 1)*(y - 1), f"Expected (x - 1)*(y - 1), got {res}"
    assert expand(res) == z, f"expand({res}) != {z}"


def test_factor_extension_true():
    # Factoring with extension=True must preserve all factors and the value of the original expression.
    x, y = symbols('x y')

    # Original example
    z = expand((x - 1)*(y - 1))
    res = factor(z, extension=True)
    assert res == (x - 1)*(y - 1), f"Expected (x - 1)*(y - 1), got {res}"
    assert expand(res) == z, f"expand({res}) != {z}"

    # Multivariate polynomial with complex algebraic coefficient
    expr1 = expand((x - I)*(y - 1))
    res1 = factor(expr1, extension=True)
    assert res1 == (x - I)*(y - 1), f"Expected (x - I)*(y - 1), got {res1}"
    assert expand(res1) == expr1, f"expand({res1}) != {expr1}"

    # Multivariate polynomial with real algebraic coefficient
    expr2 = expand((x - sqrt(2))*(y - 1))
    res2 = factor(expr2, extension=True)
    assert res2 == (x - sqrt(2))*(y - 1), f"Expected (x - sqrt(2))*(y - 1), got {res2}"
    assert expand(res2) == expr2, f"expand({res2}) != {expr2}"


def test_ordinary_factoring():
    # Ordinary factoring of the example must continue to return (x - 1)*(y - 1).
    x, y = symbols('x y')
    z = expand((x - 1)*(y - 1))
    res = factor(z)
    assert res == (x - 1)*(y - 1), f"Expected (x - 1)*(y - 1), got {res}"
    assert expand(res) == z, f"expand({res}) != {z}"


def test_multivariate_products_complex_extension():
    # Factoring multivariate products over complex extensions must preserve the entire original polynomial.
    x, y, z = symbols('x y z')

    # Factoring over extension=I
    p0 = expand((x - 1)*(y - 1))
    res0 = factor(p0, extension=I)
    assert res0 == (x - 1)*(y - 1), f"Expected (x - 1)*(y - 1), got {res0}"
    assert expand(res0) == p0, f"expand({res0}) != {p0}"

    # (x**2 + 1)*(y - 1) over extension=[I]
    p1 = expand((x**2 + 1)*(y - 1))
    res1 = factor(p1, extension=[I])
    assert res1 == (x - I)*(x + I)*(y - 1), f"Expected (x - I)*(x + I)*(y - 1), got {res1}"
    assert expand(res1) == p1, f"expand({res1}) != {p1}"

    # (x - 1)*(y**2 + 1) over extension=[I]
    p2 = expand((x - 1)*(y**2 + 1))
    res2 = factor(p2, extension=[I])
    assert res2 == (x - 1)*(y - I)*(y + I), f"Expected (x - 1)*(y - I)*(y + I), got {res2}"
    assert expand(res2) == p2, f"expand({res2}) != {p2}"

    # 3 variables: (x - 1)*(y - 1)*(z - 1) over extension=[I]
    p3 = expand((x - 1)*(y - 1)*(z - 1))
    res3 = factor(p3, extension=[I])
    assert res3 == (x - 1)*(y - 1)*(z - 1), f"Expected (x - 1)*(y - 1)*(z - 1), got {res3}"
    assert expand(res3) == p3, f"expand({res3}) != {p3}"


def main():
    test_issue_factor_extension()
    test_factor_extension_true()
    test_ordinary_factoring()
    test_multivariate_products_complex_extension()
    print("All tests passed.")


if __name__ == '__main__':
    main()
