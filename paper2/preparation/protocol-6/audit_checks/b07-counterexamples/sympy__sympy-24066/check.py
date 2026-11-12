"""
Verification test for sympy__sympy-24066:
SI._collect_factor_and_dimension() cannot properly detect that exponent is dimensionless
"""

import sys


def test_dimensionless_function_argument():
    from sympy import exp, E
    from sympy.physics import units
    from sympy.physics.units.dimensions import Dimension
    from sympy.physics.units.systems.si import SI

    # 1. Recognize that second / (ohm * farad) has a dimensionless dimension in SI.
    expr = units.second / (units.ohm * units.farad)
    factor, dim = SI._collect_factor_and_dimension(expr)
    assert factor == 1, f"Expected factor 1, got {factor}"
    assert SI.get_dimension_system().is_dimensionless(dim), (
        f"Expected {dim} to be recognized as dimensionless in SI"
    )

    # 2. Factor and dimension of exp(second / (ohm * farad))
    exp_factor, exp_dim = SI._collect_factor_and_dimension(exp(expr))
    assert exp_factor == E, f"Expected exp_factor E, got {exp_factor}"
    assert exp_dim == Dimension(1), f"Expected exp_dim Dimension(1), got {exp_dim}"

    # 3. Collect factor and dimension of 100 + exp(second / (ohm * farad)) without ValueError
    buggy_expr = 100 + exp(expr)
    add_factor, add_dim = SI._collect_factor_and_dimension(buggy_expr)
    assert add_factor == 100 + E, f"Expected add_factor 100 + E, got {add_factor}"
    assert add_dim == Dimension(1), f"Expected add_dim Dimension(1), got {add_dim}"


if __name__ == "__main__":
    try:
        test_dimensionless_function_argument()
        print("All tests passed.")
        sys.exit(0)
    except Exception:
        import traceback
        traceback.print_exc()
        sys.exit(1)
