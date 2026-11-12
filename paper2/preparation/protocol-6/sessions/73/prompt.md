The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
Poly(0, ...).lcm(Poly(0, ...)) result depends on backend
`DMP_Python.lcm(0, 0)` raises ZeroDivisionError, while other polynomial backends return the zero polynomial. 

This makes the result of `Poly(0, ...).lcm(Poly(0, ...))` depend on the selected ground-type backend. The discrepancy appears to come from the `DMP_Python LCM` path attempting a quotient involving `gcd(0, 0)` rather than handling a zero input as a special case.

See also [other differences](https://github.com/sympy/sympy/pull/30604#discussion_r4182401530).
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
