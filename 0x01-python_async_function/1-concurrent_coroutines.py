#!/usr/bin/env python3
""" This module contains the function wait_n """


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
    max_delay: maximum time to be generated
    Returns:
      a list of float values for time btween 0 and max-delay
    """
    array: List[float] = []
    for i in range(n):
        task = wait_random(max_delay)
        array.append(task)
    return [await i for i in asyncio.as_completed(array)]
