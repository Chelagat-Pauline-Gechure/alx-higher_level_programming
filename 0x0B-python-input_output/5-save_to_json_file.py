#!/usr/bin/python3
"""
Moduele: 5-save_to_json_file
Has function that that writes an Object to a text file,
using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
