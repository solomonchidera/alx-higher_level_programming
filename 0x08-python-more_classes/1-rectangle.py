#!/usr/bin/python3
# 1-rectangle.py
"""Define a Rectangle class"""


class Rectangle():
    """Definition of Rectangle class

    Args:
        width: Optional by default 0
        height: Optional by default 0

    Exceptions:
        TypeError with msg 'width must be an integer'
        ValueError with msg 'width must be >= 0'
        TypeError with msg 'height must be an integer'
        ValueError with msg 'height must be >= 0'
    """
    def __init__(self, width=0, height=0):
        """Initialize Rectangle attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width attribute getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width attribute setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height attribute getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height attribute setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
