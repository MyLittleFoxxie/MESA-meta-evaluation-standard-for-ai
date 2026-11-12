"""Verification script for sympy__sympy-30808.

Issue: wrong result / assumptions:
b = Symbol('b', finite=True, real=False); (b*I).is_real, (b*I).is_integer
Expected: None for both.
"""
import sys
from sympy import Symbol, I


def test_symbol_finite_not_real_mul_i():
    for name in ("b", "x", "symbol_test"):
        s = Symbol(name, finite=True, real=False)

        # Testing (s * I)
        prod1 = s * I
        assert prod1.is_real is None, (
            f"Expected ({name} * I).is_real to be None, got {prod1.is_real}"
        )
        assert prod1.is_integer is None, (
            f"Expected ({name} * I).is_integer to be None, got {prod1.is_integer}"
        )

        # Testing (I * s)
        prod2 = I * s
        assert prod2.is_real is None, (
            f"Expected (I * {name}).is_real to be None, got {prod2.is_real}"
        )
        assert prod2.is_integer is None, (
            f"Expected (I * {name}).is_integer to be None, got {prod2.is_integer}"
        )


def main():
    test_symbol_finite_not_real_mul_i()
    print("All checks passed successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
