import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,3*np.pi,0.01)
y = np.sin(x)
z = np.cos(x)
plt.plot(x,y,x,z)

plt.scatter(x[np.abs(np.sin(x)-np.cos(x)) < 0.1], np.sin(x[np.abs(np.sin(x)-np.cos(x)) < 0.1]))
plt.scatter(x[np.abs(np.sin(x)-np.cos(x)) < 0.1], np.cos(x[np.abs(np.sin(x)-np.cos(x)) < 0.1]))

plt.show()
