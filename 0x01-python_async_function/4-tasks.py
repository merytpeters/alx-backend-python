#!/usr/bin/env python3
"""Async routine, identical to wait_n"""


from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Async function identical to wait_random"""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
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
