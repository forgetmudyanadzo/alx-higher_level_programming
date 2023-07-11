#!/usr/bin/python3

"""Python class-to-JSON function"""


def class_to_json(obj):
    """returns the  object dictionary"""
    return obj.__dict__
