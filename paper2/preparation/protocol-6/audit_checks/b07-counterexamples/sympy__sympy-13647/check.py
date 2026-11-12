"""Verification test for sympy__sympy-13647.

Checks Matrix.col_insert() behavior when inserting columns into a Matrix.
"""
import sys
import sympy as sm


def test_col_insert_identity():
    # Issue reproduction:
    # Inserting a 6x2 matrix of twos at index 3 in a 6x6 identity matrix
    M = sm.eye(6)
    V = 2 * sm.ones(6, 2)
    res = M.col_insert(3, V)

    # 1. Output dimensions should be 6-by-8
    assert res.shape == (6, 8), f"Expected shape (6, 8), got {res.shape}"
    assert res.rows == 6 and res.cols == 8

    # Expected 6-by-8 matrix:
    # First 3 columns from original M (columns 0, 1, 2 of eye(6))
    # Columns 3 and 4 are all 2s
    # Columns 5, 6, 7 are columns 3, 4, 5 of eye(6)
    expected = sm.Matrix([
        [1, 0, 0, 2, 2, 0, 0, 0],
        [0, 1, 0, 2, 2, 0, 0, 0],
        [0, 0, 1, 2, 2, 0, 0, 0],
        [0, 0, 0, 2, 2, 1, 0, 0],
        [0, 0, 0, 2, 2, 0, 1, 0],
        [0, 0, 0, 2, 2, 0, 0, 1],
    ])

    # Check key elements specifically mentioned in issue:
    # In the buggy code, the right 3x3 identity block was shifted to the top 3 rows:
    # res[0, 5] was 1 instead of 0, res[3, 5] was 0 instead of 1.
    assert res[0, 5] == 0, f"Expected res[0, 5] == 0, got {res[0, 5]}"
    assert res[1, 6] == 0, f"Expected res[1, 6] == 0, got {res[1, 6]}"
    assert res[2, 7] == 0, f"Expected res[2, 7] == 0, got {res[2, 7]}"

    assert res[3, 5] == 1, f"Expected res[3, 5] == 1, got {res[3, 5]}"
    assert res[4, 6] == 1, f"Expected res[4, 6] == 1, got {res[4, 6]}"
    assert res[5, 7] == 1, f"Expected res[5, 7] == 1, got {res[5, 7]}"

    # Check column preservation and order
    assert res[:, :3] == M[:, :3], "Left columns before insertion point were corrupted"
    assert res[:, 3:5] == V, "Inserted columns do not match input"
    assert res[:, 5:] == M[:, 3:], "Right columns after insertion point were corrupted"

    # Full matrix equality
    assert res == expected, f"Result does not match expected matrix:\nResult:\n{res}\nExpected:\n{expected}"


def main():
    test_col_insert_identity()
    print("All checks passed successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
