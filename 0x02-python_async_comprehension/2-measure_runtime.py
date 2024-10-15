#!/usr/bin/env python3
"""Coroutine that will execute async_comprehension four
times in parallel"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure time, execute async_comprehension 4 times in parallel"""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    total_runtime = time.perf_counter() - start_time

    return total_runtime
