# import numpy as np
# import matplotlib.pyplot as plt

# # สร้างกริดสำหรับสนามทิศทาง
# x_vals = np.linspace(-4, 4, 20)
# y_vals = np.linspace(-4, 4, 20)
# X, Y = np.meshgrid(x_vals, y_vals)

# # สนามทิศทาง dy/dx = x^2 - y
# U = np.ones_like(X)
# V = X**2 - Y

# # เส้นคำตอบจากผลเฉลยเชิงวิเคราะห์ y(0)=1
# x_curve = np.linspace(-4, 4, 400)
# y_curve = x_curve**2 - 2*x_curve + 2 - np.exp(-x_curve)

# # พล็อตกราฟ
# plt.figure(figsize=(10, 6))
# plt.quiver(X, Y, U, V, color='black')
# plt.plot(x_curve, y_curve, 'r', linewidth=2)

# plt.xlim(-4, 4)
# plt.ylim(-4, 4)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Quiver plot of dy/dx = x^2 - y')

# plt.show()

import numpy as np
import matplotlib.pyplot as plt
x_vals = np.linspace(-4, 4, 20)
y_vals = np.linspace(-4, 4, 20)
X, Y = np.meshgrid(x_vals, y_vals)
F = X**2 - Y
U = 1 / np.sqrt(1 + F**2)
V = F / np.sqrt(1 + F**2)
x_curve = np.linspace(-4, 4, 400)
y_curve = x_curve**2 - 2*x_curve + 2 - np.exp(-x_curve)
plt.figure(figsize=(10, 6))
plt.quiver(X, Y, U, V, color='black')
plt.plot(x_curve, y_curve, 'r', linewidth=2)
plt.xlim(-4, 4)
plt.ylim(-4, 4)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quiver plot of dy/dx = x**2 - y')
plt.show()
