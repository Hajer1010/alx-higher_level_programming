#!/usr/bin/python3

"""
    more Classes and Objects in Python
"""


class Rectangle:
    """
    def __init__(self, width=0, height=0):
    """
    def __init__(self, width=0, height=0):
        """
            width : the width of rectangle
            height : the height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
            value: The new width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
            value: The new height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
