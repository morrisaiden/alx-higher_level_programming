#!/usr/bin/python3
"""
Module 6-load_from_json_file.
Creates an Object from 'JSON file'.
"""


import json


def load_from_json_file(filename):
    """Creates an object from filename.
    Arguments:
        filename: name of the JSON file
    Returns: the object
    """

    with open(filename, 'r') as f:
        return json.load(f)
