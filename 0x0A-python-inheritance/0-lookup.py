#!/usr/bin/python3
"""Module with function to create list of all attributes from an object"""


def lookup(obj):
    """Return list of attributes in obj"""
    return dir(obj)
