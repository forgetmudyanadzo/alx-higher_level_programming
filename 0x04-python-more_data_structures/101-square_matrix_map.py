#!/usr/bin/python3
# 101-square_matrix_map.py

def square_matrix_map(matrix=[]):
    return (list(map(lambda row: list(map(lambda n: n**2, row)), matrix)))
