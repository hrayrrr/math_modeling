a = int(input('Введите длину первого отрезка: '))
b = int(input('Введите длину второго отрезка: '))
c = int(input('Введите длину третьего отрезка: '))

if a + b > c and a + c > b and b + c > a:
  if a != b and a != c and b != c:
    print('Треугольник существует, он является разносторонним')
  elif (a == b and a != c and b != c) or (a != b and a == c and b != c) or (a != b and a != c and b == c):
    print ('Треугольник существует, он является равнобедренным')
  elif a == b and a == c and b == c:
    print('Треугольник существует, он является равносторонним')
else:
  print('Треугольник не существует')