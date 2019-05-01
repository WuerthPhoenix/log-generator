# -*- coding: utf-8 -*-

"""Utils module for rl_generator."""


import random


def randint(min_value, max_value):
    """Return random integer in range [min_value, max_value],
    including both end points

    Arguments:
        min_value {int} -- min value
        max_value {int} -- max value

    Returns:
        int -- random integer in range [min_value, max_value]
    """
    return random.randint(int(min_value), int(max_value))
