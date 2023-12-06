#!/usr/bin/python3
"""Define a class_to_json function"""


def class_to_json(obj):
    """Definition of class_to_json function
    That returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object

    Args:
        obj: the giving object
    """
    return obj.__dict__
