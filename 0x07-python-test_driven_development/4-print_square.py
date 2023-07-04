#!/usr/bin/python3

"""
This is the "Print Square" module.

The Print Square module prints a square using "#".
The argument supplied should determine the width/height of square.
"""


def print_square(size):
    """Print a perfect square given a valid int or float argument.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for n in range(0, size):
        for m in range(size):
            print("#", end="")
            print("")
