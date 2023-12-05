#!/usr/bin/python3
"""Define inherits_from function"""


def inherits_from(obj, a_class):
    """Definition of inherits_from function
    That returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class;
    otherwise False

    Args:
        obj, a_class
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
