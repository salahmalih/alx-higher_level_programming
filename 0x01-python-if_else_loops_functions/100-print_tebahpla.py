#!/usr/bin/python3
"""ASCII alphabet."""

i = 1
for c in range(122, 96, -1):
    if i % 2 != 0:
        pass
    else:
        c = c - 32
    print("{}".format(chr(c)), end="")
    i = i + 1
