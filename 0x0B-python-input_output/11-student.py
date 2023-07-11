#!/usr/bin/python3
"""
Module 9-student
defines a class Student
"""


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student using constructor method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary representation of the Student
        """
        if attrs is None:
            return self.__dict__
        else:
            diction = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    diction[att] = self.__dict__[att]
            return diction

    def reload_from_json(self, json):
        """
        Return:
            Transfer all attributes of json to self
        """
        for x, y in json.items():
            setattr(self, x, y)
