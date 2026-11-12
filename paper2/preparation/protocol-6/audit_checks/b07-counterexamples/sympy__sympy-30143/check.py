import sys


def test_owens_t_and_integrals():
    # 1. Verify owens_t is provided in SymPy and can be imported
    try:
        from sympy import owens_t
    except ImportError as e:
        raise AssertionError(f"Could not import owens_t from sympy: {e}")

    from sympy.functions.special.error_functions import owens_t as owens_t_direct
    assert owens_t is owens_t_direct, (
        "owens_t from sympy is not identical to sympy.functions.special.error_functions.owens_t"
    )

    from sympy import Symbol, exp, erf, erfc, integrate, pi, sqrt, atan, S, diff, oo, Integral, latex, pretty

    x = Symbol('x')
    y = Symbol('y')
    n = Symbol('n')
    h = Symbol('h')
    a = Symbol('a')

    # Basic special values and symmetry properties
    assert owens_t(h, 0) == S.Zero, f"Expected owens_t(h, 0) == 0, got {owens_t(h, 0)}"
    assert owens_t(0, a) == atan(a) / (2 * pi), f"Expected owens_t(0, a) == atan(a)/(2*pi), got {owens_t(0, a)}"
    assert owens_t(-h, a) == owens_t(h, a), "owens_t should be even in first argument (h)"
    assert owens_t(h, -a) == -owens_t(h, a), "owens_t should be odd in second argument (a)"
    assert owens_t(h, 1) == erfc(-h / sqrt(2)) * erfc(h / sqrt(2)) / 8, "owens_t(h, 1) mismatch"
    assert owens_t(h, -1) == -erfc(-h / sqrt(2)) * erfc(h / sqrt(2)) / 8, "owens_t(h, -1) mismatch"
    assert owens_t(oo, a) == S.Zero, "owens_t(oo, a) should evaluate to 0"
    assert owens_t(-oo, a) == S.Zero, "owens_t(-oo, a) should evaluate to 0"

    # Differentiation
    dh = diff(owens_t(h, a), h)
    expected_dh = -sqrt(2) * exp(-h**2 / 2) * erf(sqrt(2) * a * h / 2) / (4 * sqrt(pi))
    assert (dh - expected_dh).simplify() == 0, f"diff(owens_t(h, a), h) mismatch: {dh} vs {expected_dh}"

    da = diff(owens_t(h, a), a)
    expected_da = exp(-h**2 * (a**2 + 1) / 2) / (2 * pi * (a**2 + 1))
    assert (da - expected_da).simplify() == 0, f"diff(owens_t(h, a), a) mismatch: {da} vs {expected_da}"

    # Assumptions / realness
    assert owens_t(1, 2).is_extended_real is True
    assert owens_t(1, 2).is_positive is True
    assert owens_t(1, -2).is_negative is True

    # Printing
    assert latex(owens_t(h, a)) == r"T\left(h, a\right)", f"LaTeX print mismatch: {latex(owens_t(h, a))}"
    assert pretty(owens_t(h, a)) == "T(h, a)", f"Pretty print mismatch: {pretty(owens_t(h, a))}"

    # 2. Evaluate integrate(exp(-x**2)*erf(y*x), x) for a symbolic parameter y
    res_y = integrate(exp(-x**2) * erf(y * x), x)
    assert not isinstance(res_y, Integral), f"Integral remained unevaluated: {res_y}"
    expected_y = -2 * sqrt(pi) * owens_t(sqrt(2) * x, y)
    assert res_y == expected_y, f"Expected {expected_y}, got {res_y}"

    # Verify antiderivative derivative reproduces the integrand
    diff_res_y = diff(res_y, x)
    assert (diff_res_y - exp(-x**2) * erf(y * x)).simplify() == 0, (
        f"Derivative of antiderivative {diff_res_y} does not match integrand {exp(-x**2)*erf(y*x)}"
    )

    # 3. Evaluate the same integral with parameter n
    res_n = integrate(exp(-x**2) * erf(n * x), x)
    assert not isinstance(res_n, Integral), f"Integral remained unevaluated: {res_n}"
    expected_n = -2 * sqrt(pi) * owens_t(sqrt(2) * x, n)
    assert res_n == expected_n, f"Expected {expected_n}, got {res_n}"

    diff_res_n = diff(res_n, x)
    assert (diff_res_n - exp(-x**2) * erf(n * x)).simplify() == 0, (
        f"Derivative of antiderivative {diff_res_n} does not match integrand {exp(-x**2)*erf(n*x)}"
    )


if __name__ == "__main__":
    try:
        test_owens_t_and_integrals()
        print("b07_check passed successfully.")
        sys.exit(0)
    except AssertionError as e:
        print(f"Assertion failed: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)
