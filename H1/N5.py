import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1, 1, 500)
y = np.sin(np.pi / x)
plt.plot(x, y, color='m', marker='^')
plt.xlabel('x');plt.ylabel('f(x)')
plt.xlim(-1.0, 1.0);plt.ylim(-1.5, 1.5)
plt.title('f(x) = sin(pi/x)')
plt.show()