#!/usr/bin/python3
"""Module 11-square: defines a class Square with its own description."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a square.

        Args:
            size: the size of a side (positive integer).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the description [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
