"""Verification script for sympy__sympy-30273.

Issue: combine_kronecker gives mathematically wrong results for sums of KroneckerProducts.
Behaviors requested:
- Preserve the value of sums of Kronecker products; do not merge terms that differ in multiple factor slots.
- Collect terms that share all factors except one, adding only the differing factors.
- Extract scalar coefficients and include them in the differing slot, including symbolic coefficients and negated terms.
- Apply the collection rule to Kronecker products with any number of factors.
- Correct the combine_kronecker doctest so that its sum example uses a valid identity.
"""

import doctest
import sys
from sympy import Matrix, MatrixSymbol, KroneckerProduct, symbols, S
from sympy.matrices.expressions.kronecker import combine_kronecker


def test_preserve_multislot_sum_and_numeric_check():
    """Preserve the value of sums of Kronecker products; do not merge terms

    that differ in multiple factor slots. Verify mathematically with numeric matrices.
    """
    a = MatrixSymbol('a', 2, 2)
    b = MatrixSymbol('b', 2, 2)
    c = MatrixSymbol('c', 2, 2)
    d = MatrixSymbol('d', 2, 2)

    lhs = KroneckerProduct(a, b) + KroneckerProduct(c, d)
    rhs = combine_kronecker(lhs)

    # Must not merge differing factor slots into KroneckerProduct(a + c, b + d)
    assert rhs == lhs, f"Expected unmerged sum, but got: {rhs}"

    # Numeric verification from issue description
    A_num = Matrix([[1, 2], [3, 4]])
    B_num = Matrix([[0, 1], [1, 0]])
    C_num = Matrix([[2, 0], [0, 2]])
    D_num = Matrix([[1, 1], [0, 1]])

    sub = {a: A_num, b: B_num, c: C_num, d: D_num}
    lhs_eval = lhs.subs(sub).doit()
    rhs_eval = rhs.subs(sub).doit()
    assert lhs_eval == rhs_eval, (
        f"Mathematical inequality after combine_kronecker:\n"
        f"LHS:\n{lhs_eval}\nRHS:\n{rhs_eval}"
    )

    # Also verify direct _kronecker_add method
    add_res = KroneckerProduct(a, b)._kronecker_add(KroneckerProduct(c, d))
    assert add_res == lhs, f"_kronecker_add should not merge multiple slots: {add_res}"


def test_single_slot_collection():
    """Collect terms that share all factors except one, adding only the differing factors."""
    a = MatrixSymbol('a', 2, 2)
    b = MatrixSymbol('b', 2, 2)
    c = MatrixSymbol('c', 2, 2)
    d = MatrixSymbol('d', 2, 2)

    # Differ in first slot
    res1 = combine_kronecker(KroneckerProduct(a, b) + KroneckerProduct(c, b))
    assert res1 == KroneckerProduct(a + c, b), f"Expected KroneckerProduct(a + c, b), got: {res1}"

    # Differ in second slot
    res2 = combine_kronecker(KroneckerProduct(a, b) + KroneckerProduct(a, d))
    assert res2 == KroneckerProduct(a, b + d), f"Expected KroneckerProduct(a, b + d), got: {res2}"

    # Direct _kronecker_add checks
    assert KroneckerProduct(a, b)._kronecker_add(KroneckerProduct(c, b)) == KroneckerProduct(a + c, b)
    assert KroneckerProduct(a, b)._kronecker_add(KroneckerProduct(a, d)) == KroneckerProduct(a, b + d)

    # Identical terms
    assert KroneckerProduct(a, b)._kronecker_add(KroneckerProduct(a, b)) == 2 * KroneckerProduct(a, b)


def test_scalar_coefficients_and_negations():
    """Extract scalar coefficients and include them in the differing slot,

    including symbolic coefficients and negated terms.
    """
    a = MatrixSymbol('a', 2, 2)
    b = MatrixSymbol('b', 2, 2)
    c = MatrixSymbol('c', 2, 2)
    d = MatrixSymbol('d', 2, 2)
    x, y = symbols('x y')

    # Negated terms (subtraction)
    res_sub1 = combine_kronecker(KroneckerProduct(a, b) - KroneckerProduct(c, b))
    assert res_sub1 == KroneckerProduct(a - c, b), f"Expected KroneckerProduct(a - c, b), got: {res_sub1}"

    res_sub2 = combine_kronecker(KroneckerProduct(a, b) - KroneckerProduct(a, d))
    assert res_sub2 == KroneckerProduct(a, b - d), f"Expected KroneckerProduct(a, b - d), got: {res_sub2}"

    # Numeric scalar coefficients
    res_num = combine_kronecker(2 * KroneckerProduct(a, b) + 3 * KroneckerProduct(c, b))
    assert res_num == KroneckerProduct(2 * a + 3 * c, b), f"Expected KroneckerProduct(2*a + 3*c, b), got: {res_num}"

    # Symbolic scalar coefficients
    res_sym = combine_kronecker(x * KroneckerProduct(a, b) + y * KroneckerProduct(c, b))
    assert res_sym == KroneckerProduct(x * a + y * c, b), f"Expected KroneckerProduct(x*a + y*c, b), got: {res_sym}"

    # Identical Kronecker products with scalar coefficients
    res_ident = combine_kronecker(x * KroneckerProduct(a, b) + y * KroneckerProduct(a, b))
    assert res_ident == (x + y) * KroneckerProduct(a, b), f"Expected (x + y)*KroneckerProduct(a, b), got: {res_ident}"


def test_any_number_of_factors():
    """Apply the collection rule to Kronecker products with any number of factors."""
    a = MatrixSymbol('a', 2, 2)
    b = MatrixSymbol('b', 2, 2)
    c = MatrixSymbol('c', 2, 2)
    d = MatrixSymbol('d', 2, 2)
    e = MatrixSymbol('e', 2, 2)

    # 3 factors - 1 slot differing (middle slot)
    kp3_1 = KroneckerProduct(a, b, c)
    kp3_2 = KroneckerProduct(a, d, c)
    res3 = combine_kronecker(kp3_1 + kp3_2)
    assert res3 == KroneckerProduct(a, b + d, c), f"Expected KroneckerProduct(a, b + d, c), got: {res3}"

    # 3 factors - 2 slots differing (must NOT merge)
    kp3_3 = KroneckerProduct(e, d, c)
    res3_no = combine_kronecker(kp3_1 + kp3_3)
    assert res3_no == kp3_1 + kp3_3, f"Expected unmerged 3-factor sum, got: {res3_no}"

    # 4 factors - 1 slot differing
    f = MatrixSymbol('f', 2, 2)
    kp4_1 = KroneckerProduct(a, b, c, d)
    kp4_2 = KroneckerProduct(a, b, f, d)
    res4 = combine_kronecker(kp4_1 + kp4_2)
    assert res4 == KroneckerProduct(a, b, c + f, d), f"Expected KroneckerProduct(a, b, c + f, d), got: {res4}"


def test_doctest_corrected():
    """Correct the combine_kronecker doctest so that its sum example uses a valid identity."""
    doc = combine_kronecker.__doc__
    assert doc is not None, "combine_kronecker.__doc__ is missing"

    # Old invalid rewrite must not be in docstring
    assert "KroneckerProduct(A + B.T, B + A.T)" not in doc, (
        "combine_kronecker docstring still contains mathematically invalid example: "
        "KroneckerProduct(A + B.T, B + A.T)"
    )

    # Correct single-slot example must be present
    assert "combine_kronecker(KroneckerProduct(A, B)+KroneckerProduct(B.T, B))" in doc, (
        "combine_kronecker docstring should contain the corrected single-slot example"
    )

    # Doctest runner must pass on combine_kronecker
    runner = doctest.DocTestRunner(verbose=False)
    finder = doctest.DocTestFinder()
    tests = finder.find(combine_kronecker, "combine_kronecker")
    for t in tests:
        res = runner.run(t)
        assert res.failed == 0, f"Doctest failed with {res.failed} failures: {res}"


def test_symbolic_shapes_from_doctest():
    """Check symbolic rectangular shapes as presented in doctest."""
    m_sym, n_sym = symbols('m n', integer=True)
    A = MatrixSymbol('A', m_sym, n_sym)
    B = MatrixSymbol('B', n_sym, m_sym)

    # When both slots differ, even if structurally equal, do NOT merge
    res_multidiff = combine_kronecker(KroneckerProduct(A, B) + KroneckerProduct(B.T, A.T))
    assert res_multidiff == KroneckerProduct(A, B) + KroneckerProduct(B.T, A.T), (
        f"Expected unmerged sum for structurally equal but differing slots, got: {res_multidiff}"
    )

    # When only one slot differs, merge correctly
    res_singlediff = combine_kronecker(KroneckerProduct(A, B) + KroneckerProduct(B.T, B))
    assert res_singlediff == KroneckerProduct(A + B.T, B), (
        f"Expected KroneckerProduct(A + B.T, B), got: {res_singlediff}"
    )


def main():
    test_preserve_multislot_sum_and_numeric_check()
    test_single_slot_collection()
    test_scalar_coefficients_and_negations()
    test_any_number_of_factors()
    test_doctest_corrected()
    test_symbolic_shapes_from_doctest()
    print("All combine_kronecker verification tests passed successfully.")
    sys.exit(0)


if __name__ == '__main__':
    main()
