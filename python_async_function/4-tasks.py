#!/usr/bin/env python3

"""The module is for asynchronous cooroutines that complete as they finish"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This function is calling coroutines that wait for a random time"""

    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed = [await time for time in asyncio.as_completed(tasks)]

    return completed
