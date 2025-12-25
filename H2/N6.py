import sympy as sym
x,y = sym.symbols('x y')
f_1 = 1/sym.sqrt((1-x)**2+y**2)
f_2 = 1/sym.sqrt((1+x)**2+y**2)
f = f_1 + f_2
sol1 = sym.limit(f,x,1)
sol2 = sym.limit(sol1,y,0)
print(sol2)