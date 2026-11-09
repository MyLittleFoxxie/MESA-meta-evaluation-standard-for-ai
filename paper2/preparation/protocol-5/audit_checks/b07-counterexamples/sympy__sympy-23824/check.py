import sys
from sympy.physics.hep.gamma_matrices import GammaMatrix as G, LorentzIndex, kahane_simplify
from sympy.tensor.tensor import tensor_indices

a, b, c, mu, nu, rho, sigma = tensor_indices("a, b, c, mu, nu, rho, sigma", LorentzIndex)


def same(t, expected):
    try:
        r = kahane_simplify(t)
        return bool(r.equals(expected)) and str(r) == str(expected)
    except Exception:
        return False


tests = [
    (1, lambda: same(G(rho) * G(sigma) * G(mu) * G(-mu), 4 * G(rho) * G(sigma))),
    (2, lambda: same(G(mu) * G(-mu) * G(rho) * G(sigma), 4 * G(rho) * G(sigma))),
    (3, lambda: same(G(a) * G(b) * G(c) * G(mu) * G(-mu), 4 * G(a) * G(b) * G(c))),
    (4, lambda: same(G(a) * G(b) * G(mu) * G(nu) * G(-mu) * G(-nu), -8 * G(a) * G(b)) and
        same(G(a) * G(b) * G(mu) * G(nu) * G(-mu), -2 * G(a) * G(b) * G(nu))),
]
bad = [n for n, t in tests if not t()]
if bad:
    print("FAILED behaviors:", bad)
    sys.exit(1)
print("all behaviors hold")
