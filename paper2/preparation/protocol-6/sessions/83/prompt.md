The repository in this folder is SymPy at the commit where the issue below was open.

<issue>
Missing parentheses around Mod in generated code: `-2*Mod(p, q)` prints as `-2*p % q`
I hit this generating C from an expression containing `Mod` and it took a while to work out why
the numbers were wrong. The printers emit `Mod` as an infix `%` but don't always parenthesize it:

```python
>>> from sympy import symbols, Mod, ccode, jscode, lambdify
>>> from sympy.printing.pycode import pycode
>>> x, y = symbols('x y')
>>> p1, p2 = symbols('p1 p2', integer=True, positive=True)
>>> r = symbols('r', real=True)

>>> ccode(-2*Mod(p1, p2))
'-2*p1 % p2'
>>> jscode(-2*Mod(p1, p2))
'-2*p1 % p2'
>>> pycode(-2*Mod(x, 3), fully_qualified_modules=False)
'-2*x % 3'
>>> ccode(-p1/Mod(p1, p2))
'-p1/p1 % p2'
```

`%` has the same precedence as `*` and `/` and binds left to right in C, JS and Python, so these
parse as `(-2*p1) % p2` rather than `-2*(p1 % p2)`.

The obvious cases are all fine, which is why it doesn't look broken at first —
`ccode(2*Mod(p1, p2))` gives `'2*(p1 % p2)'` and `pycode(-Mod(x, 3))` gives `'-(x % 3)'`. It needs
a minus sign together with a second factor or a denominator.

Compiling what `ccode` gave me, with `p1 = 5`, `p2 = 3`: emitted `-2*p1 % p2` = `-1`, intended
`-2*(p1 % p2)` = `-4`. In one case it doesn't even compile — `ccode(r*Mod(p1, p2))` is fine and
there's a test for it, but with a minus in front you get `'-r*p1 % p2'`, and the `%` lands on a
double: `error: invalid operands to binary % (have 'double' and 'int')`.

`lambdify` is also wrong on the `math`/`mpmath`/`modules=[]` backends (NumPy is fine, it emits
`numpy.mod`):

```python
>>> lambdify(x, -2*Mod(x, 3), modules='math')(1)
1                                            # should be -2
>>> lambdify((x, y), -x*Mod(x, y), modules='math')(3, 7)
5                                            # should be -9
```

No warning in any of these. LaTeX, pretty, str, Octave, Julia, Maple and GLSL all get it right —
it's only the printers that emit a literal `%`.

## Where it comes from

`CodePrinter._print_Mul` (`sympy/printing/codeprinter.py` ~L550) works out the parenthesization
level from the signed `Mul`, then strips the sign and reuses that level on the factors:

```python
prec = precedence(expr)          # L552, computed on the signed Mul
c, e = expr.as_coeff_Mul()
if c < 0:
    expr = _keep_coeff(-c, e); sign = "-"
...
a_str = [self.parenthesize(x, prec) for x in a]    # L593
b_str = [self.parenthesize(x, prec) for x in b]    # L594
```

`precedence_Mul` returns `Add` (40) for anything that can pull out a minus sign, so a `Mod` factor
at 50 never trips the check:

```python
>>> from sympy.printing.precedence import precedence
>>> precedence(Mod(x, 3)), precedence(2*Mod(x, 3)), precedence(-2*Mod(x, 3))
(50, 50, 40)
```

The special case at L591 for `len(a) == 1 and sign == "-"` is why plain `-Mod(x, y)` works (that
went in for gh-17737); it just doesn't cover a second factor, and `b_str` uses the stale `prec`
regardless, so denominators slip through too.

I wondered whether gh-25026 already covered this, but its fix looks for a `Function` with a
`precedence` attribute *below* `Mul`, and `Mod` misses on both counts —
`hasattr(Mod(x, 3), 'precedence')` is `False` (it's in `PRECEDENCE_VALUES`, not a class attribute)
and its precedence is exactly 50, not below it.

## Fix

I think `_print_Mul` should parenthesize the factors at `PRECEDENCE["Mul"]` rather than
`precedence(signed_expr)`, since the sign has already been split off by that point — keeping the
existing unary-minus level for the single-factor branch. `precedence_Mul` only ever returns 40 or
50, so that can only add parentheses, and `Mod` is about the only thing it changes in practice.
`StrPrinter._print_Mul` has the same pattern, hidden there because `str` prints `Mod` as a function
call. Changing `precedence_Mul` itself would also affect `_print_Add` and `_print_Pow`, so the
local fix seemed safer.

There's a smaller related one worth doing at the same time — `_print_Mod` parenthesizes its args at
`Mul` level, but `1/y` reports `Pow` precedence (60) despite printing as a division:

```python
>>> pycode(Mod(1, 1/x), fully_qualified_modules=False)
'1 % 1/x'                                    # parses as (1 % 1)/x, i.e. 0
```

Only `exp == -1` is affected.

The existing tests happen to cover only the combinations that work (`-Mod(x, y)`, `r*Mod(p1, p2)`,
`x*Mod(p1, p2)` and similar) — nothing puts a minus sign together with another factor or a
denominator, which is presumably how it went unnoticed. Happy to put a PR together if this approach
sounds right.

On master @ 48b80f446e (1.15.0.dev), Python 3.12.10.
</issue>

Change the source code so that the issue is resolved. Hidden tests will check your change; you do not need to add
tests. Work only inside this folder and do not use the internet.
Limits: 15 minutes. Stop when you are done.
