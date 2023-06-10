#!/usr/bin/python3
#5-no_c.py

def no_c(my_string):
    return my_string.translate({ord(c): None for c in "cC"})
