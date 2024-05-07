#!/usr/bin/env python3
"""Module for async comprehension"""
from typing import List

async def async_comprehension() -> List[float]:
    """Async comprehension that returns a list of floats.

    Returns:
        List[float]: A list of floats.
    """
    return [num async for num in [10.0 for _ in range(10)]]
