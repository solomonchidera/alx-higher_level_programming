#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for array in range(len(matrix)):
            if matrix[array]:
                for element in range(len(matrix[array])):
                    if element != (len(matrix[array]) - 1):
                        print("{:d}".format(matrix[array][element]), end=" ")
                    else:
                        print("{:d}".format(matrix[array][element]), end="\n")
            else:
                print("")
