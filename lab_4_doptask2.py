def fib(n):
  f0 = 0
  f1 = 1
  if n == 0:
    return f0
  elif n == 1:
    return f1
  elif n < 0:
    for i in range(-n+1, 1, -1):
      f = f1 - f0
      f1 = f0
      f0 = f
    return f
  else:
    for i in range(1, n, 1):
      f = f0 + f1
      f0 = f1
      f1 = f
    return f

print(fib(24))