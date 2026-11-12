#!/usr/bin/env python3
"""
Verification check script for sympy__sympy-23413.

Issue:
Bug with HNF removing rows.
np.flip(hermite_normal_form(Matrix(np.flip(np.array([[5, 8, 12], [0, 0, 1]]))).T).T)
should give [[5, 8, 0], [0, 0, 1]], but instead gives [[5, 8, 0]].
HNF falsely identified the matrix as rank-deficient and removed a row when
attempting to achieve row-style HNF using flips and transposes.
"""

import sys
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form


def flip_matrix(mat):
    """Flip a 2D Matrix along both row and column axes (equivalent to np.flip)."""
    rows, cols = mat.shape
    return Matrix(rows, cols, lambda i, j: mat[rows - 1 - i, cols - 1 - j])


def test_hnf_row_style_flip():
    # Original matrix from the issue
    orig = Matrix([[5, 8, 12], [0, 0, 1]])

    # Row-style HNF calculation using flips and transposes
    # Expected: [[5, 8, 0], [0, 0, 1]]
    flipped_orig = flip_matrix(orig)
    assert flipped_orig == Matrix([[1, 0, 0], [12, 8, 5]])

    transposed = flipped_orig.T
    assert transposed == Matrix([[1, 12], [0, 8], [0, 5]])
    assert transposed.shape == (3, 2)

    # In unpatched sympy, _hermite_normal_form only inspected min(m, n) = 2 rows
    # from the bottom, missing row 0 and falsely dropping a column (returning shape 3x1).
    hnf_intermediate = hermite_normal_form(transposed)
    assert hnf_intermediate.shape == (3, 2), (
        f"Expected intermediate HNF shape (3, 2), but got {hnf_intermediate.shape}."
    )
    assert hnf_intermediate == Matrix([[1, 0], [0, 8], [0, 5]]), (
        f"Expected intermediate HNF [[1, 0], [0, 8], [0, 5]], but got {hnf_intermediate}."
    )

    # Complete the flip/transpose row-style HNF calculation
    result = flip_matrix(hnf_intermediate.T)

    # Behavior requested:
    # 1. Preserve both independent rows instead of falsely treating the matrix as rank deficient and dropping one.
    assert result.shape == (2, 3), (
        f"Expected result shape (2, 3) preserving both rows, but got shape {result.shape}."
    )
    assert result.rows == 2, (
        f"Expected 2 rows preserved, but got {result.rows}."
    )

    # 2. The flip/transpose row-style HNF calculation for [[5, 8, 12], [0, 0, 1]] must return [[5, 8, 0], [0, 0, 1]].
    expected = Matrix([[5, 8, 0], [0, 0, 1]])
    assert result == expected, (
        f"Expected {expected}, but got {result}."
    )


def test_hnf_m_greater_than_n():
    # Additional test for m > n with zero rows at the bottom
    # Verifies that pivots in upper rows are not skipped
    m = Matrix([[1, 0], [0, 1], [0, 0]])
    hnf = hermite_normal_form(m)
    assert hnf.shape == (3, 2), (
        f"Expected shape (3, 2), but got {hnf.shape}."
    )
    assert hnf == Matrix([[1, 0], [0, 1], [0, 0]]), (
        f"Expected [[1, 0], [0, 1], [0, 0]], but got {hnf}."
    )


def test_with_numpy_if_available():
    try:
        import numpy as np
    except ImportError:
        return

    orig_arr = np.array([[5, 8, 12], [0, 0, 1]])
    res = np.flip(hermite_normal_form(Matrix(np.flip(orig_arr)).T).T)

    assert res.shape == (2, 3), (
        f"numpy: Expected shape (2, 3), got {res.shape}."
    )
    assert Matrix(res.tolist()) == Matrix([[5, 8, 0], [0, 0, 1]]), (
        f"numpy: Expected [[5, 8, 0], [0, 0, 1]], got {res.tolist()}."
    )


def main():
    test_hnf_row_style_flip()
    test_hnf_m_greater_than_n()
    test_with_numpy_if_available()
    print("All HNF verification tests passed successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
