import sympy as sym
x = sym.symbols('x')
y = sym.Function('y')
ode = sym.Eq(x*y(x).diff(x) + y(x), x)
#General Solution
print("General Solution:")
print(sym.dsolve(ode, y(x)))
#Particular Solution
print("Particular Solution:")
print(sym.dsolve(ode, y(x), ics={y(1): 2}))
