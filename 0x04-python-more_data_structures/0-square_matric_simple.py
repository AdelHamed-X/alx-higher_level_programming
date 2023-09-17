#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for column in matrix:
        res = list(map(lambda x: x**2, col))
        new_matrix.append(res)
    return new_matrix
