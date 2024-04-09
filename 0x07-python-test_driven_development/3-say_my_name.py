#!/usr/bin/python3
"""Definition of name-printing function."""


def say_my_name(first_name, last_name=""):
    """Prints a name.
    Args:
        first_name (str): first name for printing.
        last_name (str): last name for printing.
    Raises:
        TypeError: If whether first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name should be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name should be a string")
    print("My name is {} {}".format(first_name, last_name))
