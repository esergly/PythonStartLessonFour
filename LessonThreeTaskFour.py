vysota = int(input('Введите высоту прямоугольника: '))
shirina = int(input('Введите ширину прямоугольника: '))
temp = vysota
while vysota > 0:
    if vysota == temp or vysota == 1:
        print("*" * shirina)
    else:
        print('*' + ' ' * (shirina - 2) + '*')
    vysota = vysota - 1
