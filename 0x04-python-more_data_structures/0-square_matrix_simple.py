#!/usr/bin/python3
# 0-square_matrix_simple.py

def square_matrix_simple(matrix=[]):
    return [list(map(lambda n: n**2, sublist)) for sublist in matrix]
