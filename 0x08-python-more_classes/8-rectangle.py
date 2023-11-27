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

    """ Class attribute """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Constructor """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Retrieves Information Stored in Attributes """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the private variabe width to the value of the attribute """
        if not isinstance(value, int):
            """ Checks for thetype error """
            raise TypeError("width must be an integer")
        if value < 0:
            """ Checks for value error """
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Retrieves Information Stored in Attributes """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the private variable height to the value of the attribute """
        if not isinstance(value, int):
            """ Checks for type error """
            raise TypeError("height must be an integer")
        if value < 0:
            """ Checks for value error """
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Computes the area of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ Computes the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return a string representation of the rectangle.

        Rectangle is printed with the character `#`
        """

        if self.__width == 0 or self.__height == 0:
            return ''
        for i in range(self.__height):
            if i < self.__height - 1:
                print(str(self.print_symbol) * self.__width)
            else:
                print(str(self.print_symbol) * self.__width, end='')
        return ''

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """ Destuctor """
        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ A static method that returns the biggest
        rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1.area()
        else:
            return rect_2.area()
