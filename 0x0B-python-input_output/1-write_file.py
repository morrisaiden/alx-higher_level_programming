#!/usr/bin/python3
"""
module write file that writes a string to a text file and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    module write_file

    """
    with open(filename, 'w') as f:
        return f.write(text)
