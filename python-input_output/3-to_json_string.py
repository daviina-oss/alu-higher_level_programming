#!/usr/bin/python3
"""Module 3-to_json_string: converts an object to a JSON string."""
import json


def to_json_string(my_obj):
    """Return the JSON representation (a string) of an object."""
    return json.dumps(my_obj)
