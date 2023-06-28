#!/usr/bin/python3

def my_function(a, b):
    """
    >>> my_function(2, 3)
    6
    >>> my_function('a', 3)
    'aaa'
    """
    return a*b


def reset(variable):
    """
    >>> battery = 78
    >>> batter = reset(battery)
    >>> battery
    0
    """
    variable = 0
    return variable
