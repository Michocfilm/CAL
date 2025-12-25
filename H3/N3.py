import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2
min_idx = np.unravel_index(np.argmin(Z), Z.shape)
min_x = X[min_idx]
min_y = Y[min_idx]
min_z = Z[min_idx]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.9)
ax.scatter(min_x, min_y, min_z, color='red', s=100, label='Optimal Base Location')
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Star CS-2024')
cbar = fig.colorbar(surf, shrink=0.5, aspect=10)
cbar.set_ticks([5, 10, 15, 20, 25, 30])
plt.show()
