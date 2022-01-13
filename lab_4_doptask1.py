a = 3
n = 4

def func(a, n):
  for i in range(1, (n-1)):
    a *= a
  return a

print(func(a,n))