#!/usr/bin/env python3
"""Duck typing an iterable object"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Iterable"""
    return [(i, len(i)) for i in lst]
