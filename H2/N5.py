import sympy as sym
x,y = sym.symbols('x y')
on = 1-sym.cos(x**2 + y**2)
under = (x**2 + y**2)*sym.exp(x**2+y**2)
f = on/under
sol1 = sym.limit(f,x,1)
sol2 = sym.limit(sol1,y,-1)
print(sol2)