The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
integrate exp(-x^2)*erf(ax)
SymPy:

```python
In [1]: integrate(exp(-x**2)*erf(y*x), x)
Out[1]: 
⌠                 
⎮    2            
⎮  -x             
⎮ ℯ   ⋅erf(x⋅y) dx
⌡                 

In [2]: integrate(exp(-x**2)*erf(n*x), x)
Out[2]: 
⌠                 
⎮    2            
⎮  -x             
⎮ ℯ   ⋅erf(n⋅x) dx
⌡                 
```

Wolfram Alpha:

<img width="1040" height="300" alt="Image" src="https://github.com/user-attachments/assets/ef809ce9-e828-4db3-a068-54193671c444" />

Currently, Owen T function is not supported in sympy, so it will need to be implemented first before this integral is tackled.
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
