#!/usr/bin/python3
"""
Moduele: 4-from_json_string
Has function that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """ Returns JSON representation of an object (Python data structure) """
    return json.loads(my_str)
