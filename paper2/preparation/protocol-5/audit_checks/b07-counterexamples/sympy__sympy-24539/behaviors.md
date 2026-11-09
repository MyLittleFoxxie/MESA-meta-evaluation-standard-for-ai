1. PolyElement.as_expr(U, V, W) with the right number of symbols returns the polynomial written in those symbols (3*U**2*V - U*V*W + 7*W**3 + 1 for the example).
2. as_expr() without arguments still uses the ring's own symbols.
3. A wrong number of symbols, too few or too many, raises ValueError.
4. Symbols that are the ring's own symbols in another order are applied by position, not substituted one after another: f.as_expr(y, z, x) gives 3*y**2*z - y*z*x + 7*x**3 + 1.
5. Constant and zero polynomials accept symbols: R(5).as_expr(U, V, W) is 5 and R(0).as_expr(U, V, W) is 0.
