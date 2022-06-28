#!/usr/bin/python3
"""Module defining Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class definition"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method to be called on instantiation of new Rectangle object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def validate(self, name, value):
        """Validate inputs before creating object"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if (name == 'width' or name == 'height') and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if (name == 'x' or name == 'y') and value < 0:
            raise ValueError(f"{name} must be >= 0")

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
        self.validate('width', value)
        self.__width = value

    @property
    def height(self):
        """Method to retrieve value of private variable __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Method to set value of private variable __height"""
        self.validate('height', value)
        self.__height = value

    @property
    def x(self):
        """Method to retrieve value of private variable __x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Method to set value of private variable __x"""
        self.validate('x', value)
        self.__x = value

    @property
    def y(self):
        """Method to retrieve value of private variable __y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Method to set value of private variable __y"""
        self.validate('y', value)
        self.__y = value

    def area(self):
        """Returns area of a rectangle object"""
        return self.width * self.height

    def display(self):
        """display rectangle with # symbol"""
        print(self.y * '\n', end='')
        for i in range(self.height):
            print(self.x * ' ' + self.width * '#')

    def __str__(self):
        """return string representation of object"""
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def update(self, *args):
        """Update object with supplied arguments"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]
