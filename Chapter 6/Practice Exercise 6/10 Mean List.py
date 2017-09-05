def sum_list(list):
    lst = 0
    for i in list:
        lst += i
    return lst

def mean_list(list):
	mean = sum_list(list) / float(len(list))
	return mean

print(mean_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
