#!/usr/bin/python3
"""
You are not allowed to import any module
"""


class MyList(list):
    """
    a function that returns the list of available attributes
and methods of an object:
    Prototype: def lookup(obj):
    Returns a list object
    You are not allowed to import any module
    """

    def __init__(self):
        """initialise the object"""
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
