def lnz(type = int(input('Введите тип линзы (1 - собирающая; 2 - рассеивающая): ')),
        d = float(input('Введите расстояние до линзы: ')),
        F = float(input('Введите фокусное расстояние линзы: '))):
    if type == 2:
      print('Изображение прямое, мнимое, уменьшенное')
    elif type == 1:
      if d == F:
        print('Изображения нет')
      elif d < F:
        print('Изображение прямое, мнимое, увеличенное')
      elif d > F and d <= 2 * F:
        print('Изображение обратное, действительное, увеличенное')
      elif d > 2 * F:
        print('Изображение обратное, действительное, уменьшенное')
      else:
        print('Изображения нет')
    else:
      print('Изображения нет')
    return type

lnz()