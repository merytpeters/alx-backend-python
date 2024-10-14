#!/usr/bin/env python3
"""Asynchronous coroutine and using random module"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Async coroutine that takes an integer that
    waits for a random delay and returns it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
