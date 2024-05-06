#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file.
    Args:
        filename (str): name of the file.
    Returns:
        object: object.
    """
    with open(filename) as f:
        return json.load(f)
