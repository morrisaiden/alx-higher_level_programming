#!/usr/bin/python3
"""add_integer module"""


def add_integer(a, b=98):
    """Adds two integers.

    Arguments:
        a: first int.
        b: second int.

    Raises:
        TypeError: if a, b are != int/float.

    Returns:
        sum of a and b.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
