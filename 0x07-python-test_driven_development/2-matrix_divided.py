#!/usr/bin/python3
""" This module defines a function that divides a matrix
by a number (div)"""


def matrix_divided(matrix, div):
    """
    All elements of the matrix should be divided by div, rounded to 2 decimal places
    :param matrix: a list of lists of integers or floats
    :param div: a number (integer or float)
    :return: a new matrix
    """

    new_matrix = []
    for row in matrix:
        if (not isinstance(row, list) and
                not all(isinstance(x, int) for x in row) or
                not all(isinstance(x, float) for x in row)):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
