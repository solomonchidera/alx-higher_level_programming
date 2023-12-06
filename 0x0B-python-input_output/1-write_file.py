#!/usr/bin/python3
"""Define write_file function"""


def write_file(filename="", text=""):
    """Definition of write_file function
        That writes a string to a text file (UTF8) and
        returns the number of characters written

        Args:
            filename : the name of the file (Optional)
            text: The text to be writing in the file (Optional)
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)