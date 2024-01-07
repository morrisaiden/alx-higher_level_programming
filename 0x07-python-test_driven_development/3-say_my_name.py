#!/usr/bin/python3
"""
Module say_my_name
Prints first name and last name from user.
"""


def say_my_name(first_name, last_name=""):
    """Prints <first_name>
    and <last_name>.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
