#!/usr/bin/env python3
"""Async generator coroutine"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Coroutine that loops 10 times, asynchronously wait 1second
    and yields a random number"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
