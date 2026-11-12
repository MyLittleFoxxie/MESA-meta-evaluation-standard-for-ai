"""
Verification script for sympy__sympy-30311:
Refactor manualintegrate into a stateful solver with stateless generator rules,
supporting branching control, depth limits, shifted exponential quotients,
polynomial-quadratic trigonometric products, and Fresnel antiderivatives.
"""

import sys
import types
from sympy.core.numbers import E, I, Rational, pi
from sympy.core.symbol import Dummy, Symbol
from sympy.functions.elementary.exponential import exp
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.functions.elementary.trigonometric import cos, sin
from sympy.functions.special.error_functions import Ei, fresnelc
from sympy.integrals.integrals import Integral, integrate
from sympy.integrals.manualintegrate import (
    AddRule,
    AlternativeRule,
    BranchQuery,
    ConstantRule,
    DontKnowRule,
    IntegralInfo,
    IntegrationSolver,
    PartsUCheck,
    URule,
    add_rule,
    alternatives,
    integral_steps,
    manualintegrate,
    mul_rule,
    trig_cmplx_exp_rule,
    trig_poly_mul_rule,
    trig_product_to_sum_rule,
)


def test_solver_architecture():
    """Verify IntegrationSolver exists and owns search state."""
    x = Symbol("x")

    solver = IntegrationSolver(max_depth=50, branch=True)
    assert solver.max_depth == 50, f"Expected max_depth=50, got {solver.max_depth}"
    assert solver.branch is True, f"Expected branch=True, got {solver.branch}"
    assert isinstance(solver._active, set), "Expected _active to be a set"
    assert isinstance(solver._parts_u_count, dict), "Expected _parts_u_count to be a dict"
    assert isinstance(solver._solved, dict), "Expected _solved to be a dict"
    assert solver._starved is False, "Expected _starved to be False initially"

    # Solver state isolation between instances
    s1 = IntegrationSolver()
    s2 = IntegrationSolver()
    s1._active.add(1)
    assert 1 not in s2._active, "Solvers should have isolated _active sets"

    # PartsUCheck counter
    assert s1._check_parts_u(x) is True
    assert s1._parts_u_count[x] == 1
    assert s2._parts_u_count[x] == 0, "Solvers should have isolated parts counters"
    assert s1._check_parts_u(x) is True
    assert s1._check_parts_u(x) is True
    # Exceeding the parts-u limit (> 2 uses already recorded) returns False
    assert s1._check_parts_u(x) is False

    # PartsUCheck and BranchQuery request handling via run_generator
    def gen_parts():
        allowed = yield PartsUCheck(Dummy("z"))
        return allowed

    def gen_branch():
        b = yield BranchQuery()
        return b

    assert s1.run_generator(gen_parts()) is True

    s_nobranch = IntegrationSolver(branch=False)
    s_branch = IntegrationSolver(branch=True)
    assert s_nobranch.run_generator(gen_branch()) is False
    assert s_branch.run_generator(gen_branch()) is True


def test_generator_rules():
    """Verify rules act as generators requesting subproblems with IntegralInfo."""
    x = Symbol("x")

    # add_rule is a generator
    gen_add = add_rule(IntegralInfo(x + 1, x))
    assert isinstance(gen_add, types.GeneratorType), "add_rule should return a generator"
    req_add = next(gen_add)
    assert isinstance(req_add, IntegralInfo), "add_rule should yield IntegralInfo"

    # mul_rule is a generator
    gen_mul = mul_rule(IntegralInfo(2 * x, x))
    assert isinstance(gen_mul, types.GeneratorType), "mul_rule should return a generator"
    req_mul = next(gen_mul)
    assert isinstance(req_mul, IntegralInfo), "mul_rule should yield IntegralInfo"
    assert req_mul.integrand == x

    # IntegrationSolver drives generator rules to completion
    solver = IntegrationSolver()
    step = solver.run(add_rule, IntegralInfo(x + 1, x))
    assert isinstance(step, AddRule), "Driving add_rule should produce AddRule"
    assert not step.contains_dont_know()


def test_depth_limits_and_caching():
    """Verify max_depth enforcement and safe result caching."""
    x = Symbol("x")

    # max_depth=1 starves subproblem solving for expressions needing subintegrals
    step_starved = integral_steps(x + 1, x, max_depth=1)
    assert step_starved.contains_dont_know(), "max_depth=1 should yield DontKnowRule for subproblems"

    # Default depth solves without starvation
    step_normal = integral_steps(x + 1, x)
    assert not step_normal.contains_dont_know(), "Normal depth should solve x + 1"

    # Cache population on solver
    solver = IntegrationSolver()
    r1 = solver.solve(x**2, x)
    assert len(solver._solved) > 0, "Completed subproblems should be cached in _solved"
    r2 = solver.solve(x**2, x)
    assert r1.eval() == r2.eval(), "Cached results should match"


def test_branching_alternatives():
    """Verify first-success (branch=False) vs all-alternatives (branch=True)."""
    x = Symbol("x")

    r1 = lambda info: ConstantRule(1, info.symbol)
    r2 = lambda info: ConstantRule(2, info.symbol)

    strat_nobranch = alternatives(r1, r2, branch=False)
    res_nobranch = strat_nobranch(IntegralInfo(x, x))
    assert isinstance(res_nobranch, ConstantRule), "branch=False should return first rule directly"
    assert not isinstance(res_nobranch, AlternativeRule), "branch=False should not wrap in AlternativeRule"

    strat_branch = alternatives(r1, r2, branch=True)
    res_branch = strat_branch(IntegralInfo(x, x))
    assert isinstance(res_branch, AlternativeRule), "branch=True should combine into AlternativeRule"


def test_shifted_exponential_quotients():
    """Verify integrating shifted exponential quotients like exp(x)/(x-1)."""
    x = Symbol("x")

    f1 = exp(x) / (x - 1)
    F1 = manualintegrate(f1, x)
    assert not F1.has(Integral), f"exp(x)/(x-1) produced unevaluated Integral: {F1}"
    assert F1 == E * Ei(x - 1), f"Unexpected result for exp(x)/(x-1): {F1}"
    assert (F1.diff(x) - f1).simplify() == 0, "Derivative does not match integrand"

    f2 = exp(x) / (x + 2)
    F2 = manualintegrate(f2, x)
    assert not F2.has(Integral), f"exp(x)/(x+2) produced unevaluated Integral: {F2}"
    assert (F2.diff(x) - f2).simplify() == 0, "Derivative does not match integrand"


def test_polynomial_quadratic_trig_products():
    """Verify integrating x**2*sin(x**2)*cos(x) and trig product-to-sum rewrites."""
    x = Symbol("x")

    # Verify trig_product_to_sum_rule is available and produces a generator
    gen = trig_product_to_sum_rule(IntegralInfo(sin(x**2) * cos(x), x))
    assert isinstance(gen, types.GeneratorType), "trig_product_to_sum_rule should return a generator"

    f = x**2 * sin(x**2) * cos(x)
    F = manualintegrate(f, x)
    assert not F.has(Integral), f"x**2*sin(x**2)*cos(x) produced unevaluated Integral: {F}"

    dF = F.diff(x)
    assert not dF.has(Integral)
    # Check derivative numerically at multiple test points
    for pt in (Rational(1, 2), Rational(3, 4), Rational(1, 1)):
        err = abs((dF - f).subs(x, pt).evalf())
        assert err < 1e-10, f"Derivative mismatch at x={pt}: err={err}"


def test_fresnel_with_polynomial_arguments():
    """Verify integrating polynomial factors times Fresnel functions."""
    x = Symbol("x")

    arg = sqrt(2) * (2 * x + 1) / (2 * sqrt(pi))
    f = x * fresnelc(arg)
    F = manualintegrate(f, x)
    assert not F.has(Integral), f"x*fresnelc(...) produced unevaluated Integral: {F}"

    dF = F.diff(x)
    assert not dF.has(Integral)
    for pt in (Rational(1, 3), Rational(2, 3), Rational(1, 2)):
        err = abs((dF - f).subs(x, pt).evalf())
        assert err < 1e-10, f"Fresnel derivative mismatch at x={pt}: err={err}"


def test_sin_quadratic_plus_linear_times_cos():
    """Verify integrating sin(x**2+x)*cos(x)."""
    x = Symbol("x")

    f = sin(x**2 + x) * cos(x)
    F = manualintegrate(f, x)
    assert not F.has(Integral), f"sin(x**2+x)*cos(x) produced unevaluated Integral: {F}"

    dF = F.diff(x)
    assert not dF.has(Integral)
    for pt in (Rational(1, 4), Rational(1, 2), Rational(3, 4)):
        err = abs((dF - f).subs(x, pt).evalf())
        assert err < 1e-10, f"sin(x**2+x)*cos(x) derivative mismatch at x={pt}: err={err}"


def test_exp_sin_quadratic_times_cos_termination():
    """Verify search termination and exponential rewrites for exp(x)*sin(x**2+x)*cos(x)."""
    x = Symbol("x")

    f = exp(x) * sin(x**2 + x) * cos(x)

    # trig_cmplx_exp_rule applies to this integrand with quadratic phase
    gen = trig_cmplx_exp_rule(IntegralInfo(f, x))
    assert isinstance(gen, types.GeneratorType), "trig_cmplx_exp_rule should apply and return generator"

    # manualintegrate terminates cleanly and finds the antiderivative
    F = manualintegrate(f, x)
    assert not F.has(Integral), f"exp(x)*sin(x**2+x)*cos(x) produced unevaluated Integral: {F}"

    dF = F.diff(x)
    for pt in (Rational(1, 3), Rational(1, 2)):
        err = abs((dF - f).subs(x, pt).evalf())
        assert err < 1e-10, f"exp*sin*cos derivative mismatch at x={pt}: err={err}"


def test_public_api_and_baseline_integrals():
    """Verify public integrate(..., manual=True) and standard manualintegrate behaviors."""
    x = Symbol("x")

    # integrate(..., manual=True) uses manualintegrate pipeline
    res = integrate(exp(x) / (x - 1), x, manual=True)
    assert not res.has(Integral)
    assert (res.diff(x) - exp(x) / (x - 1)).simplify() == 0

    # Baseline integrals continue to work correctly
    assert manualintegrate(x**2, x) == x**3 / 3
    assert manualintegrate(exp(x), x) == exp(x)
    assert manualintegrate(sin(x), x) == -cos(x)


def main():
    print("Running b07_check test suite...")
    test_solver_architecture()
    print("  [PASS] Solver architecture and state isolation")
    test_generator_rules()
    print("  [PASS] Generator rules request subproblems via IntegralInfo")
    test_depth_limits_and_caching()
    print("  [PASS] Depth limits and safe result caching")
    test_branching_alternatives()
    print("  [PASS] Branching control (branch=False vs branch=True)")
    test_shifted_exponential_quotients()
    print("  [PASS] Shifted exponential quotients (exp(x)/(x-1))")
    test_polynomial_quadratic_trig_products()
    print("  [PASS] Polynomial * quadratic trig products (x**2*sin(x**2)*cos(x))")
    test_fresnel_with_polynomial_arguments()
    print("  [PASS] Fresnel functions with polynomial arguments")
    test_sin_quadratic_plus_linear_times_cos()
    print("  [PASS] sin(x**2+x)*cos(x) integration")
    test_exp_sin_quadratic_times_cos_termination()
    print("  [PASS] exp(x)*sin(x**2+x)*cos(x) termination and exponential rewrites")
    test_public_api_and_baseline_integrals()
    print("  [PASS] Public API and baseline integration preservation")

    print("\nAll b07_check tests passed successfully!")
    sys.exit(0)


if __name__ == "__main__":
    main()
