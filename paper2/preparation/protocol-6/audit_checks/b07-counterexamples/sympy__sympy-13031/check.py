#!/usr/bin/env python3
import sys


def test_sparse_matrix_hstack_zero_rows():
    from sympy.matrices import SparseMatrix

    # Horizontal stacking must preserve and add the column counts of matrices with zero rows;
    # widths 0, 1, 2, and 3 must produce shape (0, 6).
    m1 = SparseMatrix.zeros(0, 0)
    m2 = SparseMatrix.zeros(0, 1)
    m3 = SparseMatrix.zeros(0, 2)
    m4 = SparseMatrix.zeros(0, 3)

    h_stacked = SparseMatrix.hstack(m1, m2, m3, m4)
    assert h_stacked.shape == (0, 6), f"Expected shape (0, 6), got {h_stacked.shape}"

    joined = m1.row_join(m2).row_join(m3).row_join(m4)
    assert joined.shape == (0, 6), f"Expected shape (0, 6), got {joined.shape}"


def test_sparse_matrix_hstack_one_row():
    from sympy.matrices import SparseMatrix

    # Horizontal stacking of one-row matrices with widths 0, 1, 2, and 3 must continue to produce shape (1, 6).
    m1 = SparseMatrix.zeros(1, 0)
    m2 = SparseMatrix.zeros(1, 1)
    m3 = SparseMatrix.zeros(1, 2)
    m4 = SparseMatrix.zeros(1, 3)

    h_stacked = SparseMatrix.hstack(m1, m2, m3, m4)
    assert h_stacked.shape == (1, 6), f"Expected shape (1, 6), got {h_stacked.shape}"

    joined = m1.row_join(m2).row_join(m3).row_join(m4)
    assert joined.shape == (1, 6), f"Expected shape (1, 6), got {joined.shape}"


def test_sparse_matrix_vstack_zero_cols():
    from sympy.matrices import SparseMatrix

    # Vertical stacking should preserve and add row counts for matrices with zero columns,
    # the corresponding vstack behavior named in the issue.
    m1 = SparseMatrix.zeros(0, 0)
    m2 = SparseMatrix.zeros(1, 0)
    m3 = SparseMatrix.zeros(2, 0)
    m4 = SparseMatrix.zeros(3, 0)

    v_stacked = SparseMatrix.vstack(m1, m2, m3, m4)
    assert v_stacked.shape == (6, 0), f"Expected shape (6, 0), got {v_stacked.shape}"

    joined = m1.col_join(m2).col_join(m3).col_join(m4)
    assert joined.shape == (6, 0), f"Expected shape (6, 0), got {joined.shape}"


def test_sparse_matrix_vstack_one_col():
    from sympy.matrices import SparseMatrix

    # Vertical stacking of one-column matrices with heights 0, 1, 2, and 3 must produce shape (6, 1).
    m1 = SparseMatrix.zeros(0, 1)
    m2 = SparseMatrix.zeros(1, 1)
    m3 = SparseMatrix.zeros(2, 1)
    m4 = SparseMatrix.zeros(3, 1)

    v_stacked = SparseMatrix.vstack(m1, m2, m3, m4)
    assert v_stacked.shape == (6, 1), f"Expected shape (6, 1), got {v_stacked.shape}"

    joined = m1.col_join(m2).col_join(m3).col_join(m4)
    assert joined.shape == (6, 1), f"Expected shape (6, 1), got {joined.shape}"


def test_dense_matrix_behaviors():
    from sympy.matrices import Matrix

    # Verify dense Matrix exhibits the same consistent behaviors
    m1 = Matrix.zeros(0, 0)
    m2 = Matrix.zeros(0, 1)
    m3 = Matrix.zeros(0, 2)
    m4 = Matrix.zeros(0, 3)
    assert Matrix.hstack(m1, m2, m3, m4).shape == (0, 6)

    m1_r = Matrix.zeros(1, 0)
    m2_r = Matrix.zeros(1, 1)
    m3_r = Matrix.zeros(1, 2)
    m4_r = Matrix.zeros(1, 3)
    assert Matrix.hstack(m1_r, m2_r, m3_r, m4_r).shape == (1, 6)

    m1_c = Matrix.zeros(0, 0)
    m2_c = Matrix.zeros(1, 0)
    m3_c = Matrix.zeros(2, 0)
    m4_c = Matrix.zeros(3, 0)
    assert Matrix.vstack(m1_c, m2_c, m3_c, m4_c).shape == (6, 0)


def main():
    test_sparse_matrix_hstack_zero_rows()
    test_sparse_matrix_hstack_one_row()
    test_sparse_matrix_vstack_zero_cols()
    test_sparse_matrix_vstack_one_col()
    test_dense_matrix_behaviors()
    print("All Matrix hstack and vstack shape tests passed successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
