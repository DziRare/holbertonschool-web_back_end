#!/usr/bin/env python3
"""This module is for async comprehension and genertation"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None, None]:
    """This function is for async comprehension and genertation"""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
