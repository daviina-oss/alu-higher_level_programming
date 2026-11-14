#!/usr/bin/python3
"""Module 12-pascal_triangle: builds Pascal's triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle.

    Args:
        n: the number of rows. An empty list is returned if n <= 0.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for _ in range(n - 1):
        prev = triangle[-1]
        triangle.append([1] + [prev[i] + prev[i + 1]
                               for i in range(len(prev) - 1)] + [1])
    return triangle
