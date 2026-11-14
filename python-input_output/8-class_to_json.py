#!/usr/bin/python3
"""Module 8-class_to_json: describes an object as a serializable dict."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    All attributes of the object are assumed to be serializable: list,
    dictionary, string, integer or boolean.
    """
    return obj.__dict__
