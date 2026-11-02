#!/usr/bin/env python3

"""The module is for asynchronous cooroutines that complete as they finish"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """This function is calling coroutines that wait for a random time"""

    delays = [max_delay] * n

    tasks = [asyncio.create_task(wait_random(delay)) for delay in delays]
    completed = []

    for time in asyncio.as_completed(tasks):
        completed.append(await time)

    return completed
