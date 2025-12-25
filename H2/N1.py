import sympy as sym
n = sym.symbols('n')
sol = sym.limit((n**2+3*n+4)/(2*n**2+5),n,sym.oo)
print(float(sol))
