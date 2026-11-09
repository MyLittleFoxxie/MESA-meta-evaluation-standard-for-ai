1. Symbol('s') has no __dict__ attribute, and Symbol('s').__slots__ is ('name',).
2. Dummy and Wild instances have no __dict__.
3. Other core objects with slots have no __dict__ either: Basic(), Integer, Rational, Float, sums, products, powers, S.One, oo, pi, Eq, Poly.
4. A new subclass of Printable that declares __slots__ = () has no __dict__ (the Printable mixin does not add one).
