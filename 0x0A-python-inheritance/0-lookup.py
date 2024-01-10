#!/usr/bin/python3
"""
module 0-lookup.
returns the list of methods and attributes in an object
"""


def lookup(obj):
    """
    function: lookup()
    Returns a list object
    """
    return dir(obj)
