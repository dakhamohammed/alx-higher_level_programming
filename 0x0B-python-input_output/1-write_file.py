#!/usr/bin/python3
"""function that write to text file"""


def write_file(filename="", text=""):
    """write to a UTF8 text file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
