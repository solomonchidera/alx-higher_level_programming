#!/usr/bin/python3
"""Define from_json_string function"""
import json


def from_json_string(my_str):
    """Definition of from_json_string function
    that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str : the string to be converted
    """
    return json.loads(my_str)
