#!/usr/bin/python3
"""Define save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Definition of save_to_json_file function
    That writes an Object to a text file, using a
    JSON representation

    Args:
        my_obj: the giving object
        filename: the name of the file
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
