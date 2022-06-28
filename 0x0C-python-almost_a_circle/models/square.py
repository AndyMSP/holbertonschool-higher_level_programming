#!/usr/bin/python3
"""Module defining Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class definition"""

    def __init__(self, size, x=0, y=0, id=None):
        """Called on instantiation of new Square object"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return string representation of object"""
        return (
            f"[Square] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}"
        )
