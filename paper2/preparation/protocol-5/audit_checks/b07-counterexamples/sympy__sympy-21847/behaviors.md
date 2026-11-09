1. itermonomials([x1, x2, x3], 3, min_degrees=3) returns all ten monomials of total degree 3, including x1*x2**2, not only the pure cubes.
2. With min_degrees below max_degrees, for example variables x, y with max 4 and min 2, every monomial with 2 <= total degree <= 4 is returned (12 monomials) and none outside that range.
3. Without min_degrees the result is unchanged: all monomials up to the maximum degree.
4. The same holds for noncommutative symbols: a, b with max 2 and min 2 give a**2, a*b, b*a, b**2.
5. Per variable degree lists still work: variables x, y with max [2, 2] and min [1, 1] give the four monomials x*y, x**2*y, x*y**2, x**2*y**2.
6. min_degrees greater than max_degrees gives no monomials.
