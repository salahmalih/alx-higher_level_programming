#!/usr/bin/python3


def number_keys(a_dictionary):
    """
    Write a function that returns the number of keys in a dictionary.
    """
    key = 0
    for row in a_dictionary:
        key += 1
    return key
