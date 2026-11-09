1. `symbols(('q:2', 'u:2'), cls=Function)` returns two tuples, and every item is an undefined function (not a Symbol), named q0, q1, u0, u1.
2. The same holds when the outer container is a list: the result is a list of the same kind of items.
3. The same holds when the containers are nested more than once.
4. The `cls` argument is passed on for other classes as well (for example `Dummy`), not only for `Function`.
5. Without `cls`, a container of names still gives Symbols, and other keyword arguments (for example `real=True`) still reach them.
