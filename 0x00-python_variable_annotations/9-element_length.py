#!/usr/bin/env python3
"""Duck typing an iterable object"""
from typing import Sequence, List, Tuple, Any


def element_length(lst: Sequence[Any]) -> List[Tuple[Sequence[Any], int]]:
    return [(i, len(i)) for i in lst]
