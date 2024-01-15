#!/usr/bin/python3

def read_file(filename=""):
    """ function reads n prints lines of a text file (UTF8) prints it stdout """

    with open(filename) as f:
        lines = f.read()
    print(lines, end="")

