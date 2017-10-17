def discount_ten(lst):
    for i in range(len(lst)):
        lst[i] = int(lst[i])*0.9

    return lst

lst = [12, 14, 14]

print(discount_ten(lst))
