#!/usr/bin/env python3
"""Function that takes a string and another argument that
could be an int or float and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple where the first element is a string
    and teh second element is the square of either the int
    or float
    """
    return (k, (v ** 2))
