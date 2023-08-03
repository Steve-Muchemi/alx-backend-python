#!/usr/bin/env python3
""" This module contains the function make_multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns the multiplier function"""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
