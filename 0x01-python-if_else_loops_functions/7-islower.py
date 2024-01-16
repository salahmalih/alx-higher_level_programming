#!/usr/bin/python3
"""function that checks for lowercase character."""

def islower(c):
    asci = ord(c)
    if asci >= 97 and asci <= 122:
        return True
    return False
