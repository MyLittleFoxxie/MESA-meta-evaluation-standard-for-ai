The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
ask(Q.eq(x, y), Q.negative_infinite(x) & Q.extended_nonpositive(y)) returns True instead of None
```python
>>> from sympy import symbols, ask, Q
>>> x, y = symbols('x y')
>>> print(ask(Q.eq(x, y), Q.negative_infinite(x) & Q.extended_nonpositive(y)))
True
```
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
