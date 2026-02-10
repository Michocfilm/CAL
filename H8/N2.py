import numpy as np
import matplotlib.pyplot as plt
theta = np.linspace(np.pi/2,np.pi/2 + 2*np.pi,6)[:-1]
x = np.cos(theta)
y = np.sin(theta)
plt.figure(figsize=(6,6))
lw=5
plt.plot([x[1],x[4]],[y[1],y[4]],color='#336600',linewidth=lw)
plt.plot([x[4],x[2]],[y[4],y[2]],color='#99ccff',linewidth =lw)
plt.plot([x[2],x[0]],[y[2],y[0]],color = '#ff6600',linewidth=lw)
plt.plot([x[0],x[3]],[y[0],y[3]],color='#ff3300',linewidth=lw)
plt.plot([x[3],x[1]],[y[3],y[1]],color='#ffff00',linewidth=lw)
plt.title('five-line star with custom colors')
plt.xlim(-1.1,1.1)
plt.ylim(-1.1,1.1)
plt.show()
