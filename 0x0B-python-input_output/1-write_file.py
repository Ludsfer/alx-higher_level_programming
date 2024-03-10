#!/usr/bin/python3
"""
A script that implements a function to write to a file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of
    characters written

    Args:
        filename: Name of the file
        text:     The string to be written to file
    """
    with open(filename, mode='w', encoding='utf-8') as txt_file:
        char_count = txt_file.write(text)
    return char_count
