#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """This executes a function safely """
    try:
        return fct(*args)
    except Exception as expt:
        print("Exception: {}".format(expt), file=sys.stderr)
        return None
