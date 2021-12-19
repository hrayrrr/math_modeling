import numpy as np

from physical_constants import g

x0 = 15
y0 = 20
vx0 = 45
vy0 = 30
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