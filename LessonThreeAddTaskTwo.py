number = 1
while number < 101:
    i = 2
    while i < number:
        if number % i == 0:
            number = number + 1
            break
        i = i + 1
    else:
        print(str(number), end=", ")
        number = number + 1
