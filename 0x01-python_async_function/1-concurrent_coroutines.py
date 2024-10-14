#!/usr/bin/env python3
"""Async routine, random delay in ascending order"""


from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Async function that spawns wait_random n times and returns
    sorted list of delays without using sort()"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in tasks:
        delay = await task
        if not delays:
            delays.append(delay)
        else:
            inserted = False
            for i in range(len(delays)):
                if delay < delays[i]:
                    delays.insert(i, delay)
                    inserted = True
                    break
            if not inserted:
                delays.append(delay)
    return delays
