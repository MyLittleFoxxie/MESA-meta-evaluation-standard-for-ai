import sys
from sympy import I, Quaternion, Rational, Symbol, cosh, sqrt, tanh, trigsimp


def main():
    t = Symbol('t', real=True)
    tq = Rational(3, 4)

    q = Quaternion(
        2**tq * sqrt(sqrt(2) + 2) * sqrt(cosh(t) + 1) / (4 * sqrt(cosh(t))),
        2**tq * sqrt(sqrt(2) + 2) * sqrt(cosh(t)) * tanh(t) / (4 * sqrt(cosh(t) + 1)),
        2**tq * sqrt(2 - sqrt(2)) * sqrt(cosh(t) + 1) / (4 * sqrt(cosh(t))),
        -2**tq * sqrt(2 - sqrt(2)) * sqrt(cosh(t)) * tanh(t) / (4 * sqrt(cosh(t) + 1)),
    )

    norm_val = q.norm()
    expected_norm = 2**Rational(1, 4)

    assert norm_val == expected_norm or norm_val.equals(expected_norm), (
        f"Expected q.norm() to be {expected_norm}, got {norm_val}"
    )
    assert not norm_val.has(I), f"q.norm() contains spurious complex unit I: {norm_val}"

    inv = q.inverse()

    assert not inv.has(I), f"q.inverse() contains spurious complex unit I: {inv}"
    for idx, comp in enumerate(inv.args):
        assert not comp.has(I), f"q.inverse() component {idx} contains spurious complex unit I: {comp}"

    scalar_part = trigsimp((q * q.conjugate()).args[0].together())
    expected_inv = q.conjugate() / scalar_part

    assert inv == expected_inv or all(
        trigsimp((c1 - c2).together()) == 0 for c1, c2 in zip(inv.args, expected_inv.args)
    ), f"Expected inverse {expected_inv}, got {inv}"

    prod = q * inv
    assert trigsimp(prod.a.together()) == 1, f"Expected scalar part of q * q.inverse() to be 1, got {prod.a}"
    assert trigsimp(prod.b.together()) == 0, f"Expected b component of q * q.inverse() to be 0, got {prod.b}"
    assert trigsimp(prod.c.together()) == 0, f"Expected c component of q * q.inverse() to be 0, got {prod.c}"
    assert trigsimp(prod.d.together()) == 0, f"Expected d component of q * q.inverse() to be 0, got {prod.d}"


if __name__ == '__main__':
    main()
