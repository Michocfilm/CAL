import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
x,C1 = sym.symbols('x C1')
y = sym.Function('y')
ode = sym.Eq(x * y(x).diff(x) + 2*y(x) - 1/x**3, 0)
sol = sym.dsolve(ode,y(x))
y_exp = sol.rhs
y_part = y_exp.subs(C1,1.50)
func = sym.lambdify(x,y_part,'numpy')
x_vals = np.linspace(1,10,100)
y_vals = func(x_vals)
plt.figure(figsize=(8,5))
plt.plot(x_vals,y_vals,label='C1 = 1.50',linewidth=3)
plt.title('Graph of y(x) with C1 = 1.50')
plt.xlabel('x')
plt.ylabel('y')
plt.ylim(0,0.5)
plt.xlim(0,10)
plt.legend()
plt.grid(True,alpha=0.3)
plt.show()