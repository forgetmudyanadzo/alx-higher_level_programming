#!/usr/bin/python3

"""
This is the "Matrix Divided" module.

The Matrix Divided module takes in a list of lists matrix and divisor.
All valid elements are divided by the divisor and returned as new matrix.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with all values divided by `div`.
    Matrix must be a list of lists.
    Each sub-list must contain only integers or floats.
    Empty sub-lists are not allowed.
    Divisor must be greater than 0 and must be an int or float.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
                raise TypeError("matrix must be a matrix (list of lists) of "
                        "integer/floats")

                if not all(len(row) == len(matrix[0]) for row in matrix):
                    raise TypeError("Each row of the matrix must have the same size")

                if not isinstance(div, int) and not isinstance(div, float):
                    raise TypeError("div must be a number")

                if div == 0:
                    raise ZeroDivisionError("division by zero")

                return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
