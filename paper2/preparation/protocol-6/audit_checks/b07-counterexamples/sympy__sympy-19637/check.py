import sys
from sympy.core.sympify import kernS
from sympy import Symbol


def main():
    x = Symbol('x')
    expected = 2 * x / (x - 1)

    # Behavior 1: kernS should parse parenthesized fraction `(2*x)/(x-1)` as `2*x/(x-1)`
    # without raising UnboundLocalError: local variable 'kern' referenced before assignment.
    expr = kernS("(2*x)/(x-1)")
    assert expr == expected, f"Expected {expected}, got {expr}"

    # Behavior 2: Spaces in the same expression should not cause the reported error.
    space_variants = [
        "(2 * x) / (x - 1)",
        " (2*x) / (x - 1) ",
        "(2*x) / (x-1)",
        "(2*x)/(x - 1)",
    ]
    for text in space_variants:
        expr_spaced = kernS(text)
        assert expr_spaced == expected, f"Expected {expected} for {text!r}, got {expr_spaced}"

    print("All checks passed successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
