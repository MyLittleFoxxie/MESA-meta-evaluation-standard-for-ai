#!/usr/bin/env python3
"""
Verification script for sympy__sympy-13878:
Precompute the CDF of several continuous distributions where integration doesn't work well.
"""

import sys
import signal
from contextlib import contextmanager


class TimeoutException(Exception):
    pass


@contextmanager
def time_limit(seconds):
    if hasattr(signal, 'SIGALRM'):
        def signal_handler(signum, frame):
            raise TimeoutException(f"Timed out after {seconds} seconds")
        old_handler = signal.signal(signal.SIGALRM, signal_handler)
        signal.alarm(seconds)
        try:
            yield
        finally:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old_handler)
    else:
        yield


def main():
    from sympy import (
        S, Rational, Symbol, sqrt, pi, exp, asin,
        lowergamma, uppergamma, hyper, gamma, Integral,
        Float, N, simplify, Sum
    )
    from sympy.stats import (
        cdf, density, Arcsin, Dagum, Erlang, Frechet,
        Gamma, GammaInverse, Kumaraswamy, Laplace,
        Logistic, Nakagami, StudentT, UniformSum
    )

    z = Symbol('z')

    # 1. Arcsin
    # Issue: cdf(Arcsin("x", 0, 3))(1) returns unevaluated Integral
    with time_limit(10):
        X_arcsin = Arcsin("x", 0, 3)
        val = cdf(X_arcsin)(1)
        assert not val.has(Integral), f"Arcsin CDF has unevaluated Integral: {val}"
        expected = 2 * asin(sqrt(S(1) / 3)) / pi
        assert simplify(val - expected) == 0, f"Arcsin CDF mismatch: {val} != {expected}"

        # Outside support
        assert cdf(X_arcsin)(-1) == S.Zero, f"Arcsin CDF below support should be 0, got {cdf(X_arcsin)(-1)}"
        assert cdf(X_arcsin)(4) == S.One, f"Arcsin CDF above support should be 1, got {cdf(X_arcsin)(4)}"

        # Derivative agrees with PDF
        dF = cdf(X_arcsin)(z).diff(z)
        pdf = density(X_arcsin)(z)
        assert simplify(dF.subs(z, 1) - pdf.subs(z, 1)) == 0, "Arcsin CDF derivative != PDF"

    # 2. Dagum
    # Issue: cdf(Dagum("x", S(1)/3, S(1)/5, 2))(3) hangs
    with time_limit(10):
        X_dagum = Dagum("x", S(1)/3, S(1)/5, 2)
        val = cdf(X_dagum)(3)
        assert not val.has(Integral), f"Dagum CDF has unevaluated Integral: {val}"
        expected = (S.One + (S(3)/2)**(-S(1)/5))**(-S(1)/3)
        assert simplify(val - expected) == 0, f"Dagum CDF mismatch: {val} != {expected}"

        # Outside support
        assert cdf(X_dagum)(-1) == S.Zero, f"Dagum CDF below support should be 0, got {cdf(X_dagum)(-1)}"

        # Derivative agrees with PDF
        dF = cdf(X_dagum)(z).diff(z)
        pdf = density(X_dagum)(z)
        assert abs(N(dF.subs(z, 3)) - N(pdf.subs(z, 3))) < 1e-10, "Dagum CDF derivative != PDF"

    # 3. Erlang
    # Issue: cdf(Erlang("x", 1, 1))(1) returns float instead of exact expression
    with time_limit(10):
        X_erlang = Erlang("x", 1, 1)
        val = cdf(X_erlang)(1)
        assert not val.has(Integral), f"Erlang CDF has unevaluated Integral: {val}"
        assert not val.has(Float) and not isinstance(val, float), f"Erlang CDF returned float: {val}"
        expected = 1 - exp(-1)
        assert simplify(val - expected) == 0, f"Erlang CDF mismatch: {val} != {expected}"

        # Derivative agrees with PDF
        dF = cdf(X_erlang)(z).diff(z)
        pdf = density(X_erlang)(z)
        assert simplify(dF.subs(z, 1) - pdf.subs(z, 1)) == 0, "Erlang CDF derivative != PDF"

    # 4. Frechet
    # Issue: cdf(Frechet("x", S(4)/3, 1, 2))(3) hangs
    with time_limit(10):
        X_frechet = Frechet("x", S(4)/3, 1, 2)
        val = cdf(X_frechet)(3)
        assert not val.has(Integral), f"Frechet CDF has unevaluated Integral: {val}"
        expected = exp(-1)
        assert simplify(val - expected) == 0, f"Frechet CDF mismatch: {val} != {expected}"

        # Outside support
        assert cdf(X_frechet)(1) == S.Zero, f"Frechet CDF below support should be 0, got {cdf(X_frechet)(1)}"

        # Derivative agrees with PDF
        dF = cdf(X_frechet)(z).diff(z)
        pdf = density(X_frechet)(z)
        assert simplify(dF.subs(z, 3) - pdf.subs(z, 3)) == 0, "Frechet CDF derivative != PDF"

    # 5. Gamma
    # Issue: cdf(Gamma("x", 0.1, 2))(3) leaves unevaluated integral
    with time_limit(10):
        X_gamma = Gamma("x", 0.1, 2)
        val = cdf(X_gamma)(3)
        assert not val.has(Integral), f"Gamma CDF has unevaluated Integral: {val}"
        assert val.has(lowergamma), f"Gamma CDF should use lowergamma: {val}"
        expected = lowergamma(0.1, S(3)/2) / gamma(0.1)
        assert simplify(val - expected) == 0, f"Gamma CDF mismatch: {val} != {expected}"

        # Derivative agrees with PDF
        X_gamma_exact = Gamma("x", 2, 3)
        dF = cdf(X_gamma_exact)(z).diff(z)
        pdf = density(X_gamma_exact)(z)
        assert simplify(dF.subs(z, 2) - pdf.subs(z, 2)) == 0, "Gamma CDF derivative != PDF"

    # 6. GammaInverse
    # Issue: cdf(GammaInverse("x", S(5)/7, 2))(3) hangs
    with time_limit(10):
        X_gammainv = GammaInverse("x", S(5)/7, 2)
        val = cdf(X_gammainv)(3)
        assert not val.has(Integral), f"GammaInverse CDF has unevaluated Integral: {val}"
        assert val.has(uppergamma), f"GammaInverse CDF should use uppergamma: {val}"
        expected = uppergamma(S(5)/7, S(2)/3) / gamma(S(5)/7)
        assert simplify(val - expected) == 0, f"GammaInverse CDF mismatch: {val} != {expected}"

        # Outside support
        assert cdf(X_gammainv)(-1) == S.Zero, f"GammaInverse CDF below support should be 0, got {cdf(X_gammainv)(-1)}"

        # Derivative agrees with PDF
        dF = cdf(X_gammainv)(z).diff(z)
        pdf = density(X_gammainv)(z)
        assert simplify(dF.subs(z, 3) - pdf.subs(z, 3)) == 0, "GammaInverse CDF derivative != PDF"

    # 7. Kumaraswamy
    # Issue: cdf(Kumaraswamy("x", S(1)/123, 5))(S(1)/3) hangs
    with time_limit(10):
        X_kumar = Kumaraswamy("x", S(1)/123, 5)
        val = cdf(X_kumar)(S(1)/3)
        assert not val.has(Integral), f"Kumaraswamy CDF has unevaluated Integral: {val}"
        expected = 1 - (1 - (S(1)/3)**(S(1)/123))**5
        assert simplify(val - expected) == 0, f"Kumaraswamy CDF mismatch: {val} != {expected}"

        # Outside support
        assert cdf(X_kumar)(-1) == S.Zero, f"Kumaraswamy CDF below support should be 0, got {cdf(X_kumar)(-1)}"
        assert cdf(X_kumar)(2) == S.One, f"Kumaraswamy CDF above support should be 1, got {cdf(X_kumar)(2)}"

        # Derivative agrees with PDF
        dF = cdf(X_kumar)(z).diff(z)
        pdf = density(X_kumar)(z)
        assert simplify(dF.subs(z, S(1)/3) - pdf.subs(z, S(1)/3)) == 0, "Kumaraswamy CDF derivative != PDF"

    # 8. Laplace
    # Issue: cdf(Laplace("x", 2, 3))(5) returns unevaluated Integral
    with time_limit(10):
        X_laplace = Laplace("x", 2, 3)
        val = cdf(X_laplace)(5)
        assert not val.has(Integral), f"Laplace CDF has unevaluated Integral: {val}"
        expected = 1 - S.Half * exp(-1)
        assert simplify(val - expected) == 0, f"Laplace CDF mismatch: {val} != {expected}"

        # Left piece (x < mu)
        val_left = cdf(X_laplace)(-1)
        expected_left = S.Half * exp(-1)
        assert simplify(val_left - expected_left) == 0, f"Laplace CDF left piece mismatch: {val_left} != {expected_left}"

        # Derivative agrees with PDF
        dF = cdf(X_laplace)(z).diff(z)
        pdf = density(X_laplace)(z)
        assert simplify(dF.subs(z, 5) - pdf.subs(z, 5)) == 0, "Laplace CDF derivative != PDF"
        assert simplify(dF.subs(z, 0) - pdf.subs(z, 0)) == 0, "Laplace CDF derivative != PDF"

    # 9. Logistic
    # Issue: cdf(Logistic("x", 1, 0.1))(2) throws an exception
    with time_limit(10):
        X_logistic = Logistic("x", 1, 0.1)
        val = cdf(X_logistic)(2)
        assert not val.has(Integral), f"Logistic CDF has unevaluated Integral: {val}"
        expected = 1 / (1 + exp(-10))
        assert abs(N(val) - N(expected)) < 1e-10, f"Logistic CDF mismatch: {val} != {expected}"

        # Derivative agrees with PDF
        dF = cdf(X_logistic)(z).diff(z)
        pdf = density(X_logistic)(z)
        assert abs(N(dF.subs(z, 2)) - N(pdf.subs(z, 2))) < 1e-10, "Logistic CDF derivative != PDF"

    # 10. Nakagami
    # Issue: cdf(Nakagami("x", S(7)/3, 1))(2) hangs
    with time_limit(10):
        X_nakagami = Nakagami("x", S(7)/3, 1)
        val = cdf(X_nakagami)(2)
        assert not val.has(Integral), f"Nakagami CDF has unevaluated Integral: {val}"
        assert val.has(lowergamma), f"Nakagami CDF should use lowergamma: {val}"
        expected = lowergamma(S(7)/3, S(28)/3) / gamma(S(7)/3)
        assert simplify(val - expected) == 0, f"Nakagami CDF mismatch: {val} != {expected}"

        # Outside support
        assert cdf(X_nakagami)(-1) == S.Zero, f"Nakagami CDF below support should be 0, got {cdf(X_nakagami)(-1)}"

        # Derivative agrees with PDF
        dF = cdf(X_nakagami)(z).diff(z)
        pdf = density(X_nakagami)(z)
        assert simplify(dF.subs(z, 2) - pdf.subs(z, 2)) == 0, "Nakagami CDF derivative != PDF"

    # 11. StudentT
    # Issue: cdf(StudentT("x", 10))(2) hangs
    with time_limit(10):
        X_studentt = StudentT("x", 10)
        val = cdf(X_studentt)(2)
        assert not val.has(Integral), f"StudentT CDF has unevaluated Integral: {val}"
        assert val.has(hyper), f"StudentT CDF should use hyper: {val}"
        expected = S.Half + 2 * gamma(S(11)/2) * hyper((S.Half, S(11)/2), (S(3)/2,), -S(4)/10) / (sqrt(10*pi) * gamma(5))
        assert simplify(val - expected) == 0, f"StudentT CDF mismatch: {val} != {expected}"

        # Derivative agrees with PDF
        dF = cdf(X_studentt)(z).diff(z)
        pdf = density(X_studentt)(z)
        assert abs(N(dF.subs(z, 2)) - N(pdf.subs(z, 2))) < 1e-10, "StudentT CDF derivative != PDF"

    # 12. UniformSum
    # Issue: cdf(UniformSum("x", 5))(2) hangs
    with time_limit(10):
        X_unisum = UniformSum("x", 5)
        val = cdf(X_unisum)(2)
        assert not val.has(Integral), f"UniformSum CDF has unevaluated Integral: {val}"
        assert val.has(Sum), f"UniformSum CDF should use Sum: {val}"
        assert val.doit() == Rational(9, 40), f"UniformSum CDF doit() mismatch: {val.doit()} != 9/40"

        # evaluate=False mode
        val_uneval = cdf(X_unisum, evaluate=False)(2)
        assert val_uneval.doit() == Rational(9, 40), f"UniformSum evaluate=False doit() mismatch: {val_uneval.doit()} != 9/40"

        # Outside support
        assert cdf(X_unisum)(-1) == S.Zero, f"UniformSum CDF below support should be 0, got {cdf(X_unisum)(-1)}"
        assert cdf(X_unisum)(6) == S.One, f"UniformSum CDF above support should be 1, got {cdf(X_unisum)(6)}"

    print("All tests passed.")
    sys.exit(0)


if __name__ == '__main__':
    main()
