#!/usr/bin/python3
"""Module defines a class called BaseGeometry"""


class BaseGeometry():
    """Class of type BaseGeometry"""

    def area(self):
        """function which only throws an error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
