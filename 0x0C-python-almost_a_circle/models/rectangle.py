#!/usr/bin/python3
"""Module defining Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class definition"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method to be called on instantiation of new Rectangle object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @classmethod
    def reset(self):
        """Reset all class attributes"""
        super().reset()

    @property
    def width(self):
        """Method to retrieve value of private variable __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Method to set value of private variable __width"""
        self.__width = value

    @property
    def height(self):
        """Method to retrieve value of private variable __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set value of private variable __height"""
        self.__height = value

    @property
    def x(self):
        """Method to retrieve value of private variable __x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Method to set value of private variable __x"""
        self.__x = value

    @property
    def y(self):
        """Method to retrieve value of private variable __y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Method to set value of private variable __y"""
        self.__y = value
