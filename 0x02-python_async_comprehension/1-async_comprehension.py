#!/usr/bin/env python3
"""
Async Comprehension

an asynchronous comprehension that uses random numbers.
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous comprehension that collects random numbers.

    Returns:
        List[float]: A list of random numbers.
    """
    return [i async for i in async_generator()]
