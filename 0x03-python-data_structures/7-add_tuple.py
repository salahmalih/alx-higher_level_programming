#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) == 1:
            add_t = (tuple_a[0] + tuple_b[0], tuple_a[1])
    elif len(tuple_b) == 0:
        add_t = tuple_a
    else:
        add_t = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return add_t
