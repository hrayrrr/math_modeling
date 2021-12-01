b = int(input('Введите первый член: '))
q = int(input('Введите знаменатель: '))
a = int(input('Введите количество членов: '))

i = 1

g = [b]

while i < a:
  i = i + 1
  g.append(g[-1] * q)

print('Геометрическая прогрессия: ')
print(*g, sep=', ')