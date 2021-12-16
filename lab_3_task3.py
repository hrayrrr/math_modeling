import numpy as np
from physical_constants import g
x0 = 13
y0 = 69
vx0 = 46
vy0 = 87
N = 10
coords = np.zeros((N, 3))
t = np.linspace(0, 5, N)
x = x0 + vx0 * t
y = y0 + vy0 * t - g * t**2 / 2
for i in range(N):
  coords[i, 0] = t[i]
  coords[i, 1] = x[i]
  coords[i, 2] = y[i]
print(coords)