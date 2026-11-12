The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
limit() raises NotImplementedError for expressions involving Min/Max
Ran into this while playing around with limits involving Min/Max — looks like the MRV computation in gruntz.py treats Min(f(x), g(x)) as a multi-arg function and just gives up:

from sympy import symbols, limit, Min, Max, exp, sin, oo
x = symbols('x', real=True)

limit(Min(x, x**2), x, 0)
# NotImplementedError: MRV set computation for functions in several variables not implemented.

limit(Max(x, sin(x)), x, 0)
# same error

limit(Min(exp(x), exp(2*x)), x, oo)
# same error

Tested this on live.sympy.org too, same result there.

This seems tied to the broader multi-arg MRV limitation that's come up in a few older issues, but specifically for Min/Max it looks pretty fixable — rewriting to Abs first works fine:

limit(Min(x, x**2).rewrite(Abs), x, 0)
# 0

Wondering if limit()/gruntz() could just do that rewrite automatically whenever it hits a Min or Max. Happy to dig into a fix if that sounds like the right direction.
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
