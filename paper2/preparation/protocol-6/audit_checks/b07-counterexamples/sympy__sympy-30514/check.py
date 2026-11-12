"""
Verification check for sympy__sympy-30514:
fcode: numerically-folded function base loses parentheses under a power, flipping the sign.
"""
import sys
from sympy import Float, Integer, Mul, Pow, Symbol, asin, atan, cos, pi, sin, sqrt
from sympy.printing.fortran import fcode


def test_sin_reproduction():
    # Issue reproduction: sin(...) folding to negative float under power
    e = sin(Float("1.265344399150595") - Float("0.5") * pi)
    res = fcode(e ** 2, source_format="free", standard=95)
    # Fortran binds ** tighter than unary minus, so (-a)**2 is required.
    assert res.startswith("(-"), f"Expected base to be parenthesized with '(-', got: {res}"
    assert ")**2" in res, f"Expected power to bind to parenthesized base, got: {res}"
    assert "-0.3007242143351585" in res, f"Expected numeric literal in output, got: {res}"


def test_cos_reproduction():
    # Cosine reproduction
    e = cos(Float("1.0") * 2 * pi / 3) ** 2
    res = fcode(e, source_format="free", standard=95)
    assert res.startswith("(-"), f"Expected base to be parenthesized with '(-', got: {res}"
    assert ")**2" in res, f"Expected power to bind to parenthesized base, got: {res}"


def test_other_numeric_inputs_and_powers():
    # Negative folded function under different powers (e.g. 3, 4)
    e1 = sin(Float("-1.0")) ** 3
    res1 = fcode(e1, source_format="free", standard=95)
    assert res1.startswith("(-"), f"Expected '(-', got: {res1}"
    assert ")**3" in res1, f"Expected ')**3', got: {res1}"

    e2 = sin(Float("-1.0")) ** 4
    res2 = fcode(e2, source_format="free", standard=95)
    assert res2.startswith("(-"), f"Expected '(-', got: {res2}"
    assert ")**4" in res2, f"Expected ')**4', got: {res2}"

    # Positive folded function under power should NOT have redundant outer parentheses on base
    pos = sin(Float("1.0")) ** 2
    res_pos = fcode(pos, source_format="free", standard=95)
    assert not res_pos.startswith("("), f"Expected no parentheses for positive folded base, got: {res_pos}"
    assert "**2" in res_pos, f"Expected '**2', got: {res_pos}"


def test_kinematic_nested_expression():
    # Kinematic example from issue report where folded power is nested in larger expression
    crank, short_side, long_side = 0.221, 0.06646, 0.21077
    coupler_angle = pi / 2.0 - atan(long_side / short_side)
    coupler_length = sqrt(short_side ** 2 + long_side ** 2)
    x = -crank * cos(asin(coupler_length * sin(coupler_angle) / crank))

    res = fcode(x, source_format="free", standard=95)
    # The nested power base is negative: it must be parenthesized like (-0.3007...d0)**2
    # and not bare *-0.3007...d0**2
    assert "*-0.3007" not in res, f"Found unparenthesized negative base under power in nested expr: {res}"
    assert "(-0.3007242143351585" in res, f"Expected parenthesized base in nested expr, got: {res}"
    assert ")**2" in res, f"Expected power binding to parenthesized base, got: {res}"


def test_already_negative_bases_and_symbolic():
    # Bases that are already negative expressions must keep correct parentheses
    res_neg_float = fcode(Pow(Float("-0.3"), Integer(2), evaluate=False), source_format="free")
    assert res_neg_float.startswith("(-"), f"Expected '(-', got: {res_neg_float}"
    assert res_neg_float.endswith(")**2"), f"Expected ')**2', got: {res_neg_float}"

    x = Symbol("x")
    res_neg_x = fcode(Pow(Mul(Integer(-1), x, evaluate=False), Integer(2), evaluate=False), source_format="free")
    assert res_neg_x == "(-x)**2", f"Expected (-x)**2, got: {res_neg_x}"

    res_neg_int = fcode(Pow(Integer(-2), Integer(2), evaluate=False), source_format="free")
    assert res_neg_int == "(-2)**2", f"Expected (-2)**2, got: {res_neg_int}"

    # Symbolic function should not have redundant outer parentheses
    res_sym_func = fcode(sin(x) ** 2, source_format="free")
    assert res_sym_func == "sin(x)**2", f"Expected sin(x)**2, got: {res_sym_func}"


def main():
    test_sin_reproduction()
    test_cos_reproduction()
    test_other_numeric_inputs_and_powers()
    test_kinematic_nested_expression()
    test_already_negative_bases_and_symbolic()
    print("All tests passed!")


if __name__ == "__main__":
    main()
