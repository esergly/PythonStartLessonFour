  
# Правильное решение с применением только одного цикла    
number = int(input('Введите высоту рисуемой фигуры: '))
k = 1
while k < (number * 2):
    if k < number + 1:
        print('*' * k)
        k += 1
    else:
        print('*' * ((number * 2) - k))
        k += 1

        
# Второй вариант решения, но цикл имеет ещё и вложенный цикл внутри себя
number = int(input('Введите высоту рисуемой фигуры: '))
i = 1
j = 1
while i <= number:
    while j <= number - 1:
        print('*' * j)
        j += 1
    print('*' * number)
    number -= 1

