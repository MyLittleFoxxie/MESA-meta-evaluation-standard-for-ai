1. `kahane_simplify(G(rho)*G(sigma)*G(mu)*G(-mu))` equals `4*G(rho)*G(sigma)`: leading matrices without contractions keep their order.
2. `kahane_simplify(G(mu)*G(-mu)*G(rho)*G(sigma))` still equals `4*G(rho)*G(sigma)`.
3. With three leading matrices, `G(a)*G(b)*G(c)*G(mu)*G(-mu)` gives `4*G(a)*G(b)*G(c)`.
4. Leading matrices keep their order when the contracted part has other contractions: `G(a)*G(b)*G(mu)*G(nu)*G(-mu)*G(-nu)` gives `-8*G(a)*G(b)`, and `G(a)*G(b)*G(mu)*G(nu)*G(-mu)` gives `-2*G(a)*G(b)*G(nu)`.
