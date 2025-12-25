import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
x = sym.symbols('x')
C = sym.ln(x)
dCdx = sym.diff(C, x)
def tangent_line(x_point):
    slope = float(dCdx.subs(x, x_point))
    y_point = float(C.subs(x, x_point))
    b = y_point - slope * x_point
    return lambda t: slope * t + b, slope, y_point

x_points = [1, 10, 50]
tangents = [tangent_line(xp) for xp in x_points]
x_vals = np.linspace(0.1, 60, 500)
y_vals = np.log(x_vals)
plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, 'b-', label='C(x) = ln(x)')
colors = ['r', 'g', 'y']
for i, xp in enumerate(x_points):
    tan_func, slope, y_val = tangents[i]
    x_ranges = {1: 0.5, 10: 3, 50: 10}
    x_range = np.linspace(xp - x_ranges[xp], xp + x_ranges[xp], 100)
    plt.plot(x_range, tan_func(x_range), colors[i]+'--',
             label=f'Tangent at x={xp} (C({xp})={y_val:.2f}')
    plt.plot(xp, y_val, colors[i]+'o')

plt.xlabel('x')
plt.ylabel('C(x)')
plt.title('C(x) = ln(x)')
plt.legend()
plt.grid(True)
plt.ylim(-3, 5)
plt.yticks(np.arange(-2, 5, 1))
plt.show()
