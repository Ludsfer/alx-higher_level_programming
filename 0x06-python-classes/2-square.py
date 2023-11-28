#!/usr/bin/python3
"""A Square class that checks fo rthe right input"""


class Square:
    """This is a Square"""

    def __init__(self, size=0):
        """Constructs the square

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
