#!/usr/bin/python3
# 2-rectangle.py
"""Define Rectangle class
    with two methods:
        area()
        perimeter()
"""


class Rectangle():
    """Definition of the class Rectangle

    Args:
        width: Optional by default 0
        height: Optional by default 0

    Methods:
        area(): returns the rectangle area
        perimeter(): returns the rectangle perimeter

    Exceptions:
        TypeError with msg 'width must be an integer'
        TypeError with msg 'height must be an integer'
        ValueError with msg 'width must be >= 0'
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

    def area(self):
        """area function returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter function returns the rectangle
            perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
