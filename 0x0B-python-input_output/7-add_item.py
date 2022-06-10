#!/usr/bin/python3
"""Module with function to append list items to json file"""


def add_items():
    """Function to add items to a json list"""
    import json
    import sys
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file =\
        __import__('6-load_from_json_file').load_from_json_file

    try:
        old_list = load_from_json_file('add_items.json')
    except Exception:
        old_list = []

    new_items = sys.argv[1:]
    new_list = old_list + new_items

    save_to_json_file(new_list, 'add_items.json')


add_items()
