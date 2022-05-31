#!/usr/bin/python3
"""Module to divide each element of a matrix by some value"""


def matrix_divided(matrix, div):
    return [[j / div for j in i] for i in matrix]
