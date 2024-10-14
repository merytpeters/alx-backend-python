#!/usr/bin/env python3
"""Measures total execution time"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Using the time module to measure time elapsed and returns
    total time / n"""
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if max_delay < 0:
        raise ValueError("maximum delay must be a positive integer")

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return (total_time / n)
