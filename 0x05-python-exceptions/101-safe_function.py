#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    """Function executes a function safely.

    Args:
        fct: The function to execute.
        args: Arguments for fct.

    Returns:
        If an error occurs - None.
        Otherwise - the result of the call to fct.
    """

    try:
        result = fct(*args)
    except BaseException as e:
        result = None

        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return result
