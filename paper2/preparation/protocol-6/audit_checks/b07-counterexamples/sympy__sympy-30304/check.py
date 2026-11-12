#!/usr/bin/env python3
"""
Verification check for sympy__sympy-30304: Add SkewNormal distribution to sympy.stats.
"""
import sys


def main():
    try:
        from sympy.stats import SkewNormal, density, cdf, Normal
    except ImportError as e:
        print(f"FAILED: Could not import SkewNormal from sympy.stats: {e}")
        sys.exit(1)

    import sympy.stats
    from sympy.stats.crv_types import SkewNormalDistribution
    from sympy import Symbol, exp, erf, sqrt, pi, S, I, atan, Float, simplify
    from sympy.functions.special.error_functions import owens_t

    # 1. Verification of module export
    assert "SkewNormal" in sympy.stats.__all__, "SkewNormal must be in sympy.stats.__all__"

    # 2. Parameter validation
    # Scale parameter omega must be strictly positive (> 0)
    try:
        SkewNormal("X", 0, 0, 1)
        assert False, "Expected ValueError for omega = 0"
    except ValueError:
        pass

    try:
        SkewNormal("X", 0, -1, 1)
        assert False, "Expected ValueError for omega < 0"
    except ValueError:
        pass

    # Shape parameter alpha must be real
    try:
        SkewNormal("X", 0, 1, I)
        assert False, "Expected ValueError for non-real alpha"
    except ValueError:
        pass

    # Valid positive, negative, and zero alpha must be accepted
    X_pos = SkewNormal("X", 0, 1, 2)
    X_neg = SkewNormal("X", 0, 1, -2)
    X_zero = SkewNormal("X", 0, 1, 0)
    assert isinstance(X_pos.pspace.distribution, SkewNormalDistribution)
    assert isinstance(X_neg.pspace.distribution, SkewNormalDistribution)
    assert isinstance(X_zero.pspace.distribution, SkewNormalDistribution)

    # 3. PDF formula verification
    xi = Symbol("xi")
    omega = Symbol("omega", positive=True)
    alpha = Symbol("alpha")
    x = Symbol("x")

    X = SkewNormal("X", xi, omega, alpha)
    f = density(X)(x)
    z = (x - xi) / omega
    expected_f = exp(-z**2 / 2) * (1 + erf(alpha * z / sqrt(2))) / (sqrt(2 * pi) * omega)
    assert simplify(f - expected_f) == 0, f"PDF mismatch: {f} != {expected_f}"

    # 4. CDF formula verification
    F = cdf(X)(x)
    expected_F = erf(sqrt(2) * z / 2) / 2 + S.Half - 2 * owens_t(z, alpha)
    assert simplify(F - expected_F) == 0, f"CDF mismatch: {F} != {expected_F}"

    # 5. Reduction to Normal distribution when shape alpha == 0
    N = Normal("X", xi, omega)
    X_normal = SkewNormal("X", xi, omega, 0)
    assert density(X_normal)(x) == density(N)(x), "Density must reduce to Normal when alpha=0"
    assert simplify(cdf(X_normal)(x) - cdf(N)(x)) == 0, "CDF must reduce to Normal when alpha=0"

    # 6. Reflection identity: -X ~ SkewNormal(-xi, omega, -alpha)
    f_refl = density(SkewNormal("X", xi, omega, alpha))(-x)
    f_neg = density(SkewNormal("X", -xi, omega, -alpha))(x)
    assert simplify(f_refl - f_neg) == 0, "Reflection identity must hold"

    # 7. Numerical evaluations
    X_std = SkewNormal("X", 0, 1, 2)
    val_pdf_0 = density(X_std)(0).evalf()
    expected_pdf_0 = (1 / sqrt(2 * pi)).evalf()
    assert abs(val_pdf_0 - expected_pdf_0) < 1e-12, f"PDF at 0 mismatch: {val_pdf_0} vs {expected_pdf_0}"

    val_cdf_0 = cdf(X_std)(0).evalf()
    expected_cdf_0 = (S.Half - atan(2) / pi).evalf()
    assert abs(val_cdf_0 - expected_cdf_0) < 1e-12, f"CDF at 0 mismatch: {val_cdf_0} vs {expected_cdf_0}"

    # High-precision left-tail probability computation
    val_cdf_tail = cdf(X_std)(-6).evalf(50)
    expected_cdf_tail = Float("7.1180791900429369578422321160567160549025580712477e-43", 50)
    assert abs(val_cdf_tail - expected_cdf_tail) < Float("1e-55", 50), (
        f"Left-tail probability mismatch: {val_cdf_tail} vs {expected_cdf_tail}"
    )

    print("All SkewNormal verification checks passed successfully.")


if __name__ == "__main__":
    main()
