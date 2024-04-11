#!/usr/bin/python3
"""Definition of square-printing function."""


def print_square(size):
    """Printing square including the # character.
    Args:
        size (int): The hight/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
