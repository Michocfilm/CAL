import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
x = sym.symbols('x')
f = (1)/(1+sym.exp(-x))
oo_positive = sym.limit(f,x,sym.oo)
oo_negative = sym.limit(f,x,-sym.oo)
print(oo_positive)
print(oo_negative)

x_plot = np.linspace(-5,4,100)
y_plot = 1/(1+np.exp(-x_plot))
plt.figure(figsize=(8,5))
plt.plot(x_plot,y_plot,color = 'blue',linestyle = '-')
plt.title('f(x) = 1/(1+e**-x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()