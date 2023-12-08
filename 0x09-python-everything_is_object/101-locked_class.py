#!/usr/bin/python3
"""A locked class implementation wiht no class object or attribute"""


class LockedClass:
    """Allow only instatiation of an attribute called first_name"""
    __slots__ = ('first_name')
