#!/usr/bin/python3
"""Define a class BaseGeometry with a area method"""


class BaseGeometry():
    """Definition of BaseGeometry class

    methods:
        area: that raises an Exception with msg:
            area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")
