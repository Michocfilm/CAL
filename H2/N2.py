import sympy as sym
x,y = sym.symbols('x y')
sol1 = sym.limit((5*x**2+7*y)/(3*x**2+2*x*y+y**2),x,sym.oo)
sol2 = sym.limit(sol1,y,10)
print(f"{sol2:.5f}")