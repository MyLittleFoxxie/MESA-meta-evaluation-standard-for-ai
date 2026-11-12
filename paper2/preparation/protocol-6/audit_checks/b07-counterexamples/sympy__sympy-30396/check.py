"""
Verification test script for sympy__sympy-30396.
Tests JaxPrinter/NumPyPrinter scalar assignment printing and ArrayElementwiseApplyFunc handling.
"""

import sys
from sympy import symbols, sqrt, sin, Lambda, Sum, MatrixSymbol
from sympy.codegen.ast import Assignment
from sympy.printing.numpy import NumPyPrinter, JaxPrinter
from sympy.tensor.indexed import IndexedBase
from sympy.tensor.array.expressions.array_expressions import (
    ArraySymbol,
    ArrayAdd,
    ArrayElementwiseApplyFunc,
    ArrayContraction,
    ArrayTensorProduct,
)
from sympy.tensor.array.expressions.from_indexed_to_array import convert_indexed_to_array


def test_pure_scalar_assignment_printing():
    x, y, z = symbols('x y z')
    out = symbols('out')
    np_p = NumPyPrinter()
    jp = JaxPrinter()

    # 1. Pure scalar Add preserves normal infix syntax in assignments (doprint and Assignment)
    assert np_p.doprint(x + y + z, 'out') == 'out = x + y + z'
    assert jp.doprint(x + y + z, 'out') == 'out = x + y + z'
    assert np_p.doprint(Assignment(out, x + y + z)) == 'out = x + y + z'
    assert jp.doprint(Assignment(out, x + y + z)) == 'out = x + y + z'

    # Infix Add and Mul combined
    assert np_p.doprint(x + y * z, 'out') == 'out = x + y*z'
    assert jp.doprint(x + y * z, 'out') == 'out = x + y*z'
    assert np_p.doprint(Assignment(out, x + y * z)) == 'out = x + y*z'
    assert jp.doprint(Assignment(out, x + y * z)) == 'out = x + y*z'

    # 2. Scalar expressions with powers, roots, and functions print consistently with and without assign_to
    expr = x**2 + sqrt(y) - sin(x * z)

    np_expected = 'x**2 + numpy.sqrt(y) - numpy.sin(x*z)'
    jp_expected = 'x**2 + jax.numpy.sqrt(y) - jax.numpy.sin(x*z)'

    assert np_p.doprint(expr) == np_expected
    assert jp.doprint(expr) == jp_expected

    assert np_p.doprint(expr, 'out') == f'out = {np_expected}'
    assert jp.doprint(expr, 'out') == f'out = {jp_expected}'

    assert np_p.doprint(Assignment(out, expr)) == f'out = {np_expected}'
    assert jp.doprint(Assignment(out, expr)) == f'out = {jp_expected}'


def test_genuine_array_operations_preserved():
    # Genuine indexed expressions retain array conversion and array operations
    A_idx = IndexedBase('A')
    B_idx = IndexedBase('B')
    C_idx = IndexedBase('C')
    i = symbols('i')
    np_p = NumPyPrinter()
    jp = JaxPrinter()

    assert np_p.doprint(A_idx[i] + B_idx[i], C_idx[i]) == 'C = numpy.add(A, B)'
    assert jp.doprint(A_idx[i] + B_idx[i], C_idx[i]) == 'C = jax.numpy.add(A, B)'
    assert np_p.doprint(Assignment(C_idx[i], A_idx[i] + B_idx[i])) == 'C = numpy.add(A, B)'
    assert jp.doprint(Assignment(C_idx[i], A_idx[i] + B_idx[i])) == 'C = jax.numpy.add(A, B)'

    # Explicit ArrayAdd node preserves array addition syntax
    A_arr = ArraySymbol('A', (3, 3))
    B_arr = ArraySymbol('B', (3, 3))
    C_arr = ArraySymbol('C', (3, 3))
    assert np_p.doprint(ArrayAdd(A_arr, B_arr), C_arr) == 'C = numpy.add(A, B)'
    assert jp.doprint(ArrayAdd(A_arr, B_arr), C_arr) == 'C = jax.numpy.add(A, B)'


def test_array_elementwise_apply_func():
    A_arr = ArraySymbol('A', (3, 3))
    C_arr = ArraySymbol('C', (3, 3))
    d, k = symbols('d k')
    np_p = NumPyPrinter()
    jp = JaxPrinter()

    # 1. Standard unary function applied elementwise
    elem_sin = ArrayElementwiseApplyFunc(sin, A_arr)
    assert np_p.doprint(elem_sin) == 'numpy.sin(A)'
    assert jp.doprint(elem_sin) == 'jax.numpy.sin(A)'
    assert np_p.doprint(elem_sin, C_arr) == 'C = numpy.sin(A)'
    assert jp.doprint(elem_sin, C_arr) == 'C = jax.numpy.sin(A)'

    # 2. Lambda elementwise power
    elem_pow = ArrayElementwiseApplyFunc(Lambda(d, d**2), A_arr)
    assert np_p.doprint(elem_pow) == 'A**2'
    assert jp.doprint(elem_pow) == 'A**2'
    assert np_p.doprint(elem_pow, C_arr) == 'C = A**2'
    assert jp.doprint(elem_pow, C_arr) == 'C = A**2'

    # 3. Preserving function-body symbols
    elem_sym_mul = ArrayElementwiseApplyFunc(Lambda(d, k * d**2), A_arr)
    assert np_p.doprint(elem_sym_mul) == 'A**2*k'
    assert jp.doprint(elem_sym_mul) == 'A**2*k'

    elem_sym_add = ArrayElementwiseApplyFunc(Lambda(d, d + k), A_arr)
    assert np_p.doprint(elem_sym_add) == 'A + k'
    assert jp.doprint(elem_sym_add) == 'A + k'

    # 4. Preserving operand grouping (parenthesizing non-atomic operand)
    nested = ArrayElementwiseApplyFunc(
        Lambda(d, d**2),
        ArrayElementwiseApplyFunc(Lambda(d, d + 1), A_arr),
    )
    assert np_p.doprint(nested) == '(A + 1)**2'
    assert jp.doprint(nested) == '(A + 1)**2'

    # 5. Atomic operand requires no extra parentheses
    nested_atomic = ArrayElementwiseApplyFunc(
        Lambda(d, d**2),
        ArrayElementwiseApplyFunc(sin, A_arr),
    )
    assert np_p.doprint(nested_atomic) == 'numpy.sin(A)**2'
    assert jp.doprint(nested_atomic) == 'jax.numpy.sin(A)**2'


def test_rank_0_array_expression_power():
    # Rank-0 array contraction power converts to tensor product
    M = MatrixSymbol('M', 2, 2)
    idx_i = symbols('i')
    tr = Sum(M[idx_i, idx_i], (idx_i, 0, 1))
    res = convert_indexed_to_array(tr**2)
    assert isinstance(res, ArrayTensorProduct)
    assert res.args == (ArrayContraction(M, (0, 1)), ArrayContraction(M, (0, 1)))


def main():
    test_pure_scalar_assignment_printing()
    test_genuine_array_operations_preserved()
    test_array_elementwise_apply_func()
    test_rank_0_array_expression_power()
    print("All tests passed.")


if __name__ == '__main__':
    main()
