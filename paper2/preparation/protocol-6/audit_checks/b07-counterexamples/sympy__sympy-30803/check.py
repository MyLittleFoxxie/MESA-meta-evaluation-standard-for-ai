"""
Verification script for sympy__sympy-30803:
FracField over EXRAW: RecursionError if built from Integer
"""
import sys
from sympy import EXRAW, symbols, sympify, Integer, Rational
from sympy.polys.domains import ZZ
from sympy.polys.fields import FracElement


def test_issue_reproducer():
    """Verify constructing a fraction field element over EXRAW from Integer."""
    s = symbols("s")
    domain = EXRAW
    ring = domain.poly_ring(s)
    field = domain.frac_field(s)

    expr = sympify(1)
    dom_elem = domain.from_sympy(expr)
    ring_elem = ring.from_sympy(expr)
    frac_elem = field.from_sympy(expr)

    assert isinstance(frac_elem, FracElement), f"Expected FracElement, got {type(frac_elem)}"
    assert frac_elem.field == field.field, f"Expected field {field.field}, got {frac_elem.field}"
    assert frac_elem == field.field.one, f"Expected {field.field.one}, got {frac_elem}"
    assert frac_elem.as_expr() == expr, f"Expected {expr}, got {frac_elem.as_expr()}"
    assert field.to_sympy(frac_elem) == expr, f"Expected {expr}, got {field.to_sympy(frac_elem)}"


def test_exraw_integers():
    """Verify various integers preserve value and field over EXRAW."""
    s = symbols("s")
    domain = EXRAW
    field = domain.frac_field(s)
    F = field.field

    for val in [0, 1, -1, 5, -42, 100]:
        int_expr = Integer(val)
        elem = field.from_sympy(int_expr)
        assert isinstance(elem, FracElement)
        assert elem.field == F
        assert elem.as_expr() == int_expr

        from_expr_elem = F.from_expr(int_expr)
        assert isinstance(from_expr_elem, FracElement)
        assert from_expr_elem.field == F
        assert from_expr_elem == elem

        field_new_elem = F.field_new(int_expr)
        assert isinstance(field_new_elem, FracElement)
        assert field_new_elem.field == F
        assert field_new_elem == elem

    assert field.from_sympy(Integer(0)) == F.zero
    assert field.from_sympy(Integer(1)) == F.one


def test_rebuild_ground_coefficients():
    """Verify ground coefficients are rebuilt as FracElement instances."""
    s = symbols("s")
    domain = EXRAW
    field = domain.frac_field(s)
    F = field.field

    mapping = dict(list(zip(F.symbols, F.gens)))

    rebuilt_1 = F._rebuild_expr(sympify(1), mapping)
    assert isinstance(rebuilt_1, FracElement), (
        f"_rebuild_expr should return FracElement, got {type(rebuilt_1)}"
    )
    assert rebuilt_1.field == F
    assert rebuilt_1 == F.one

    rebuilt_5 = F._rebuild_expr(sympify(5), mapping)
    assert isinstance(rebuilt_5, FracElement)
    assert rebuilt_5.field == F
    assert rebuilt_5.as_expr() == Integer(5)

    # Composite expressions involving generators and integer coefficients
    poly_expr = sympify(3) * s + sympify(5)
    poly_elem = field.from_sympy(poly_expr)
    assert isinstance(poly_elem, FracElement)
    assert poly_elem.field == F
    assert poly_elem.as_expr() == poly_expr

    rat_expr = (s + sympify(1)) / (s - sympify(2))
    rat_elem = field.from_sympy(rat_expr)
    assert isinstance(rat_elem, FracElement)
    assert rat_elem.field == F
    assert rat_elem.as_expr() == rat_expr


def test_multivariate_exraw():
    """Verify multivariate fraction field over EXRAW with integers."""
    x, y = symbols("x y")
    field = EXRAW.frac_field(x, y)
    F = field.field

    one_elem = field.from_sympy(Integer(1))
    assert isinstance(one_elem, FracElement)
    assert one_elem.field == F
    assert one_elem == F.one

    expr = (sympify(2)*x + y + sympify(1)) / (x - sympify(3)*y + sympify(4))
    elem = field.from_sympy(expr)
    assert isinstance(elem, FracElement)
    assert elem.field == F
    assert elem.as_expr() == expr


def test_rebuild_associated_field():
    """Verify ground conversion for domains with assoc_field (e.g., ZZ with Rational)."""
    s = symbols("s")
    field_zz = ZZ.frac_field(s)
    F_zz = field_zz.field
    mapping = dict(list(zip(F_zz.symbols, F_zz.gens)))

    rebuilt_rat = F_zz._rebuild_expr(Rational(1, 2), mapping)
    assert isinstance(rebuilt_rat, FracElement), (
        f"_rebuild_expr should return FracElement, got {type(rebuilt_rat)}"
    )
    assert rebuilt_rat.field == F_zz
    assert rebuilt_rat.as_expr() == Rational(1, 2)


def main():
    test_issue_reproducer()
    test_exraw_integers()
    test_rebuild_ground_coefficients()
    test_multivariate_exraw()
    test_rebuild_associated_field()
    print("All verification tests passed successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
