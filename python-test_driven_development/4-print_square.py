#!/usr/bin/python3
"""Module 4-print_square.

Defines print_square(size), a function that prints a square with the
character #.
"""


def print_square(size):
    """Print a square of size x size with the character #.
    size must be an integer (TypeError otherwise) and at least 0
    (ValueError otherwise).
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
