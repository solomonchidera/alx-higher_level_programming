#!/usr/bin/python3
"""Define a BaseGeometry class
    with methods: area(), integer_validator()
"""


class BaseGeometry():
    """Definition of the BaseGeometry class

    Instance methods:
        area: raises an Exception with msg
            'area() is not implemented'
        integer_validator: that validates value
            args: name, value
            Exceptions:
                TypeError: <name> must be an integer
                ValueError: <name> must be greater than 0
    """

    def area(self):
        """raises an Exception with the message:
        'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """That validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
