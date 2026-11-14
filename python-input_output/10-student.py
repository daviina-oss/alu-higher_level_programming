#!/usr/bin/python3
"""Module 10-student: defines a class Student with a filtered description."""


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
