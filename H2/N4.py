import sympy as sym
x,y = sym.symbols('x y')
sol1 = sym.limit(x*y/(sym.sqrt(x*y+1)-1),x,0)
sol2 = sym.limit(sol1,y,0)
print(sol2)