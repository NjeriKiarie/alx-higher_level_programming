#!/usr/bin/python3
"""
Module 10-square.py
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The class inherits from Rectangle class """

    def __init__(self, size):
        """ Constructor of the instaance """
        if self.integer_validator('size', size):
            self.__size = size
        super().__init__(size, size)

    def area(self):
        """ method defines the area of Square object"""
        return super().area()
