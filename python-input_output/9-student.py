#!/usr/bin/python3
"""Module 9-student: defines a class Student with a JSON description."""


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

    def to_json(self):
        """Return the dictionary representation of a Student instance."""
        return self.__dict__
