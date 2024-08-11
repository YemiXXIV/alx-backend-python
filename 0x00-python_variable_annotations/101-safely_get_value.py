#!/usr/bin/env python3
"""
Function to safely get a value from a dictionary
"""
from typing import Union, Any, Mapping, TypeVar, Optional


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Retrieve values safely from dict, default to None if not found
    """
    if key in dct:
        return dct[key]
    else:
        return default
