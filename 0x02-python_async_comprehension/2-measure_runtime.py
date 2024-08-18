#!/usr/bin/env python3
"""
This module contains a coroutine `measure_runtime` which
executes `async_comprehension` four times in parallel
and measures the total runtime.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that executes `async_comprehension` four times in parallel
    and measures the total runtime.
    """
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time.perf_counter()
    return (end - start)
