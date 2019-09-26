from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np


data = [(j,i,i**2 + j) for j in range(1,27) for i in range(4)]

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(0, 4, 1)
Y = np.arange(1, 27, 1)
X, Y = np.meshgrid(X, Y)


Z = np.array([z for _,_,z in data]).reshape(26,4)

surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
        linewidth=0, antialiased=True)

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.xlabel('X')
plt.ylabel('Y')

plt.show()