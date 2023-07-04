#!/usr/bin/python3
def matrix_divided(matrix, div):
"""
    Check if matrix is a list of lists of integers or floats
    Check if each row of the matrix has the same size
    Check if div is a number (integer or float)
    Check if div is not equal to zero
    Perform division and round the result to 2 decimal places
    Return the new matrix
"""
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_lengths = set(len(row) for row in matrix)
    if len(row_lengths) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return new_matrix
