#!/usr/bin/python3
""" Module defines a class Student """


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """ Initializes a new Student using constructor method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns dictionary representation of the Student """
        return self.__dict__
