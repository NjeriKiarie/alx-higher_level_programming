#!/usr/bin/python3
"""Module containing the function write_file"""


def write_file(filename="", text=""):
    """
    Write a function that writes a string to a text file (UTF8)
    and returns the number of characters written.
    """
    with open(filename, encoding='utf-8') as f:
        """This method returns the number of characters written to a file."""
        return f.write(text)
