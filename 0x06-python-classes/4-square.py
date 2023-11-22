#!/usr/bin/python3
# 4-square.py
"""Define Square class."""


class Square:
    """Definition of the Square class
    fields:
    size Optional by default 0
    if size < 0 raise ValueError with msg "size must be >= 0"
    if size is not integer raise TypeErrot with msg
                                "size must be an integer"
    methods:
    area : function that returns the area of the current square
    getter and setter of size
    """

    def __init__(self, size=0):
        """function that initialise size field"""
        self.__size = size

    def area(self):
        """function that returns the area of the current square"""
        return self.__size**2

    @property
    def size(self):
        """getter of size field"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter of size field"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
