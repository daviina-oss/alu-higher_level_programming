#!/usr/bin/python3
"""Module 5-square: defines a class Square that can print itself."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size: the size of the square (integer >= 0).
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
