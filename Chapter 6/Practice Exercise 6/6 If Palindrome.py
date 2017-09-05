print ("\nExercise 6\n")
word = list(input("Input a word: "))
word2 = word
word3 = word2.reverse()
def is_palindrome(word):
    if word == word2:
        print("true")
    else: 
        print("false")

is_palindrome(word)
