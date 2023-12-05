#!/usr/bin/python3
"""Define a Rectangle class that inherite from
    BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Definition of Rectangle class"""

    def __init__(self, width, height):
        """ Initialize Rectangle attributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
