#!/usr/bin/python3
# 101-locked_class.py
"""Define a LockedClass"""


class LockedClass:
    """Definition of LockedClass
        class that prevent the user from creating
        new instance attributes, except if the new
        instance attribute is called first_name.
    """
    __slots__ = ["first_name"]
