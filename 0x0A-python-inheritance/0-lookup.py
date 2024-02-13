#!/usr/bin/python3
"""
Module with method class lookup
"""


def lookup(obj):
    """
    a function that returns the list of available attributes
and methods of an object:
    Prototype: def lookup(obj):
    Returns a list object
    You are not allowed to import any module
    """
    return dir(obj)
