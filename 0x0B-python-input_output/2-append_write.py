#!/usr/bin/python3
"""module append_file.py
appends a str to a text file"""


def append_write(filename="", text=""):
    """Appends a string to the end of a text file.
    Argumentss:
        filename: The name of the file to append to.
        text : The string to append to the file.
    Returns:
        No of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
