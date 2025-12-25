import sympy as sym
x = sym.symbols('x')
y = sym.log(x**2 + x + 1)
ans4 = sym.diff(y, x)
print(sym.simplify(ans4))
