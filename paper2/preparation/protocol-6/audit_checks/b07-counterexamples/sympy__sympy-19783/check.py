import sys
from sympy.physics.quantum.dagger import Dagger
from sympy.physics.quantum.operator import Operator, IdentityOperator


def main():
    A = Operator('A')
    Identity = IdentityOperator()

    # Multiplying an operator by IdentityOperator() on the right returns that operator.
    mul_op_right = A * Identity
    assert mul_op_right == A, f"Expected {A}, got {mul_op_right}"

    # Multiplying an operator by IdentityOperator() on the left returns that operator.
    mul_op_left = Identity * A
    assert mul_op_left == A, f"Expected {A}, got {mul_op_left}"

    # Multiplying Dagger(A) by IdentityOperator() on the right returns Dagger(A).
    B = Dagger(A)
    mul_dagger_right = B * Identity
    assert mul_dagger_right == B, f"Expected {B}, got {mul_dagger_right}"

    # Multiplying Dagger(A) by IdentityOperator() on the left returns Dagger(A).
    mul_dagger_left = Identity * B
    assert mul_dagger_left == B, f"Expected {B}, got {mul_dagger_left}"

    # Additional test with another operator
    C = Operator('C')
    assert Dagger(C) * Identity == Dagger(C), f"Expected {Dagger(C)}, got {Dagger(C) * Identity}"
    assert Identity * Dagger(C) == Dagger(C), f"Expected {Dagger(C)}, got {Identity * Dagger(C)}"

    print("All tests passed.")


if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except AssertionError as e:
        print(f"Assertion failed: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
