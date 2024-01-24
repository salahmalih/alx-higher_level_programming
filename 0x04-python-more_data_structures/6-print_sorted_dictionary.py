#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    Write a function that prints a dictionary by ordered keys.
    """
    for row, value  in sorted(a_dictionary.items()):
            print("{}: {}".format(row, value))
