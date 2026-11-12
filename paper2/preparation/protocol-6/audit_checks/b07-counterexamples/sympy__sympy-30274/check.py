#!/usr/bin/env python3
"""
Verification script for sympy__sympy-30274:
Latex and pretty printing for ArrayTensorProduct and ArrayAdd.
"""

import sys
from sympy import MatrixSymbol, symbols, latex, pretty, sstr
from sympy.tensor.array.expressions import (
    ArrayTensorProduct,
    ArrayAdd,
    PermuteDims,
    ArrayContraction,
)


def test_latex_array_tensor_product():
    A = MatrixSymbol('A', 3, 4)
    B = MatrixSymbol('B', 4, 5)
    C = MatrixSymbol('C', 5, 6)

    # Two operands
    tp2 = ArrayTensorProduct(A, B)
    l_tp2 = latex(tp2)
    assert l_tp2 == r"A \boxtimes B", f"Expected 'A \\boxtimes B', got: {l_tp2!r}"
    assert r"\operatorname{ArrayTensorProduct}" not in l_tp2

    # More than two operands and preservation of order
    tp3_abc = ArrayTensorProduct(A, B, C)
    l_tp3_abc = latex(tp3_abc)
    assert l_tp3_abc == r"A \boxtimes B \boxtimes C", (
        f"Expected 'A \\boxtimes B \\boxtimes C', got: {l_tp3_abc!r}"
    )

    tp3_cba = ArrayTensorProduct(C, B, A)
    l_tp3_cba = latex(tp3_cba)
    assert l_tp3_cba == r"C \boxtimes B \boxtimes A", (
        f"Expected 'C \\boxtimes B \\boxtimes A', got: {l_tp3_cba!r}"
    )


def test_latex_parenthesize_sums():
    A = MatrixSymbol('A', 3, 4)
    B = MatrixSymbol('B', 3, 4)
    C = MatrixSymbol('C', 4, 5)
    x, y = symbols('x y')

    # ArrayAdd as first operand
    tp_add_first = ArrayTensorProduct(ArrayAdd(A, B), C)
    l_first = latex(tp_add_first)
    assert l_first == r"\left(A + B\right) \boxtimes C", (
        f"Expected r'\\left(A + B\\right) \\boxtimes C', got: {l_first!r}"
    )

    # ArrayAdd as second operand
    tp_add_second = ArrayTensorProduct(C, ArrayAdd(A, B))
    l_second = latex(tp_add_second)
    assert l_second == r"C \boxtimes \left(A + B\right)", (
        f"Expected r'C \\boxtimes \\left(A + B\\right)', got: {l_second!r}"
    )

    # ArrayAdd for both operands
    D = MatrixSymbol('D', 4, 5)
    E = MatrixSymbol('E', 4, 5)
    tp_add_both = ArrayTensorProduct(ArrayAdd(A, B), ArrayAdd(D, E))
    l_both = latex(tp_add_both)
    assert l_both == r"\left(A + B\right) \boxtimes \left(D + E\right)", (
        f"Expected r'\\left(A + B\\right) \\boxtimes \\left(D + E\\right)', got: {l_both!r}"
    )

    # Core Add inside ArrayTensorProduct
    tp_core_add = ArrayTensorProduct(x + y, C)
    l_core_add = latex(tp_core_add)
    assert l_core_add == r"\left(x + y\right) \boxtimes C", (
        f"Expected r'\\left(x + y\\right) \\boxtimes C', got: {l_core_add!r}"
    )


def test_latex_array_add():
    A = MatrixSymbol('A', 3, 4)
    B = MatrixSymbol('B', 3, 4)
    C = MatrixSymbol('C', 3, 4)

    # Ordinary sum
    add2 = ArrayAdd(A, B)
    l_add2 = latex(add2)
    assert l_add2 == "A + B", f"Expected 'A + B', got: {l_add2!r}"
    assert r"\operatorname{ArrayAdd}" not in l_add2

    # More than two operands and preservation of order
    add3_abc = ArrayAdd(A, B, C)
    assert latex(add3_abc) == "A + B + C", f"Expected 'A + B + C', got: {latex(add3_abc)!r}"

    add3_cba = ArrayAdd(C, B, A)
    assert latex(add3_cba) == "C + B + A", f"Expected 'C + B + A', got: {latex(add3_cba)!r}"

    # Sum of tensor products
    D = MatrixSymbol('D', 4, 5)
    E = MatrixSymbol('E', 4, 5)
    tp1 = ArrayTensorProduct(A, D)
    tp2 = ArrayTensorProduct(B, E)
    add_tp = ArrayAdd(tp1, tp2)
    l_add_tp = latex(add_tp)
    assert l_add_tp == r"A \boxtimes D + B \boxtimes E", (
        f"Expected 'A \\boxtimes D + B \\boxtimes E', got: {l_add_tp!r}"
    )


def test_pretty_array_tensor_product_unicode_and_ascii():
    A = MatrixSymbol('A', 3, 4)
    B = MatrixSymbol('B', 4, 5)
    C = MatrixSymbol('C', 5, 6)

    # Unicode mode: \u22a0 (boxed times)
    p_u2 = pretty(ArrayTensorProduct(A, B), use_unicode=True)
    assert p_u2 == "A\u22a0B", f"Expected 'A\u22a0B', got: {p_u2!r}"

    p_u3_abc = pretty(ArrayTensorProduct(A, B, C), use_unicode=True)
    assert p_u3_abc == "A\u22a0B\u22a0C", f"Expected 'A\u22a0B\u22a0C', got: {p_u3_abc!r}"

    p_u3_cba = pretty(ArrayTensorProduct(C, B, A), use_unicode=True)
    assert p_u3_cba == "C\u22a0B\u22a0A", f"Expected 'C\u22a0B\u22a0A', got: {p_u3_cba!r}"

    # ASCII fallback mode: .*
    p_a2 = pretty(ArrayTensorProduct(A, B), use_unicode=False)
    assert p_a2 == "A.*B", f"Expected 'A.*B', got: {p_a2!r}"

    p_a3_abc = pretty(ArrayTensorProduct(A, B, C), use_unicode=False)
    assert p_a3_abc == "A.*B.*C", f"Expected 'A.*B.*C', got: {p_a3_abc!r}"

    p_a3_cba = pretty(ArrayTensorProduct(C, B, A), use_unicode=False)
    assert p_a3_cba == "C.*B.*A", f"Expected 'C.*B.*A', got: {p_a3_cba!r}"


def test_pretty_parenthesize_sums():
    A = MatrixSymbol('A', 3, 4)
    B = MatrixSymbol('B', 3, 4)
    C = MatrixSymbol('C', 4, 5)
    x, y = symbols('x y')

    # Unicode mode
    pu_first = pretty(ArrayTensorProduct(ArrayAdd(A, B), C), use_unicode=True)
    assert pu_first == "(A + B)\u22a0C", f"Expected '(A + B)\u22a0C', got: {pu_first!r}"

    pu_second = pretty(ArrayTensorProduct(C, ArrayAdd(A, B)), use_unicode=True)
    assert pu_second == "C\u22a0(A + B)", f"Expected 'C\u22a0(A + B)', got: {pu_second!r}"

    pu_core_add = pretty(ArrayTensorProduct(x + y, C), use_unicode=True)
    assert pu_core_add == "(x + y)\u22a0C", f"Expected '(x + y)\u22a0C', got: {pu_core_add!r}"

    # ASCII mode
    pa_first = pretty(ArrayTensorProduct(ArrayAdd(A, B), C), use_unicode=False)
    assert pa_first == "(A + B).*C", f"Expected '(A + B).*C', got: {pa_first!r}"

    pa_second = pretty(ArrayTensorProduct(C, ArrayAdd(A, B)), use_unicode=False)
    assert pa_second == "C.*(A + B)", f"Expected 'C.*(A + B)', got: {pa_second!r}"

    pa_core_add = pretty(ArrayTensorProduct(x + y, C), use_unicode=False)
    assert pa_core_add == "(x + y).*C", f"Expected '(x + y).*C', got: {pa_core_add!r}"


def test_pretty_array_add():
    A = MatrixSymbol('A', 3, 4)
    B = MatrixSymbol('B', 3, 4)
    C = MatrixSymbol('C', 3, 4)

    # Unicode & ASCII ordinary sums
    assert pretty(ArrayAdd(A, B), use_unicode=True) == "A + B"
    assert pretty(ArrayAdd(A, B), use_unicode=False) == "A + B"
    assert pretty(ArrayAdd(A, B, C), use_unicode=True) == "A + B + C"
    assert pretty(ArrayAdd(C, B, A), use_unicode=True) == "C + B + A"
    assert pretty(ArrayAdd(A, B, C), use_unicode=False) == "A + B + C"
    assert pretty(ArrayAdd(C, B, A), use_unicode=False) == "C + B + A"

    # Sum of tensor products
    D = MatrixSymbol('D', 4, 5)
    E = MatrixSymbol('E', 4, 5)
    tp1 = ArrayTensorProduct(A, D)
    tp2 = ArrayTensorProduct(B, E)
    add_tp = ArrayAdd(tp1, tp2)

    pu_add_tp = pretty(add_tp, use_unicode=True)
    assert pu_add_tp == "A\u22a0D + B\u22a0E", f"Expected 'A\u22a0D + B\u22a0E', got: {pu_add_tp!r}"

    pa_add_tp = pretty(add_tp, use_unicode=False)
    assert pa_add_tp == "A.*D + B.*E", f"Expected 'A.*D + B.*E', got: {pa_add_tp!r}"


def test_str_printer_and_unaffected_classes():
    A = MatrixSymbol('A', 3, 4)
    B = MatrixSymbol('B', 4, 5)
    A2 = MatrixSymbol('A2', 3, 4)

    # str printer keeps ASCII, re-parseable functional form
    assert str(ArrayTensorProduct(A, B)) == "ArrayTensorProduct(A, B)"
    assert sstr(ArrayTensorProduct(A, B)) == "ArrayTensorProduct(A, B)"
    assert str(ArrayAdd(A, A2)) == "ArrayAdd(A, A2)"
    assert sstr(ArrayAdd(A, A2)) == "ArrayAdd(A, A2)"

    # PermuteDims and ArrayContraction retain functional output
    M = MatrixSymbol('M', 3, 3)
    p = PermuteDims(M, (1, 0))
    assert "PermuteDims" in str(p)
    assert "PermuteDims" in latex(p)
    assert "PermuteDims" in pretty(p)

    c = ArrayContraction(M, (0, 1))
    assert "ArrayContraction" in str(c)
    assert "ArrayContraction" in latex(c)
    assert "ArrayContraction" in pretty(c)


def main():
    test_latex_array_tensor_product()
    test_latex_parenthesize_sums()
    test_latex_array_add()
    test_pretty_array_tensor_product_unicode_and_ascii()
    test_pretty_parenthesize_sums()
    test_pretty_array_add()
    test_str_printer_and_unaffected_classes()
    print("All tests passed successfully.")


if __name__ == '__main__':
    try:
        main()
    except AssertionError as e:
        print(f"Assertion failed: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)
    sys.exit(0)
