#!/usr/bin/python3
"""Module defines a class of type Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class of type Rectangle"""

    def __init__(self, width, height):
        """function called on instantiation"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        __width = width
        __height = height
