#!/usr/bin/python3
# 102-complex_delete.py

def complex_delete(a_dictionary, value):
    copy = a_dictionary.copy()

    for k, v in copy.items():
        if value in v:
            del a_dictionary[k]

            return a_dictionary
