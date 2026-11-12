#!/usr/bin/env python3
"""
Verification check script for sympy__sympy-30344:
Ensure default_sort_key and printers handle nan safely without
raising TypeError: Invalid NaN comparison.
"""
import sys
from sympy import Function, Symbol, Piecewise, S, Rational, Float, nan
from sympy.core.sorting import default_sort_key, ordered
from sympy.printing.str import sstr
from sympy.printing.latex import latex
from sympy.printing.pretty import pretty


def test_nan_sort_key():
    key = nan.sort_key()
    expected = (nan.class_key(), (0, ()), (), S.NegativeInfinity)
    assert key == expected, f"Expected {expected}, got {key}"


def test_ordered_nan_and_numbers():
    # Sorting keys must support nan alongside numbers
    result1 = list(ordered([nan, S.One]))
    assert result1 == [nan, S.One], f"Unexpected ordering: {result1}"

    result2 = list(ordered([S.One, nan]))
    assert result2 == [nan, S.One], f"Unexpected ordering: {result2}"

    # Also with raw int/float/rationals/infinities
    nums = [S.NegativeInfinity, S.NegativeOne, S.Zero, Rational(1, 2), S.One, Float(2.5), S.Infinity, nan]
    sorted_nums = list(ordered(nums))
    assert len(sorted_nums) == len(nums), "Length mismatch when ordering numbers with nan"
    assert nan in sorted_nums, "nan missing from sorted numbers"


def test_printing_function_with_nan():
    # Printing sums such as f(nan) + f(1) must not raise TypeError("Invalid NaN comparison")
    f = Function('f')
    expr = f(nan) + f(1)

    s = str(expr)
    assert "f(nan)" in s and "f(1)" in s, f"Unexpected str output: {s}"

    ss = sstr(expr)
    assert "f(nan)" in ss and "f(1)" in ss, f"Unexpected sstr output: {ss}"

    p = pretty(expr)
    assert "f" in p, f"Unexpected pretty output: {p}"

    ltx = latex(expr)
    assert "f" in ltx, f"Unexpected latex output: {ltx}"


def test_same_class_subexpressions():
    # Sorting and printing must work when nan occurs inside same-class subexpressions
    f = Function('f')
    fn_sorted = list(ordered([f(nan), f(1)]))
    assert fn_sorted == [f(nan), f(1)], f"Unexpected function ordering: {fn_sorted}"

    fn_sorted_rev = list(ordered([f(1), f(nan)]))
    assert fn_sorted_rev == [f(nan), f(1)], f"Unexpected function ordering: {fn_sorted_rev}"

    # Piecewise expressions
    x = Symbol('x')
    p1 = Piecewise((nan, x > 0), (0, True))
    p2 = Piecewise((1, x > 0), (0, True))

    pw_sorted = list(ordered([p1, p2]))
    assert len(pw_sorted) == 2, f"Unexpected Piecewise ordering length: {len(pw_sorted)}"

    pw_sum = p1 + p2
    s_pw = str(pw_sum)
    assert len(s_pw) > 0, "Piecewise sum str was empty"


def main():
    try:
        test_nan_sort_key()
        test_ordered_nan_and_numbers()
        test_printing_function_with_nan()
        test_same_class_subexpressions()
        print("All tests passed successfully.")
        sys.exit(0)
    except Exception as e:
        print(f"Test failed: {type(e).__name__}: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
