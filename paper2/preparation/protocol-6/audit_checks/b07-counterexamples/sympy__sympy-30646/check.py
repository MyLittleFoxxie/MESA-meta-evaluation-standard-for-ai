"""Verification test script for sympy__sympy-30646.

Verifies fixes in lie_group heuristics:
1. lie_heuristic_abaco2_unique_general: symbolic expression membership errors (TypeError on Mul/Pow)
2. lie_heuristic_bivariate: uninitialized polyy UnboundLocalError
3. lie_heuristic_abaco2_similar: KeyError on C_ and TypeError on NoneType match
4. hint='default' and hint='all' continue through heuristics properly
"""

import sys
from sympy import Function, symbols, diff, exp
from sympy.solvers.ode.lie_group import (
    infinitesimals,
    lie_heuristic_abaco2_similar,
)


def test_kamke_1_117_default_hint():
    # Kamke 1.117: expression-membership TypeError in lie_heuristic_abaco2_unique_general
    x = symbols('x')
    y = Function('y')(x)
    eq = x*diff(y, x) - y - x - x*exp(y/x)
    res = infinitesimals(eq, y)
    assert isinstance(res, list) and len(res) > 0, (
        f"Expected non-empty list of infinitesimals for Kamke 1.117 (default hint), got {res}"
    )


def test_kamke_1_117_all_hints():
    # Kamke 1.117 with hint='all'
    x = symbols('x')
    y = Function('y')(x)
    eq = x*diff(y, x) - y - x - x*exp(y/x)
    res = infinitesimals(eq, y, hint='all')
    assert isinstance(res, list) and len(res) > 0, (
        f"Expected non-empty list of infinitesimals for Kamke 1.117 (hint='all'), got {res}"
    )


def test_uninitialized_polyy_bivariate():
    # y' = 1 - y**2: hint='all' triggers lie_heuristic_bivariate where polyy was uninitialized
    x = symbols('x')
    y = Function('y')(x)
    eq = diff(y, x) + y**2 - 1
    res = infinitesimals(eq, y, hint='all')
    assert isinstance(res, list) and len(res) > 0, (
        f"Expected non-empty list of infinitesimals for y' = 1 - y**2, got {res}"
    )


def test_abaco2_similar_keyerror_kamke_1_382():
    # Kamke 1.382: missing wild match C_ causes KeyError in lie_heuristic_abaco2_similar
    x, a, b, c = symbols('x a b c')
    y = Function('y')(x)
    eq = diff(y, x)**2 + a*x*diff(y, x) - b*x**2 - c
    res = infinitesimals(eq, y, hint='all')
    assert isinstance(res, list), (
        f"Expected list of infinitesimals for Kamke 1.382, got {res}"
    )


def test_abaco2_similar_nonetype_match():
    # In abaco2_similar inverse check block: match on hinv instead of h,
    # handling NoneType match without TypeError
    x, y_sym = symbols('x y')
    func = Function('y')(x)
    h = y_sym**(1 + 1/x) / (1 + 1/x)
    match_dict = {
        'h': h,
        'hx': h.diff(x),
        'hy': h.diff(y_sym),
        'func': func,
        'hinv': exp(y_sym),
        'y': y_sym,
    }
    # Should not raise TypeError: 'NoneType' object is not subscriptable
    res = lie_heuristic_abaco2_similar(match_dict)
    assert res is None or isinstance(res, list), (
        f"Expected None or list from lie_heuristic_abaco2_similar, got {res}"
    )


def main():
    test_kamke_1_117_default_hint()
    test_kamke_1_117_all_hints()
    test_uninitialized_polyy_bivariate()
    test_abaco2_similar_keyerror_kamke_1_382()
    test_abaco2_similar_nonetype_match()
    print("All lie_group heuristic verification tests passed successfully.")
    sys.exit(0)


if __name__ == '__main__':
    main()
