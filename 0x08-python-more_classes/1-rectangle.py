#!/usr/bin/python3
"""Rectangle class definition."""


class Rectangle:
    """rectangle reprsentation."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): new rectangle width.
            height (int): new rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width should be an integer")
        if value < 0:
            raise ValueError("width shoulf be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height shld be an integer")
        if value < 0:
            raise ValueError("height shld be >= 0")
        self.__height = value
