#!/usr/bin/env python3
"""
Verification check for sympy__sympy-30952:
Division by zero error in reshape when an empty template is provided.
"""

import sys
from sympy.utilities.iterables import reshape


def test_empty_template_rejects_with_value_error():
    test_cases = [
        ((1,), ()),
        ([], ()),
        ([1, 2, 3], []),
        (tuple(range(4)), ()),
        ([1, 2], [[]]),
        ((1, 2), ((), ())),
    ]

    for seq, how in test_cases:
        try:
            reshape(seq, how=how)
        except ValueError:
            # Expected behavior: ValueError raised before division
            pass
        except ZeroDivisionError as e:
            raise AssertionError(
                f"reshape({seq!r}, how={how!r}) raised ZeroDivisionError instead of ValueError"
            ) from e
        except Exception as e:
            raise AssertionError(
                f"reshape({seq!r}, how={how!r}) raised unexpected exception {type(e).__name__}: {e}"
            ) from e
        else:
            raise AssertionError(
                f"reshape({seq!r}, how={how!r}) did not raise ValueError"
            )


def test_valid_reshape_works():
    seq = list(range(8))
    res = reshape(seq, [2, 2])
    expected = [[0, 1], [2, 3], [4, 5], [6, 7]]
    assert res == expected, f"Expected {expected}, got {res}"


def main():
    test_empty_template_rejects_with_value_error()
    test_valid_reshape_works()
    print("All checks passed successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
