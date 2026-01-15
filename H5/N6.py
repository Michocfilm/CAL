import sympy as sym

n = sym.symbols('n', positive=True, integer=True)

S = sym.Sum(1/2**n + 1/3**n, (n, 1, sym.oo))

result = S.evalf()

print(result)

