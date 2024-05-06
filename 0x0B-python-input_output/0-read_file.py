#!/usr/bin/python3
"""Module containing the function read_file"""


def read_file(filename=""):
    """ function reads n prints lines of a text file"""

    with open(filename, 'r', encoding="utf-8") as f:
        lines = f.read()
    print(lines, end="")
