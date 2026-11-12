import sys
from sympy import Product, Symbol, S, Rational, simplify

def test_product_sum_split_issue_13551():
    n = Symbol('n')
    k = Symbol('k')

    # Issue 13551: Product(n + 1 / 2**k, [k, 0, n-1]).doit()
    # Unpatched sympy incorrectly treated Add inside Product as sum of products,
    # yielding 2**(n*(-n + 1)/2) + n**n instead of preserving the full product
    # via exp(Sum(log(...))).
    p = Product(n + S.One / 2**k, (k, 0, n - 1)).doit()

    bad_expr = 2**(n*(-n + 1)/2) + n**n
    assert p != bad_expr, "Product.doit() incorrectly split Add into sum of products: %s" % p

    p_simp = simplify(p)
    assert p_simp != bad_expr, "simplify(p) equals the incorrect sum: %s" % p_simp

    # For n=2: (2 + 1) * (2 + 1/2) = 3 * 5/2 = 15/2
    val2 = p.subs(n, 2)
    if hasattr(val2, 'doit'):
        val2 = val2.doit()
    assert val2 != Rational(9, 2), "p.subs(n, 2) gave 9/2 instead of 15/2"
    assert val2 == Rational(15, 2), "p.subs(n, 2) expected 15/2, got %s" % val2

    # For simplified expression substituted with n=2
    val2_simp = p_simp.subs(n, 2)
    if hasattr(val2_simp, 'doit'):
        val2_simp = val2_simp.doit()
    assert val2_simp == Rational(15, 2), "simplify(p).subs(n, 2) expected 15/2, got %s" % val2_simp

    # For n=3: (3 + 1) * (3 + 1/2) * (3 + 1/4) = 4 * 7/2 * 13/4 = 91/2
    val3 = p.subs(n, 3)
    if hasattr(val3, 'doit'):
        val3 = val3.doit()
    assert val3 != Rational(217, 8), "p.subs(n, 3) gave 217/8 instead of 91/2"
    assert val3 == Rational(91, 2), "p.subs(n, 3) expected 91/2, got %s" % val3

    # Also test with limits as list [k, 0, n - 1] as written in the issue description
    p_list = Product(n + S.One / 2**k, [k, 0, n - 1]).doit()
    val_list = p_list.subs(n, 2)
    if hasattr(val_list, 'doit'):
        val_list = val_list.doit()
    assert val_list == Rational(15, 2), "p_list.subs(n, 2) expected 15/2, got %s" % val_list

if __name__ == '__main__':
    try:
        test_product_sum_split_issue_13551()
        print("All tests passed.")
        sys.exit(0)
    except AssertionError as e:
        print("AssertionError: %s" % e)
        sys.exit(1)
    except Exception as e:
        print("Exception: %s" % e)
        sys.exit(1)
