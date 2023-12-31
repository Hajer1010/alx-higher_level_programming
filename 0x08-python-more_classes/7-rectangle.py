#!/usr/bin/python3

"""
More Classes and Objects
"""


class Rectangle:
    """
    class Rectangle
    """
    __width = None
    __height = None
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__
        Arguments:
            width : width of rectangle
            height : height of rectangle
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width
            value: The new width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height
            value: The new height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter"""
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __repr__(self):
        """__repr__"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __str__(self):
        """__str__"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join([str(self.print_symbol) * self.__width] *
                         self.__height)

    def __del__(self):
        """__del__"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
