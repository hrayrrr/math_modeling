i = int(input('Введите число: '))

if i == 1:
  print('1')
elif i == 2:
  print('1 1')
else:
  f = [1, 1]
  x = 1
  while x < i:
    x = x + 1
    f.append(f[-1] + f[-2])
  print(*f)