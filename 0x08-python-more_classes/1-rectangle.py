#!/usr/bin/python3
"""This module defines an empty class called Rectangle"""


class Rectangle:
    """This Rectangle has a positive integer height and width"""

    def __init__(self, width=0, height=0):
        """Method executed when new Rectangle instance is created"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method to get private variable __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set private variable __width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method to get private variable __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set private variable __height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
