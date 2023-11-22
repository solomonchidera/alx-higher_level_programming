#!/usr/bin/python3
# 3-square.py
"""Define Square class"""


class Square:
    """ Definition of Square class
    fields:
    size Optional by default : 0
    if size < 0 raise ValueError with message "size must be >= 0"
    if size is not an integer raise TypeError with message:
                            "size must be an integer
    methods:
        area : that returns the area of the current square
    """

    def __init__(self, size=0):
        """Function to initialise Square fields"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Function that return the area of the current square"""
        return self.__size**2
