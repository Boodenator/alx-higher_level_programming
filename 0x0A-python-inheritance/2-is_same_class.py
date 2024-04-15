#!/usr/bin/python3
"""Defines the class-checking function."""


def is_same_class(obj, a_class):
    """Check if the object is an instance of a given class.
    Argumts:
        obj (any): is the object to check.
        a_class (type): is he class to match the type of obj to.
    Returns:
        If obj is an instance of a_class - True.
        Otherwise - False.
    """

    if type(obj) == a_class:
        return True
    return False
