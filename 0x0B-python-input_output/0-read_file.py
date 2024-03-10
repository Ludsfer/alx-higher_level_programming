#!/usr/bin/python3
"""
A module that implements a file reading function.
"""


def read_file(filename=""):
    """
    A function that reads a text file (UTF8) and prints it to stdout.
    Args:
        filename (str): Name of file.
    """
    if isinstance(filename, str):
        with open(filename, mode='r', encoding='utf-8') as txt_file:
            print(txt_file.read(), end="")
