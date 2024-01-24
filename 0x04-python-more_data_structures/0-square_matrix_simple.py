#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_new = [list(row) for row in matrix]
    for i in matrix_new:
        for j in range(len(i)):
            i[j] = i[j] * i[j]
    return matrix_new
