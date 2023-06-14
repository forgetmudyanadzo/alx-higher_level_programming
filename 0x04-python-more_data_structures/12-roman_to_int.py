#!/usr/bin/python3
# 12-roman_to_int.py

def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return (0)

    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [data[x] for x in roman_string] + [0]
    list_num = 0

    for i in range(len(numbers) - 1):
        if numbers[i] >= numbers[i + 1]:
            list_num += numbers[i]
        else:
            list_num -= numbers[i]

            return (list_num)
