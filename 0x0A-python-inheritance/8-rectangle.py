#!/usr/bin/python3
 """
 Module containing rectangle base_geometry
 """
 BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry(7-base_geometry.py)
    """

    def __init__(self, width, height):
         """Initilizes the rectangle method"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
