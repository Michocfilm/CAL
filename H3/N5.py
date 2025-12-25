import sympy as sym
x = sym.symbols('x')
y = sym.exp(x) / (sym.exp(x) - 1)
ans5 = sym.diff(y, x)
print(sym.simplify(ans5))
