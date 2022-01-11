import numpy as np

def mult_func(a):
  x = np.prod(a)
  return x

a = np.array([1, 3, 5, 7, 9, 11, 13, 15])

print(mult_func(a))