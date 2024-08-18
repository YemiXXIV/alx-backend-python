#!/usr/bin/env python3
"""
This module contains the `async_comprehension` coroutine which
collects 10 random numbers using asynchronous comprehension
"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from the `async_generator`.
    """
    floats = [nums async for nums in async_generator()]
    return floats
