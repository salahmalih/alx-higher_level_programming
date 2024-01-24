#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """
    Write a function that deletes a key in a dictionary
    """
    if key == "":
        return a_dictionary
    elif key in a_dictionary:
       del a_dictionary[key]
    return a_dictionary
