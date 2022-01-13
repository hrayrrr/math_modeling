import numpy as np

def mean_func(a):
  x = np.mean(a)
  return x

a = np.array([1, 3, 5, 7, 9, 11, 13, 15])

print(mean_func(a))