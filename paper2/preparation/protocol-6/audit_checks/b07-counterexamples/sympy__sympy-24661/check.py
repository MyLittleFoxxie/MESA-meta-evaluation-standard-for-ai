import sys
from sympy.parsing.sympy_parser import parse_expr
from sympy import (
    Lt, Le, Gt, Ge, Eq, Ne,
    Add, And, Or, Tuple, Symbol, S, Integer, Float
)


def test_parse_expr_relational_evaluate_false():
    # 1. parse_expr(..., evaluate=False) must return an unevaluated relational
    # instead of a Boolean, including '1 < 2' as Lt(1, 2, evaluate=False).
    res = parse_expr('1 < 2', evaluate=False)
    assert isinstance(res, Lt), f"Expected Lt, got {type(res)}: {res!r}"
    assert res == Lt(1, 2, evaluate=False), f"Expected Lt(1, 2, evaluate=False), got {res!r}"
    assert res is not True and res is not S.true, f"Result evaluated to boolean True: {res!r}"
    assert res.lhs == Integer(1)
    assert res.rhs == Integer(2)

    # 2. Preserve comparison operator and operands for all 6 relationals,
    # without restricting the fix to particular numeric literals.
    cases = [
        ('1 < 2', Lt, Integer(1), Integer(2)),
        ('2 < 1', Lt, Integer(2), Integer(1)),
        ('1 <= 2', Le, Integer(1), Integer(2)),
        ('2 <= 1', Le, Integer(2), Integer(1)),
        ('2 > 1', Gt, Integer(2), Integer(1)),
        ('1 > 2', Gt, Integer(1), Integer(2)),
        ('2 >= 1', Ge, Integer(2), Integer(1)),
        ('1 >= 2', Ge, Integer(1), Integer(2)),
        ('1 == 1', Eq, Integer(1), Integer(1)),
        ('1 == 2', Eq, Integer(1), Integer(2)),
        ('1 != 2', Ne, Integer(1), Integer(2)),
        ('1 != 1', Ne, Integer(1), Integer(1)),
    ]
    for expr_str, expected_cls, expected_lhs, expected_rhs in cases:
        val = parse_expr(expr_str, evaluate=False)
        expected = expected_cls(expected_lhs, expected_rhs, evaluate=False)
        assert isinstance(val, expected_cls), f"For '{expr_str}', expected {expected_cls}, got {type(val)}: {val!r}"
        assert val == expected, f"For '{expr_str}', expected {expected!r}, got {val!r}"
        assert val.lhs == expected_lhs, f"For '{expr_str}', expected lhs {expected_lhs}, got {val.lhs}"
        assert val.rhs == expected_rhs, f"For '{expr_str}', expected rhs {expected_rhs}, got {val.rhs}"

    # Non-integer literals and symbols
    x = Symbol('x')
    y = Symbol('y')
    val_sym_eq = parse_expr('x == x', evaluate=False)
    assert isinstance(val_sym_eq, Eq)
    assert val_sym_eq == Eq(x, x, evaluate=False)
    assert val_sym_eq is not True and val_sym_eq is not S.true

    val_sym_lt = parse_expr('x < y', evaluate=False)
    assert isinstance(val_sym_lt, Lt)
    assert val_sym_lt == Lt(x, y, evaluate=False)

    val_float = parse_expr('1.5 <= 2.5', evaluate=False)
    assert isinstance(val_float, Le)
    assert val_float == Le(Float('1.5'), Float('2.5'), evaluate=False)

    # Compound operands
    val_compound = parse_expr('1 + 2 < 3 + 4', evaluate=False)
    assert isinstance(val_compound, Lt)
    assert val_compound.lhs == Add(1, 2, evaluate=False)
    assert val_compound.rhs == Add(3, 4, evaluate=False)

    # 3. Honor evaluate=False for nested relational expressions
    # Inside Tuple container
    val_tuple = parse_expr('Tuple(1 < 2, 3 > 4)', evaluate=False)
    assert isinstance(val_tuple, Tuple)
    assert isinstance(val_tuple[0], Lt)
    assert val_tuple[0] == Lt(1, 2, evaluate=False)
    assert isinstance(val_tuple[1], Gt)
    assert val_tuple[1] == Gt(3, 4, evaluate=False)

    # Inside logical And / Or expressions
    val_and = parse_expr('(1 < 2) & (3 > 4)', evaluate=False)
    assert isinstance(val_and, And)
    assert Lt(1, 2, evaluate=False) in val_and.args
    assert Gt(3, 4, evaluate=False) in val_and.args

    val_or = parse_expr('(1 == 2) | (3 <= 4)', evaluate=False)
    assert isinstance(val_or, Or)
    assert Eq(1, 2, evaluate=False) in val_or.args
    assert Le(3, 4, evaluate=False) in val_or.args

    # 4. Standard evaluate=True still works normally
    assert parse_expr('1 < 2') == S.true
    assert parse_expr('2 < 1') == S.false
    assert parse_expr('1 == 1') == S.true
    assert parse_expr('1 != 1') == S.false


if __name__ == '__main__':
    try:
        test_parse_expr_relational_evaluate_false()
        print("All tests passed successfully.")
        sys.exit(0)
    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
