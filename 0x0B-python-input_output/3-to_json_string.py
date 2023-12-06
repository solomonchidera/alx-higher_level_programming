#!/usr/bin/python3
"""Define append_write function"""


def append_write(filename="", text=""):
    """Definition of append_write function
        That writes a string to a text file (UTF8) and
        returns the number of characters written

        Args:
            filename : the name of the file (Optional)
            text: The text to be writing in the file (Optional)
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
