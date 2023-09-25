#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for column in matrix:
        res = map(lambda x: x**2, column)
        new_matrix.append(res)
    return new_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
