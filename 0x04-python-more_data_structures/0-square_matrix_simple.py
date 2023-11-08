#!/usr/bin/python3

def square_list(N):
    return (N**2)


def square_matrix_simple(matrix=[]):
    return [list(map(square_list, matrix[i])) for i in range(len(matrix))]
