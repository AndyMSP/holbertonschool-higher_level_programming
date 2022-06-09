#!/usr/bin/python3
"""Module with function to convert from json"""


def from_json_string(my_str):
    """Function returns object converted from json string"""
    import json
    return json.loads(my_str)
