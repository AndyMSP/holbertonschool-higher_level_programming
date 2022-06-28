#!/usr/bin/python3
"""Module defining Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class definition"""

    def __init__(self, size, x=0, y=0, id=None):
        """Called on instantiation of new Square object"""
        self.size = size;
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Method to get value of variable size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set size variable"""
        self.validate('size', value)
        self.__size = value
        self.width = self.__size
        self.height = self.__size
        

    def __str__(self):
        """return string representation of object"""
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}"
        )
