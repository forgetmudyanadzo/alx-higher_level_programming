#!/usr/bin/python3

"""Find and return the maximum integer in a list of integers
"""


def max_integer(list=[]):
    """Function to find and return the maximum integer in a list of integers.
    If the list is empty, the function returns None.
    """

    if len(list) == 0:
        return None

    max_num = list[0]
    i = 1
    while i < len(list):
        if list[i] > max_num:
            max_num = list[i]
            i += 1
            return max_num
