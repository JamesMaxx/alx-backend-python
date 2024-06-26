#!/usr/bin/env python3
'''Take the code from wait_n and alter it into a new function task_wait_n
'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes n instances of task_wait_random.
    '''
    wait_tasks = [task_wait_random(max_delay) for _ in range(n)]
    wait_times = await asyncio.gather(*wait_tasks)
    return sorted(wait_times)
