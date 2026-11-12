import sys
from sympy import ring, ZZ, QQ, symbols


def assert_raises_value_error(fn, *args, **kwargs):
    try:
        fn(*args, **kwargs)
    except ValueError:
        return
    except Exception as e:
        raise AssertionError(f"Expected ValueError, got {type(e).__name__}: {e}")
    raise AssertionError("Expected ValueError, but no exception was raised")


def test_no_arguments():
    # With no arguments, convert the polynomial using its ring's symbols
    R, x, y, z = ring("x,y,z", ZZ)
    X, Y, Z = R.symbols
    f = 3*x**2*y - x*y*z + 7*z**3 + 1

    expr = f.as_expr()
    assert expr == 3*X**2*Y - X*Y*Z + 7*Z**3 + 1
    assert expr.free_symbols == {X, Y, Z}

    # Single-generator ring
    R1, x1 = ring("x", ZZ)
    X1, = R1.symbols
    f1 = 5*x1**3 - 2*x1 + 4
    expr1 = f1.as_expr()
    assert expr1 == 5*X1**3 - 2*X1 + 4
    assert expr1.free_symbols == {X1}

    # Zero-generator ring (constant polynomial)
    R0, = ring("", ZZ)
    f0 = R0(42)
    assert f0.as_expr() == 42


def test_supplied_symbols_generator_order_and_powers():
    # With exactly one supplied symbol per generator, use those symbols in generator order
    # and preserve the polynomial's coefficients and powers
    R, x, y, z = ring("x,y,z", ZZ)
    f = 3*x**2*y - x*y*z + 7*z**3 + 1
    U, V, W = symbols("u,v,w")

    expr = f.as_expr(U, V, W)
    assert expr == 3*U**2*V - U*V*W + 7*W**3 + 1
    assert expr.free_symbols == {U, V, W}

    # Verify generator order when symbols are passed in reversed order
    expr_rev = f.as_expr(W, V, U)
    assert expr_rev == 3*W**2*V - W*V*U + 7*U**3 + 1
    assert expr_rev.free_symbols == {U, V, W}

    # Additional polynomial verifying higher powers and coefficients
    p = 2*x**4*y**2 - 5*y*z**3 + 11
    A, B, C = symbols("a,b,c")
    expr_p = p.as_expr(A, B, C)
    assert expr_p == 2*A**4*B**2 - 5*B*C**3 + 11
    assert expr_p.free_symbols == {A, B, C}


def test_various_ring_sizes_and_overlapping_symbols():
    # Accept valid replacement symbols for any ring size,
    # including symbols that also occur among the original generators
    u, v, w = symbols("u,v,w")

    # Ring size 1
    R1, x = ring("x", ZZ)
    X, = R1.symbols
    f1 = 4*x**2 - 3
    t = symbols("t")
    assert f1.as_expr(t) == 4*t**2 - 3
    assert f1.as_expr(t).free_symbols == {t}
    assert f1.as_expr(X) == 4*X**2 - 3

    # Ring size 2
    R2, x2, y2 = ring("x,y", QQ)
    X2, Y2 = R2.symbols
    f2 = 2*x2**3 - 3*y2 + 1
    s, t = symbols("s,t")
    assert f2.as_expr(s, t) == 2*s**3 - 3*t + 1
    assert f2.as_expr(s, t).free_symbols == {s, t}

    # Replacement symbols that occur among original generators (e.g. permuted or mixed)
    assert f2.as_expr(Y2, X2) == 2*Y2**3 - 3*X2 + 1
    assert f2.as_expr(X2, Y2) == 2*X2**3 - 3*Y2 + 1
    assert f2.as_expr(X2, t) == 2*X2**3 - 3*t + 1

    # Ring size 3 permuting original ring generators
    R3, x3, y3, z3 = ring("x,y,z", ZZ)
    X3, Y3, Z3 = R3.symbols
    f3 = 3*x3**2*y3 - x3*y3*z3 + 7*z3**3 + 1
    assert f3.as_expr(Z3, Y3, X3) == 3*Z3**2*Y3 - Z3*Y3*X3 + 7*X3**3 + 1
    assert f3.as_expr(X3, Z3, Y3) == 3*X3**2*Z3 - X3*Z3*Y3 + 7*Y3**3 + 1
    assert f3.as_expr(X3, Y3, u) == 3*X3**2*Y3 - X3*Y3*u + 7*u**3 + 1

    # Ring size 4
    R4, a, b, c, d = ring("a,b,c,d", ZZ)
    A, B, C, D = R4.symbols
    f4 = a*b*c*d + 1
    s1, s2, s3, s4 = symbols("s1,s2,s3,s4")
    assert f4.as_expr(s1, s2, s3, s4) == s1*s2*s3*s4 + 1
    assert f4.as_expr(D, C, B, A) == D*C*B*A + 1


def test_reject_wrong_number_of_symbols():
    # Reject a nonempty list with the wrong number of symbols
    u, v, w, extra = symbols("u,v,w,extra")

    # Ring size 3
    R, x, y, z = ring("x,y,z", ZZ)
    f = 3*x**2*y - x*y*z + 7*z**3 + 1
    assert_raises_value_error(f.as_expr, u)
    assert_raises_value_error(f.as_expr, u, v)
    assert_raises_value_error(f.as_expr, u, v, w, extra)
    assert_raises_value_error(f.as_expr, u, v, w, extra, symbols("more"))

    # Ring size 1
    R1, x1 = ring("x", ZZ)
    f1 = x1 + 1
    assert_raises_value_error(f1.as_expr, u, v)

    # Ring size 2
    R2, x2, y2 = ring("x,y", ZZ)
    f2 = x2 + y2
    assert_raises_value_error(f2.as_expr, u)
    assert_raises_value_error(f2.as_expr, u, v, w)

    # Ring size 0
    R0, = ring("", ZZ)
    f0 = R0(5)
    assert_raises_value_error(f0.as_expr, u)


def main():
    test_no_arguments()
    test_supplied_symbols_generator_order_and_powers()
    test_various_ring_sizes_and_overlapping_symbols()
    test_reject_wrong_number_of_symbols()
    print("All tests passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
