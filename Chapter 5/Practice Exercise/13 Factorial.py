def factorial(number):
    num = 1
    while number >= 1:
        num = num * number
        number = number - 1
    return num

print(factorial(4))
