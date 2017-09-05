lst = [int(x) for x in input().split()]
mean = sum(lst) / float(len(lst))
deviation = []
def list_of_deviation(lst):
    for x in lst:
        x = mean - x
        deviation.append(x)
    print (deviation)
print (list_of_deviation(lst))
