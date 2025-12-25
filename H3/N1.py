import sympy as sym
s = sym.symbols('s')
t = s**2 / 10 + 5
rate = sym.diff(t, s)
print("Rate of change =", rate)
sizes = [20, 55, 99]
for size in sizes:
    time = t.subs(s, size)
    print(f"Download time for file size {size} MB:", float(time), "seconds")
