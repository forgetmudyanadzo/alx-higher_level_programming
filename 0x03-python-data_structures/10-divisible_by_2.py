#!/usr/bin/python3
#10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    if my_list is None:
        return

    new_list = []
    for n in my_list:
        if n % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
            return new_list
