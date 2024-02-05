#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        rslt = fct(*args)
    except Exception as err:
        sys.stderr.write(f"Exception: {err}\n")
        rslt = None
    return rslt
