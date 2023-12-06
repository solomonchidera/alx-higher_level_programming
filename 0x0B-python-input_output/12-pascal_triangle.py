#!/usr/bin/python3
"""Define pascal_triangle function"""


def pascal_triangle(n):
    """Definition of pascal_triangle function

    Returns a list of lists of integers representing
    the Pascal’s triangle
    """

    if n <= 0:
        return []

    my_triangles = [[1]]
    while len(my_triangles) != n:
        last = my_triangles[-1]
        next = [1]
        for i in range(0, len(last) - 1):
            next.append(last[i] + last[i + 1])
        next.append(1)
        my_triangles.append(next)
    return my_triangles
