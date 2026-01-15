import sympy as sym
i = sym.symbols('i', integer=True, positive=True)
R = 1 / i**2
S = sym.Sum(R, (i, 1, 30))
result = S.evalf(5)
print(result)
