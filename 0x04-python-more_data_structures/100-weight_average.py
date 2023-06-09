#!/usr/bin/python3
# 100-weight_average.py

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    a = list(map(list, zip(*my_list)))
    b = [x * y for x, y in zip(a[0], a[1])]
    return sum(b) / sum(a[1])
