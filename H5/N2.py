import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
x = sp.symbols('x')
f = x**2 * sp.cos(x)**2
x_vals = np.linspace(-10, 10, 1000)
f_true = sp.lambdify(x, f, 'numpy')(x_vals)
orders = [15, 20, 25, 30, 35, 40, 45, 50, 55]
plt.figure(figsize=(15, 12))
for i, n in enumerate(orders, 1):
    taylor = sp.series(f, x, 0, n).removeO()
    f_taylor = sp.lambdify(x, taylor, 'numpy')(x_vals)
    plt.subplot(3, 3, i)
    plt.plot(x_vals, f_true, '--', label='Original')
    plt.plot(x_vals, f_taylor, label=f'Taylor (n={n})')
    plt.axvline(0, linestyle='--', color='gray')
    plt.title(f'n = {n}')
    plt.xlim(-10, 10)
    plt.ylim(0, 100)
    plt.grid()
    plt.legend(fontsize=8)
plt.tight_layout()
plt.show()
