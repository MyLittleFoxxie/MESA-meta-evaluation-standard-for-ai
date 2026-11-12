The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
airyaiprime(z).rewrite(besseli) uses the wrong Bessel order for generic z (-1/3 instead of -2/3)
While testing the Bessel-module rewrites numerically I noticed that the
generic branch of `airyaiprime._eval_rewrite_as_besseli` (taken when
`Re(z) > 0` is not known, e.g. for a plain `Symbol`) uses `besseli(-1/3, ...)`
where [DLMF 9.6.3](https://dlmf.nist.gov/9.6#E3)

$$\operatorname{Ai}'(z) = \frac{z}{3}\left(I_{2/3}(\zeta) - I_{-2/3}(\zeta)\right), \qquad \zeta = \tfrac{2}{3}z^{3/2}$$

requires `besseli(-2/3, ...)`. The rewrite therefore disagrees with
`airyaiprime` everywhere; for negative real input it even gives a complex
value:

```python
>>> from sympy import symbols, airyaiprime, besseli, N
>>> z = symbols('z')
>>> airyaiprime(z).rewrite(besseli)
z**2*besseli(2/3, 2*z**(3/2)/3)/(3*(z**(3/2))**(2/3)) - (z**(3/2))**(2/3)*besseli(-1/3, 2*z**(3/2)/3)/3
>>> N(airyaiprime(z).rewrite(besseli).subs(z, 1))
-0.226602029017611
>>> N(airyaiprime(1))
-0.159147441296793
>>> N(airyaiprime(z).rewrite(besseli).subs(z, -1))
-0.0919801823464775 + 0.148900951028358*I
>>> N(airyaiprime(-1))
-0.0101605671166452
```

It looks like an old typo (present since at least SymPy 1.0): the `Re(z) > 0`
branch and the counterpart `airybiprime` already use the correct order.
Changing `-1/3` to `-2/3` makes the rewrite agree with `airyaiprime` at all
points I tested. A pull request with the fix follows.
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
