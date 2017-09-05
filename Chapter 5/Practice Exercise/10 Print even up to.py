zero = 0
num1 = int(input("What number would you like to count up to?: "))

def print_upto(num):
    global zero
    while zero < num + 1:
        print(zero)
        zero = zero + 2

print(print_upto(num1))
