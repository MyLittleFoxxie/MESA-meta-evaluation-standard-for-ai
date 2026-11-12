import inspect
import sys
from sympy import Mod, symbols, lambdify
from sympy.printing.pycode import pycode
from sympy.printing.precedence import precedence, PRECEDENCE


def test_mod_precedence():
    x, y = symbols('x y')
    # Mod must have Mul precedence so printers treat it with equal precedence as Mul
    assert precedence(Mod(x, y)) == PRECEDENCE["Mul"], (
        f"precedence(Mod(x, y)) should be PRECEDENCE['Mul'] ({PRECEDENCE['Mul']}), "
        f"got {precedence(Mod(x, y))}"
    )


def test_pycode_mod_unary_minus():
    x, y = symbols('x y')
    expr = -Mod(x, y)
    code = pycode(expr)
    assert code == "-(x % y)", f"pycode(-Mod(x, y)) should be '-(x % y)', got '{code}'"


def test_pycode_mod_multiplier():
    x, y, z = symbols('x y z')
    # Integer multiplier
    code2 = pycode(2 * Mod(x, y))
    assert code2 == "2*(x % y)", f"pycode(2 * Mod(x, y)) should be '2*(x % y)', got '{code2}'"

    # Negative integer multiplier
    code_neg = pycode(-2 * Mod(x, y))
    assert code_neg == "-2*(x % y)", f"pycode(-2 * Mod(x, y)) should be '-2*(x % y)', got '{code_neg}'"

    # Symbolic multiplier
    code_sym = pycode(z * Mod(x, y))
    assert code_sym == "z*(x % y)", f"pycode(z * Mod(x, y)) should be 'z*(x % y)', got '{code_sym}'"


def test_lambdify_mod_unary_minus():
    x, y = symbols('x y')
    expr = -Mod(x, y)

    # Default lambdify
    f = lambdify([x, y], expr)
    f_res = f(3, 7)
    assert f_res == -3, f"Default lambdify of -Mod(x, y) at (3, 7) returned {f_res}, expected -3"

    # modules=[] lambdify
    g = lambdify([x, y], expr, modules=[])
    g_res = g(3, 7)
    assert g_res == -3, (
        f"lambdify([x, y], -Mod(x, y), modules=[]) at (3, 7) returned {g_res}, expected -3 "
        f"(should match default lambdify {f_res})"
    )

    # Check that generated code groups remainder properly
    src = inspect.getsource(g)
    assert "-(x % y)" in src, f"Expected '-(x % y)' in lambdify source, got:\n{src}"


def test_lambdify_mod_multiplication():
    x, y, z = symbols('x y z')

    # Positive integer multiplier: 2 * (5 % 3) = 2 * 2 = 4
    g1 = lambdify([x, y], 2 * Mod(x, y), modules=[])
    res1 = g1(5, 3)
    assert res1 == 4, f"lambdify([x, y], 2 * Mod(x, y), modules=[]) at (5, 3) returned {res1}, expected 4"
    src1 = inspect.getsource(g1)
    assert "(x % y)" in src1, f"Expected '(x % y)' in lambdify source, got:\n{src1}"

    # Symbolic multiplier: z * (5 % 3) with z=2 => 4; with z=-1 => -2
    g2 = lambdify([x, y, z], z * Mod(x, y), modules=[])
    res2 = g2(5, 3, 2)
    assert res2 == 4, f"lambdify([x, y, z], z * Mod(x, y), modules=[]) at (5, 3, 2) returned {res2}, expected 4"
    res3 = g2(5, 3, -1)
    assert res3 == -2, f"lambdify([x, y, z], z * Mod(x, y), modules=[]) at (5, 3, -1) returned {res3}, expected -2"

    # Compound expression multiplier: (x + 1) * Mod(x, y) at (5, 3) => 6 * 2 = 12
    g3 = lambdify([x, y], (x + 1) * Mod(x, y), modules=[])
    res4 = g3(5, 3)
    assert res4 == 12, f"lambdify([x, y], (x + 1) * Mod(x, y), modules=[]) at (5, 3) returned {res4}, expected 12"


def main():
    test_mod_precedence()
    test_pycode_mod_unary_minus()
    test_pycode_mod_multiplier()
    test_lambdify_mod_unary_minus()
    test_lambdify_mod_multiplication()
    print("All tests passed successfully.")


if __name__ == "__main__":
    main()
