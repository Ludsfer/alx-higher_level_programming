#!/usr/bin/python3
"""
A module that implements a function to deserialize
a JSON string to object.
"""


def from_json_string(my_str: str) -> object:
    """
    Returns a JSON representation of a python data structure.

    Args:
        my_str: A JSON string

    Returns:
        A Python object.
    """
    import json

    return json.loads(my_str)
