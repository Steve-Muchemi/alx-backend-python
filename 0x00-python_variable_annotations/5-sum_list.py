#!/usr/bin/env python3
""" This module contains the sum_list function"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns the sum of items in a list"""
    a: float = 0
    for i in input_list:
        a = a + i
    return a
