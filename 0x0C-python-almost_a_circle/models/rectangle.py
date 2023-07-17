#!/usr/bin/python3
""" Module: Rectangle """

from models.base import Base


class Rectangle(Base):
    """ Defines the Rectangle class that inherits frm Base class. """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Rectangle object initialization.

        Args:
        self: reference of newly created object
        width (int): rectangle's width
        height (int): rectangle's height
        x (int, optional) : x-coordinate of rectangle's top-left corner.
        y (int, optional) : y-coordinate of rectangle's top-left corner.
        id (optional): rectangle's unique identifier
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """ Set rectangle's width. """
            return self.__width

        @width.setter
        def width(self, value):
            """ Checks the rectangle's width """
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """ Set rectangle's height. """
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """ Set rectangle's x coordinate. """
            return self.__x

        @x.setter
        def x(self, value):
            if type(value) is not int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """ Set rectangle's y coordinate. """
            return self.__y

        @y.setter
        def y(self, value):
            if type(value) is not int:
                return TypeError("y must be an integer")
            if value < 0:
                return ValueError("y must be >= 0")
