#!/usr/bin/python3
"""creates a copy of the string, removing the character at the position n."""


def remove_char_at(str, n):
    if 0 <= n < len(str):
        return str[:n] + str[n+1:]
    else:
        return str
