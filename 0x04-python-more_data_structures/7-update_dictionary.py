#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    temp = {key: value}
    a_dictionary.update(temp)
    return a_dictionary
