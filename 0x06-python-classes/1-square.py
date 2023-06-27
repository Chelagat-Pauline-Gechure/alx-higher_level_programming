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
        self.__size = size
