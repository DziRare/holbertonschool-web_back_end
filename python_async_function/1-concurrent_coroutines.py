#!/usr/bin/env python3

"""The module is for asynchronous cooroutines that complete as they finish"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """This function is calling coroutines that wait for a random time"""

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    completed = [await time for time in asyncio.as_completed(tasks)]

    return completed
