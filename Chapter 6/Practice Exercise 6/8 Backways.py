print ("\nExercise 8\n")
def backways(text):
    output = []
    for i in range(len(text)-1, -1, -1):
        output.append(text[i])
    return output

print(backways([1, 2, 3, 4, 5]))
