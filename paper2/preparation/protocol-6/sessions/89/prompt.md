The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
Improving rational integration in manualintegrate
At the moment, rational integration in `manualintegrate` is rather inefficient. This is both because it is very slow (I will explain a possible solution below) and because there are not many methods available to integrate rational integrals. Sometimes `trig_substitution_rule` handles them, but it can only solve a subset of these integrals and often takes a long time. The point is that, at the moment, `partial_fractions_rule` splits the integral either into the form

```python
A / (a*x + b)**n
```

or into

```python
(A*x + B) / (a*x**2 + b*x + c)**n
```

The first family of integrals is correctly solved by substitution. The second only finds a solution for `n = 1` by rewriting the numerator in the standard calculus form.

Let $q(x) = a x^2 + b x + c$ and $q'(x) = 2ax + b$.

Then $Ax + B = \frac{A}{2a}(2ax+b) + \left(B-\frac{Ab}{2a}\right)$ so that $\frac{Ax+B}{q(x)^n} = \frac{A}{2a}\frac{q'(x)}{q(x)^n} + \left(B-\frac{Ab}{2a}\right)\frac{1}{q(x)^n}$

The first term can be solved by substitution. With $u = q(x)$ we have $\int \frac{q'(x)}{q(x)^n}\mathrm{d}x = -\frac{1}{(n-1)q(x)^{n-1}}$ for $n > 1$

The problem is that when `n > 1` the remaining term is not solved (case where n>1 is not handled in general by the actual rule). For example:

```python
In [33]: integrate(f, x, manual=True)
Out[33]:
⌠
⎮        1
⎮ ─────────────── dx
⎮               3
⎮ ⎛ 2          ⎞
⎮ ⎝x  + 4⋅x + 2⎠
⌡
```

This could however be solved easily.

Let $q(x) = ax^2 + bx + c$ and $\Delta = 4ac - b^2$

For $n > 1$,

$\frac{d}{dx}\left(\frac{2ax+b}{q(x)^{n-1}}\right) = \frac{(n-1)\Delta}{q(x)^n} - \frac{2a(2n-3)}{q(x)^{n-1}}$

If $\Delta \neq 0$ this gives

$\frac{1}{q(x)^n} = \frac{1}{(n-1)\Delta}\frac{d}{dx}\left(\frac{2ax+b}{q(x)^{n-1}}\right) + \frac{2a(2n-3)}{(n-1)\Delta}\frac{1}{q(x)^{n-1}}$

Therefore

$\int \frac{\mathrm{d}x}{q(x)^n} = \frac{2ax+b}{(n-1)\Delta q(x)^{n-1}} + \frac{2a(2n-3)}{(n-1)\Delta}\int\frac{\mathrm{d}x}{q(x)^{n-1}}$

This reduces the exponent from $n$ to $n-1$

If $\Delta = 0$ and $a \neq 0$ set $u = x + \frac{b}{2a}$. Then $q(x) = au^2$ and

$\int\frac{\mathrm{d}x}{q(x)^n} = \frac{1}{a^n}\int u^{-2n}\mathrm{d}u$

which is handled by the power rule.

While reading the code I also noticed that several `Piecewise` conditions are not correct. For example:

```python
In [43]: f = a/(b*x**2 + c*x + d)

In [44]: integrate(f, x, manual=True)
Out[44]:
      ⎛⎧             c                              ⎞
      ⎜⎪        x + ───                             ⎟
      ⎜⎪            2⋅b                    2        ⎟
      ⎜⎪       ──────────             for b  = 0    ⎟
      ⎜⎪                2                           ⎟
      ⎜⎪       4⋅b⋅d - c                            ⎟
      ⎜⎪                                            ⎟
      ⎜⎪          -1                           2    ⎟
      ⎜⎪     ──────────────       for 4⋅b⋅d - c  = 0⎟
      ⎜⎪        2 ⎛     c ⎞                         ⎟
      ⎜⎪     4⋅b ⋅⎜x + ───⎟                         ⎟
      ⎜⎪          ⎝    2⋅b⎠                         ⎟
      ⎜⎪                                            ⎟
      ⎜⎪    ⎛     ⎛     c ⎞    ⎞                    ⎟
4⋅a⋅b⋅⎜⎨atan⎜──────────────────⎟      otherwise     ⎟
      ⎜⎪    ⎜      ____________⎟                    ⎟
      ⎜⎪    ⎜     ╱          2 ⎟                    ⎟
      ⎜⎪    ⎜    ╱  4⋅b⋅d - c  ⎟                    ⎟
      ⎜⎪    ⎜   ╱   ────────── ⎟                    ⎟
      ⎜⎪    ⎜  ╱         2     ⎟                    ⎟
      ⎜⎪    ⎝╲╱         b      ⎠                    ⎟
      ⎝⎩                                            ⎠
```

There is a division by `b` in the denominator even in the branch where `b = 0`. In particular the substitution used in the second rule of `quadratic_denom_rule` is invalid for `b = 0`.

There are other similar issues that I will fix directly in the code.

Finally regarding rational integrals `expand_rule` and `cancel_rule` are almost always unnecessary. The cancellation of common factors that `cancel` could perform is already handled by `apart`.

The only other useful reason to use `expand` or `cancel` would be to help matching. For example:

```python
In [56]: pattern = a*x**2 + b

In [57]: f.match(pattern)
Out[57]: {a: 0, b: (x - 1)*(x + 1)}

In [58]: f.expand().match(pattern)
Out[58]: {a: 1, b: -1}
```

However when dealing with rational expressions we can simply use `Poly` on the numerator and denominator and extract the coefficients directly:

```python
In [69]: pol = Poly(f)

In [70]: pol
Out[70]: Poly(x**2 - 1, x, domain='ZZ')

In [71]: pol.nth(1)
Out[71]: 0

In [72]: pol.nth(2)
Out[72]: 1

```

This can save many unnecessary alternatives which often lead to the same result and are useless and computationally expensive. After some testing the integration speed improved very much for rationals.
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
