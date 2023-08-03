#!/usr/bin/env python3
""" This module contains function to_kv"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns a tuple with a string and float"""
    return (k, v ** 2)
