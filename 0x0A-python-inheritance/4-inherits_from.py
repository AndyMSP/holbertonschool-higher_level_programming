#!/usr/bin/python3
"""Module contains a function and a test script"""


def inherits_from(obj, a_class):
    """Determines if obj's class inherited from a_class"""
    return a_class in type(obj).mro()[1:]


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
