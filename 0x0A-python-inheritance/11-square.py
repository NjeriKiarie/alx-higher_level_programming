#!/usr/bin/python3
"""
Square class Module 11-square.py
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inherits from Rectangle """

    def __init__(self, size):
        """ Constructor  theat initailises the class"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method returns area of a square"""
        return self.__size ** 2

    def __str__(self):
        """ print(self) method """
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
