import sys
from sympy import Symbol, Rational, I, airyaiprime, besseli, N, im, Pow


def test_airyaiprime_rewrite_besseli_generic_orders():
    # Plain symbol with no assumptions (Re(z) > 0 is not known)
    z = Symbol('z')
    rw = airyaiprime(z).rewrite(besseli)

    # Behavior 1: Use Bessel I order -2/3, alongside +2/3, in generic formula
    bessel_calls = list(rw.atoms(besseli))
    assert len(bessel_calls) == 2, f"Expected 2 besseli calls, got {len(bessel_calls)}"
    bessel_orders = {b.args[0] for b in bessel_calls}
    expected_orders = {Rational(2, 3), Rational(-2, 3)}
    assert bessel_orders == expected_orders, (
        f"Expected orders {expected_orders}, got {bessel_orders}"
    )


def test_airyaiprime_rewrite_besseli_generic_formula():
    # Plain symbol with no assumptions
    z = Symbol('z')
    rw = airyaiprime(z).rewrite(besseli)

    ot = Rational(1, 3)
    tt = Rational(2, 3)
    a = Pow(z, Rational(3, 2))
    b = Pow(a, tt)
    c = Pow(a, -tt)
    expected_generic = ot * (z**2 * c * besseli(tt, tt * a) - b * besseli(-tt, tt * a))

    # Behavior 2: Apply correct generic formula to plain Symbol
    assert rw == expected_generic, f"Rewritten expression {rw} != expected {expected_generic}"


def test_airyaiprime_rewrite_besseli_numerical():
    z = Symbol('z')
    rw = airyaiprime(z).rewrite(besseli)

    # Behavior 3: Make rewritten expression agree numerically with airyaiprime,
    # including substitution at z = 1 and z = -1 (negative real must give correct real value)
    val_1 = N(rw.subs(z, 1))
    exp_1 = N(airyaiprime(1))
    assert abs(val_1 - exp_1) < 1e-12, (
        f"At z = 1: rewritten {val_1} != airyaiprime(1) {exp_1}"
    )

    val_neg1 = N(rw.subs(z, -1))
    exp_neg1 = N(airyaiprime(-1))
    assert abs(im(val_neg1)) < 1e-12, (
        f"At z = -1: expected real value, got imaginary part {im(val_neg1)}"
    )
    assert abs(val_neg1 - exp_neg1) < 1e-12, (
        f"At z = -1: rewritten {val_neg1} != airyaiprime(-1) {exp_neg1}"
    )

    # Test direct negative input rewrite
    rw_neg1 = airyaiprime(-1).rewrite(besseli)
    val_direct_neg1 = N(rw_neg1)
    assert abs(im(val_direct_neg1)) < 1e-12, (
        f"airyaiprime(-1).rewrite(besseli) imaginary part: {im(val_direct_neg1)}"
    )
    assert abs(val_direct_neg1 - exp_neg1) < 1e-12, (
        f"airyaiprime(-1).rewrite(besseli) {val_direct_neg1} != airyaiprime(-1) {exp_neg1}"
    )

    # Additional points to ensure general numerical agreement
    for pt in [2, -2, 1 + 2 * I, -1 + I]:
        v_rw = N(rw.subs(z, pt))
        v_ai = N(airyaiprime(pt))
        assert abs(v_rw - v_ai) < 1e-12, (
            f"At z = {pt}: rewritten {v_rw} != airyaiprime({pt}) {v_ai}"
        )


def test_airyaiprime_rewrite_besseli_positive_real():
    # Behavior 4: Preserve correct rewrite for inputs whose real part is known positive
    zp = Symbol('zp', positive=True)
    rw_pos = airyaiprime(zp).rewrite(besseli)

    tt = Rational(2, 3)
    a = tt * Pow(zp, Rational(3, 2))
    expected_pos = zp / 3 * (besseli(tt, a) - besseli(-tt, a))

    assert rw_pos == expected_pos, (
        f"Positive symbol rewrite {rw_pos} != expected {expected_pos}"
    )

    val_pos_1 = N(rw_pos.subs(zp, 1))
    exp_1 = N(airyaiprime(1))
    assert abs(val_pos_1 - exp_1) < 1e-12, (
        f"Positive symbol at zp = 1: {val_pos_1} != airyaiprime(1) {exp_1}"
    )


def main():
    test_airyaiprime_rewrite_besseli_generic_orders()
    test_airyaiprime_rewrite_besseli_generic_formula()
    test_airyaiprime_rewrite_besseli_numerical()
    test_airyaiprime_rewrite_besseli_positive_real()
    print("All tests passed.")
    sys.exit(0)


if __name__ == '__main__':
    main()
