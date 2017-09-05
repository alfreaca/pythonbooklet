num1 = input("What is your first number?: ")
num2 = input("What is your second number?: ")
num3 = input("What is your third number?: ")

def largest(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1

    elif num2 > num1 and num2 > num3:
        return num2

    else:
        return num3 

print(largest(num1, num2, num3))
