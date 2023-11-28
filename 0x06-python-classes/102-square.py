#!/usr/bin/python3
"""A documentation of the square class"""


class Square:
    """This defines a square class"""

    def __init__(self, size=0):
        """constructs a new square upon instanciation

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """An attriibute that returns the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """This defines the area of a square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """This returns a boolean value based on == operator"""
        return self.area() == other.area()

    def __ne__(self, other):
        """This returns a boolean value based on != operator"""
        return self.area() != other.area()

    def __lt__(self, other):
        """This returns a boolean value based on < operator"""
        return self.area() < other.area()

    def __le__(self, other):
        """This returns a boolean value based on <= operator"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """This return a boolean value based on > operator"""
        return self.area() > other.area()

    def __ge__(self, other):
        """This returns a boolean value based on >= operator"""
        return self.area() >= other.area()
