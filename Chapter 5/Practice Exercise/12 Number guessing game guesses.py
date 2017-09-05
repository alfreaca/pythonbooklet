counter = 0
while counter < 6:
    num = 7
    guess = int(input("Input a number\n"))
    def magic_number(num):
        return num
    if guess > 7:
        print ("Too high")
        counter = counter + 1
    elif guess < 7:
        print ("Too low")
        counter = counter + 1
    elif guess == 7:
        print ("Well done")
        counter = counter + 1

print("Out of turns")
