#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        tmp_a = [*tuple_a]
    if len(tuple_a) == 1:
        tmp_a = [tuple_a[0], 0]
    if len(tuple_a) == 0:
        tmp_a = [0, 0]

    if len(tuple_b) >= 2:
        tmp_b = [*tuple_b]
    if len(tuple_b) == 1:
        tmp_b = [tuple_b[0], 0]
    if len(tuple_b) == 0:
        tmp_b = [0, 0]

    return (tmp_a[0] + tmp_b[0], tmp_a[1] + tmp_b[1])
