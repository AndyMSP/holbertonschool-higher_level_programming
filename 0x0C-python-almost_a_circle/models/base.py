#!/usr/bin/python3
"""Module defines Base class"""


import json


class Base:
    """Base class for managing id attribute in other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Method called each time new object is instantiated"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @classmethod
    def reset(cls):
        """Reset all class variables"""
        cls.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of a list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)
