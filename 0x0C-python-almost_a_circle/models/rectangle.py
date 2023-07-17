#!/usr/bin/python3
""" Module: Rectangle """

from models.base import Base


class Rectangle(Base):
    """ Defines the Retangle class. """
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

        Errors:
            TypeError: If the input of width, height, x or y is not an integer.
            ValueError: If width or height <= 0.
            ValueError: If of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Set rectangle's width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Validate the rectangle's width """
        if type(value) != int:
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
        """ Validate the rectangle's height """
        if type(value) != int:
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
        """ Validate the x coordinate. """
        if type(value) != int:
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
        """ Validate the y coordinate. """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # 4. Area first
    def area(self):
        """ Calculate and return Rectangle's area. """
        return self.width * self.height

    # 5. Display #0
    def display(self):
        """Print the Rectangle using the `#` to stdout."""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    # 6. __str__
    def __str__(self):
        """ Updating Rectangle by overriding the __str__ method. """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    # 8. Update #0
    def update(self, *args, **kwargs):
        """Updating Rectangle class.

        Args:
            *args (tuple): New attribute values.
                - 1st argument should be the id attribute
                - 2nd argument should be the width attribute
                - 3rd argument should be the height attribute
                - 4th argument should be the x attribute
                - 5th argument should be the y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Returning the dictionary representation of the Rectangle."""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width,
        }
