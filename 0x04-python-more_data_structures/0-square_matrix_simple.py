#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with same size as input
    result = [[0]*len(row) for row in matrix]

# Computing the square value for each integer
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = matrix[i][j]**2
    return result
