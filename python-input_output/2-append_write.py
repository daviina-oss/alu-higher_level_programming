#!/usr/bin/python3
"""Module 2-append_write: defines a function that appends to a text file."""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF8 text file.

    The file is created if it does not exist.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
