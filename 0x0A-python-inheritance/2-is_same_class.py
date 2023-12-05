#!/usr/bin/python3
"""Define a function is_same_class"""


def is_same_class(obj, atype):
    """Definition of is_same_class function
    That return True if obj is an instance of atype
    and False otherwize
    """
    return type(obj) == atype
