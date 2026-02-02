import numpy as np
import matplotlib.pyplot as plt
N = 1000
k = 0.05
t = np.linspace(0,100,500)
I = N * (1 - np.exp(-k * t))

plt.figure(figsize = (10,6))
plt.plot(t,I, color='deepskyblue', linewidth = 3, label = r'$I(t) = N(1 - e^{-kt})$')
t_target = 32.19
I_target = 800
plt.plot([t_target, t_target],[0,I_target],color='plum',linestyle='--',linewidth=1.5)
plt.plot([0, t_target],[I_target,I_target],color='plum',linestyle='--',linewidth=1.5)
plt.title('Data Propagation in a Network')
plt.xlabel('Time (seconds)')
plt.ylabel('Number of devices with data')
plt.xlim(0,100)
plt.ylim(0,1000)
plt.grid(True)
plt.legend(loc='upper left')
plt.show() 