#!/usr/bin/python3
"""Module 1-write_file: defines a function that writes to a text file."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file, overwriting any existing content.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
