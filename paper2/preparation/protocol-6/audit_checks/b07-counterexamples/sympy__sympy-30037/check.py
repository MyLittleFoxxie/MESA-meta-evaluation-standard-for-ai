"""
Independent verification test for sympy__sympy-30037:
Improving rational integration in manualintegrate.
"""
import sys

def main():
    try:
        from sympy import (
            Symbol, symbols, Eq, S, exp, simplify, Integral, Piecewise
        )
        from sympy.integrals.manualintegrate import (
            manualintegrate,
            quadratic_denom_rule,
            cancel_rule,
            distribute_expand_rule,
            _if_zero_implies_zero,
        )
    except Exception as e:
        print(f"Import error: {e}", file=sys.stderr)
        sys.exit(1)

    def call_rule(rule, integrand, symbol):
        try:
            from sympy.integrals.manualintegrate import IntegralInfo
            try:
                return rule(IntegralInfo(integrand, symbol))
            except TypeError:
                return rule((integrand, symbol))
        except (ImportError, AttributeError):
            return rule((integrand, symbol))

    x = Symbol('x')
    a, b, c = symbols('a b c')

    # 1. Integrate constant or linear numerators over powers of quadratic denominators for n > 1
    f1 = 1 / (x**2 + 4*x + 2)**3
    res1 = manualintegrate(f1, x)
    assert not res1.has(Integral), f"Expected closed-form for {f1}, got {res1}"
    assert simplify(res1.diff(x) - f1) == 0, f"Derivative of {res1} did not match {f1}"

    f2 = (3*x + 5) / (x**2 + 4*x + 2)**3
    res2 = manualintegrate(f2, x)
    assert not res2.has(Integral), f"Expected closed-form for {f2}, got {res2}"
    assert simplify(res2.diff(x) - f2) == 0, f"Derivative of {res2} did not match {f2}"

    f_deg2 = (2*x + 7) / (x**2 + 2*x + 5)**2
    res_deg2 = manualintegrate(f_deg2, x)
    assert not res_deg2.has(Integral), f"Expected closed-form for {f_deg2}, got {res_deg2}"
    assert simplify(res_deg2.diff(x) - f_deg2) == 0, f"Derivative of {res_deg2} did not match {f_deg2}"

    # 2. Split linear numerator into derivative multiple and constant remainder
    f3 = (4*x + 7) / (x**2 + 2*x + 3)**2
    rule3 = call_rule(quadratic_denom_rule, f3, x)
    assert rule3 is not None, f"quadratic_denom_rule should match {f3}"
    res3 = rule3.eval()
    assert simplify(res3.diff(x) - f3) == 0, f"Derivative mismatch for {f3}"

    # Exact derivative in linear numerator
    f3_exact = (2*x + 2) / (x**2 + 2*x + 3)**2
    rule3_exact = call_rule(quadratic_denom_rule, f3_exact, x)
    assert rule3_exact is not None, f"quadratic_denom_rule should match {f3_exact}"
    res3_exact = rule3_exact.eval()
    assert simplify(res3_exact - (-1 / (x**2 + 2*x + 3))) == 0, f"Unexpected result for {f3_exact}"

    # 3. Reduce nondegenerate quadratic denominator from power n to n - 1
    f4 = 1 / (x**2 + 1)**2
    rule4 = call_rule(quadratic_denom_rule, f4, x)
    assert rule4 is not None, f"quadratic_denom_rule should match {f4}"
    res4 = rule4.eval()
    assert simplify(res4.diff(x) - f4) == 0, f"Derivative mismatch for {f4}"

    # 4. Handle zero discriminant by shifting variable and applying power rule
    f5 = 1 / (x**2 + 2*x + 1)**2
    rule5 = call_rule(quadratic_denom_rule, f5, x)
    assert rule5 is not None, f"quadratic_denom_rule should match {f5}"
    res5 = rule5.eval()
    assert simplify(res5 - (-1 / (3 * (x + 1)**3))) == 0, f"Unexpected result for {f5}: {res5}"
    assert simplify(res5.diff(x) - f5) == 0, f"Derivative mismatch for {f5}"

    # 5. Valid Piecewise branches without division by zero
    f6 = 1 / (a*x**2 + b*x + c)
    pw = manualintegrate(f6, x)
    assert isinstance(pw, Piecewise), f"Expected Piecewise for {f6}, got {type(pw)}"

    branch_a = [expr for expr, cond in pw.args if cond == Eq(a, 0)]
    assert len(branch_a) == 1, f"Expected exactly one branch for Eq(a, 0), found {len(branch_a)}"
    expr_a = branch_a[0]
    # Branch for a = 0 must not contain a or divide by a
    assert not expr_a.has(a), f"Branch for a = 0 should not depend on a: {expr_a}"

    branch_disc = [expr for expr, cond in pw.args if cond == Eq(4*a*c - b**2, 0)]
    assert len(branch_disc) == 1, f"Expected branch for Eq(4*a*c - b**2, 0), found {len(branch_disc)}"

    # 6. Extract rational numerator and denominator coefficients with Poly (factored & constant factors)
    f7_unexpanded = 1 / ((x - 2)*(x + 3) + 7)
    rule7_unexpanded = call_rule(quadratic_denom_rule, f7_unexpanded, x)
    assert rule7_unexpanded is not None, f"quadratic_denom_rule should match unexpanded {f7_unexpanded}"
    res7_unexpanded = rule7_unexpanded.eval()
    assert simplify(res7_unexpanded.diff(x) - f7_unexpanded) == 0

    f7_const = 1 / (3 * (x**2 + 2*x + 2)**2)
    rule7_const = call_rule(quadratic_denom_rule, f7_const, x)
    assert rule7_const is not None, f"quadratic_denom_rule should match denominator with constant factor {f7_const}"
    res7_const = rule7_const.eval()
    assert simplify(res7_const.diff(x) - f7_const) == 0

    # 7. Avoid redundant expand and cancel alternatives for rational integrands
    r = (x + 1) / (x**2 - 1)
    assert call_rule(cancel_rule, r, x) is None, f"cancel_rule should return None for rational {r}"

    p = (x + 1)**2
    assert call_rule(distribute_expand_rule, p, x) is None, f"distribute_expand_rule should return None for rational {p}"

    h = (exp(x) + 1)**2
    assert call_rule(distribute_expand_rule, h, x) is not None, f"distribute_expand_rule should trigger for non-rational {h}"

    k = (exp(2*x) - 1) / (exp(x) - 1)
    assert call_rule(cancel_rule, k, x) is not None, f"cancel_rule should trigger for non-rational {k}"

    # 8. Check _if_zero_implies_zero optimization
    assert _if_zero_implies_zero(S(2), x) is True
    assert _if_zero_implies_zero(S(0), S(0)) is True
    assert _if_zero_implies_zero(S(0), S(1)) is False

    print("All tests passed successfully.")
    sys.exit(0)

if __name__ == '__main__':
    main()
