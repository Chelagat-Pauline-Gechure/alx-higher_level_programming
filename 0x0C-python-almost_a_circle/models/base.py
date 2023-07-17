#!/usr/bin/python3
""" Module: Base"""

import json
import csv
import turtle
import os
from pathlib import Path


# 1. Base class
class Base:
    """ This class will be the “base” of all other classes in this project.
    It's goals is to manage all "id" attribute of future classes. """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # 15. Dictionary to JSON string
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Serializses list of dictionaries to JSON string.
        Args: list of dictionaries called list_dictionaries
        Returns: JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
