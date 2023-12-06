#!/usr/bin/python3
"""Define a Student class"""


class Student():
    """Definition of Student class

    Attributes:
        first_name
        last_name
        age

    Methods:
        to_json: that retrieves a dictionary representation of
        a Student instance
    """

    def __init__(self, first_name, last_name, age):
        """Initialize Student attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of Student instance"""
        return self.__dict__
