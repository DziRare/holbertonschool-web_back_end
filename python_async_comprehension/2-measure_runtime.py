#!/usr/bin/env python3
"""This module is for measuring runtime"""

import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """This function is for measuring runtime"""

    start = time.perf_counter()
    await async_comprehension()
    end = time.perf_counter()

    return end - start
