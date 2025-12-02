from pylab import *
x = linspace(5, 10, 15)
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(x, ((x**3)-x+1), color="black", linewidth=0.5, linestyle='-', marker='o')
ax.plot(x, ((x**4)-(3*(x**2))+x), color="yellow",linewidth=1.0, linestyle='-.', marker='o')
ax.plot(x, ((3*(x**5))-(25*(x**3))+(60*x)), color="cyan", linewidth=1.5, linestyle='--', marker='s')
show()