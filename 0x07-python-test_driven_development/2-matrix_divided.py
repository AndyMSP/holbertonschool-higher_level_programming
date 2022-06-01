#!/usr/bin/python3
"""Module to divide each element of a matrix by some value"""


def matrix_divided(matrix, div):
    """Function to divide all elements in Matrix by div"""
    try:
        if not all([all([isinstance(j, (int, float))
                    for j in i]) for i in matrix]):
            raise TypeError(("matrix must be a matrix"
                            " (list of lists) of integers/floats"))
    except Exception:
        raise TypeError(("matrix must be a matrix (list of lists)"
                        " of integers/floats"))
    if not all([len(i) == len(matrix[0]) for i in matrix]):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(j / div, 2) for j in i] for i in matrix]
