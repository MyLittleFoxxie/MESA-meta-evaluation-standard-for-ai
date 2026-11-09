import sys
from xml.dom.minidom import parseString
from sympy import Symbol, symbols, MatrixSymbol
from sympy.printing.mathml import mathml

def fail(n, msg):
    print("behavior %d failed: %s" % (n, msg)); sys.exit(1)

def doc(e, **kw):
    return parseString("<math>%s</math>" % mathml(e, printer="presentation", **kw).replace("&InvisibleTimes;", "*")).documentElement

def elems(n):
    return [c for c in n.childNodes if c.nodeType == 1]

def text(n):
    return "".join(c.nodeValue for c in n.childNodes if c.nodeType == 3)

def nested_mi(root):
    return [m for m in root.getElementsByTagName("mi") if elems(m)]

def leaf(n, tag, val):
    return n.nodeName == tag and not elems(n) and text(n) == val

x2, z = symbols("x2 z")
for e in (x2, Symbol("x__2"), Symbol("y_a__b"), Symbol("alpha1"), x2 * z + x2 ** 3):
    if nested_mi(doc(e)): fail(1 if e == x2 else 2, "mi contains elements for %s" % e)

n = elems(doc(x2))[0]
if n.nodeName != "msub" or len(elems(n)) != 2 or not leaf(elems(n)[0], "mi", "x") or not leaf(elems(n)[1], "mi", "2"):
    fail(1, "x2 gives %s" % n.toxml())
n = elems(doc(Symbol("x__2")))[0]
if n.nodeName != "msup" or not leaf(elems(n)[0], "mi", "x") or not leaf(elems(n)[1], "mi", "2"):
    fail(2, "x__2 gives %s" % n.toxml())
n = elems(doc(Symbol("y_a__b")))[0]
k = elems(n)
if n.nodeName != "msubsup" or len(k) != 3 or [text(c) for c in k] != ["y", "a", "b"]:
    fail(2, "y_a__b gives %s" % n.toxml())
n = elems(doc(Symbol("x")))[0]
if not leaf(n, "mi", "x"): fail(3, "x gives %s" % n.toxml())
for name, tag in (("M", "mi"), ("M_1", "msub"), ("M__1", "msup")):
    r = doc(MatrixSymbol(name, 2, 2), mat_symbol_style="bold")
    n = elems(r)[0]
    if n.nodeName != tag or n.getAttribute("mathvariant") != "bold" or nested_mi(r):
        fail(4, "%s bold gives %s" % (name, n.toxml()))
if doc(MatrixSymbol("M", 2, 2)).getElementsByTagName("*")[0].getAttribute("mathvariant"): fail(4, "plain style set bold")
print("ok")
