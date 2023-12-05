#!/usr/bin/python3
"""Define a Square class that inherite from
    Rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of Square class
        That inherite from Rectangle

        Args: size (required)

        Methods:
            area
            str
    """

    def __init__(self, size):
        """initialize Square attribute"""
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)

    def area(self):
        """returns the square area"""
        return Rectangle.area(self)

    def __str__(self):
        """returns a string representation of Square"""
        return "[Square]" + Rectangle.__str__(self)[11:]
