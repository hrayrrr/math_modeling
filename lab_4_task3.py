import numpy as np
from physical_constants import g

def energy_func(a):
  x = (a[0] * g * a[1]) + ((a[0] * a[2] ** 2)/2)
  return x

m = 45
h = 20
v = 25

a = np.array([m, h, v])

print(energy_func(a))