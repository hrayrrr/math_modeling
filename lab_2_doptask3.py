i = int(input('Введите число: '))

x = 0

while i > 0:
  x = x * 10 + i % 10
  i = i // 10
  
print(x)