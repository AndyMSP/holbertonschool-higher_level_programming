#!/usr/bin/python3
"""Module with function to convert object to json string"""


def class_to_json(obj):
    """Function converts an object <obj> to json string"""
    import json
    return json.dumps(obj.__dict__)
