#!/usr/bin/python3
"""Module contains a function to test an objects class"""


def is_same_class(obj, a_class):
    """Function determines if obj is an exact instance of a_class.  Returns
    True if yes or False if no"""
    if type(obj) == a_class:
        return True
    else:
        return False
