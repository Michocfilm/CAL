import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
x = sym.symbols('x')
T = sym.Function('T')

ode = sym.Eq(T(x).diff(x) + 0.3*T(x), 30+10*sym.sin(0.5*x))
sol = sym.dsolve(ode,T(x))
general =  sol.rhs
x_vals = np.linspace(0,20,200)
plt.figure(figsize=(10,6))
temps = range(40,105,5)
for T0 in temps:
    eq_initial = sym.Eq(general.subs(x,0),T0)
    C1_symbol = sym.Symbol('C1')
    C1_val = sym.solve(eq_initial, C1_symbol)[0]
    particular = general.subs(C1_symbol, C1_val)
    T_plot = sym.lambdify(x,particular, modules= 'numpy')
    y_vals = T_plot(x_vals)
    label_text = f"y(0) = {T0:.2f}, C1 = {C1_val:.2f}"
    plt.plot(x_vals,y_vals, label= label_text, linewidth=2)
    
plt.title('CPU Temperature Variation Over Time')
plt.xlabel('Time (Seconds)')
plt.ylabel('CPU Temperature (Â°C)')
plt.xlim(0,20)
plt.ylim(40,125)
plt.grid(True)
plt.legend(loc='lower right', fontsize='small', ncol =1)
plt.show()