#!/usr/bin/env python3

import asyncio
import random
from typing import AsyncIterator


"""
Module containing an asynchronous generator function.
"""



async def async_generator() -> AsyncIterator[float]:
    """
    Generates a sequence of random floats.

    Yields:
        float: A random float between 0 and 10.

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
