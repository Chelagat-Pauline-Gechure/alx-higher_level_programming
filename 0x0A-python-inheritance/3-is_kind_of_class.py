#!/usr/bin/python3

""" Module to check whether it is the same class 
    or it inherits from another """


def is_kind_of_class(obj, a_class):
    """ Check if the object is an instance of 'a_class' or 'object'
    Args:
        obj: object to verify.
        a_class: class to match obj
    Returns:
        True: if object is exact match
        False: otherwise """
    return isinstance(obj, a_class)
