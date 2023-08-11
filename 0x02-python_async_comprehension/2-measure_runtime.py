#!/usr/bin/env python3
"""
Run time for four parallel comprehensions

This module defines a coroutine that measures the runtime 
of parallel async comprehensions.
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the runtime of parallel async comprehensions.

    Returns:
        float: Total runtime of the parallel async comprehensions.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()
    return end_time - start_time
