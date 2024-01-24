#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    function that returns a set of common elements in two sets.
    """
    c_set = []
    for set1 in set_1:
        for set2 in set_2:
            if set1 == set2:
                c_set.append(set1)
    return c_set
