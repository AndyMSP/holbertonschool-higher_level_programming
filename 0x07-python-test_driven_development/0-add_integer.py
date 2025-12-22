#!/usr/bin/python3
"""Line 1 to fix documentation
Module containing the add_integer function
Add_integer raises errors appropriately
Used to practice doctest feature
"""


def add_integer(a, b=98):
    """Line 1 to fix documentaion
    Adds two numbers and returns value
    line 3 to fix documentation"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
