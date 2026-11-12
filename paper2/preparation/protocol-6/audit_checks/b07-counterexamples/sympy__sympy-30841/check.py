"""Verification script for sympy__sympy-30841.
Tests fixes for singularities() and continuous_domain() with 0**exp and variable-exponent powers.
"""
import sys
from sympy import Symbol, Interval, S, Union, FiniteSet, oo
from sympy.calculus.singularities import singularities
from sympy.calculus.util import continuous_domain


def main():
    x = Symbol('x', real=True)

    # 1. 0**exp when exponent is strictly positive on a subdomain
    # Prior to fix: solveset returned EmptySet and EmptySet.inf crashed with NotImplementedError.
    sing_1 = singularities(0**(x - 1), x, Interval(2, 5))
    assert sing_1 == S.EmptySet, f"Expected EmptySet, got {sing_1}"

    dom_1 = continuous_domain(0**(x - 1), x, Interval(2, 5))
    assert dom_1 == Interval(2, 5), f"Expected Interval(2, 5), got {dom_1}"

    # 2. Disconnected solution sets for 0**exp
    # Prior to fix: Interval.open(inf, sup) corrupted (-oo, -1) U (1, oo) to Interval(-oo, oo).
    sing_2 = singularities(0**(1 - x**2), x)
    expected_sing_2 = Union(Interval.open(-oo, -1), Interval.open(1, oo))
    assert sing_2 == expected_sing_2, f"Expected {expected_sing_2}, got {sing_2}"

    dom_2 = continuous_domain(0**(1 - x**2), x, S.Reals)
    assert dom_2 == Interval(-1, 1), f"Expected Interval(-1, 1), got {dom_2}"

    # 3. Exclude exponent-zero points for 0**exp powers
    sing_zero_exp = singularities(0**(x - 1), x, Interval(1, 5))
    assert sing_zero_exp == S.EmptySet, f"Expected EmptySet, got {sing_zero_exp}"

    sing_bounded = singularities(0**(x - 1), x, Interval(0, 5))
    expected_bounded = Interval.Ropen(0, 1)
    assert sing_bounded == expected_bounded, f"Expected {expected_bounded}, got {sing_bounded}"

    # 4. Variable base with variable exponent
    # Prior to fix: i.exp.is_negative evaluated to None, skipping check and returning EmptySet.
    sing_var_1 = singularities((x - 2)**(x - 3), x)
    assert sing_var_1 == FiniteSet(2), f"Expected FiniteSet(2), got {sing_var_1}"

    sing_var_2 = singularities((x**2 - 4)**(x - 1), x)
    assert sing_var_2 == FiniteSet(-2), f"Expected FiniteSet(-2), got {sing_var_2}"

    sing_var_3 = singularities(((x - 1)*(x - 3))**(x - 2), x)
    assert sing_var_3 == FiniteSet(1), f"Expected FiniteSet(1), got {sing_var_3}"

    sing_var_4 = singularities((x - 2)**(3 - x), x)
    assert sing_var_4 == S.EmptySet, f"Expected EmptySet, got {sing_var_4}"

    print("All verification checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
