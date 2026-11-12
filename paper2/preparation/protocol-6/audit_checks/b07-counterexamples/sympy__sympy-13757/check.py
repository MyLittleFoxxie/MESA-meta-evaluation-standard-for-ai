import sys

def main():
    from sympy import Poly, S, Symbol

    x = Symbol('x')

    # 1. Poly(x) * x
    res1 = Poly(x) * x
    assert isinstance(res1, Poly), f"Poly(x) * x must be a Poly, got {type(res1)}: {res1}"
    assert res1 == Poly(x**2, x, domain='ZZ'), f"Poly(x) * x gave {res1}, expected Poly(x**2, x, domain='ZZ')"

    # 2. x * Poly(x)
    res2 = x * Poly(x)
    assert isinstance(res2, Poly), f"x * Poly(x) must be a Poly, got {type(res2)}: {res2}"
    assert res2 == Poly(x**2, x, domain='ZZ'), f"x * Poly(x) gave {res2}, expected Poly(x**2, x, domain='ZZ')"
    assert res2 == res1, f"x * Poly(x) should equal Poly(x) * x, got {res2} != {res1}"

    # 3. Native -2 * Poly(x)
    res3 = -2 * Poly(x)
    assert isinstance(res3, Poly), f"-2 * Poly(x) must be a Poly, got {type(res3)}: {res3}"
    assert res3 == Poly(-2*x, x, domain='ZZ'), f"-2 * Poly(x) gave {res3}, expected Poly(-2*x, x, domain='ZZ')"

    # 4. S(-2) * Poly(x)
    res4 = S(-2) * Poly(x)
    assert isinstance(res4, Poly), f"S(-2) * Poly(x) must be a Poly, got {type(res4)}: {res4}"
    assert res4 == Poly(-2*x, x, domain='ZZ'), f"S(-2) * Poly(x) gave {res4}, expected Poly(-2*x, x, domain='ZZ')"

    # 5. Poly(x) * S(-2)
    res5 = Poly(x) * S(-2)
    assert isinstance(res5, Poly), f"Poly(x) * S(-2) must be a Poly, got {type(res5)}: {res5}"
    assert res5 == Poly(-2*x, x, domain='ZZ'), f"Poly(x) * S(-2) gave {res5}, expected Poly(-2*x, x, domain='ZZ')"
    assert res4 == res5, f"S(-2) * Poly(x) should equal Poly(x) * S(-2), got {res4} != {res5}"

    # 6. Compound expression: (x + 1) * Poly(x) vs Poly(x) * (x + 1)
    res6 = (x + 1) * Poly(x)
    assert isinstance(res6, Poly), f"(x + 1) * Poly(x) must be a Poly, got {type(res6)}: {res6}"
    assert res6 == Poly(x**2 + x, x, domain='ZZ'), f"(x + 1) * Poly(x) gave {res6}, expected Poly(x**2 + x, x, domain='ZZ')"
    assert res6 == Poly(x) * (x + 1), f"(x + 1) * Poly(x) should equal Poly(x) * (x + 1)"

    print("All checks passed successfully.")
    sys.exit(0)

if __name__ == '__main__':
    main()
