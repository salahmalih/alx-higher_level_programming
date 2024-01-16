#!/usr/bin/python3
"""prints a string in uppercase followed by a new line."""
def uppercase(str):
    for i in range(0, len(str)):
        c = ord(str[i])
        if c >= 97 and c <= 122:
            c = c - 32
        print("{}".format(chr(c)), end="")
    print("")
