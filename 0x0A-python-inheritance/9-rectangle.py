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

    def area(self):
        """return the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return a Rectangle string representation"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
