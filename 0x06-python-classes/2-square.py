#!/usr/bin/python3
"""
    Creating & defining a square class
"""


class Square:
    """ Defining a square class  """
    def __init__(self, size):
        """Initialization of instance attributes.

        Args: size (int): Size/unit length of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
