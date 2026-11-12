The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
owens_t(h, a).evalf() breaks Add cancellation, giving wrong sign/magnitude in differences
`owens_t(h, a).evalf()` returns an unevaluated `Float * Integral` rather than a plain `Float`:

```pycon
>>> from sympy.functions.special.error_functions import owens_t
>>> owens_t(1, 2).evalf()
0.164611992413795  # this one is fine
```

The problem shows up when `owens_t` is added to (or subtracted from) another term whose value is close in magnitude, and the correct result is their small difference. `evalf`'s `Add` handler raises precision on each term until the cancellation resolves, but that only works if every term in the sum is a genuine `Float`. Because `owens_t`'s term stays frozen (see below), the whole expression comes out with only the default ~53 bits, so a tiny true value prints with the wrong order of magnitude, or even the wrong sign:

```pycon
>>> from sympy import erf, sqrt, S
>>> h, a = -6, 2
>>> expr = erf(sqrt(2)*h/2)/2 + S.Half - 2*owens_t(h, a)
>>> expr.evalf()
-1.24370024995070e-19
>>> expr.evalf(50)
7.1180791900429369578422321160567160549025580712477e-43
```

At the default precision the sign is wrong and the magnitude is off by 24 orders of magnitude. Raising the precision by hand (`evalf(50)`) does eventually recover the right answer, so the quadrature itself isn't the issue.

I ran into this because I monkeypatched `owens_t._eval_evalf` to return a real `Float` and the standard `Add` cancellation machinery then handled the 50+ digit cancellation above with no explicit `evalf(N)` needed, which points at `_eval_evalf` returning something evalf's `Add` handler can't use, rather than at the underlying integral.

### Where this comes from

`owens_t` was added in #30143. `sympy.stats` now has a public consumer of it: `SkewNormal`'s `cdf` is `Phi(z) - 2*owens_t(z, alpha)` (#30304), so this now surfaces to anyone computing a left-tail probability, e.g.:

```pycon
>>> from sympy.stats import SkewNormal, cdf
>>> cdf(SkewNormal('x', 0, 1, 2))(-6).evalf()
-1.24370024995070e-19   # true value: 7.118e-43
```
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
