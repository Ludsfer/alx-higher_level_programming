#!/usr/bin/python3
"""A documentation of the Square class"""


class Square:
    """This is the definition of the Square class"""

    def __init__(self, size=0):
        """Construct a square class

        Args:
            size (int): The size of the new square
        """
        self.size = size

    @property
    def size(self):
        """An attribute that returns the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This returns the area of the square"""
        return (self.__size * self.__size)
