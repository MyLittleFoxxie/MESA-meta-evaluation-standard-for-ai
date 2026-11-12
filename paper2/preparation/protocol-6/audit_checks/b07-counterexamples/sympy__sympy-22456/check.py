"""
Verification script for sympy__sympy-22456.

Issue: Argument invariance of codegen.ast String
Currently, the codegen.ast String class does not support argument invariance like:
expr.func(*expr.args) == expr, but instead uses the invariance expr.func(**expr.kwargs()) == expr.
The former should hold for any Basic subclass, which String is.

Behaviors requested:
- Every codegen.ast String instance must satisfy expr.func(*expr.args) == expr,
  preserving its text for any valid string value.
- This Basic reconstruction rule also applies to String subclasses.
"""
import sys


def main():
    from sympy.codegen.ast import String, QuotedString, Comment

    test_strings = [
        "hello",
        "",
        "   ",
        "hello\nworld\t!",
        "with 'single' and \"double\" quotes",
        "special chars: \\ / $ # @ ! % ^ & * ( ) _ + - = ~ ` { } [ ] : ; < > , . ?",
        "unicode: \u03b1\u03b2\u03b3 \u03c0 \u221e \u222b",
        "long string: " + "abc" * 100,
    ]

    class CustomString(String):
        pass

    class CustomQuotedString(QuotedString):
        pass

    class CustomComment(Comment):
        pass

    classes_to_test = [
        String,
        QuotedString,
        Comment,
        CustomString,
        CustomQuotedString,
        CustomComment,
    ]

    for cls in classes_to_test:
        for val in test_strings:
            expr = cls(val)
            reconstructed = expr.func(*expr.args)

            # Reconstructed object must equal original
            assert reconstructed == expr, f"Failed equality for {cls.__name__}({val!r}): {reconstructed!r} != {expr!r}"

            # Text attribute must be preserved
            assert reconstructed.text == expr.text == val, (
                f"Failed text preservation for {cls.__name__}({val!r}): reconstructed.text={reconstructed.text!r}"
            )

            # Type must be preserved
            assert type(reconstructed) is type(expr), (
                f"Failed type preservation for {cls.__name__}({val!r}): {type(reconstructed)} is not {type(expr)}"
            )

    print("All checks passed successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
