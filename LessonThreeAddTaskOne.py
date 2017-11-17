number = int(input('Введите высоту рисуемой фигуры: '))
i = 1
j = 1
while i <= number:
    while j <= number - 1:
        print('*' * j)
        j += 1
    print('*' * number)
    number -= 1
