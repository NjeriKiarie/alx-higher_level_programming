#!/usr/bin/python3
"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure.
    Args:
        obj (MyClass): object.

    Returns:
        dict: dictionary.
    """
    return obj.__dict__
