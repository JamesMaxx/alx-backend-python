#!/usr/bin/env python3
"""
Module for async comprehension.
"""
from typing import List
from 0-async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over async_generator,
    then returns the 10 random numbers.
    """
    result = [num async for num in async_generator()]
    return result
