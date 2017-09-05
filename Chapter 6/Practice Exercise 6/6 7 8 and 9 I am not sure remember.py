print ("\nExercise 6\n")
word = input("Input a word\n")
def is_palindrome(word):
   if word = word.reverse():
        return true
    else:
        return false

print ("\nExercise 7\n")
def unique_elements(l):
    data_list = []
    return list(set(l))

print ("\nExercise 8\n")
def backways(text):
    output = []
    for i in range(len(text)-1, -1, -1):
        output.append(text[i])
    return output

print ("\nExercise 9\n")
def sum_list(list):
    lst = 0
    for i in list:
        lst += i
    return lst
