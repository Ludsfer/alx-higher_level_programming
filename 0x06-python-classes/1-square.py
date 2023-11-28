#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """A Square class"""

    def __init__(self, size):
        """A Square constructor with a private variable size

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
