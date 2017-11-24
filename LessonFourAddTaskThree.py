vysota = int(input('Введите высоту фигуры (нечётное число): '))
if vysota%2==0:
    print('Введённое число не соответствует заданным условиям.')
    print('Картинка при выводе на экран не будет симметричной.')
temp = vysota
i = 0
while i < vysota:
    print('*' * vysota)
    vysota -= 2
vysota = 3
while vysota < temp + 2:
    print('*' * vysota)
    vysota += 2
