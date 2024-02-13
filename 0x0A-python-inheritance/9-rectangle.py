#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
module with class BaseGeometry
"""

class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    (7-base_geometry.py). (task based on 8-rectangle.py)
    """

    def __init__(self, width, height):
        """Method for initializing the attrubutes"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Redefines an area method in the parent class"""

        return self.__width * self.__height

    def __str__(self):
        """__str__ method returns the next string"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
