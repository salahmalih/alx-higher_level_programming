#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """
    Write a function that returns a set of
    all elements present in only one set.
    """
    c_set = []
    for set1 in set_1:
        if set1 not in set_2:
            c_set.append(set1)
    for set2 in set_2:
        if set2 not in set_1 and set2 not in c_set:
            c_set.append(set2)
    return c_set
