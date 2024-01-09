#!/usr/bin/python3
"""
module t0-json_string that returns the JSON representation of an object (string)
"""

import json


def to_json_string(my_obj):
    """
     returns JSON representation
    """
    return json.dumps(my_obj)
