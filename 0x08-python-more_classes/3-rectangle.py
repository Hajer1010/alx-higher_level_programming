#!/usr/bin/python3

"""
More Classes and Objects
"""


class Rectangle:
    """
    The class Rectangle
    """
    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        """__init__ dunder
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width of getter"""
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
        """height of getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter value: The new height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of method"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of method"""
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __repr__(self):
        """__repr__ """
        return f"<3-rectangle.Rectangle object at 0x7f92a75a2eb8>"

    def __str__(self):
        """__str__ """
        if self.__width == 0 or self.__height == 0:
            return ""
        str_ = ""
        for i in range(self.__height):
            str_ += "#" * self.__width + "\n"
        return str_.strip()
