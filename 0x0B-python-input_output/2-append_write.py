#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """appends a string to the end of a UTF8 text file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
