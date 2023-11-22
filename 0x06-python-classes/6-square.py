#!/usr/bin/python3
# 5-square.py
"""Define Square class."""


class Square:
    """Definition of the Square class
    fields:
    size Optional by default 0
        if size < 0 raise ValueError with msg "size must be >= 0"
        if size is not integer raise TypeErrot with msg
                                "size must be an integer"
    position: the position of the square - by default (0, 0)

    methods:
    area : function that returns the area of the current square
    getter and setter of size field
    getter and setter of position field
    my_print : function that prints a square with the character #
    """

    def __init__(self, size=0, position=(0, 0)):
        """function that initialise square fields"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter of position field"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter of position field"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(val, int) for val in value) or
                not all(val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """function that prints a square in stdout with the
        character #
        if size = 0 that we print an empty line"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for k in range(0, self.__position[0])]
            [print("#", end="") for j in range(0, self.__size)]
            print("")
