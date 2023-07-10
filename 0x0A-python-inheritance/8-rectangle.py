#!/usr/bin/python3

""" Rectangle class Module """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Define the Rectangle class """

    def __init__(self, width, height):
        """Initialize rectangle method"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
