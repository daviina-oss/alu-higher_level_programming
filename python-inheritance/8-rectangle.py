#!/usr/bin/python3
"""Module 8-rectangle: defines a class Rectangle based on BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a rectangle.

        Args:
            width: the width (positive integer).
            height: the height (positive integer).
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
