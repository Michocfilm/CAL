import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0,20,100)
temps = [40,50,60,70,80]
plt.figure(figsize=(10,6))
for T0 in temps:
    C = T0 - 100
    T = 100 + C*np.exp(-0.3 * t)
    plt.plot(t,T,label=f'Initial CPU Temp = {T0} C', linewidth= 2)
plt.title('CPU Cooling Behavior Under Different Initial Loads')
plt.xlabel('Time (second)')
plt.ylabel('CPU Temperature (C)')
plt.xlim(0,20)
plt.ylim(35,105)
plt.grid(True)
plt.legend
plt.show()

