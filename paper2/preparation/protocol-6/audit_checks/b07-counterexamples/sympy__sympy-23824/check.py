"""Verification check script for sympy__sympy-23824.

Issue: physics.hep.kahane_simplify() incorrectly reverses order of leading uncontracted gamma matrices.
"""

import sys
from sympy.matrices.dense import eye
from sympy.physics.hep.gamma_matrices import (
    GammaMatrix as G,
    LorentzIndex,
    kahane_simplify,
)
from sympy.tensor.tensor import tensor_indices


def test_kahane_simplify_leading_matrices():
    mu, nu, rho, sigma, tau = tensor_indices("mu, nu, rho, sigma, tau", LorentzIndex)
    a, b, c, d = tensor_indices("a, b, c, d", LorentzIndex)
    a1, a2, mu11, mu21, mu31 = tensor_indices("a1, a2, mu11, mu21, mu31", LorentzIndex)

    # 1. Behavior: Simplify contracted gamma products using gamma matrix identities
    # Adjacent contracted pair giving a factor of 4:
    t = G(mu) * G(-mu)
    r = kahane_simplify(t)
    assert r.equals(4 * eye(4)), f"Expected 4*eye(4), got {r}"

    # 2. Behavior: Both G(mu)*G(-mu)*G(rho)*G(sigma) and G(rho)*G(sigma)*G(mu)*G(-mu) must simplify to 4*G(rho)*G(sigma)
    t1 = G(mu) * G(-mu) * G(rho) * G(sigma)
    r1 = kahane_simplify(t1)
    assert r1.equals(4 * G(rho) * G(sigma)), f"Expected 4*G(rho)*G(sigma), got {r1}"

    t2 = G(rho) * G(sigma) * G(mu) * G(-mu)
    r2 = kahane_simplify(t2)
    assert r2.equals(4 * G(rho) * G(sigma)), f"Expected 4*G(rho)*G(sigma), got {r2}"

    # 3. Behavior: Preserve the order of every leading uncontracted gamma matrix
    # when simplifying the contracted remainder, for any number of leading matrices
    # 1 leading matrix:
    t = G(a) * G(mu) * G(-mu)
    r = kahane_simplify(t)
    assert r.equals(4 * G(a)), f"Expected 4*G(a), got {r}"

    # 2 leading matrices:
    t = G(a) * G(b) * G(mu) * G(-mu)
    r = kahane_simplify(t)
    assert r.equals(4 * G(a) * G(b)), f"Expected 4*G(a)*G(b), got {r}"

    # 3 leading matrices:
    t = G(a) * G(b) * G(c) * G(mu) * G(-mu)
    r = kahane_simplify(t)
    assert r.equals(4 * G(a) * G(b) * G(c)), f"Expected 4*G(a)*G(b)*G(c), got {r}"

    # 4 leading matrices:
    t = G(a) * G(b) * G(c) * G(d) * G(mu) * G(-mu)
    r = kahane_simplify(t)
    assert r.equals(4 * G(a) * G(b) * G(c) * G(d)), f"Expected 4*G(a)*G(b)*G(c)*G(d), got {r}"

    # Leading and trailing uncontracted matrices:
    t = G(rho) * G(sigma) * G(mu) * G(-mu) * G(tau)
    r = kahane_simplify(t)
    assert r.equals(4 * G(rho) * G(sigma) * G(tau)), f"Expected 4*G(rho)*G(sigma)*G(tau), got {r}"

    # 4. Behavior: Preserve that leading sequence on every resulting term,
    # including products with multiple contractions.
    # Multiple contractions collapsing to a scalar factor:
    t = G(a) * G(b) * G(mu) * G(nu) * G(-mu) * G(-nu)
    r = kahane_simplify(t)
    assert r.equals(-8 * G(a) * G(b)), f"Expected -8*G(a)*G(b), got {r}"

    t = G(a) * G(b) * G(c) * G(mu) * G(nu) * G(-mu) * G(-nu)
    r = kahane_simplify(t)
    assert r.equals(-8 * G(a) * G(b) * G(c)), f"Expected -8*G(a)*G(b)*G(c), got {r}"

    # Single contraction producing multiple terms with leading matrices:
    # G(mu)*G(nu)*G(rho)*G(-mu) simplifies to 2*G(nu)*G(rho) + 2*G(rho)*G(nu)
    t = G(a) * G(b) * G(mu) * G(nu) * G(rho) * G(-mu)
    r = kahane_simplify(t)
    expected = 2 * G(a) * G(b) * G(nu) * G(rho) + 2 * G(a) * G(b) * G(rho) * G(nu)
    assert r.equals(expected), f"Expected {expected}, got {r}"

    # Multiple contractions producing multiple terms with leading matrices:
    # G(a1)*G(mu11)*G(a2)*G(mu21)*G(-a1)*G(mu31)*G(-a2) simplifies to
    # -4*G(mu11)*G(mu31)*G(mu21) - 4*G(mu31)*G(mu11)*G(mu21)
    t = G(rho) * G(sigma) * G(a1) * G(mu11) * G(a2) * G(mu21) * G(-a1) * G(mu31) * G(-a2)
    r = kahane_simplify(t)
    expected = (
        -4 * G(rho) * G(sigma) * G(mu11) * G(mu31) * G(mu21)
        - 4 * G(rho) * G(sigma) * G(mu31) * G(mu11) * G(mu21)
    )
    assert r.equals(expected), f"Expected {expected}, got {r}"


def main():
    try:
        test_kahane_simplify_leading_matrices()
        print("All tests passed.")
        sys.exit(0)
    except AssertionError as e:
        print(f"Assertion failed: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
