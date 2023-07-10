#!/usr/bin/python3
"""Only sub class of"""


def inherits_from(obj, a_class):
    """
        Checks if `obj` is an instance of a subclass of `a_class`
        but not exactly an instance of `a_class` itself.

    Args:
        obj: object to verify.
        a_class: class to match obj
    Returns:
        True: if object is exact match
        False: otherwise
    """
    return isinstance(obj, a_class) and type(obj) != a_class
