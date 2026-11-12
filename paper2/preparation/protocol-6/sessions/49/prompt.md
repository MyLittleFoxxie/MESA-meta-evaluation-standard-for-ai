The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
Landau order term doesn't update correctly when part of an expression and x0!=0
Minimal example:

```py
x=symbols('x')
err=O((x-5)**3,(x,5))
((err+1)*(x-5)).expand() # error term stays O((x-5)**3) when it should be O((x-5)**4)
```

The scaling seems to work when it's not part of an expression. It also seems to work when part of an expression for x0=0. It also seems to properly scale for division instead of multiplication.

sympy version: 1.14.0
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
