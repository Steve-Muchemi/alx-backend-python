#!/usr/bin/env python3
"""
Run time for four parallel comprehensions

This module defines a coroutine that measures the runtime 
of parallel async comprehensions.
"""


import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of parallel async comprehensions.

    Returns:
        float: Total runtime of the parallel async comprehensions.
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
