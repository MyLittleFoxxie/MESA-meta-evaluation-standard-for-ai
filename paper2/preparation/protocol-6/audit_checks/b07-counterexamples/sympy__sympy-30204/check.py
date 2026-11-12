#!/usr/bin/env python3
import sys
import warnings

# Grounding: test imports from sympy and dependencies
from sympy.matrices.dense import Matrix
from sympy.matrices.sparse import MutableSparseMatrix, ImmutableSparseMatrix
from sympy.physics.quantum.matrixutils import (
    sympy_to_scipy_sparse,
    to_scipy_sparse,
    to_sympy,
    to_numpy,
    matrix_eye,
    matrix_zeros,
    matrix_tensor_product,
    scipy_sparse_matrix,
)
from sympy.physics.quantum.operator import Operator
from sympy.physics.quantum.represent import represent
from sympy.physics.quantum.commutator import Commutator
from sympy.physics.quantum.anticommutator import AntiCommutator
from sympy.physics.quantum.qubit import Qubit
from sympy.physics.quantum.identitysearch import is_scalar_sparse_matrix
from sympy.physics.quantum.gate import X
from sympy.printing.numpy import NumPyPrinter

try:
    import numpy as np
    import scipy.sparse as sparse
except ImportError as err:
    print(f"Skipping or failing due to missing numpy/scipy: {err}")
    sys.exit(1)


def test_converting_sympy_matrix_to_scipy_sparse():
    m = Matrix([[1, 2], [3, 4]])

    with warnings.catch_warnings(record=True) as recorded_warnings:
        warnings.simplefilter("always")
        s = sympy_to_scipy_sparse(m)
        for w in recorded_warnings:
            if issubclass(w.category, DeprecationWarning) and "csr_matrix" in str(w.message):
                raise AssertionError(f"Deprecation warning raised when converting sympy to scipy sparse: {w.message}")

    assert type(s) is sparse.csr_array, f"Expected csr_array from sympy_to_scipy_sparse, got {type(s)}"
    assert not isinstance(s, sparse.csr_matrix), "Result should not be an instance of deprecated csr_matrix"
    assert np.allclose(s.toarray(), np.array([[1, 2], [3, 4]], dtype=complex))

    s2 = to_scipy_sparse(m)
    assert type(s2) is sparse.csr_array, f"Expected csr_array from to_scipy_sparse(Matrix), got {type(s2)}"
    assert not isinstance(s2, sparse.csr_matrix)

    np_arr = np.array([[1, 2], [3, 4]], dtype=complex)
    s_from_np = to_scipy_sparse(np_arr)
    assert type(s_from_np) is sparse.csr_array, f"Expected csr_array from to_scipy_sparse(ndarray), got {type(s_from_np)}"
    assert not isinstance(s_from_np, sparse.csr_matrix)


def test_quantum_matrixutils_helpers():
    # matrix_eye
    eye_arr = matrix_eye(3, format='scipy.sparse')
    assert type(eye_arr) is sparse.csr_array, f"Expected csr_array from matrix_eye, got {type(eye_arr)}"
    assert not isinstance(eye_arr, sparse.csr_matrix)
    assert np.allclose(eye_arr.toarray(), np.eye(3, dtype=complex))

    # matrix_zeros
    z_csr = matrix_zeros(2, 3, format='scipy.sparse', spmatrix='csr')
    assert type(z_csr) is sparse.csr_array, f"Expected csr_array from matrix_zeros(csr), got {type(z_csr)}"
    assert not isinstance(z_csr, sparse.csr_matrix)
    assert z_csr.shape == (2, 3)

    z_lil = matrix_zeros(2, 3, format='scipy.sparse', spmatrix='lil')
    assert type(z_lil) is sparse.lil_array, f"Expected lil_array from matrix_zeros(lil), got {type(z_lil)}"
    assert z_lil.shape == (2, 3)

    # matrix_tensor_product
    m = Matrix([[1, 2], [3, 4]])
    tp = matrix_tensor_product(m, m, format='scipy.sparse')
    assert type(tp) is sparse.csr_array, f"Expected csr_array from matrix_tensor_product, got {type(tp)}"
    assert not isinstance(tp, sparse.csr_matrix)
    expected_tp = np.kron([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    assert np.allclose(tp.toarray(), expected_tp)

    # scipy_sparse_matrix type check and conversions
    test_csr = sparse.csr_array([[1, 2], [3, 4]])
    assert isinstance(test_csr, scipy_sparse_matrix), "csr_array must be recognized as an instance of scipy_sparse_matrix"
    assert to_scipy_sparse(test_csr) is test_csr
    assert to_sympy(test_csr) == m
    assert np.allclose(to_numpy(test_csr), np.array([[1, 2], [3, 4]]))


def test_qubit_represent():
    q = represent(Qubit('0'), format='scipy.sparse')
    assert type(q) is sparse.csr_array, f"Expected csr_array from represent(Qubit), got {type(q)}"
    assert not isinstance(q, sparse.csr_matrix)


def test_quantum_operations_matrix_behavior():
    class TestOpA(Operator):
        def _represent_default_basis(self, **options):
            return self._represent_A(None, **options)
        def _represent_A(self, basis, **options):
            return Matrix([[1, 2], [3, 4]])

    class TestOpB(Operator):
        def _represent_default_basis(self, **options):
            return self._represent_A(None, **options)
        def _represent_A(self, basis, **options):
            return Matrix([[5, 6], [7, 8]])

    A = TestOpA('A')
    B = TestOpB('B')

    # Multiplication must perform matrix multiplication (@), not elementwise (*)
    rep_AB = represent(A * B, basis=A, format='scipy.sparse')
    assert type(rep_AB) is sparse.csr_array, f"Expected csr_array, got {type(rep_AB)}"
    expected_AB = np.array([[19, 22], [43, 50]], dtype=complex)
    assert np.allclose(rep_AB.toarray(), expected_AB), f"Expected matrix product {expected_AB}, got {rep_AB.toarray()}"

    # Matrix power must perform matrix power, not elementwise power
    rep_A2 = represent(A ** 2, basis=A, format='scipy.sparse')
    assert type(rep_A2) is sparse.csr_array, f"Expected csr_array, got {type(rep_A2)}"
    expected_A2 = np.array([[7, 10], [15, 22]], dtype=complex)
    assert np.allclose(rep_A2.toarray(), expected_A2), f"Expected matrix power {expected_A2}, got {rep_A2.toarray()}"

    rep_A3 = represent(A ** 3, basis=A, format='scipy.sparse')
    assert type(rep_A3) is sparse.csr_array, f"Expected csr_array, got {type(rep_A3)}"
    expected_A3 = np.array([[37, 54], [81, 118]], dtype=complex)
    assert np.allclose(rep_A3.toarray(), expected_A3), f"Expected matrix power {expected_A3}, got {rep_A3.toarray()}"

    # Commutator and AntiCommutator
    rep_comm = represent(Commutator(A, B), basis=A, format='scipy.sparse')
    assert type(rep_comm) is sparse.csr_array, f"Expected csr_array, got {type(rep_comm)}"
    expected_comm = np.array([[19, 22], [43, 50]], dtype=complex) - np.array([[23, 34], [31, 46]], dtype=complex)
    assert np.allclose(rep_comm.toarray(), expected_comm)

    rep_acomm = represent(AntiCommutator(A, B), basis=A, format='scipy.sparse')
    assert type(rep_acomm) is sparse.csr_array, f"Expected csr_array, got {type(rep_acomm)}"
    expected_acomm = np.array([[19, 22], [43, 50]], dtype=complex) + np.array([[23, 34], [31, 46]], dtype=complex)
    assert np.allclose(rep_acomm.toarray(), expected_acomm)


def test_identitysearch_with_sparse_array():
    # is_scalar_sparse_matrix internally represents the circuit in scipy.sparse format
    # and calls matrix.toarray() instead of deprecated matrix.todense().getA()
    assert is_scalar_sparse_matrix([X(0), X(0)], 1, identity_only=True) is True
    assert is_scalar_sparse_matrix([X(0)], 1, identity_only=True) is False


def test_numpy_printer_sparse():
    code_mut = NumPyPrinter().doprint(MutableSparseMatrix([[1, 2], [0, 4]]))
    assert 'scipy.sparse.coo_array' in code_mut, f"Expected coo_array in printed code, got: {code_mut}"
    assert 'scipy.sparse.coo_matrix' not in code_mut, f"coo_matrix found in printed code: {code_mut}"

    code_immut = NumPyPrinter().doprint(ImmutableSparseMatrix([[1, 2], [0, 4]]))
    assert 'scipy.sparse.coo_array' in code_immut, f"Expected coo_array in printed code, got: {code_immut}"
    assert 'scipy.sparse.coo_matrix' not in code_immut, f"coo_matrix found in printed code: {code_immut}"


def main():
    test_converting_sympy_matrix_to_scipy_sparse()
    test_quantum_matrixutils_helpers()
    test_qubit_represent()
    test_quantum_operations_matrix_behavior()
    test_identitysearch_with_sparse_array()
    test_numpy_printer_sparse()
    print("All tests passed successfully.")
    sys.exit(0)


if __name__ == '__main__':
    main()
