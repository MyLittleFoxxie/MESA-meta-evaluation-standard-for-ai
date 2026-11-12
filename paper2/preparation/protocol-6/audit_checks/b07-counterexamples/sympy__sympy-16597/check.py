#!/usr/bin/env python3
"""
Verification check for sympy__sympy-16597:
Verifies that even symbols and values known to be even imply finite (is_finite is True).
"""

import sys


def test_even_symbol_is_finite():
    from sympy import Symbol

    m = Symbol('m', even=True)
    assert m.is_even is True, f"Expected m.is_even to be True, got {m.is_even}"
    assert m.is_finite is True, f"Expected m.is_finite to be True, got {m.is_finite}"
    assert m.is_infinite is False, f"Expected m.is_infinite to be False, got {m.is_infinite}"


def test_even_expression_is_finite():
    from sympy import Symbol

    k = Symbol('k', even=True)
    neg_k = -k
    assert neg_k.is_even is True, f"Expected (-k).is_even to be True, got {neg_k.is_even}"
    assert neg_k.is_finite is True, f"Expected (-k).is_finite to be True, got {neg_k.is_finite}"

    x = Symbol('x', integer=True)
    even_expr = 2 * x
    assert even_expr.is_even is True, f"Expected (2*x).is_even to be True, got {even_expr.is_even}"
    assert even_expr.is_finite is True, f"Expected (2*x).is_finite to be True, got {even_expr.is_finite}"


def test_even_assumption_implies_finite():
    from sympy import Symbol
    from sympy.assumptions import ask, Q

    a = Symbol('a')
    res = ask(Q.finite(a), Q.even(a))
    assert res is True, f"Expected ask(Q.finite(a), Q.even(a)) to be True, got {res}"

    m = Symbol('m', even=True)
    res_m = ask(Q.finite(m))
    assert res_m is True, f"Expected ask(Q.finite(m)) to be True, got {res_m}"


def main():
    try:
        test_even_symbol_is_finite()
        test_even_expression_is_finite()
        test_even_assumption_implies_finite()
        print("All tests passed.")
        sys.exit(0)
    except AssertionError as e:
        print(f"Assertion failed: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
