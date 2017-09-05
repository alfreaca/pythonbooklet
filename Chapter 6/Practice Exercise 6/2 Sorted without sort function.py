numbers = [-5, -23, 5, 0, 23, -6, 23, 67]
sorted_list = []

while numbers:
    minimum = numbers[0]  
    for x in numbers: 
        if x < minimum:
            minimum = x
    sorted_list.append(minimum)
    numbers.remove(minimum)    

print (sorted_list)
