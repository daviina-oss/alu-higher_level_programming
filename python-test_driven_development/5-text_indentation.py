#!/usr/bin/python3
"""Module 5-text_indentation.

Defines text_indentation(text), a function that prints a text with two new
lines after each of the characters . ? and :
"""


def text_indentation(text):
    """Print text with 2 new lines after each ., ? and : character.
    Spaces at the beginning and at the end of each printed line are removed.
    text must be a string, otherwise a TypeError is raised.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        if char in ".?:":
            print((line + char).strip(" "), end="\n\n")
            line = ""
        elif char == "\n":
            print(line.strip(" "))
            line = ""
        else:
            line += char
    print(line.strip(" "), end="")
