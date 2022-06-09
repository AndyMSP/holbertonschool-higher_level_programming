#!/usr/bin/python3
"""Module contains function that converts data to json"""


def to_json_string(my_obj):
    """function to convert python object to json string"""
    import json
    return json.dumps(my_obj)
