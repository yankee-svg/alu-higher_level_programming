#!/usr/bin/python3
"""Are you documented ?"""


def append_write(filename="", text=""):
    """How far """
    with open(filename, 'a+') as f:
        return f.write(text)
