The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
infinitesimals(): heuristics raise TypeError/KeyError/UnboundLocalError, and hint='default' and hint='all' abort instead of trying the next heuristic
```python
from sympy import Function, symbols, diff, exp
from sympy.solvers.ode.lie_group import infinitesimals

x, a, b, c = symbols('x a b c')
y = Function('y')(x)

# Kamke 1.117: even the default hint fails
infinitesimals(x*diff(y, x) - y - x - x*exp(y/x), y)
# TypeError: argument of type 'Mul' is not a container or iterable
#   lie_group.py:961 (lie_heuristic_abaco2_unique_general: `if x not in etaval`, etaval an expression)

# y' = 1 - y**2: the default hint works, 'all' fails
infinitesimals(diff(y, x) + y**2 - 1, y, hint='all')
# UnboundLocalError: cannot access local variable 'polyy' where it is not associated with a value
#   lie_group.py:535

# Kamke 1.382 (and Kamke 1.471 from the report above)
infinitesimals(diff(y, x)**2 + a*x*diff(y, x) - b*x**2 - c, y, hint='all')
# KeyError: C_
#   lie_group.py:768 (lie_heuristic_abaco2_similar: match[C] missing)
```

Each heuristic run on its own still finds generators for most of these equations, so the dispatcher could catch the failure of one heuristic and try the next. In a run over Kamke's first order equations (hint='all'): the `etaval` TypeError in 63 equations (4 more with 'Pow' instead of 'Mul'; 34 + 2 also with the default hint), KeyError C_ in 12, a `'NoneType' object is not subscriptable` TypeError in 7, the `polyy` UnboundLocalError in 3.
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
