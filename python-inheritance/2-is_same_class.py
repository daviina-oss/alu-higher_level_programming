#!/usr/bin/python3
"""Module 2-is_same_class: checks if an object is exactly of a class."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class, else False."""
    return type(obj) is a_class
