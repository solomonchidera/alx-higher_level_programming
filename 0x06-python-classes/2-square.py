#!/usr/bin/python3
# 2-square.py
"""Define square class"""


class Square:
    """ Square class
    args:
    size Optional 0 by default.
    if size < 0 --> raise ValueError with msg : size must be >= 0.
    if size is not integer --> raise TypeError with
                            msg : size must be an integer.
    """

    def __init__(self, size=0):
        """Function to initialize square attribute size.
            if size < 0 raise ValueError
            if size is not integer raise TypeError
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
