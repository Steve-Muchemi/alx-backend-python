#!/usr/bin/env python3
""" this module contains a type-annotated function sum_mixed_list"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns sum of list"""
    a: float = 0
    for i in mxd_lst:
        a = a + i
    return a
