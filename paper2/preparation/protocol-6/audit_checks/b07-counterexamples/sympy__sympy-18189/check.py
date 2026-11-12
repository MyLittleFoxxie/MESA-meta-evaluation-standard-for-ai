"""
Verification check for sympy__sympy-18189.
Issue: diophantine: incomplete results depending on syms order with permute=True.
"""

import sys
from sympy import symbols
from sympy.solvers.diophantine import diophantine


def test_diophantine_permute_syms_order():
    expected = {
        (-3, -2), (-3, 2), (-2, -3), (-2, 3),
        (2, -3), (2, 3), (3, -2), (3, 2)
    }

    # Test with issue's symbols (m, n)
    m, n = symbols("m n")
    eq_mn = n**4 + m**4 - 2**4 - 3**4

    sol_mn = diophantine(eq_mn, syms=(m, n), permute=True)
    assert sol_mn == expected, f"Expected {expected}, got {sol_mn} for syms=(m, n)"

    sol_nm = diophantine(eq_mn, syms=(n, m), permute=True)
    assert sol_nm == expected, f"Expected {expected}, got {sol_nm} for syms=(n, m)"

    # Test with alternative variable names (a, b)
    a, b = symbols("a b")
    eq_ab = a**4 + b**4 - 2**4 - 3**4

    sol_ab = diophantine(eq_ab, syms=(a, b), permute=True)
    assert sol_ab == expected, f"Expected {expected}, got {sol_ab} for syms=(a, b)"

    sol_ba = diophantine(eq_ab, syms=(b, a), permute=True)
    assert sol_ba == expected, f"Expected {expected}, got {sol_ba} for syms=(b, a)"

    # Test with alternative variable names (x, y)
    x, y = symbols("x y")
    eq_xy = x**4 + y**4 - 2**4 - 3**4

    sol_xy = diophantine(eq_xy, syms=(x, y), permute=True)
    assert sol_xy == expected, f"Expected {expected}, got {sol_xy} for syms=(x, y)"

    sol_yx = diophantine(eq_xy, syms=(y, x), permute=True)
    assert sol_yx == expected, f"Expected {expected}, got {sol_yx} for syms=(y, x)"


if __name__ == "__main__":
    try:
        test_diophantine_permute_syms_order()
        print("All diophantine permute syms order tests passed successfully.")
        sys.exit(0)
    except AssertionError as e:
        print(f"Assertion failed: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)
