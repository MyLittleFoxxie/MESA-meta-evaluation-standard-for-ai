"""
Verification test for sympy/sympy issue:
Result from clear_denoms() prints like zero poly but behaves weirdly (due to unstripped DMP)
"""
import sys
from sympy import symbols, sympify, Poly
from sympy.polys.domains import EX


def test_expression_domain_bool():
    # Test that EX.__bool__ recognizes mathematically zero expressions
    expr_str = (
        "-117968192370600*18**(1/3)/(217603955769048*(24201 + 253*sqrt(9165))**(1/3) + 2273005839412*sqrt(9165)*(24201 + 253*sqrt(9165))**(1/3)) "
        "- 15720318185*2**(2/3)*3**(1/3)*(24201 + 253*sqrt(9165))**(2/3)/(217603955769048*(24201 + 253*sqrt(9165))**(1/3) + 2273005839412*sqrt(9165)*(24201 + 253*sqrt(9165))**(1/3)) "
        "+ 15720318185*12**(1/3)*(24201 + 253*sqrt(9165))**(2/3)/(217603955769048*(24201 + 253*sqrt(9165))**(1/3) + 2273005839412*sqrt(9165)*(24201 + 253*sqrt(9165))**(1/3)) "
        "+ 117968192370600*2**(1/3)*3**(2/3)/(217603955769048*(24201 + 253*sqrt(9165))**(1/3) + 2273005839412*sqrt(9165)*(24201 + 253*sqrt(9165))**(1/3))"
    )
    expr = sympify(expr_str)
    assert expr.is_zero is True, "Expression should evaluate to zero via is_zero"
    assert expr != 0, "Expression is structurally not equal to 0"

    ex_val = EX(expr)
    assert not bool(ex_val), "EX(expr) for mathematically zero expr must evaluate to False in bool context"

    # Also test basic EX truth values
    assert not bool(EX(0)), "EX(0) must be falsy"
    assert bool(EX(1)), "EX(1) must be truthy"
    x = symbols("x")
    assert bool(EX(x)), "EX(x) for non-zero symbol must be truthy"


def test_clear_denoms_zero_poly():
    x = symbols("x")
    expr_str = (
        "-117968192370600*18**(1/3)/(217603955769048*(24201 + 253*sqrt(9165))**(1/3) + 2273005839412*sqrt(9165)*(24201 + 253*sqrt(9165))**(1/3)) "
        "- 15720318185*2**(2/3)*3**(1/3)*(24201 + 253*sqrt(9165))**(2/3)/(217603955769048*(24201 + 253*sqrt(9165))**(1/3) + 2273005839412*sqrt(9165)*(24201 + 253*sqrt(9165))**(1/3)) "
        "+ 15720318185*12**(1/3)*(24201 + 253*sqrt(9165))**(2/3)/(217603955769048*(24201 + 253*sqrt(9165))**(1/3) + 2273005839412*sqrt(9165)*(24201 + 253*sqrt(9165))**(1/3)) "
        "+ 117968192370600*2**(1/3)*3**(2/3)/(217603955769048*(24201 + 253*sqrt(9165))**(1/3) + 2273005839412*sqrt(9165)*(24201 + 253*sqrt(9165))**(1/3))"
    )
    f = Poly(sympify(expr_str), x)
    coeff, p = f.clear_denoms()

    # 1. Poly should be recognized as zero
    assert p.is_zero is True, f"p.is_zero must be True, got {p.is_zero}"

    # 2. Consistent with as_expr()
    expr = p.as_expr()
    assert expr == 0, f"p.as_expr() must be 0, got {expr}"
    assert expr.is_zero is True, "p.as_expr().is_zero must be True"

    # 3. Stripped DMP representation
    rep_list = p.rep.to_list()
    assert rep_list == [], f"DMP representation must be stripped to [], got {rep_list}"

    # 4. terms_gcd() should not raise IndexError and return a zero poly
    monoms, gcd_poly = p.terms_gcd()
    assert gcd_poly.is_zero is True, f"terms_gcd() poly must be zero, got {gcd_poly}"

    # 5. primitive() should return zero content and zero poly
    cont, prim_poly = p.primitive()
    assert cont == 0, f"primitive() content must be 0, got {cont}"
    assert prim_poly.is_zero is True, f"primitive() poly must be zero, got {prim_poly}"


def test_poly_construction_zero_ex():
    x = symbols("x")
    expr_str = (
        "-117968192370600*18**(1/3)/(217603955769048*(24201 + 253*sqrt(9165))**(1/3) + 2273005839412*sqrt(9165)*(24201 + 253*sqrt(9165))**(1/3)) "
        "- 15720318185*2**(2/3)*3**(1/3)*(24201 + 253*sqrt(9165))**(2/3)/(217603955769048*(24201 + 253*sqrt(9165))**(1/3) + 2273005839412*sqrt(9165)*(24201 + 253*sqrt(9165))**(1/3)) "
        "+ 15720318185*12**(1/3)*(24201 + 253*sqrt(9165))**(2/3)/(217603955769048*(24201 + 253*sqrt(9165))**(1/3) + 2273005839412*sqrt(9165)*(24201 + 253*sqrt(9165))**(1/3)) "
        "+ 117968192370600*2**(1/3)*3**(2/3)/(217603955769048*(24201 + 253*sqrt(9165))**(1/3) + 2273005839412*sqrt(9165)*(24201 + 253*sqrt(9165))**(1/3))"
    )
    # Directly constructing a polynomial with this zero EX coefficient
    p = Poly(sympify(expr_str), x, domain='EX')
    assert p.is_zero is True, "Poly with zero EX coefficient should have is_zero=True"
    assert p.rep.to_list() == [], f"Poly DMP representation must be [], got {p.rep.to_list()}"


def main():
    try:
        test_expression_domain_bool()
        test_clear_denoms_zero_poly()
        test_poly_construction_zero_ex()
        print("All tests passed successfully.")
        sys.exit(0)
    except AssertionError as e:
        print(f"Test failed: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
