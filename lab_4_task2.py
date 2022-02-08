import numpy as np

def prod_func(a):
  x = 1
  for i in a:
    x *= i
  return x

a = np.array([1, 3, 5, 7, 9, 11, 13, 15])

print(prod_func(a))