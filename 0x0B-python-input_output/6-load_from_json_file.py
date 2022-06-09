#!/usr/bin/python3
"""Module contains a function to load json files into objects"""


def load_from_json_file(filename):
    """Function loads object from json file"""
    import json
    with open(filename, 'r', encoding='utf-8') as jsfile:
        return json.loads(jsfile.read())
