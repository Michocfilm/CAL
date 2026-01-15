import sympy as sym

x = sym.symbols('x')

f = sym.exp(x)*sym.sin(x)

taylor_4 = sym.series(f, x, 0, 5).removeO()

print(taylor_4)
