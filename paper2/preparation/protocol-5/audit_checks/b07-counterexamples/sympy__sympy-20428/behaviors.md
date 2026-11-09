1. The polynomial returned by clear_denoms() on the issue's constant polynomial is the zero polynomial: is_zero is True and its representation has no stored zero coefficient (rep is [] as for Poly(0, x, domain='EX')).
2. A polynomial over the EX domain whose coefficient is that expression, also multiplied by x, is zero (is_zero True).
3. terms_gcd() on it returns ((0,), zero polynomial) instead of raising IndexError; primitive() returns a zero polynomial.
4. The EX domain element for that expression is false in a boolean test, while EX(sqrt(2)) and EX(x) stay true.
5. Other methods agree with the zero polynomial: degree is -oo, it equals Poly(0, x, domain='EX'), sqf_list() is (0, []), monic() does not raise ZeroDivisionError.
