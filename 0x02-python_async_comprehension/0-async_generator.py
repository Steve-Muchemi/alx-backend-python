#!/usr/bin/env python3
"""
Async Generator

This module defines an asynchronous generator
that yields random numbers after a delay.
"""

import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields random numbers after a 1-second delay.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
