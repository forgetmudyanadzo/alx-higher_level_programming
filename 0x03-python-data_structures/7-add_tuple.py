#!/usr/bin/python3
#7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a) + [0]*2
    list_b = list(tuple_b) + [0]*2
    c = [x + y for x, y in zip(list_a, list_b)]
    return tuple(c[0:2])
