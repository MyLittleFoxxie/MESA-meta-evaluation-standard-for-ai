1. A symbol whose name ends in a number, such as x2, prints in presentation MathML as a subscript (msub with mi x and mi 2) that is not nested inside another mi element.
2. The same holds for symbols with superscripts and with both, such as x__2 (msup) and y_a__b (msubsup), and inside larger expressions such as x2*z + x2**3.
3. A plain symbol x still prints as one mi element.
4. A matrix symbol with the bold style sets mathvariant to bold on the element that represents the whole symbol, with or without a subscript.
