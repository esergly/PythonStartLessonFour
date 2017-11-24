number = int(input('Введите любое целое число больше 4-х, но меньше 16-ти: \n'))
attempt = number
factorial = 1
if number < 4 or number > 16:
    print('Введённое число не соответствует заданному условию. Попробуйте ещё раз.')
else:
    while number >= 1:
        factorial = factorial * number
        number = number - 1
print(str(attempt) + '! = ' + str(factorial))
