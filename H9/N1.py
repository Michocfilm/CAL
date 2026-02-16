import sympy as sym
x = sym.symbols('x')
y = sym.Function('y')
ode = sym.Eq(x*y(x).diff(x) + 2*y(x) - 1/x**3,0)
sol = sym.dsolve(ode,y(x))
print(sol)