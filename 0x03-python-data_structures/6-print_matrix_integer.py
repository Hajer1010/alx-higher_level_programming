#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for _matrix_integer in matrix:
        if len(_matrix_integer) == 0:
            print()
        for i in range(len(_matrix_integer)):
            print("{:d}".format(_matrix_integer[i]),
                  end="\n" if i is len(_matrix_integer) - 1 else " ")
