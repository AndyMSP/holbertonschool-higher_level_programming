#!/usr/bin/python3
"""
Module containing the add_integer function
Add_integer raises errors appropriately
Used to practice doctest feature
"""


def add_integer(a, b=98):
    """
    Adds two numbers and returns value
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
