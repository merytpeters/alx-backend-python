#!/usr/bin/env python3
"""Function that return the sun of a list
The lists contains mixed type of integers
and float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of integers and floats"""
    return sum(mxd_lst)
