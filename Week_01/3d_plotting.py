# -*- coding: utf-8 -*-
"""
@author: Alex Muirhead
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, +1, 9)
y = np.linspace(-1, +1, 9)

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot_surface(X, Y, Z)
plt.show()
