#!/usr/bin/python3
"""Module containing Rectangle class and test script"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Representation of a rectangle"""

    def __init__(self, width, height):
        """Iniitalize rectangle"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """return calculated area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return human readable string representation of Rectangle instance"""
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
