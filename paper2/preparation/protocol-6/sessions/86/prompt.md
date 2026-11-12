The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
acot(-x) and acoth(-x) evaluate to -acot(x) and -acoth(x), which is wrong at x = 0
`acot(-x).subs(x, 0)` should be equal to `acot(0)`. Same with `acoth(-x).subs(x, 0)` and `acoth(0)`.

```python
>>> from sympy import symbols, acot, acoth
>>> x = symbols('x')
>>> acot(-x)
-acot(x)
>>> acot(-x).subs(x, 0), acot(0)
(-pi/2, pi/2)
>>> acoth(-x)
-acoth(x)
>>> acoth(-x).subs(x, 0), acoth(0)
(-I*pi/2, I*pi/2)
```
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
