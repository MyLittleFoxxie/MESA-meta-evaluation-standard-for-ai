The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
`swinnerton_dyer_poly` does not capture sympification of x
In the swinnerton_dyer_poly routine, the sympification of x is not captured:

```python
    if x is not None:
        sympify(x) <--------- should be x = sympify(x)
```
hence:
```python
>>> from sympy.polys.specialpolys import swinnerton_dyer_poly as f
>>> f(2,'x')
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

```
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
