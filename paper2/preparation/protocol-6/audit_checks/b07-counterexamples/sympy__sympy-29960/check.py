"""
Verification script for sympy__sympy-29960.
Tests:
1. integrate(x*exp(x)*erf(x), x) returns a closed-form antiderivative.
2. manualintegrate(x*exp(x)*erf(x), x) reduces the integral to a solvable remainder involving Integral(x*exp(-x**2 + x), x).
3. integrate(x*exp(-x**2 + x), x, heurisch=True) evaluates to -exp(x)*exp(-x**2)/2 + sqrt(pi)*exp(1/4)*erf(x - 1/2)/4.
"""
import sys
from sympy import (
    Symbol,
    Rational,
    exp,
    erf,
    sqrt,
    pi,
    Integral,
    integrate,
    simplify,
)
from sympy.integrals.manualintegrate import manualintegrate


def test_integrate_x_exp_erf():
    x = Symbol('x')
    f = x * exp(x) * erf(x)
    result = integrate(f, x)

    # Must return a closed-form antiderivative without unevaluated Integral
    assert not result.has(Integral), f"integrate({f}, x) returned unevaluated Integral: {result}"

    # Verify that differentiating the result gives back the integrand
    derivative = result.diff(x)
    diff_simplified = simplify(derivative - f)
    assert diff_simplified == 0 or (derivative - f).equals(0), (
        f"Derivative of antiderivative does not match integrand: {derivative} != {f}"
    )


def test_manualintegrate_reduction():
    x = Symbol('x')
    f = x * exp(x) * erf(x)
    mres = manualintegrate(f, x)

    rem_integrals = mres.atoms(Integral)
    assert len(rem_integrals) > 0, (
        f"Expected unevaluated Integral in manualintegrate result, got: {mres}"
    )

    # Must reduce the integral to a solvable remainder involving Integral(x*exp(-x**2 + x), x)
    # On unpatched sympy, this remained Integral(x*exp(x)*exp(-x**2), x) where powers were not combined.
    has_combined_remainder = any(
        itg == Integral(x * exp(-x**2 + x), x) or
        itg == Integral(x * exp(x - x**2), x) or
        itg.function == x * exp(-x**2 + x) or
        itg.function == x * exp(x - x**2)
        for itg in rem_integrals
    )
    assert has_combined_remainder, (
        f"manualintegrate did not reduce to Integral(x*exp(-x**2 + x), x). "
        f"Found remaining integrals: {rem_integrals}"
    )


def test_integrate_heurisch_intermediate():
    x = Symbol('x')
    f = x * exp(-x**2 + x)
    hres = integrate(f, x, heurisch=True)

    assert not hres.has(Integral), (
        f"integrate({f}, x, heurisch=True) returned unevaluated Integral: {hres}"
    )

    expected = (
        -exp(x) * exp(-x**2) / 2
        + sqrt(pi) * exp(Rational(1, 4)) * erf(x - Rational(1, 2)) / 4
    )
    assert simplify(hres - expected) == 0 or (hres - expected).equals(0), (
        f"integrate({f}, x, heurisch=True) = {hres}, expected {expected}"
    )


def main():
    print("Running test_integrate_x_exp_erf...")
    test_integrate_x_exp_erf()
    print("test_integrate_x_exp_erf passed.")

    print("Running test_manualintegrate_reduction...")
    test_manualintegrate_reduction()
    print("test_manualintegrate_reduction passed.")

    print("Running test_integrate_heurisch_intermediate...")
    test_integrate_heurisch_intermediate()
    print("test_integrate_heurisch_intermediate passed.")

    print("All tests passed successfully.")
    sys.exit(0)


if __name__ == '__main__':
    main()
