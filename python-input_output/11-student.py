#!/usr/bin/python3
"""Module 11-student: defines a Student that can be saved and reloaded."""


class Student:
    """A student defined by a first name, a last name and an age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student.

        Args:
            first_name: the first name of the student.
            last_name: the last name of the student.
            age: the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of a Student instance.

        Args:
            attrs: optional list of strings. If given, only the attributes
                whose name is in this list are retrieved. Otherwise, all
                attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace the attributes of the instance from a dictionary.

        Args:
            json: a dictionary whose keys are public attribute names and
                whose values are the attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
