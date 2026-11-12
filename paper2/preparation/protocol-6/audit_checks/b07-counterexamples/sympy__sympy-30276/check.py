"""Standalone verification test script for sympy__sympy-30276.

Verifies:
- Merging identical tensor-product addends by adding their scalar coefficients.
- Recognizing proportional tensor products after extracting scalar coefficients.
- Returning a ZeroArray with the full shape when coefficients cancel.
- Providing opt-in factoring for tensor products that agree in every slot except one.
- Putting the weighted sum of differing factors into that slot, including negated terms.
- Preserving sums that differ in more than one slot; never adding all slots at once.
- Supporting collection across large sums of tensor products.
"""

import sys


def test_merge_identical_tensor_products():
    from sympy import MatrixSymbol
    from sympy.tensor.array.expressions import ArrayTensorProduct, ArrayAdd

    A = MatrixSymbol("A", 3, 4)
    B = MatrixSymbol("B", 4, 5)
    T = ArrayTensorProduct(A, B)

    # T + T -> 2*T
    add_2 = ArrayAdd(T, T)
    assert add_2 == ArrayTensorProduct(2, A, B), f"Expected ArrayTensorProduct(2, A, B), got {add_2}"

    # T + T + T -> 3*T
    add_3 = ArrayAdd(T, T, T)
    assert add_3 == ArrayTensorProduct(3, A, B), f"Expected ArrayTensorProduct(3, A, B), got {add_3}"

    # 2*T + 3*T -> 5*T
    add_5 = ArrayAdd(2 * T, 3 * T)
    assert add_5 == ArrayTensorProduct(5, A, B), f"Expected ArrayTensorProduct(5, A, B), got {add_5}"


def test_recognize_proportional_tensor_products():
    from sympy import MatrixSymbol
    from sympy.tensor.array.expressions import ArrayTensorProduct, ArrayAdd

    A = MatrixSymbol("A", 3, 4)
    B = MatrixSymbol("B", 4, 5)

    # Proportional terms with coefficients inside the MatrixSymbol factors
    expr1 = ArrayAdd(ArrayTensorProduct(2 * A, B), ArrayTensorProduct(A, 3 * B))
    assert expr1 == ArrayTensorProduct(5, A, B), f"Expected ArrayTensorProduct(5, A, B), got {expr1}"

    # Proportional terms with explicit scalar factor
    expr2 = ArrayAdd(ArrayTensorProduct(2, A, B), ArrayTensorProduct(3, A, B))
    assert expr2 == ArrayTensorProduct(5, A, B), f"Expected ArrayTensorProduct(5, A, B), got {expr2}"

    # Multiplied ArrayTensorProducts
    T = ArrayTensorProduct(A, B)
    expr3 = ArrayAdd(2 * T, 3 * T)
    assert expr3 == ArrayTensorProduct(5, A, B), f"Expected ArrayTensorProduct(5, A, B), got {expr3}"


def test_cancellation_to_zero_array():
    from sympy import MatrixSymbol
    from sympy.tensor.array.expressions import ArrayTensorProduct, ArrayAdd, ZeroArray, ArraySymbol

    A = MatrixSymbol("A", 3, 4)
    B = MatrixSymbol("B", 4, 5)
    T = ArrayTensorProduct(A, B)

    # T - T -> ZeroArray(3, 4, 4, 5)
    res1 = ArrayAdd(T, -T)
    assert isinstance(res1, ZeroArray), f"Expected ZeroArray, got {type(res1)}"
    assert res1.shape == (3, 4, 4, 5), f"Expected shape (3, 4, 4, 5), got {res1.shape}"
    assert res1 == ZeroArray(3, 4, 4, 5), f"Expected ZeroArray(3, 4, 4, 5), got {res1}"

    # Proportional cancellation with MatrixSymbol coefficients
    res2 = ArrayAdd(ArrayTensorProduct(2 * A, B), ArrayTensorProduct(A, -2 * B))
    assert isinstance(res2, ZeroArray), f"Expected ZeroArray, got {type(res2)}"
    assert res2 == ZeroArray(3, 4, 4, 5), f"Expected ZeroArray(3, 4, 4, 5), got {res2}"

    # Cancellation with ArraySymbol
    X = ArraySymbol("X", (2, 3))
    Y = ArraySymbol("Y", (3, 4))
    T_arr = ArrayTensorProduct(X, Y)
    res3 = ArrayAdd(T_arr, -T_arr)
    assert isinstance(res3, ZeroArray), f"Expected ZeroArray, got {type(res3)}"
    assert res3 == ZeroArray(2, 3, 3, 4), f"Expected ZeroArray(2, 3, 3, 4), got {res3}"


def test_opt_in_factoring_single_slot():
    from sympy import MatrixSymbol
    from sympy.tensor.array.expressions import (
        ArrayTensorProduct,
        ArrayAdd,
        ArraySymbol,
        collect_tensor_products,
    )

    A = MatrixSymbol("A", 2, 2)
    B = MatrixSymbol("B", 2, 2)
    C = MatrixSymbol("C", 2, 2)

    # ArrayAdd does NOT automatically factor terms differing in one slot
    raw_add = ArrayAdd(ArrayTensorProduct(A, B), ArrayTensorProduct(A, C))
    assert isinstance(raw_add, ArrayAdd), f"Expected raw ArrayAdd, got {type(raw_add)}"
    assert len(raw_add.args) == 2, f"Expected 2 args in unsimplified ArrayAdd, got {len(raw_add.args)}"

    # Factoring in second slot: A x B + A x C -> A x (B + C)
    factored_1 = collect_tensor_products(raw_add)
    assert factored_1 == ArrayTensorProduct(A, B + C), f"Expected ArrayTensorProduct(A, B + C), got {factored_1}"

    # Factoring in first slot: A x C + B x C -> (A + B) x C
    raw_add_2 = ArrayAdd(ArrayTensorProduct(A, C), ArrayTensorProduct(B, C))
    factored_2 = collect_tensor_products(raw_add_2)
    assert factored_2 == ArrayTensorProduct(A + B, C), f"Expected ArrayTensorProduct(A + B, C), got {factored_2}"

    # Factoring with non-matrix array expressions (ArraySymbol)
    X = ArraySymbol("X", (2, 3))
    Y = ArraySymbol("Y", (3, 4))
    Z = ArraySymbol("Z", (3, 4))
    raw_add_arr = ArrayAdd(ArrayTensorProduct(X, Y), ArrayTensorProduct(X, Z))
    factored_arr = collect_tensor_products(raw_add_arr)
    assert factored_arr == ArrayTensorProduct(X, ArrayAdd(Y, Z)), (
        f"Expected ArrayTensorProduct(X, ArrayAdd(Y, Z)), got {factored_arr}"
    )


def test_weighted_sum_and_negated_terms():
    from sympy import MatrixSymbol
    from sympy.tensor.array.expressions import (
        ArrayTensorProduct,
        ArrayAdd,
        collect_tensor_products,
    )

    A = MatrixSymbol("A", 2, 2)
    B = MatrixSymbol("B", 2, 2)
    C = MatrixSymbol("C", 2, 2)

    # Weighted sum with scalar factor: 2*(A x B) + 3*(A x C) -> A x (2*B + 3*C)
    expr1 = ArrayAdd(ArrayTensorProduct(2, A, B), ArrayTensorProduct(3, A, C))
    res1 = collect_tensor_products(expr1)
    assert res1 == ArrayTensorProduct(A, 2 * B + 3 * C), (
        f"Expected ArrayTensorProduct(A, 2*B + 3*C), got {res1}"
    )

    # Weighted sum with differing slot 0: (2*A) x B + (3*C) x B -> (2*A + 3*C) x B
    expr2 = ArrayAdd(ArrayTensorProduct(2 * A, B), ArrayTensorProduct(3 * C, B))
    res2 = collect_tensor_products(expr2)
    assert res2 == ArrayTensorProduct(2 * A + 3 * C, B), (
        f"Expected ArrayTensorProduct(2*A + 3*C, B), got {res2}"
    )

    # Negated term: A x B - A x C -> A x (B - C)
    expr3 = ArrayAdd(ArrayTensorProduct(A, B), -ArrayTensorProduct(A, C))
    res3 = collect_tensor_products(expr3)
    assert res3 == ArrayTensorProduct(A, B - C), (
        f"Expected ArrayTensorProduct(A, B - C), got {res3}"
    )

    # Negated term with scalar: 2*(A x B) - 3*(A x C) -> A x (2*B - 3*C)
    expr4 = ArrayAdd(ArrayTensorProduct(2, A, B), ArrayTensorProduct(-3, A, C))
    res4 = collect_tensor_products(expr4)
    assert res4 == ArrayTensorProduct(A, 2 * B - 3 * C), (
        f"Expected ArrayTensorProduct(A, 2*B - 3*C), got {res4}"
    )


def test_preserve_sums_differing_in_multiple_slots():
    from sympy import MatrixSymbol
    from sympy.tensor.array.expressions import (
        ArrayTensorProduct,
        ArrayAdd,
        collect_tensor_products,
    )

    A = MatrixSymbol("A", 2, 2)
    B = MatrixSymbol("B", 2, 2)
    C = MatrixSymbol("C", 2, 2)
    D = MatrixSymbol("D", 2, 2)
    E = MatrixSymbol("E", 2, 2)

    # Differing in 2 out of 2 slots: A x B + C x D must NOT be merged to (A + C) x (B + D)
    expr2 = ArrayAdd(ArrayTensorProduct(A, B), ArrayTensorProduct(C, D))
    res2 = collect_tensor_products(expr2)
    assert res2 == expr2, f"Expected {expr2} preserved untouched, got {res2}"
    assert res2 != ArrayTensorProduct(A + C, B + D), "Incorrectly merged all slots at once"

    # Differing in 2 out of 3 slots: A x B x C + A x D x E must NOT be merged
    expr3 = ArrayAdd(ArrayTensorProduct(A, B, C), ArrayTensorProduct(A, D, E))
    res3 = collect_tensor_products(expr3)
    assert res3 == expr3, f"Expected {expr3} preserved untouched, got {res3}"


def test_large_sums_collection():
    from sympy import MatrixSymbol
    from sympy.tensor.array.expressions import (
        ArrayTensorProduct,
        ArrayAdd,
        PermuteDims,
        collect_tensor_products,
    )

    A = MatrixSymbol("A", 2, 2)
    B = MatrixSymbol("B", 2, 2)
    C = MatrixSymbol("C", 2, 2)
    D = MatrixSymbol("D", 2, 2)
    E = MatrixSymbol("E", 2, 2)
    F = MatrixSymbol("F", 2, 2)

    # 4-term collection: A x C x E + A x C x F + A x D x E + A x D x F -> A x (C + D) x (E + F)
    s4 = ArrayAdd(
        ArrayTensorProduct(A, C, E),
        ArrayTensorProduct(A, C, F),
        ArrayTensorProduct(A, D, E),
        ArrayTensorProduct(A, D, F),
    )
    res4 = collect_tensor_products(s4)
    expected4 = ArrayTensorProduct(A, C + D, E + F)
    assert res4 == expected4, f"Expected {expected4}, got {res4}"

    # 8-term collection: (A + B) x (C + D) x (E + F) expanded -> collapses back
    s8 = ArrayAdd(
        ArrayTensorProduct(A, C, E),
        ArrayTensorProduct(A, C, F),
        ArrayTensorProduct(A, D, E),
        ArrayTensorProduct(A, D, F),
        ArrayTensorProduct(B, C, E),
        ArrayTensorProduct(B, C, F),
        ArrayTensorProduct(B, D, E),
        ArrayTensorProduct(B, D, F),
    )
    res8 = collect_tensor_products(s8)
    expected8 = ArrayTensorProduct(A + B, C + D, E + F)
    assert res8 == expected8, f"Expected {expected8}, got {res8}"

    # Recursive collection inside nested expression trees
    nested = PermuteDims(
        ArrayAdd(ArrayTensorProduct(A, B), ArrayTensorProduct(A, C)),
        [1, 0, 2, 3],
    )
    res_nested = collect_tensor_products(nested)
    expected_nested = PermuteDims(ArrayTensorProduct(A, B + C), [1, 0, 2, 3])
    assert res_nested == expected_nested, f"Expected {expected_nested}, got {res_nested}"


def main():
    test_merge_identical_tensor_products()
    test_recognize_proportional_tensor_products()
    test_cancellation_to_zero_array()
    test_opt_in_factoring_single_slot()
    test_weighted_sum_and_negated_terms()
    test_preserve_sums_differing_in_multiple_slots()
    test_large_sums_collection()
    print("All tests passed successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
