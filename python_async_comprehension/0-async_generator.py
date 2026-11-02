#!/usr/bin/env python3
"""This module is for async comprehension and genertation"""

import asyncio
from typing import NoReturn
import random


async def async_generator() -> NoReturn:
    """This function is for async comprehension and genertation"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
