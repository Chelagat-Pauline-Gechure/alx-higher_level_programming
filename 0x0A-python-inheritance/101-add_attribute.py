#!/usr/bin/python3
""" Add new attribute module"""


def add_attribute(obj, name, value):
    """ Checks if the attribute can be added and if
    it is possible
    """
    if hasattr(obj, "__dict__") or \
       (hasattr(obj, "__slots__") and name in obj.__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
