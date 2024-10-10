#!/usr/bin/env python3
"""Mutiplication function that returns a float"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def multiply_by(value: float) -> float:
        """callable function"""
        return value * multiplier
    return multiply_by
