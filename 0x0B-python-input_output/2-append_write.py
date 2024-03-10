#!/usr/bin/python3
"""
A module to append at the end of a file.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns
    the number of characters added

    Args:
        filename: Name/path to file to edit
        text:     The text to append to file
    """
    with open(filename, mode='a', encoding='utf-8') as txt_file:
        char_count = txt_file.write(text)
    return char_count
