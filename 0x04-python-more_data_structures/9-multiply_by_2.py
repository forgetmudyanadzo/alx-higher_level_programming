#!/usr/bin/python3
# 9-multiply_by_2.py

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    key = list(new_dict.keys())

    for k in key:
        new_dict[k]*= 2

        return (new_dict)
