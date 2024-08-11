#!/usr/bin/env python3
"""
an asynchronous routine that takes in an integer argument
that waits for a random delay and eventually returns it.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random delay between 0 and
    max_delay seconds and returns the delay
    """
    random_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
