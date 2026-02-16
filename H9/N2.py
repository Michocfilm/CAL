import sympy as sym
x,C1 = sym.symbols('x C1')
y= (C1*x - 1) / x**3
eq = sym.Eq(0.5,y.subs(x,1))
c1 = sym.solve(eq,C1)
print(f"{c1[0]:.2f}")