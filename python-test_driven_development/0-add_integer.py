#!/usr/bin/python3
"""Module 0-add_integer.

Defines add_integer(a, b=98), a function that adds two numbers.
The numbers can be integers or floats; floats are cast to integers.
"""


def add_integer(a, b=98):
    """Add two numbers and return the sum as an integer.
    Floats are cast to integers first.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
