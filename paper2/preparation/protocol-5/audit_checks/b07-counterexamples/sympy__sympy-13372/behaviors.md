1. `Mul(Max(0, y), x, evaluate=False).evalf()` returns `x*Max(0, y)` and does not raise `UnboundLocalError`, the same result as with the arguments in the other order.
2. The order of arguments does not matter for other unevaluated sums and products with a `Max` term: `Add(Max(0, y), x, evaluate=False)` and `Mul(Max(0, y), Max(1, x), evaluate=False)` evaluate without an error and keep the `Max` terms.
3. Numeric factors are still evaluated next to a `Max` term: `Mul(Max(0, y), 2, evaluate=False).evalf()` is `2.0*Max(0, y)`.
4. Substituting values still gives numbers: `Mul(Max(0, y), x, evaluate=False).evalf(subs={x: 2, y: 3})` is 6.0, and a partial substitution keeps the other `Max` term without an error.
5. A product with a factor whose real part is zero and whose imaginary part is not a number (real symbols, factor `polar_lift(I*Max(0, yr))`) also evaluates, in both orders, without `UnboundLocalError`.
