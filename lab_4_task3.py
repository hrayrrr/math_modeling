import numpy as np
from physical_constants import g

def mult_func(a):
  x = (a[0] * g * a[1]) + ((a[0] * a[2] ** 2)/2)

a = np.array([45, 20, 25])

print(mult_func(a))