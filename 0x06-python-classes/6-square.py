#!/usr/bin/python3
"""
Defines class Square with private size and position; and public area

"""


class Square:
    """
    class Square definition

    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes square
        Attributes:
            size (int): defaults to 0 if none; don't use __size to call setter
            position (int): tuple of two positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """"
        Getter function for private attribute size.
        Return: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter function for private attribute size.
        Args:
            value: sets size to value if int and >= 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """"
        Getter function for private attribute position.
        Return: position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter function for private attribute position.

        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates area of square
        """
        return (self.__size)**2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join([" " * self.__position[0] +
                             "#" * self.__size
                             for rows in range(self.__size)]))
