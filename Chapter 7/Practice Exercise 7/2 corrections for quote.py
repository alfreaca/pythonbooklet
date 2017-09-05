import sqlite3
print ("Exercise 2\n")
new_file = open("my_quote.txt", 'w')
new_file.close()

def update_file(new_file, quote):
    new_file = open("my_quote.txt", 'a')
    new_file.write("This is an update\n")
    new_file.write(quote)
    new_file.write("\n\n")

for index in range(3):
    quote = input("Input a quote: ")
    update_file(new_file, quote)

new_file = open("my_quote.txt", 'r')
print (new_file.read())

new_file.close()
