#!/usr/bin/python3
"""Module with function to save object to json file"""


def save_to_json_file(my_obj, filename):
    """Write <my_obj> to <filename> as a json file"""
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
