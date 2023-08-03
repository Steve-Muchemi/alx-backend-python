#!/usr/bin/env python3
""" this module contains te eleent_length function"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return a list"""
    return [(i, len(i)) for i in lst]
