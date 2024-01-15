#!/usr/bin/python3

def read_file(filename=""):
    """ function reads n prints lines of a text file"""

    with open(filename) as f:
        lines = f.read()
    print(lines, end="")
