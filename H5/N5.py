import sympy as sym

x = sym.symbols('x')

f = x / sym.sqrt(x**2 + 4)

taylor_5 = sym.series(f, x, 0, 6).removeO()

print(taylor_5)
