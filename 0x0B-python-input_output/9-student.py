#!/usr/bin/python3
"""
A module that defines the class Student
"""


class Student:
    """
    Class to create student instances
    """

    def __init__(self, first_name, last_name, age):
        """
        Student constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        A method to retrieves a dictionary representation of
        a Student instance
        """
        return self.__dict__.copy()
