#!/usr/bin/python3

"""file-appending function."""


def append_write(filename="", text=""):
    """string to the end of a UTF8 text file is being appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
