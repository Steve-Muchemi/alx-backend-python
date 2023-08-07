#!/usr/bin/env python3
""" This module contains basic async syntax"""


import asyncio
import random


async def wait_random(mandatory: int = 10) -> float:
    """a simple wait function returns seconds waited"""
    wait: float = random.uniform(0, mandatory)
    await asyncio.sleep(wait)
    return wait
