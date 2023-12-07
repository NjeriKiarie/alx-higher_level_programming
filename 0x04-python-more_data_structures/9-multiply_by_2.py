#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """A function that returns a new dictionary with
    all values multiplied by 2."""
    new_d = a_dictionary.copy()
    list_keys = list(new_d.keys())

    for i in list_keys:
        new_d[i] *= 2

    return (new_d)
