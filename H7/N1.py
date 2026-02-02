import sympy as sym
t = sym.symbols('t')
I = sym.Function('I')
N = 1000
k = 0.05
ode = sym.Eq(I(t).diff(t),k * (N - I(t)))
sol = sym.dsolve(ode, I(t) , ics = {I(0): 0})
equation = sym.Eq(sol.rhs, 800)
ans = sym.solve(equation, t)
print(f"{ans[0]:.2f}")