"""
Independent verification test for sympy__sympy-30590.
"""

from sympy import I, acot, acoth, pi, symbols


def main():
    # For a symbol x that can equal zero, acot(-x).subs(x, 0) must equal acot(0), namely pi/2.
    # For a symbol x that can equal zero, acoth(-x).subs(x, 0) must equal acoth(0), namely I*pi/2.
    x = symbols('x')

    expected_acot = acot(0)
    assert expected_acot == pi / 2, f"acot(0) expected pi/2, got {expected_acot}"
    val_acot = acot(-x).subs(x, 0)
    assert val_acot == expected_acot, (
        f"acot(-x).subs(x, 0) expected {expected_acot}, got {val_acot}"
    )

    expected_acoth = acoth(0)
    assert expected_acoth == I * pi / 2, f"acoth(0) expected I*pi/2, got {expected_acoth}"
    val_acoth = acoth(-x).subs(x, 0)
    assert val_acoth == expected_acoth, (
        f"acoth(-x).subs(x, 0) expected {expected_acoth}, got {val_acoth}"
    )

    # Real symbol that can equal zero
    xr = symbols('x', real=True)
    assert acot(-xr).subs(xr, 0) == expected_acot, (
        f"acot(-xr).subs(xr, 0) expected {expected_acot}, got {acot(-xr).subs(xr, 0)}"
    )
    assert acoth(-xr).subs(xr, 0) == expected_acoth, (
        f"acoth(-xr).subs(xr, 0) expected {expected_acoth}, got {acoth(-xr).subs(xr, 0)}"
    )

    # When symbol is known to be nonzero, minus sign extraction should still work
    y = symbols('y', nonzero=True)
    assert acot(-y) == -acot(y), f"acot(-y) expected -acot(y), got {acot(-y)}"
    assert acoth(-y) == -acoth(y), f"acoth(-y) expected -acoth(y), got {acoth(-y)}"


if __name__ == '__main__':
    main()
