#!/usr/bin/python3
"""Define is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Definition of is_kind_of_class function
    That returns True if the object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class ;
    otherwise False

    Args:
        obj, a_class
    """
    return isinstance(obj, a_class)
