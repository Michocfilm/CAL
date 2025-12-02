import sympy as sym
a, b = sym.symbols('a b')
result = sym.expand(((a**(1/2)) + (b**(1/2))) * ((a**(1/2)) - (b**(1/2))))
print(result)