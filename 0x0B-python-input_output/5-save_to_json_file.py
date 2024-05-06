#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation.
    Args:
        my_obj (type): Object to write to text file.
        filename (str): name of the file.

    Returns:
        type: JSON representation.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
        # or  json_object = json.dumps(my_obj)
