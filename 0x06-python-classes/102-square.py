#!/usr/bin/python3
class Square:
    """
    Defines the properties of square by: (based on 3-square.py).

    Attributes:
        size: size of a square (1 side)
    """

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the Property size.

        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of square.

        Returns: the current square area.
        """
        return (self.__size * self.__size)

    def __lt__(self, other):
        """
        Comparison operator to compare if square area is less
        than another.

        Args:
            other (Square): square to compare size to.

        Returns: True or false.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
         Compares if square area is less
        than or equal to another.

        Args:
            other (Square): square to compare size to.

        Returns: True or false.
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """
         Compares if square area is equal to another.

        Args:
            other (Square): square to compare size to.

        Returns: True or false.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
         Compares if square area is not equal to another.

        Args:
            other (Square): square to compare size to.

        Returns: True or false.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
         Compares if square area is greatere than another.

        Args:
            other (Square): square to compare size to.

        Returns: True or false.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
         Compares if square area is greater than or equal to another.

        Args:
            other (Square): square to compare size to.

        Returns: True or false.
        """
        return self.area() >= other.area()
