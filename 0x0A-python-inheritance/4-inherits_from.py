#!/usr/bin/python3
"""Module with function to test class inheritance"""


def inherits_from(obj, a_class):
    """Function which takes an object (obj) and determines if it was inherited
    from a class (a_class)"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
