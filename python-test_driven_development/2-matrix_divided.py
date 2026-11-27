#!/usr/bin/python3
"""Module 2-matrix_divided.

Defines matrix_divided(matrix, div), a function that divides every element
of a matrix (a list of lists of integers or floats) by a number.
"""


def matrix_divided(matrix, div):
    """Divide all the elements of a matrix by div.
    Each result is rounded to 2 decimal places and a new matrix is returned.
    Raises TypeError for a bad matrix or div, ZeroDivisionError if div is 0.
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(message)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(message)
        for number in row:
            if not isinstance(number, (int, float)):
                raise TypeError(message)
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(number / div, 2) for number in row] for row in matrix]
