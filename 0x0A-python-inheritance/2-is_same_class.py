#!/usr/bin/python3
"""
Module 2-is_same_class.
Checks whether an object is exactly an instance of a class.
"""


def is_same_class(obj, a_class):
    """
    Fn to determine if obj is an instance of a_class.

    Arguments:
          obj: object to look at
          a_class: class to verify the instance of

    Returns: True if obj is an instance of a_class,
             Else: False
    """

    return True if type(obj) is a_class else False
