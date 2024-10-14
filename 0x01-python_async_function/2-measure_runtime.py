#!/usr/bin/env python3
"""Measures total execution time"""


import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Using the time module to measure time elapsed and returns
    total time / n"""

    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time

    return (total_time / n)
