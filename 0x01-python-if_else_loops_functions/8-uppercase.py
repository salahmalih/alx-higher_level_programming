#!/usr/bin/python3
"""prints a string in uppercase followed by a new line."""


def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c)- 32) 
        print("{}".format(c), end="")
    print("")
