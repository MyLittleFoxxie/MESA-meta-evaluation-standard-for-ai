import sys
from sympy import Symbol, S, I, sqrt, diff, asech, acosh


def test_asech_derivative():
    x = Symbol('x')
    d_sym = diff(asech(x), x)
    expected_sym = -sqrt(1/(x + 1))/(x*sqrt(1 - x))

    # Check symbolic derivative formula matches the corrected formula
    assert d_sym == expected_sym, f"Expected {expected_sym}, got {d_sym}"

    # Check derivative at x = -2 evaluates to sqrt(3)*I/6
    val_neg2 = d_sym.subs(x, -2)
    expected_neg2 = sqrt(3)*I/6
    assert val_neg2 == expected_neg2, f"At x = -2, expected {expected_neg2}, got {val_neg2}"

    # Also test with symbols known to be negative
    y = Symbol('y', negative=True)
    d_neg = diff(asech(y), y)
    expected_y = -sqrt(1/(y + 1))/(y*sqrt(1 - y))
    assert d_neg == expected_y, f"Expected {expected_y}, got {d_neg}"
    assert d_neg.subs(y, -2) == expected_neg2, f"At y = -2, expected {expected_neg2}, got {d_neg.subs(y, -2)}"

    # Check consistency with acosh(1/x) for other x < -1 values
    val_neg3 = d_sym.subs(x, -3)
    acosh_neg3 = diff(acosh(1/x), x).subs(x, -3)
    assert val_neg3 == acosh_neg3, f"At x = -3, expected {acosh_neg3}, got {val_neg3}"

    # Retain correctness for 0 < x < 1
    val_half = d_sym.subs(x, S(1)/2)
    expected_half = -4*sqrt(3)/3
    assert val_half == expected_half, f"At x = 1/2, expected {expected_half}, got {val_half}"

    val_third = d_sym.subs(x, S(1)/3)
    expected_third = -9*sqrt(2)/4
    assert val_third == expected_third, f"At x = 1/3, expected {expected_third}, got {val_third}"

    # Direct fdiff check on asech
    assert asech(x).fdiff(1) == expected_sym, f"fdiff mismatch: {asech(x).fdiff(1)}"


if __name__ == '__main__':
    try:
        test_asech_derivative()
        print("All tests passed.")
        sys.exit(0)
    except AssertionError as e:
        print(f"Test failed: {e}", file=sys.stderr)
        sys.exit(1)
