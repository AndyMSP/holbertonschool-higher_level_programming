#!/usr/bin/python3


def print_matrix_integer(matrix=[]):
    """Print a matrix visually

    Args:
        matrix (2D matrix, optional): 2D matrix of ints. Defaults to [].

    Return:
        nothing
    """
    for row in matrix:
        print(*row)
