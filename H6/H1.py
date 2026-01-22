import sympy as sym
t = sym.symbols('t')
S = sym.exp(-3*t)
dS_dt = sym.diff(S, t)
d2S_dt2 = sym.diff(S, t, 2)
ODE = d2S_dt2 + 2*dS_dt - 3*S
print("S(t) =", S)
print("dS/dt =", dS_dt)
print("d²S/dt² =", d2S_dt2)
print("\nSubstitute into ODE:")
print(ODE.simplify())
