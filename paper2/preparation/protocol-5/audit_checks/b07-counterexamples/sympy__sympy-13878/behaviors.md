1. `cdf(Arcsin("x", 0, 3))` gives the arcsin form 2*asin(sqrt(x/3))/pi inside the support (for example at 1), 0 below it and 1 above it, with no unevaluated Integral.
2. `cdf(Dagum("x", 1/3, 1/5, 2))` evaluates at 3 without hanging, to (1 + (x/2)**(-1/5))**(-1/3), and is 0 for negative x.
3. `cdf(Erlang(...))` is exact: for `Erlang("x", 1, 1)` at 1 it is 1 - exp(-1) with no floating point numbers in the result (also for `Erlang("x", 3, 2)`).
4. `cdf(Frechet("x", 4/3, 1, 2))` evaluates at 3 without hanging, to exp(-1), and is 0 below the location 2.
5. `cdf(Gamma(...))` is fully evaluated with the regularized lower incomplete gamma function (no Integral left): `Gamma("x", 0.1, 2)` at 3, and `Gamma("x", 2, 3)` at 1; it is 0 for negative x.
6. `cdf(GammaInverse("x", 5/7, 2))` evaluates at 3 without hanging, to the regularized upper incomplete gamma function of b/x, and is 0 for negative x.
7. `cdf(Kumaraswamy("x", 1/123, 5))` evaluates at 1/3 without hanging, to 1 - (1 - x**a)**b, and is 0 below 0 and 1 above 1.
8. `cdf(Laplace("x", 2, 3))` evaluates to the piecewise formula with no Integral: 1 - exp(-1)/2 at 5, exp(-2/3)/2 at 0.
9. `cdf(Logistic("x", 1, 0.1))` evaluates at 2 without an exception, to 1/(1 + exp(-(x - 1)/0.1)).
10. `cdf(Nakagami("x", 7/3, 1))` evaluates at 2 without hanging, to the regularized lower incomplete gamma function of mu*x**2/omega, and is 0 for negative x.
11. `cdf(StudentT("x", 10))` evaluates at 2 and at -2 without hanging, to the integral of the density.
12. `cdf(UniformSum("x", 5), evaluate=False)` (the form the documented example uses) evaluates at 2 without hanging, to 9/40, and is 0 below 0 and 1 above 5.
