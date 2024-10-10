#!/usr/bin/env python3
"""Type annotated function that sums floats
in a list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return sum of a list of floats"""
    return sum(input_list)
