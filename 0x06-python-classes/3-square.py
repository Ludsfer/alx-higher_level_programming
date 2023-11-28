#!/usr/bin/python3
"""This ia a documentation on the a Square class"""


class Square:
    """This is a Square class"""

    def __init__(self, size=0):
        """Constructor that initializes a square

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This returns the area of a Square"""
        return (self.__size * self.__size)
