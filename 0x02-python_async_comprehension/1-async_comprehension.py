#!/usr/bin/env python3
"""Coroutine that will collect 10 random numbers using
an async comprehension over async_generator"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async Comprehension, coroutine that collects 10 random numbers
    using async comprehensing"""
    return [number async for number in async_generator()]
