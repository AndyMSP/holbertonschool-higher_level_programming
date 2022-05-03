#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return None
    for i in my_list:
        if type(i) is not int:
            return None
    my_list.reverse()
    for i in my_list:
        print(i)
