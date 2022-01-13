import numpy as np

def func(a, b, N):
  x = np.linspace(a, b, N)
  y = x ** 2
  return y

print(func(0, 5, 100))