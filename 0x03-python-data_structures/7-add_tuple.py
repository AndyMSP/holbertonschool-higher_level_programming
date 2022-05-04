#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    if tuple_a:
        if len(tuple_a) > 0:
            a[0] = tuple_a[0]
        if len(tuple_a) > 1:
            a[1] = tuple_a[1]
    b = [0, 0]
    if tuple_b:
        if len(tuple_b) > 0:
            b[0] = tuple_b[0]
        if len(tuple_b) > 1:
            b[1] = tuple_b[1]
    new = (a[0] + b[0], a[1] + b[1])
    return new
