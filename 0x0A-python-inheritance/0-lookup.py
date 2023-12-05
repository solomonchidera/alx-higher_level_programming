#!/usr/bin/python3
"""Define a lookup(object) function"""


def lookup(obj):
    """Definition of lookup function
    Args:
        obj: Required

    Returns: a list of the available attributes and methods
    of the object
    """
    return dir(obj)
