#!/usr/bin/python3
"""Module contains a function to determine if obj is a_class or
inherited from a_class"""


def is_kind_of_class(obj, a_class):
    """function to determine if object is of type a_class or inherited from
    a_class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
