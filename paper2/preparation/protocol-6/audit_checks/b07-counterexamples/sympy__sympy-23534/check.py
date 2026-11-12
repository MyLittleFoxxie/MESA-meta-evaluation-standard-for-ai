import sys
from sympy import symbols, Function
from sympy.core.function import UndefinedFunction


def test_symbols_with_tuple_and_cls():
    # Issue: Using symbols with cls=Function and names wrapped in an outer tuple
    # q, u = smp.symbols(('q:2', 'u:2'), cls=smp.Function)
    res = symbols(('q:2', 'u:2'), cls=Function)

    # symbols must honor cls=Function when names are wrapped in an outer tuple
    # and return two separate tuples
    assert isinstance(res, tuple), f"Expected outer result to be tuple, got {type(res)}"
    assert len(res) == 2, f"Expected 2 elements in outer tuple, got {len(res)}"

    q, u = res
    # q, u must be two separate tuples, each containing two functions
    assert isinstance(q, tuple), f"Expected q to be tuple, got {type(q)}"
    assert isinstance(u, tuple), f"Expected u to be tuple, got {type(u)}"
    assert len(q) == 2, f"Expected q to have 2 elements, got {len(q)}"
    assert len(u) == 2, f"Expected u to have 2 elements, got {len(u)}"

    # The functions must keep the requested names: q0, q1, u0, and u1
    assert q[0].name == 'q0', f"Expected q[0].name == 'q0', got {getattr(q[0], 'name', None)}"
    assert q[1].name == 'q1', f"Expected q[1].name == 'q1', got {getattr(q[1], 'name', None)}"
    assert u[0].name == 'u0', f"Expected u[0].name == 'u0', got {getattr(u[0], 'name', None)}"
    assert u[1].name == 'u1', f"Expected u[1].name == 'u1', got {getattr(u[1], 'name', None)}"

    # Every object in both tuples must be an UndefinedFunction, including q[0]
    for i, func in enumerate(q):
        assert isinstance(func, UndefinedFunction), (
            f"Expected q[{i}] to be UndefinedFunction, got {type(func)}"
        )
    for i, func in enumerate(u):
        assert isinstance(func, UndefinedFunction), (
            f"Expected u[{i}] to be UndefinedFunction, got {type(func)}"
        )


def main():
    test_symbols_with_tuple_and_cls()
    print("All assertions passed.")
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"Assertion failed: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)
