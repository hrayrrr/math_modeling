import numpy as np

r = 15
a = 20
b = 35
c = 10
h = 12

q = float(input('Выберите фигуру:\n\n1 - Круг\n2 - Треугольник\n3 - Прямоугольник\n\nВыбор - '))

def geometry(a, b, c, r, h, q):
  circle = np.pi * (r ** 2)
  triangle = 0.5 * a * h
  square = a * b
  error = 'Ошибка'
  if q == 1:
   return circle
  elif q == 2:
   return triangle
  elif q == 3:
   return square
  else:
    return error

print(geometry(a, b, c, r, h, q))