#!/usr/bin/python3
"""Module 4-inherits_from: checks if an object inherits from a class."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    An instance of a_class itself does not count, only instances of classes
    that inherit (directly or indirectly) from it.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
