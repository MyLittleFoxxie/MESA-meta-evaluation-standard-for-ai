"""Verification script for sympy__sympy-30530.

Issue: improve singularity handling in `inequalities.py`
Behaviors requested:
- Preserve singularities from both sides of an inequality through high-level reduction.
- Exclude values where an original denominator is zero, even when subtraction cancels that denominator.
- Keep the valid solutions of the inequality while excluding those undefined points.
"""

import sys
from sympy import Symbol, S, Eq, Ne
from sympy.solvers.inequalities import (
    reduce_inequalities,
    _solve_inequality,
    reduce_rational_inequalities,
)


def test_reduce_inequalities_identity_with_singularity():
    # Eq(1 - x, x*(1/x - 1)) is algebraically an identity (0 == 0),
    # but x = 0 is a singularity from the right-hand side denominator.
    x = Symbol('x')
    e = Eq(1 - x, x * (1 / x - 1))
    sol = reduce_inequalities(e, x)
    assert sol != S.true and sol is not True, (
        f"Expected singularity x=0 to be preserved, got {sol}"
    )
    assert sol == Ne(x, 0), f"Expected Ne(x, 0), got {sol}"
    assert sol.subs(x, 0) == False, f"x=0 should be excluded from {sol}"
    assert sol.subs(x, 2) == True, f"x=2 should be included in {sol}"


def test_reduce_inequalities_strict_with_cancelled_denom():
    # x < x*(1/x - 1) simplifies to 2*x - 1 < 0 (x < 1/2),
    # but x = 0 is undefined in the original inequality.
    x = Symbol('x')
    sol = reduce_inequalities(x < x * (1 / x - 1), x)
    assert sol.subs(x, 0) == False, f"x=0 must be excluded from {sol}"
    assert sol.subs(x, -1) == True, f"x=-1 should be valid in {sol}"
    assert sol.subs(x, 1) == False, f"x=1 should not be valid in {sol}"
    assert sol == ((x < S.Half) & Ne(x, 0)), (
        f"Expected (x < 1/2) & Ne(x, 0), got {sol}"
    )


def test_reduce_inequalities_constant_subtraction():
    # 1/x <= 1/x + 1 simplifies to -1 <= 0 (all real numbers),
    # but x = 0 is undefined on both sides.
    x = Symbol('x')
    sol = reduce_inequalities(1 / x <= 1 / x + 1, x)
    assert sol != S.true and sol is not True, (
        f"Expected singularity x=0 to be excluded, got {sol}"
    )
    assert sol.subs(x, 0) == False, f"x=0 must be excluded from {sol}"
    assert sol.subs(x, 1) == True, f"x=1 must be included in {sol}"
    assert sol == Ne(x, 0), f"Expected Ne(x, 0), got {sol}"


def test_reduce_inequalities_shifted_singularity():
    # x + 1/(x - 2) > 1/(x - 2) simplifies to x > 0,
    # but x = 2 is undefined on both sides.
    x = Symbol('x')
    sol = reduce_inequalities(x + 1 / (x - 2) > 1 / (x - 2), x)
    assert sol.subs(x, 2) == False, f"x=2 must be excluded from {sol}"
    assert sol.subs(x, 1) == True, f"x=1 must be included in {sol}"
    assert sol.subs(x, -1) == False, f"x=-1 must be excluded from {sol}"
    assert sol == ((S.Zero < x) & Ne(x, 2)), (
        f"Expected (0 < x) & Ne(x, 2), got {sol}"
    )


def test_reduce_inequalities_system():
    # System of inequalities where one has a denominator that cancels
    x = Symbol('x')
    sol = reduce_inequalities([1 / x <= 1 / x + 1, x > -2], x)
    assert sol.subs(x, 0) == False, f"x=0 must be excluded from system {sol}"
    assert sol.subs(x, 1) == True, f"x=1 must be included in system {sol}"
    assert sol.subs(x, -3) == False, f"x=-3 must be excluded from system {sol}"


def test_solve_inequality_constant_subtraction():
    # _solve_inequality should also exclude singularities when degree is 0
    x = Symbol('x')
    sol = _solve_inequality(1 / x <= 1 / x + 1, x)
    assert sol != S.true and sol is not True, (
        f"Expected Ne(x, 0), got {sol}"
    )
    assert sol.subs(x, 0) == False, f"x=0 must be excluded from {sol}"
    assert sol == Ne(x, 0), f"Expected Ne(x, 0), got {sol}"

    sol2 = _solve_inequality(1 / (x - 5) >= 1 / (x - 5), x)
    assert sol2.subs(x, 5) == False, f"x=5 must be excluded from {sol2}"
    assert sol2 == Ne(x, 5), f"Expected Ne(x, 5), got {sol2}"


def test_solve_inequality_quadratic_denom():
    # When denominator is non-linear and cancelled
    x = Symbol('x')
    sol = _solve_inequality(1 / (x**2 - 4) <= 1 / (x**2 - 4) + 1, x)
    assert sol.subs(x, 2) == False, f"x=2 must be excluded from {sol}"
    assert sol.subs(x, -2) == False, f"x=-2 must be excluded from {sol}"
    assert sol.subs(x, 0) == True, f"x=0 must be included in {sol}"


def test_reduce_rational_inequalities_lost_factors():
    # reduce_rational_inequalities should preserve denominators lost during subtraction
    x = Symbol('x')
    rel_sol = reduce_rational_inequalities([[1 / x <= 1 / x + 1]], x)
    assert rel_sol.subs(x, 0) == False, f"x=0 must be excluded from {rel_sol}"
    assert rel_sol.subs(x, 1) == True, f"x=1 must be included in {rel_sol}"

    set_sol = reduce_rational_inequalities([[1 / (x - 3) <= 1 / (x - 3) + 1]], x, relational=False)
    assert 3 not in set_sol, f"x=3 must not be in set {set_sol}"
    assert 0 in set_sol, f"x=0 must be in set {set_sol}"


def main():
    test_reduce_inequalities_identity_with_singularity()
    test_reduce_inequalities_strict_with_cancelled_denom()
    test_reduce_inequalities_constant_subtraction()
    test_reduce_inequalities_shifted_singularity()
    test_reduce_inequalities_system()
    test_solve_inequality_constant_subtraction()
    test_solve_inequality_quadratic_denom()
    test_reduce_rational_inequalities_lost_factors()
    print("All verification checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
