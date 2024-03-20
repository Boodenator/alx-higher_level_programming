#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrix = []
    for i in range(len(matrix)):
        my_matrix += [list(map(lambda x: x ** 2, matrix[i]))]
    return my_matrix
