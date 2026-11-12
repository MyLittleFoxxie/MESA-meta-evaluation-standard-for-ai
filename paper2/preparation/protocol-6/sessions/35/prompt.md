The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
diophantine: incomplete results depending on syms order with permute=True
```
In [10]: diophantine(n**4 + m**4 - 2**4 - 3**4, syms=(m,n), permute=True)
Out[10]: {(-3, -2), (-3, 2), (-2, -3), (-2, 3), (2, -3), (2, 3), (3, -2), (3, 2)}

In [11]: diophantine(n**4 + m**4 - 2**4 - 3**4, syms=(n,m), permute=True)
Out[11]: {(3, 2)}
```

diophantine: incomplete results depending on syms order with permute=True
```
In [10]: diophantine(n**4 + m**4 - 2**4 - 3**4, syms=(m,n), permute=True)
Out[10]: {(-3, -2), (-3, 2), (-2, -3), (-2, 3), (2, -3), (2, 3), (3, -2), (3, 2)}

In [11]: diophantine(n**4 + m**4 - 2**4 - 3**4, syms=(n,m), permute=True)
Out[11]: {(3, 2)}
```
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
