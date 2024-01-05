#!/usr/bin/python3
"""LockedClass defintion"""


class LockedClass:
    """
    A locked class that only lets the user dynamically create the instance
    attribute 'first_name'
    """

    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new instances of Locked Class."""

        self.first_name = "first_name"
