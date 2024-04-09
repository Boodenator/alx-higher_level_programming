#!/usr/bin/python3
"""Definition of locked class."""


class LockedClass:
    """
    Prevention of user to instantiation of new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
