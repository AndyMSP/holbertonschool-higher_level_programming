#!/usr/bin/python3
def no_c(my_string):
    while my_string.find('c') != -1:
        i = my_string.find('c')
        my_string = my_string[:i] + my_string[i + 1:]
    while my_string.find('C') != -1:
        i = i = my_string.find('C')
        my_string = my_string[:i] + my_string[i + 1:]
    return my_string
