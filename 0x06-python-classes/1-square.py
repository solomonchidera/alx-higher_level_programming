#!/usr/bin/python3
# 1-square.py
""" Define a class square with a private attribute size."""


class Square:
    """ Definition of square class
    attributes : size (private)
    """
    def __init__(self, size):
        """Initialize square class and set size value"""
        self.__size = size
