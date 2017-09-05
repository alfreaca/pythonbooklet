word = input("Enter your word: ")
score = 0
a = "a"
e = "e"
i = "i"
o = "o"
u = "u"

if "a" in word:
    score = score + 5

if "e" in word:
    score = score + 4

if "i" in word:
    score = score + 3

if "o" in word:
    score = score + 2


if "u" in word:
    score = score + 1

print("Your score is:", score)
