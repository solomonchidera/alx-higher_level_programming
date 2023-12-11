#!/usr/bin/python3
"""Define the Square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Definition of Square class that inherits from Rectangle

    Attributes:
        id: square identifier
        size: square size
        x, y: square position
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialise Square attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of a square"""
        return "[Square] (" + str(self.id) + ") " + str(self.x) + "/" \
            + str(self.y) + " - " + str(self.width)

    @property
    def size(self):
        """getter of the square size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of the square size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """that assigns attributes:
        *args is the list of arguments - no-keyworded arguments:
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        **kwargs can be thought of as a double pointer to a
        dictionary: key/value (keyworded arguments)
        """
        if args is not None and len(args) != 0:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        attrs = ["id", "size", "x", "y"]
        return {attr: getattr(self, attr) for attr in attrs}
