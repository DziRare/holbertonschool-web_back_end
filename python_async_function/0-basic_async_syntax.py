#!/usr/bin/env python3

"""The module is for async"""

import random
import asyncio


async def wait_random(max_delay: float = 10) -> float:
    """This function is for waiting a random amount of time"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
