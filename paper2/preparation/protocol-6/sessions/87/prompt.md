The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
asech derivative is wrong for x < -1
I found this issue with Claude testing the correctness of RUBI rules in my [integration test suites](https://github.com/asmeurer/integration-test-suites) repo.

SymPy's derivative for $$\mathrm{asech}(x)$$ is defined as $$\frac{-1}{x\sqrt{1-x^2}}$$. However, this derivative is only numerically correct for $$0 < x < 1$$ (https://en.wikipedia.org/wiki/Hyperbolic_functions#Derivatives). The derivative was originally implemented at https://github.com/sympy/sympy/pull/9291. 

To see this, consider the numerical derivative of `asech` as computed by mpmath at `-2`:

```py
>>> d = sympy.lambdify(x, sympy.diff(sympy.asech(x), x), 'mpmath')
>>> fn = lambda z: mpmath.asech(z)
>>> complex(d(mpmath.mpf(-2))), complex(mpmath.diff(fn, mpmath.mpf(-2)))
(-0.2886751345948129j, 0.28867513459481287j)
```

Note that mpmath defines `asech(x)` as `acosh(1/x)` https://github.com/mpmath/mpmath/blob/5fa2b9c7936c17f6d73beb5e9074ef64cb2cd0b5/mpmath/functions/functions.py#L108

You can also see that the symbolic derivative of `acosh(1/x)` is different:

```py
>>> pprint(diff(acosh(1/x)))
            -1
───────────────────────────
       ________     _______
 2    ╱      1     ╱     1
x ⋅  ╱  -1 + ─ ⋅  ╱  1 + ─
   ╲╱        x  ╲╱       x
>>> diff(acosh(1/x)).subs(x, -2)
sqrt(3)*I/6
>>> diff(asech(x)).subs(x, -2)
-sqrt(3)*I/6
```

We should change the symbolic derivative to either match this, or to use this formula from mathematica:

```
>>> pprint(-sqrt(1/(x + 1))/(x*sqrt(1 - x)))
     _______
    ╱   1
-  ╱  ─────
 ╲╱   x + 1
─────────────
     _______
 x⋅╲╱ 1 - x
```

(see https://functions.wolfram.com/ElementaryFunctions/ArcSech/20/01/). There's also this formula:

```
>>> pprint(-1/(x*sqrt((1 - x)/(x + 1))*(x + 1)))
         -1
─────────────────────
      _______
     ╱ 1 - x
x⋅  ╱  ───── ⋅(x + 1)
  ╲╱   x + 1
```

I'm not 100% sure these formula are all equivalent or correct so we should check that, and pick one to use.
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
