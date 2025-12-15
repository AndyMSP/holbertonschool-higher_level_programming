#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    li = [[k, v] for k, v in a_dictionary.items()]
    li.sort(key=(lambda entry: entry[0]))
    [print(f"{el[0]}: {el[1]}") for el in li]
