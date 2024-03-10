#!/usr/bin/python3
"""
A module that implements a function to return a dictionary description
for a JSON serialization of an object
"""


def class_to_json(obj):
    """
    Function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
