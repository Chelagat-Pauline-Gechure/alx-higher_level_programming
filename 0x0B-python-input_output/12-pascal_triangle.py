#!/usr/bin/python3
"""
Module:
Defines Pascal's Triangle function
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    pas_triangles = [[1]]
    while len(pas_triangles) != n:
        triangle = pas_triangles[-1]
        temporary = [1]
        for i in range(len(triangle) - 1):
            temporary.append(triangle[i] + triangle[i + 1])
        temporary.append(1)
        pas_triangles.append(temporary)
    return pas_triangles
