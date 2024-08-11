#!/usr/bin/env python3
"""
This module provides a function to zoom
into a tuple by repeating its elements.
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a list with elements from the
    tuple repeated based on the factor
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
