#!/usr/bin/python3
"""
module: 2-is_same_class.
Returns True if the object is an instance of or
if the object is an instance of a class that inherited from
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    function is_kind_of_class
    urguments:
      obj: an object
      a_class: a class
      Returns: Bool
    """
    return isinstance(obj, a_class)
