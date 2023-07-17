#!/usr/bin/python3
""" Module: Square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines the Square class. """
    def __init__(self, size, x=0, y=0, id=None):
        """
        New Square object initialization.

        Args:
        self: reference of newly created object
        size (int): square's width/length
        x (int, optional) : x-coordinate of rectangle's top-left corner.
        y (int, optional) : y-coordinate of rectangle's top-left corner.
        id (optional): rectangle's unique identifier
        """
        super().__init__(size, size, x, y, id)

    # 10. And now, the Square!
    def __str__(self):
        """ Overloading __str__ method  """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    # 11. Square size
    @property
    def size(self):
        """ Set Square's size. """
        return self.width

    @size.setter
    def size(self, value):
        """ Validate the rectangle's width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

# 12. Square update
    def update(self, *args, **kwargs):
        """
        Updating Square class.

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
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Returning the dictionary representation of Square. """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y
        }
