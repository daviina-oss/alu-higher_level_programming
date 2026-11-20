#!/usr/bin/python3
"""Module 100-append_after: inserts text after lines containing a string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing a specific string.

    Args:
        filename: the UTF8 text file to update.
        search_string: the string to look for in each line.
        new_string: the text inserted after each line that contains
            search_string.
    """
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
