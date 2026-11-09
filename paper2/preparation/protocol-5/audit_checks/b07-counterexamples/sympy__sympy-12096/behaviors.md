1. A function with an implementation (`_imp_`) applied to another implemented function, such as f(g(2)), evaluates numerically with evalf to the composed value (16 for f(x)=x**2 and g(x)=2*x).
2. Deeper nesting also evaluates, for example f(f(g(1))) gives 16.
3. An implemented function applied to an expression that contains another implemented function, such as f(g(2) + 1), evaluates to 25.
4. Every argument is evaluated, not only the first one: h(g(1), g(2)) with h(x, y) = x*y gives 8.
5. The requested precision is honoured through the nesting: f(g(Rational(1, 3))).evalf(50) equals 4/9 to at least 45 digits.
6. Single level calls such as f(2).evalf() still give 4.
