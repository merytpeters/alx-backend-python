#!/usr/bin/env python3
"""Function that returns a asyncio.Task"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Regular function that returns asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
