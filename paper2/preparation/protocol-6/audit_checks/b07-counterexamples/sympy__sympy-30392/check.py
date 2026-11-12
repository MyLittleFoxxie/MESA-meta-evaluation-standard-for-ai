"""
Independent verification test for sympy__sympy-30392.

Behaviors verified:
1. Extract scalar coefficients from MatrixExpr arguments during ArrayTensorProduct canonicalization
   (e.g., ArrayTensorProduct(2*M, N) -> ArrayTensorProduct(2, M, N)).
2. Combine extracted coefficients into a single leading scalar factor while preserving array shape
   and matrix factor order.
3. Convert the resulting array expressions back to correct matrix expressions, including
   contractions, axis permutations with rank-0 coefficients, and ArraySum.
"""

import sys
from sympy import symbols, S
from sympy.matrices.expressions import MatrixSymbol, MatrixExpr
from sympy.tensor.array.expressions.array_expressions import (
    ArrayTensorProduct,
    ArrayContraction,
    PermuteDims,
    ArraySum,
)
from sympy.tensor.array.expressions.from_array_to_matrix import (
    convert_array_to_matrix,
)


def test_array_tensor_product_canonicalization():
    k = symbols('k')
    x, y = symbols('x y')
    M = MatrixSymbol('M', k, k)
    N = MatrixSymbol('N', k, k)
    P = MatrixSymbol('P', k, k)

    # 1. Single matrix argument with scalar coefficient
    tp_single = ArrayTensorProduct(2 * M)
    assert tp_single.args == (2, M), f"Expected args (2, M), got {tp_single.args}"
    assert tp_single.shape == (k, k), f"Expected shape (k, k), got {tp_single.shape}"

    # 2. Two matrix arguments with scalar coefficient on the first
    tp1 = ArrayTensorProduct(2 * M, N)
    assert tp1.args == (2, M, N), f"Expected args (2, M, N), got {tp1.args}"
    assert tp1.shape == (k, k, k, k), f"Expected shape (k, k, k, k), got {tp1.shape}"

    # 3. Two matrix arguments with scalar coefficients on both, combined into leading scalar
    tp2 = ArrayTensorProduct(2 * M, 3 * N)
    assert tp2.args == (6, M, N), f"Expected args (6, M, N), got {tp2.args}"
    assert tp2.shape == (k, k, k, k), f"Expected shape (k, k, k, k), got {tp2.shape}"

    # 4. Multiple matrix arguments preserving matrix factor order
    tp3 = ArrayTensorProduct(2 * M, P, -3 * N)
    assert tp3.args == (-6, M, P, N), f"Expected args (-6, M, P, N), got {tp3.args}"
    assert tp3.shape == (k, k, k, k, k, k), f"Expected shape (k, k, k, k, k, k), got {tp3.shape}"

    # 5. Symbolic scalar coefficients
    tp_sym = ArrayTensorProduct(x * M, y * N)
    assert tp_sym.args == (x * y, M, N), f"Expected args (x*y, M, N), got {tp_sym.args}"
    assert tp_sym.shape == (k, k, k, k), f"Expected shape (k, k, k, k), got {tp_sym.shape}"


def test_convert_array_to_matrix_basic():
    k = symbols('k')
    x = symbols('x')
    M = MatrixSymbol('M', k, k)

    # Single matrix expression with extracted scalar factor
    res1 = convert_array_to_matrix(ArrayTensorProduct(2 * M))
    assert res1 == 2 * M, f"Expected 2*M, got {res1}"
    assert isinstance(res1, MatrixExpr), f"Expected MatrixExpr, got {type(res1)}"

    res2 = convert_array_to_matrix(ArrayTensorProduct(x * M))
    assert res2 == x * M, f"Expected x*M, got {res2}"
    assert isinstance(res2, MatrixExpr), f"Expected MatrixExpr, got {type(res2)}"


def test_convert_array_to_matrix_contractions():
    k = symbols('k')
    x, y = symbols('x y')
    M = MatrixSymbol('M', k, k)
    N = MatrixSymbol('N', k, k)
    P = MatrixSymbol('P', k, k)

    # Contraction of 2 matrices with scalar coefficient
    c1 = ArrayContraction(ArrayTensorProduct(2 * M, N), (1, 2))
    res_c1 = convert_array_to_matrix(c1)
    assert res_c1 == 2 * M * N, f"Expected 2*M*N, got {res_c1}"

    c2 = ArrayContraction(ArrayTensorProduct(2 * M, 3 * N), (1, 2))
    res_c2 = convert_array_to_matrix(c2)
    assert res_c2 == 6 * M * N, f"Expected 6*M*N, got {res_c2}"

    c3 = ArrayContraction(ArrayTensorProduct(x * M, y * N), (1, 2))
    res_c3 = convert_array_to_matrix(c3)
    assert res_c3 == x * y * M * N, f"Expected x*y*M*N, got {res_c3}"

    # Contraction of 3 matrices
    c_3m = ArrayContraction(ArrayTensorProduct(2 * M, -3 * N, P), (1, 2), (3, 4))
    res_c3m = convert_array_to_matrix(c_3m)
    assert res_c3m == -6 * M * N * P, f"Expected -6*M*N*P, got {res_c3m}"


def test_convert_array_to_matrix_permutations():
    k = symbols('k')
    M = MatrixSymbol('M', k, k)
    N = MatrixSymbol('N', k, k)
    P = MatrixSymbol('P', k, k)
    D = MatrixSymbol('D', k, k)

    # PermuteDims on contraction of 4 matrices with a leading rank-0 scalar factor
    # Contraction (1, 2) merges M and N -> M*N
    # Contraction (5, 6) merges P and D -> P*D
    contr_4m = ArrayContraction(ArrayTensorProduct(2 * M, N, P, D), (1, 2), (5, 6))

    # Transposing first matrix factor (M*N).T = N.T * M.T
    perm1 = PermuteDims(contr_4m, [1, 0, 2, 3])
    res_p1 = convert_array_to_matrix(perm1)
    assert isinstance(res_p1, ArrayTensorProduct), f"Expected ArrayTensorProduct, got {type(res_p1)}"
    assert res_p1.args == (2, N.T * M.T, P * D), f"Expected args (2, N.T*M.T, P*D), got {res_p1.args}"
    assert res_p1.shape == (k, k, k, k), f"Expected shape (k, k, k, k), got {res_p1.shape}"

    # Transposing both matrix factors: (M*N).T and (P*D).T
    perm2 = PermuteDims(contr_4m, [1, 0, 3, 2])
    res_p2 = convert_array_to_matrix(perm2)
    assert isinstance(res_p2, ArrayTensorProduct), f"Expected ArrayTensorProduct, got {type(res_p2)}"
    assert res_p2.args == (2, N.T * M.T, D.T * P.T), f"Expected args (2, N.T*M.T, D.T*P.T), got {res_p2.args}"
    assert res_p2.shape == (k, k, k, k), f"Expected shape (k, k, k, k), got {res_p2.shape}"


def test_convert_array_to_matrix_arraysum():
    k = symbols('k')
    i = symbols('i')
    M = MatrixSymbol('M', k, k)

    s = ArraySum(ArrayTensorProduct(2 * M), (i, 1, 3))
    res_s = convert_array_to_matrix(s)
    assert res_s == 6 * M, f"Expected 6*M, got {res_s}"


def main():
    test_array_tensor_product_canonicalization()
    test_convert_array_to_matrix_basic()
    test_convert_array_to_matrix_contractions()
    test_convert_array_to_matrix_permutations()
    test_convert_array_to_matrix_arraysum()
    print("All checks passed successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
