#!/usr/bin/env python3
'''
Imports wait_random and defines an async routine called wait_n
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Spawns wait_random n times with the specified max_delay
    '''
    wait_times = []
    for _ in range(n):
        wait_time = await wait_random(max_delay)
        wait_times.append(wait_time)
    return sorted(wait_times)
