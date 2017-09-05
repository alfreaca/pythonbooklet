def remove_five(lst):
    for i in range(len(lst)-1):
        if lst[i] == 5:
            lst.pop(i)
    return lst
