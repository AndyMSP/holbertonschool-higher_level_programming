#!/usr/bin/python3
"""Module defining Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class definition"""

    def __init__(self, size, x=0, y=0, id=None):
        """Called on instantiation of new Square object"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Method to get value of variable size"""
        return self.width

    @size.setter
    def size(self, value):
        """Method to set size variable"""
        self.width = value
        self.height = value

    def __str__(self):
        """return string representation of object"""
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}"
        )

    def update(self, *args, **kwargs):
        """Update object with supplied arguments"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        if len(args) > 0:
            return
        if 'id' in kwargs:
            self.id = kwargs['id']
        if 'size' in kwargs:
            self.size = kwargs['size']
        if 'x' in kwargs:
            self.x = kwargs['x']
        if 'y' in kwargs:
            self.y = kwargs['y']
