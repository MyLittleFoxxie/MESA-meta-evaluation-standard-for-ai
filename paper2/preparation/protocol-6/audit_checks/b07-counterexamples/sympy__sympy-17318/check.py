"""
Verification test for sympy/sympy issue #17318.
sqrtdenest raises IndexError when processing complex radicals
such as (3 - sqrt(2)*sqrt(4 + 3*I) + 3*I)/2.
When an expression cannot be denested, it should be returned unchanged.
"""
import sys
from sympy import sqrt, I, S, expand_mul
from sympy.simplify.sqrtdenest import sqrtdenest, _sqrt_match


def test_complex_radical_no_index_error():
    # Issue #17318 / #12420: sqrtdenest((3 - sqrt(2)*sqrt(4 + 3*I) + 3*I)/2) raised IndexError
    expr = (3 - sqrt(2)*sqrt(4 + 3*I) + 3*I) / 2
    res = sqrtdenest(expr)
    expected = S(3)/2 - sqrt(2)*sqrt(4 + 3*I)/2 + 3*I/2

    assert res == expected, f"Expected {expected}, got {res}"
    assert (res - expr).expand() == 0, f"Result {res} does not equal original expr {expr}"


def test_complex_expressions_returned_unchanged():
    # When complex expressions cannot be denested, they should be returned unchanged
    cases = [
        sqrt(4 + 3*I),
        sqrt(1 + I),
        sqrt(2 + 2*I),
        1 - sqrt(2)*sqrt(1 + I) + I,
    ]
    for expr in cases:
        res = sqrtdenest(expr)
        expected = expand_mul(expr)
        assert res == expected, f"Expected {expected}, got {res}"


def test_sqrt_match_complex():
    # _sqrt_match should not call split_surds when terms have negative squares
    # (avoid IndexError: tuple index out of range in _split_gcd)
    assert _sqrt_match(4 + 3*I) == [], f"Expected [], got {_sqrt_match(4 + 3*I)}"
    assert _sqrt_match(1 + I) == [], f"Expected [], got {_sqrt_match(1 + I)}"
    assert _sqrt_match(3 + 3*I) == [], f"Expected [], got {_sqrt_match(3 + 3*I)}"


def test_standard_denesting_preserved():
    # Ensure standard denesting for positive real surds continues to work
    assert sqrtdenest(sqrt(5 + 2*sqrt(6))) == sqrt(2) + sqrt(3)
    assert sqrtdenest(sqrt(3 + 2*sqrt(2))) == 1 + sqrt(2)


def main():
    test_complex_radical_no_index_error()
    test_complex_expressions_returned_unchanged()
    test_sqrt_match_complex()
    test_standard_denesting_preserved()
    print("All tests passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
