#!/usr/bin/python3
"""
A module that implements the JSON representation of an object.
"""


def to_json_string(obj: str) -> str:
    """
    Returns a JSON representation of the passed string object.

    Args:
        obj: A passed string object
    """
    import json

    return json.dumps(obj)
