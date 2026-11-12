The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
The printer can crash with `Invalid NaN comparison` on expressions containing nan
```py
>>> from sympy import Function, nan
>>> f = Function('f')
>>> str(f(nan) + f(1))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/aaronmeurer/Documents/Python/sympy/sympy/sympy/core/_print_helpers.py", line 30, in __str__
    return sstr(self, order=None)
  File "/Users/aaronmeurer/Documents/Python/sympy/sympy/sympy/printing/printer.py", line 408, in __call__
    return self.__wrapped__(*args, **kwargs)
  File "/Users/aaronmeurer/Documents/Python/sympy/sympy/sympy/printing/str.py", line 1011, in sstr
    s = p.doprint(expr)
  File "/Users/aaronmeurer/Documents/Python/sympy/sympy/sympy/printing/printer.py", line 293, in doprint
    return self._str(self._print(expr))
  File "/Users/aaronmeurer/Documents/Python/sympy/sympy/sympy/printing/printer.py", line 332, in _print
    return printmethod(expr, **kwargs)
  File "/Users/aaronmeurer/Documents/Python/sympy/sympy/sympy/printing/str.py", line 58, in _print_Add
    terms = self._as_ordered_terms(expr, order=order)
  File "/Users/aaronmeurer/Documents/Python/sympy/sympy/sympy/printing/printer.py", line 350, in _as_ordered_terms
    return expr.as_ordered_terms(order=order)
  File "/Users/aaronmeurer/Documents/Python/sympy/sympy/sympy/core/expr.py", line 1212, in as_ordered_terms
    terms, gens = self.as_terms()
  File "/Users/aaronmeurer/Documents/Python/sympy/sympy/sympy/core/expr.py", line 1261, in as_terms
    gens = sorted(gens_set, key=default_sort_key)
  File "/Users/aaronmeurer/Documents/Python/sympy/sympy/sympy/core/numbers.py", line 2025, in __lt__
    return Rational.__lt__(self, other)
  File "/Users/aaronmeurer/Documents/Python/sympy/sympy/sympy/core/numbers.py", line 1678, in __lt__
    return Expr.__lt__(*rv)
  File "/Users/aaronmeurer/Documents/Python/sympy/sympy/sympy/core/decorators.py", line 249, in _func
    return func(self, other)
  File "/Users/aaronmeurer/Documents/Python/sympy/sympy/sympy/core/expr.py", line 417, in __lt__
    return StrictLessThan(self, other)
  File "/Users/aaronmeurer/Documents/Python/sympy/sympy/sympy/core/relational.py", line 881, in __new__
    raise TypeError("Invalid NaN comparison")
TypeError: Invalid NaN comparison
```

The cause as diagnosed by Claude:

> The root cause is one level deeper: default_sort_key is not a total order when nan is involved. The key tuple's last slot is the raw sympy Number — default_sort_key(nan) ends in nan, default_sort_key(S.One) ends in 1 — and when two keys tie on the leading slots, Python's tuple comparison falls through to nan < 1, which hits the deliberate TypeError("Invalid NaN comparison") in relational.py. So the failure needs nan inside two same-class subexpressions whose keys tie until the numeric slot (f(nan) + f(1), or two Piecewises as in the PR's output); a bare x + nan prints fine. Even list(ordered([nan, S.One])) crashes with no printer involved.
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
