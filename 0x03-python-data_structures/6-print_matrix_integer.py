#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        for i in range(len(sublist)):
            print("{:d}".format(sublist[i]), end="")

            if i is not len(sublist) - 1:
                print(" ", end="")
        print("")
