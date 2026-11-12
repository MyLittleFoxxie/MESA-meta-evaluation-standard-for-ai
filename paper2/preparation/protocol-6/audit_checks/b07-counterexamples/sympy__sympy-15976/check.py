#!/usr/bin/env python3
"""
Verification check for sympy__sympy-15976.
Issue: Symbols ending with a number (e.g. x1, x2) or having sub/superscripts
are wrapped in an invalid <mi> tag when printing presentation MathML, causing
them to be rendered invisible or broken in MathML renderers like Safari.
"""

import sys
import sympy
from sympy import Symbol, MatrixSymbol, symbols
from sympy.printing.mathml import mathml, MathMLPresentationPrinter


def test_symbol_ending_with_number():
    # Symbols ending in digits, such as x2, must produce valid MathML presentation elements
    # (i.e. <msub>, NOT wrapped in an invalid <mi> tag).
    x2 = Symbol('x2')
    res_x2 = mathml(x2, printer='presentation')
    assert '<mi><msub>' not in res_x2, (
        f"Invalid MathML: <msub> nested inside <mi> in {res_x2}"
    )
    assert res_x2 == '<msub><mi>x</mi><mi>2</mi></msub>', (
        f"Expected '<msub><mi>x</mi><mi>2</mi></msub>', got '{res_x2}'"
    )

    x1 = Symbol('x1')
    res_x1 = mathml(x1, printer='presentation')
    assert res_x1 == '<msub><mi>x</mi><mi>1</mi></msub>', (
        f"Expected '<msub><mi>x</mi><mi>1</mi></msub>', got '{res_x1}'"
    )

    a0 = Symbol('a0')
    res_a0 = mathml(a0, printer='presentation')
    assert res_a0 == '<msub><mi>a</mi><mi>0</mi></msub>', (
        f"Expected '<msub><mi>a</mi><mi>0</mi></msub>', got '{res_a0}'"
    )


def test_expression_from_issue():
    # In x2*z + x2**3, both occurrences of x2 must display correctly,
    # while ordinary symbols such as x and z continue to display.
    x2, y, z = symbols('x2 y z')
    expr = x2 * z + x2**3
    res = mathml(expr, printer='presentation')

    # Must not contain <mi><msub>
    assert '<mi><msub>' not in res, (
        f"Invalid MathML nesting in {res}"
    )
    # Both occurrences of x2 should be formatted as <msub><mi>x</mi><mi>2</mi></msub>
    assert res.count('<msub><mi>x</mi><mi>2</mi></msub>') == 2, (
        f"Expected 2 occurrences of '<msub><mi>x</mi><mi>2</mi></msub>', got {res.count('<msub><mi>x</mi><mi>2</mi></msub>')} in {res}"
    )
    # z should also be displayed
    assert '<mi>z</mi>' in res, f"Expected '<mi>z</mi>' in {res}"

    # Ordinary symbols without digits continue to display correctly
    x = Symbol('x')
    expr_plain = x * z + x**3
    res_plain = mathml(expr_plain, printer='presentation')
    assert '<msub>' not in res_plain, f"Unexpected <msub> in plain expression: {res_plain}"
    assert '<mi>x</mi>' in res_plain, f"Expected '<mi>x</mi>' in {res_plain}"
    assert '<mi>z</mi>' in res_plain, f"Expected '<mi>z</mi>' in {res_plain}"
    assert mathml(x, printer='presentation') == '<mi>x</mi>'


def test_presentation_dom_structure():
    # Test the DOM node structure returned by MathMLPresentationPrinter._print
    mpp = MathMLPresentationPrinter()

    # Plain symbol
    node_x = mpp._print(Symbol('x'))
    assert node_x.nodeName == 'mi'
    assert len(node_x.childNodes) == 1
    assert node_x.childNodes[0].nodeValue == 'x'

    # Symbol with digits / subscript
    node_x2 = mpp._print(Symbol('x2'))
    assert node_x2.nodeName == 'msub', (
        f"Expected nodeName 'msub', got '{node_x2.nodeName}'"
    )
    assert node_x2.childNodes[0].nodeName == 'mi'
    assert node_x2.childNodes[0].childNodes[0].nodeValue == 'x'
    assert node_x2.childNodes[1].nodeName == 'mi'
    assert node_x2.childNodes[1].childNodes[0].nodeValue == '2'

    # Explicit subscript
    node_x_sub = mpp._print(Symbol('x_1'))
    assert node_x_sub.nodeName == 'msub', (
        f"Expected nodeName 'msub', got '{node_x_sub.nodeName}'"
    )

    # Superscript
    node_x_sup = mpp._print(Symbol('x^2'))
    assert node_x_sup.nodeName == 'msup', (
        f"Expected nodeName 'msup', got '{node_x_sup.nodeName}'"
    )

    # Subscript and superscript
    node_x_sub_sup = mpp._print(Symbol('x_1^2'))
    assert node_x_sub_sup.nodeName == 'msubsup', (
        f"Expected nodeName 'msubsup', got '{node_x_sub_sup.nodeName}'"
    )


def test_matrix_symbols():
    # Matrix symbols with bold style
    X = MatrixSymbol('X', 2, 2)
    res_X = mathml(X, printer='presentation')
    assert res_X == '<mi mathvariant="bold">X</mi>', (
        f"Expected '<mi mathvariant=\"bold\">X</mi>', got '{res_X}'"
    )

    X2 = MatrixSymbol('X2', 2, 2)
    res_X2 = mathml(X2, printer='presentation')
    assert '<mi><msub>' not in res_X2
    assert res_X2 == '<msub mathvariant="bold"><mi>X</mi><mi>2</mi></msub>', (
        f"Expected '<msub mathvariant=\"bold\"><mi>X</mi><mi>2</mi></msub>', got '{res_X2}'"
    )


def main():
    test_symbol_ending_with_number()
    test_expression_from_issue()
    test_presentation_dom_structure()
    test_matrix_symbols()
    print("All tests passed.")


if __name__ == '__main__':
    main()
