#!/usr/bin/python3
"""
define function to write a string to text (UTF8) then return total of characters written
"""


def write_file(filename="", text=""):
    """ module write_file
    """
    with open(filename, 'w') as f:
        return f.write(text)
