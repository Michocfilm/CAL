import sympy as sym
x = sym.symbols('x')
y = sym.sin(3*x + 1)**2
ans6 = sym.diff(y, x)
print(sym.simplify(ans6))
