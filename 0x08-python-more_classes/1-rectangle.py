#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:

    """ Initialize the rectangle class
    Args:
        width: represents the width of the rectangle
        height: represents the height of the rectangle
    Raises:
        TypeError: if size is not integer
        ValueError: if size is < 0
    """
    def __init__(self, width=0, height=0):
        """ Constructor """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieves Information Stored in Attributes """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the private variabe width to the value of the attribute """
        if value < 0:
            """ Checks for value error """
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            """ Checks for thetype error """
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """ Retrieves Information Stored in Attributes """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the private variable height to the value of the attribute """
        if value < 0:
            """ Checks for value error """
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            """ Checks for type error """
            raise TypeError("height must be an integer")
        self.__height = value
