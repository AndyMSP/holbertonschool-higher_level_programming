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

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON representation of objects to a file"""
        if cls.__name__ == 'Rectangle':
            filename = 'Rectangle.json'
        if cls.__name__ == 'Square':
            filename = 'Square.json'
        if cls.__name__ == 'Base':
            filename = 'Base.json'
        list_dictionaries = []
        if list_objs is not None:
            for obj in list_objs:
                temp_dict = obj.to_dictionary()
                list_dictionaries.append(temp_dict)
        json_str = cls.to_json_string(list_dictionaries)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Return list of dictionaries from json string"""
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create objects from dictionary"""
        obj = cls(1, 1, 1)
        obj.update(**dictionary)
        return obj
