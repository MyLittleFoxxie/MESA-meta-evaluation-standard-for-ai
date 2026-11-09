import multiprocessing as mp
import sys

DEADLINE = 25


def _case(i):
    from mpmath import mp as M, mpf, gammainc, asin, sqrt as msqrt, exp as mexp, pi as mpi, quad, inf, gamma as mgamma, binomial, floor
    from sympy import Float, Integral, N, Rational as R, S
    from sympy.stats import cdf, Arcsin, Dagum, Erlang, Frechet, Gamma, GammaInverse, Kumaraswamy, Laplace, Logistic, \
        Nakagami, StudentT, UniformSum
    M.dps = 25

    def close(r, e):
        if hasattr(r, 'doit'):
            r = r.doit()
        if r.has(Integral):
            return False
        return abs(complex(N(r, 20)) - complex(e)) < 1e-8

    def at(dist, pts, **kw):
        f = cdf(dist, **kw)
        return all(close(f(p), e) for p, e in pts)

    if i == 1:
        g = lambda x: 0 if x < 0 else 1 if x > 3 else 2 / mpi * asin(msqrt(mpf(x) / 3))
        return at(Arcsin("x", 0, 3), [(1, g(1)), (-1, 0), (4, 1)])
    if i == 2:
        d = lambda x: 0 if x <= 0 else (1 + (mpf(x) / 2) ** (-mpf(1) / 5)) ** (-mpf(1) / 3)
        return at(Dagum("x", R(1, 3), R(1, 5), 2), [(3, d(3)), (-1, 0)])
    if i == 3:
        f1, f2 = cdf(Erlang("x", 1, 1)), cdf(Erlang("x", 3, 2))
        r1, r2 = f1(1), f2(1)
        return close(r1, 1 - mexp(-1)) and close(r2, gammainc(3, 0, 2, regularized=True)) and \
            not r1.has(Float) and not r2.has(Float) and close(f1(-1), 0)
    if i == 4:
        return at(Frechet("x", R(4, 3), 1, 2), [(3, mexp(-1)), (1, 0)])
    if i == 5:
        r = cdf(Gamma("x", 0.1, 2))
        r2 = cdf(Gamma("x", 2, 3))
        return close(r(3), gammainc(mpf('0.1'), 0, mpf(3) / 2, regularized=True)) and close(r(-1), 0) and \
            close(r2(1), gammainc(2, 0, mpf(1) / 3, regularized=True)) and close(r2(-1), 0)
    if i == 6:
        a, b = mpf(5) / 7, 2
        return at(GammaInverse("x", R(5, 7), 2), [(3, gammainc(a, mpf(b) / 3, inf, regularized=True)), (-1, 0)])
    if i == 7:
        a = mpf(1) / 123
        k = lambda x: 0 if x < 0 else 1 if x > 1 else 1 - (1 - mpf(x) ** a) ** 5
        return at(Kumaraswamy("x", R(1, 123), 5), [(R(1, 3), k(mpf(1) / 3)), (-1, 0), (2, 1)])
    if i == 8:
        return at(Laplace("x", 2, 3), [(5, 1 - mexp(-1) / 2), (0, mexp(-mpf(2) / 3) / 2), (2, mpf(1) / 2)])
    if i == 9:
        return at(Logistic("x", 1, R(1, 10)), [(2, 1 / (1 + mexp(-10))), (0, 1 / (1 + mexp(10)))])
    if i == 10:
        mu = mpf(7) / 3
        return at(Nakagami("x", R(7, 3), 1), [(2, gammainc(mu, 0, mu * 4, regularized=True)), (-1, 0)])
    if i == 11:
        nu = 10
        pdf = lambda t: mgamma(mpf(nu + 1) / 2) / (msqrt(nu * mpi) * mgamma(mpf(nu) / 2)) * (1 + t * t / nu) ** (-mpf(nu + 1) / 2)
        return at(StudentT("x", 10), [(2, quad(pdf, [-inf, 2])), (-2, quad(pdf, [-inf, -2]))])
    if i == 12:
        u = lambda x: 0 if x < 0 else 1 if x > 5 else sum((-1) ** k * binomial(5, k) * (mpf(x) - k) ** 5 for k in range(int(floor(mpf(x))) + 1)) / 120
        return at(UniformSum("x", 5), [(2, mpf(9) / 40), (-1, 0), (6, 1), (R(5, 2), u(mpf(5) / 2))], evaluate=False)


def _run(i):
    try:
        ok = _case(i)
    except Exception:
        ok = False
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    import time
    ps = {i: mp.Process(target=_run, args=(i,)) for i in range(1, 13)}
    for p in ps.values():
        p.start()
    end = time.time() + DEADLINE
    for p in ps.values():
        p.join(max(0, end - time.time()))
    bad = []
    for i, p in ps.items():
        if p.is_alive():
            p.terminate()
            bad.append(i)
        elif p.exitcode != 0:
            bad.append(i)
    if bad:
        print("FAILED behaviors:", bad)
        sys.exit(1)
    print("all behaviors hold")
