"""
Verification check for sympy__sympy-20438.
Issue: is_subset gives wrong results for ProductSet and FiniteSet,
and Eq(b, c).simplify() raises AttributeError on Complement.
"""
import sys
from sympy import FiniteSet, ProductSet, Eq, S, Set


def test_productset_finiteset_subset_and_equality():
    a = FiniteSet(1, 2)
    b = ProductSet(a, a)
    c = FiniteSet((1, 1), (1, 2), (2, 1), (2, 2))

    # Intersection agreement
    assert b.intersection(c) == c.intersection(b)

    # Subset tests
    assert b.is_subset(c) is True
    assert c.is_subset(b) is True

    # Proper subset / not subset test
    d = FiniteSet((1, 1), (1, 2))
    assert b.is_subset(d) is False
    assert d.is_subset(b) is True

    # Equality evaluations
    assert Eq(b, c) == S.true
    assert Eq(c, b) == S.true
    assert Eq(b, d) == S.false

    # Equality simplification without AttributeError
    assert Eq(b, c).simplify() == S.true
    assert Eq(b, c, evaluate=False).simplify() == S.true

    # Non-Expr relational simplification should not attempt .equals(0) on Complement
    s1 = Set()
    s2 = Set()
    eq_uneval = Eq(s1, s2, evaluate=False)
    simplified = eq_uneval.simplify()
    assert simplified is not None


if __name__ == "__main__":
    try:
        test_productset_finiteset_subset_and_equality()
        print("All tests passed.")
        sys.exit(0)
    except Exception as e:
        print(f"Test failed: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
