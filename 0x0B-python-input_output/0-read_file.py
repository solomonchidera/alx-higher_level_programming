#!/usr/bin/python3
"""Define read_file function"""


def read_file(filename=""):
    """Definition of read_file function
        That reads a text file (UTF8) and prints it to
        stdout

        Args:
            filename : optional the name of the file
    """
    with open(filename) as file:
        print(file.read(), end="")
