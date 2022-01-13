import numpy as np

r = 15
a = 20
b = 35
c = 10

def circle(r):
  S = np.pi * (r ** 2)
  return S

def triangle(a, b, c):
  S = a * b * c
  return S

def square(a, b):
  S = a * b
  return S

q = float(input('Выберите фигуру:\n\n1 - Круг\n2 - Треугольник\n3 - Прямоугольник\n\nВыбор - '))

if q == 1:
  print('\nОтвет:')
  print(circle(r))
elif q == 2:
  print('\nОтвет:')
  print(triangle(a, b, c))
elif q == 3:
  print('\nОтвет:')
  print(square(a, b))
else:
  print('\nОшибка :(')