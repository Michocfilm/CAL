import sympy as sym
x, y = sym.symbols('x y')
result = sym.simplify(sym.cos(x)*sym.cos(y) + sym.sin(x)*sym.sin(y))
print(result)
