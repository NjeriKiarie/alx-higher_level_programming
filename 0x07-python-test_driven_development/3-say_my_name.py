#!/usr/bin/python3

"""
Module gives a function that prints say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """Prints 'my name is' followed by the
    first name and last name(optional)
    """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print('My name is', first_name, last_name)
