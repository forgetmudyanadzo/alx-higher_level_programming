#!/usr/bin/python3

"""checks if object is instance of class
or inherited class
"""


def is_kind_of_class(obj, a_class):
    """returns true if object is instance of class
    or class that the class in question inherits from
    """
    return (isinstance(obj, a_class))
