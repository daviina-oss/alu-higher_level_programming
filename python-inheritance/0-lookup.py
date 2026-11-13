#!/usr/bin/python3
"""Module 0-lookup: defines a function that lists an object's attributes."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
