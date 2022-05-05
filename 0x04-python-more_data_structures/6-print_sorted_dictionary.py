#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    s = sorted(list(a_dictionary.items()))
    for i in s:
        print(f"{i[0]}: {i[1]}")
