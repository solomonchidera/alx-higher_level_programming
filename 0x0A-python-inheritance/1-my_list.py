#!/usr/bin/python3
"""Define MyList class that inherite from list"""


class MyList(list):
    """Definition of MyList

    inherite from list class

    instance methods:
        print_sorted: that print the list in ascending order
    """

    def print_sorted(self):
        """prints the sorted list"""
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
