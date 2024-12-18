#!/usr/bin/env python3
"""TypeVar annotation"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """Safely gets value"""
    if key in dct:
        return dct[key]
    else:
        return default
